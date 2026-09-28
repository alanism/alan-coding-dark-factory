"""Regression checks for link and card-provenance validation."""
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from verify_v9_docs import local_link_errors, library_errors


class DocumentationTests(unittest.TestCase):
    def test_local_links_resolve_and_code_examples_are_ignored(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "with space.md").write_text("# Target")
            page = root / "README.md"
            page.write_text("[ok](with%20space.md)\n[web](https://example.com)\n```md\n[placeholder](missing.md)\n```\n")
            self.assertEqual(local_link_errors(page, root), [])
            page.write_text("[missing](absent.md)\n[private](file:///Users/person/a.md)\n[escape](../outside.md)")
            errors = local_link_errors(page, root)
            self.assertEqual(len(errors), 3)

    def test_current_library_is_consistent(self):
        self.assertEqual(library_errors(ROOT), [])

    def test_card_edit_without_manifest_update_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "heroes", root / "heroes")
            manifest = json.loads((root / "heroes/SOURCE_MANIFEST.json").read_text())
            path = root / "heroes" / manifest["cards"][0]["path"]
            path.write_text(path.read_text() + "\nUnreviewed change\n")
            self.assertIn("hash mismatch", "\n".join(library_errors(root)))

    def test_unindexed_or_duplicate_card_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "heroes", root / "heroes")
            index = root / "heroes/README.md"
            index.write_text("# No cards indexed\n")
            self.assertIn("not indexed", "\n".join(library_errors(root)))
            manifest_path = root / "heroes/SOURCE_MANIFEST.json"
            manifest = json.loads(manifest_path.read_text())
            manifest["cards"].append(manifest["cards"][0])
            manifest_path.write_text(json.dumps(manifest))
            self.assertIn("duplicate manifest", "\n".join(library_errors(root)))

    def test_notebook_id_and_share_link_must_match_card(self):
        self.assertEqual(library_errors(ROOT), [])
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "heroes", root / "heroes")
            manifest_path = root / "heroes/SOURCE_MANIFEST.json"
            manifest = json.loads(manifest_path.read_text())
            manifest["cards"][0]["notebook_id"] = "00000000-0000-0000-0000-000000000000"
            manifest_path.write_text(json.dumps(manifest))
            errors = "\n".join(library_errors(root))
            self.assertIn("NotebookLM link does not match", errors)
            self.assertIn("NotebookLM source does not match", errors)


if __name__ == "__main__":
    unittest.main()
