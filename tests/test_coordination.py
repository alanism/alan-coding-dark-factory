"""Behavioral checks for the v9 declaration validator; no agents are launched."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from verify_coordination import validate_contract


class CoordinationTests(unittest.TestCase):
    def fixture(self, name="parallel"):
        return json.loads((ROOT / "examples/coordination" / (name + ".json")).read_text())

    def reject(self, contract, message):
        errors = validate_contract(contract)
        self.assertTrue(errors, "invalid contract was accepted")
        self.assertIn(message, "\n".join(errors))

    def test_examples_and_template_pass(self):
        for name in ("single", "parallel"):
            with self.subTest(name=name):
                self.assertEqual(validate_contract(self.fixture(name)), [])
        template = ROOT / "templates/.acdf/changes/_template/coordination.json"
        self.assertEqual(validate_contract(json.loads(template.read_text())), [])

    def test_unordered_writers_cannot_share_files(self):
        data = self.fixture()
        data["lanes"][1]["write_files"][0] = "src/config.txt"
        self.reject(data, "concurrent ownership")

    def test_workspace_and_agent_collisions(self):
        for field in ("workspace", "agent_id"):
            data = self.fixture()
            data["lanes"][1][field] = data["lanes"][0][field]
            with self.subTest(field=field):
                self.reject(data, "concurrent")

    def test_unknown_self_and_cyclic_dependencies(self):
        for deps, message in [(["task-99"], "unknown dependency"), (["task-1"], "self dependency"), (["task-4"], "cycle")]:
            data = self.fixture()
            data["lanes"][0]["dependencies"] = deps
            self.reject(data, message)

    def test_duplicate_task_and_artifact(self):
        data = self.fixture()
        data["lanes"][1]["task_id"] = "task-1"
        self.reject(data, "duplicate task")
        data = self.fixture()
        lane = data["lanes"][1]
        lane["output_artifact"] = data["lanes"][0]["output_artifact"]
        lane["write_files"][-1] = lane["output_artifact"]
        lane["handoff"]["artifact"] = lane["output_artifact"]
        self.reject(data, "duplicate output")

    def test_reviewer_cannot_write_implementation(self):
        data = self.fixture()
        data["lanes"][2]["write_files"].append("src/config.txt")
        self.reject(data, "reviewer writes")

    def test_missing_handoff_context_checks_or_references(self):
        for field in ("context", "acceptance_checks", "stop_conditions"):
            data = self.fixture()
            data["lanes"][0][field] = []
            self.reject(data, field)
        for field in ("plan_ref", "spec_ref", "approval_ref"):
            data = self.fixture()
            del data[field]
            self.reject(data, field)
        for field in ("evidence", "recipient", "artifact", "unresolved"):
            data = self.fixture()
            del data["lanes"][0]["handoff"][field]
            self.reject(data, field)

    def test_budget_limits_and_explicit_extension(self):
        for field, value in [("max_cycles", 6), ("max_cycles", True), ("max_files", 4), ("max_files", 1), ("max_files", 0)]:
            data = self.fixture()
            data["lanes"][0]["budget"][field] = value
            self.reject(data, field)
        data = self.fixture()
        data["lanes"][0]["budget"]["max_cycles"] = 3
        self.reject(data, "extension_approval_ref")
        data["lanes"][0]["budget"]["extension_approval_ref"] = "illustrative-extension@1"
        self.assertEqual(validate_contract(data), [])

    def test_path_escape_glob_and_alias(self):
        for path in ("../secrets", "/tmp/write", "src/*", "src/./file", "src//file", "src/file/", "C:/file", "src\\file"):
            data = self.fixture()
            data["lanes"][0]["write_files"][0] = path
            self.reject(data, "path")
        data = self.fixture()
        data["lanes"][1]["write_files"][0] = "SRC/CONFIG.TXT"
        self.reject(data, "concurrent ownership")

    def test_output_must_be_owned_and_handoff_must_match(self):
        data = self.fixture()
        data["lanes"][0]["output_artifact"] = "unowned/output.patch"
        self.reject(data, "output_artifact")
        data = self.fixture()
        data["lanes"][0]["handoff"]["recipient"] = "another-agent"
        self.reject(data, "recipient")
        data = self.fixture()
        data["lanes"][0]["handoff"]["artifact"] = "wrong.patch"
        self.reject(data, "artifact")

    def test_integrator_waits_for_all_lanes(self):
        data = self.fixture()
        data["lanes"][-1]["dependencies"] = ["task-1"]
        self.reject(data, "integrator must depend")
        data = self.fixture()
        data["integration_owner"] = "missing-agent"
        self.reject(data, "integration_owner")

    def test_modes_and_unknown_fields(self):
        data = self.fixture()
        data["mode"] = "single"
        self.reject(data, "single")
        data = self.fixture()
        data["approval_mode"] = "auto"
        self.reject(data, "approval_mode")
        data = self.fixture()
        data["lanes"][0]["write_fiels"] = []
        self.reject(data, "unknown field")

    def test_malformed_shapes_are_reported_not_crashed(self):
        for value in (None, [], "x", 1, {}, {"contract_version": True}, {"lanes": [None]}, {"lanes": {}}):
            with self.subTest(value=value):
                self.assertTrue(validate_contract(value))
        original = self.fixture()
        for field in original["lanes"][0]:
            for value in (None, {}, [None], True):
                data = copy.deepcopy(original)
                data["lanes"][0][field] = value
                with self.subTest(field=field, value=value):
                    errors = validate_contract(data)
                    self.assertIsInstance(errors, list)

    def test_cli_rejects_invalid_json_and_duplicate_keys(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "contract.json"
            for content in ('{', '{"mode":"single","mode":"parallel"}'):
                path.write_text(content)
                result = subprocess.run([sys.executable, str(ROOT / "scripts/verify_coordination.py"), str(path)], capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertNotIn("Traceback", result.stderr)

    def test_cli_never_executes_acceptance_text(self):
        with tempfile.TemporaryDirectory() as directory:
            marker = Path(directory) / "must-not-exist"
            path = Path(directory) / "contract.json"
            data = self.fixture()
            data["lanes"][0]["acceptance_checks"] = ["touch " + str(marker)]
            path.write_text(json.dumps(data))
            result = subprocess.run([sys.executable, str(ROOT / "scripts/verify_coordination.py"), str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertFalse(marker.exists())


if __name__ == "__main__":
    unittest.main()
