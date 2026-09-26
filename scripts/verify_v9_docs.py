#!/usr/bin/env python3
"""Local link targets, card provenance, routing fields and coordination declarations."""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
from verify_coordination import load_contract, validate_contract

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "framework/ACDF_coordination.md", "heroes/README.md", "heroes/how-to-use.md",
    "heroes/SOURCE_MANIFEST.json", "heroes/docs/evaluation.md", "heroes/docs/role-examples.md",
    "heroes/docs/runbook.md", "heroes/docs/learning-log.md", "heroes/references/slide-layout-rubric.md",
    "docs/v9-migration.md", "docs/runbook.md", "docs/learning-log.md",
    "templates/agent_task_contract.md", "templates/.acdf/changes/_template/coordination.json",
    "examples/coordination/README.md", "examples/coordination/single.json", "examples/coordination/parallel.json",
    "scripts/verify_coordination.py", "scripts/verify_v9_docs.py",
    "tests/test_coordination.py", "tests/test_v9_docs.py",
]


def local_link_errors(path, root):
    """Check local inline Markdown targets outside fenced examples; fragments are not checked."""
    lines = []
    fence = None
    for line in path.read_text(encoding="utf-8").splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            value = marker.group(1)
            if fence is None:
                fence = value
            elif value[0] == fence[0] and len(value) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    errors = []
    for href in re.findall(r"\]\(([^)]+)\)", "\n".join(lines)):
        href = href.strip().strip("<>")
        try:
            url = urlsplit(href)
            if url.scheme in ("http", "https", "mailto", "app", "plugin"):
                continue
            if url.scheme or href.startswith("/"):
                errors.append(str(path.relative_to(root)) + ": nonportable link " + href)
                continue
            if not url.path:
                continue
            target = (path.parent / unquote(url.path)).resolve()
            if not target.is_relative_to(root.resolve()):
                errors.append(str(path.relative_to(root)) + ": link escapes repository " + href)
            elif not target.exists():
                errors.append(str(path.relative_to(root)) + ": missing link target " + href)
        except ValueError as error:
            errors.append(str(path.relative_to(root)) + ": invalid link " + str(error))
    return errors


def library_errors(root):
    errors = []
    try:
        manifest = json.loads((root / "heroes/SOURCE_MANIFEST.json").read_text())
        entries = manifest["cards"]
        paths = [entry["path"] for entry in entries]
        actual = {str(p.relative_to(root / "heroes")) for p in (root / "heroes").glob("*_Council/*_hero.md")}
        if len(paths) != len(set(paths)):
            errors.append("duplicate manifest card paths")
        if manifest["card_count"] != 17 or len(paths) != 17 or len(actual) != 17:
            errors.append("expected 17 maintained cards")
        if set(paths) != actual:
            errors.append("manifest card coverage differs from actual cards")
        index = (root / "heroes/README.md").read_text()
        router = (root / "heroes/how-to-use.md").read_text()
        for entry in entries:
            name = entry["path"]
            if name not in actual:
                continue
            path = root / "heroes" / name
            if hashlib.sha256(path.read_bytes()).hexdigest() != entry["shipped_sha256"]:
                errors.append(name + ": shipped hash mismatch")
            if not re.fullmatch(r"[a-f0-9]{64}", entry["source_sha256"]):
                errors.append(name + ": invalid source hash")
            if name not in index or name not in router:
                errors.append(name + ": not indexed in both entry points")
            content = path.read_text()
            for required in ("Stage and host scope", "## Worked application", "**Activate:**", "**Defer:**"):
                if required not in content:
                    errors.append(name + ": missing " + required)
    except (OSError, ValueError, KeyError, TypeError) as error:
        errors.append("card manifest: " + str(error))
    return errors


def validate_repo(root=ROOT):
    errors = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append("missing v9 artifact: " + name)
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts or any(part.startswith(".acdf") for part in path.relative_to(root).parts[:1]):
            continue  # Operational records are not public documentation.
        errors.extend(local_link_errors(path, root))
    errors.extend(library_errors(root))
    for name in ("examples/coordination/single.json", "examples/coordination/parallel.json", "templates/.acdf/changes/_template/coordination.json"):
        try:
            errors.extend(name + ": " + error for error in validate_contract(load_contract(root / name)))
        except (OSError, ValueError) as error:
            errors.append(name + ": " + str(error))
    for name in ("README.md", "AGENTS.md"):
        if "v9" not in (root / name).read_text().splitlines()[0]:
            errors.append(name + ": missing v9 heading")
    workflow = (root / "framework/ACDF_workflow.mmd").read_text()
    for phrase in ("Stage 2:", "Independent lanes", "One integrator", "Standalone council", "HARD_STOP"):
        if phrase not in workflow:
            errors.append("workflow: missing " + phrase)
    return errors


def main():
    errors = validate_repo()
    for error in errors:
        print("FAIL: " + error)
    if not errors:
        print("PASS: v9 local links, 17-card provenance, routing and coordination declarations.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
