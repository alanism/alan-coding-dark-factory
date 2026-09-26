#!/usr/bin/env python3
"""Validate coordination declarations only. Never execute their commands or act on approvals."""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT_FIELDS = {"contract_version", "mode", "stage", "approval_mode", "approval_ref", "plan_ref", "spec_ref", "integration_owner", "lanes"}
LANE_FIELDS = {"task_id", "agent_id", "role", "hero_lens", "dependencies", "workspace", "write_files", "output_artifact", "context", "acceptance_checks", "stop_conditions", "budget", "handoff"}
ROLES = {"planner", "reviewer", "implementer", "test-designer", "qa", "integrator", "learning"}
STAGES = {"planning", "review", "execution", "verification", "integration", "learning"}


def text(value):
    return isinstance(value, str) and bool(value.strip())


def valid_path(value):
    return (text(value) and not any(c in value for c in "\\:*?[]\n\r\x00")
            and not value.startswith("/") and all(p not in ("", ".", "..") for p in value.split("/")))


def overlaps(left, right):
    left, right = left.casefold(), right.casefold()
    return left == right or left.startswith(right + "/") or right.startswith(left + "/")


def validate_contract(data):
    """Return deterministic actionable errors. References are not authenticated or dereferenced."""
    errors = []

    def fields(obj, required, optional, label):
        if not isinstance(obj, dict):
            errors.append(label + ": expected object")
            return False
        for name in sorted(required - obj.keys()):
            errors.append(label + ": missing " + name)
        for name in sorted(obj.keys() - required - optional):
            errors.append(label + ": unknown field " + str(name))
        return True

    def strings(value, label, nonempty=True):
        if not isinstance(value, list) or (nonempty and not value) or not all(text(x) for x in value):
            errors.append(label + ": expected " + ("nonempty " if nonempty else "") + "string list")
            return False
        return True

    if not fields(data, ROOT_FIELDS, set(), "contract"):
        return errors
    if type(data.get("contract_version")) is not int or data["contract_version"] != 1:
        errors.append("contract_version: expected integer 1")
    for key, choices in (("mode", {"single", "parallel"}), ("stage", STAGES), ("approval_mode", {"human", "council"})):
        if not isinstance(data.get(key), str) or data[key] not in choices:
            errors.append(key + ": expected one of " + ", ".join(sorted(choices)))
    for key in ("plan_ref", "spec_ref", "approval_ref", "integration_owner"):
        if not text(data.get(key)):
            errors.append(key + ": required nonempty reference or identity")
    lanes = data.get("lanes")
    if not isinstance(lanes, list) or not lanes:
        return errors + ["lanes: expected nonempty list"]

    for index, lane in enumerate(lanes):
        label = "lanes[" + str(index) + "]"
        if not fields(lane, LANE_FIELDS, set(), label):
            continue
        if not isinstance(lane.get("task_id"), str) or not re.fullmatch(r"task-[0-9]+", lane["task_id"]):
            errors.append(label + ".task_id: expected task-N")
        if not text(lane.get("agent_id")):
            errors.append(label + ".agent_id: expected nonempty identity")
        if not isinstance(lane.get("role"), str) or lane["role"] not in ROLES:
            errors.append(label + ".role: unknown role")
        if lane.get("hero_lens") is not None and not text(lane["hero_lens"]):
            errors.append(label + ".hero_lens: expected null or nonempty string")
        for key in ("context", "acceptance_checks", "stop_conditions", "write_files", "dependencies"):
            if strings(lane.get(key), label + "." + key, nonempty=key != "dependencies"):
                if key in ("write_files", "dependencies") and len(set(x.casefold() for x in lane[key])) != len(lane[key]):
                    errors.append(label + "." + key + ": duplicate entries")
        for key in ("workspace", "output_artifact"):
            if not valid_path(lane.get(key)):
                errors.append(label + "." + key + ": expected canonical repository-relative path")
        writes = lane.get("write_files")
        if isinstance(writes, list):
            for path in writes:
                if not valid_path(path):
                    errors.append(label + ".write_files: invalid path " + repr(path))
            if lane.get("output_artifact") not in writes:
                errors.append(label + ".output_artifact: must be an owned write_file")
            if lane.get("role") == "reviewer" and writes != [lane.get("output_artifact")]:
                errors.append(label + ": reviewer writes must contain only its review output")
            if all(valid_path(p) for p in writes):
                for n, left in enumerate(writes):
                    for right in writes[n+1:]:
                        if overlaps(left, right):
                            errors.append(label + ".write_files: overlapping path declarations")
        budget = lane.get("budget")
        if fields(budget, {"max_cycles", "max_files"}, {"extension_approval_ref"}, label + ".budget"):
            cycles, count = budget.get("max_cycles"), budget.get("max_files")
            if type(cycles) is not int or not 1 <= cycles <= 5:
                errors.append(label + ".budget.max_cycles: integer 1..5 required")
            elif cycles > 2 and not text(budget.get("extension_approval_ref")):
                errors.append(label + ".budget.extension_approval_ref: required above default 2 cycles")
            if type(count) is not int or not 1 <= count <= 3:
                errors.append(label + ".budget.max_files: integer 1..3 required")
            elif isinstance(writes, list) and len(writes) > count:
                errors.append(label + ".budget.max_files: owned files exceed budget")
            if "extension_approval_ref" in budget and not text(budget["extension_approval_ref"]):
                errors.append(label + ".budget.extension_approval_ref: nonempty reference required")
        handoff = lane.get("handoff")
        if fields(handoff, {"artifact", "evidence", "unresolved", "recipient"}, set(), label + ".handoff"):
            if not text(handoff.get("artifact")) or handoff["artifact"] != lane.get("output_artifact"):
                errors.append(label + ".handoff.artifact: must match output_artifact")
            if not text(handoff.get("recipient")) or handoff["recipient"] != data.get("integration_owner"):
                errors.append(label + ".handoff.recipient: must match integration_owner")
            if strings(handoff.get("evidence"), label + ".handoff.evidence"):
                for path in handoff["evidence"]:
                    if not valid_path(path):
                        errors.append(label + ".handoff.evidence: invalid path")
            strings(handoff.get("unresolved"), label + ".handoff.unresolved", nonempty=False)
    # Cross-lane checks operate only after all shapes are known to be valid.
    if errors:
        return errors
    by_id = {}
    outputs = set()
    for lane in lanes:
        task_id = lane["task_id"]
        if task_id in by_id:
            errors.append("duplicate task: " + task_id)
        by_id[task_id] = lane
        output = lane["output_artifact"].casefold()
        if output in outputs:
            errors.append("duplicate output artifact: " + lane["output_artifact"])
        outputs.add(output)
    for lane in lanes:
        for dep in lane["dependencies"]:
            if dep not in by_id:
                errors.append(lane["task_id"] + ": unknown dependency " + dep)
            elif dep == lane["task_id"]:
                errors.append(lane["task_id"] + ": self dependency")
    if errors:
        return errors
    # Iterative topological resolution avoids recursive stack limits.
    ancestors = {}
    pending = set(by_id)
    while pending:
        ready = sorted(task for task in pending if all(d in ancestors for d in by_id[task]["dependencies"]))
        if not ready:
            return errors + ["dependency cycle: " + ", ".join(sorted(pending))]
        for task in ready:
            deps = by_id[task]["dependencies"]
            ancestors[task] = set(deps)
            for dep in deps:
                ancestors[task].update(ancestors[dep])
            pending.remove(task)
    agents = {lane["agent_id"] for lane in lanes}
    if data["mode"] == "single" and len(agents) != 1:
        errors.append("single mode requires one actual agent")
    if data["mode"] == "parallel" and len(agents) < 2:
        errors.append("parallel mode requires at least two actual agents")
    integrators = [lane for lane in lanes if lane["role"] == "integrator"]
    if len(integrators) != 1 or integrators[0]["agent_id"] != data["integration_owner"]:
        errors.append("integration_owner must own exactly one integrator lane")
    else:
        task = integrators[0]["task_id"]
        if ancestors[task] != set(by_id) - {task}:
            errors.append("integrator must depend transitively on all other lanes")
    for index, left in enumerate(lanes):
        for right in lanes[index+1:]:
            if left["task_id"] in ancestors[right["task_id"]] or right["task_id"] in ancestors[left["task_id"]]:
                continue
            pair = left["task_id"] + " / " + right["task_id"]
            if left["agent_id"] == right["agent_id"]:
                errors.append(pair + ": concurrent tasks share an agent; order them")
            if overlaps(left["workspace"], right["workspace"]):
                errors.append(pair + ": concurrent writers share overlapping workspace paths")
            if any(overlaps(a, b) for a in left["write_files"] for b in right["write_files"]):
                errors.append(pair + ": concurrent ownership overlaps; split files or order tasks")
    return errors


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key: " + key)
        result[key] = value
    return result


def load_contract(path):
    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=unique_keys)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract", type=Path)
    args = parser.parse_args()
    try:
        errors = validate_contract(load_contract(args.contract))
    except (OSError, ValueError, RecursionError) as error:
        errors = [str(error)]
    for error in errors:
        print("FAIL: " + error)
    if not errors:
        print("PASS: coordination declarations are consistent; runtime authority and evidence are not verified.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
