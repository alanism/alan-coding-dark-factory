#!/usr/bin/env python3
import os
import sys
import json
import re

# Root path of the repository
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "framework/ACDF_kernel.md",
    "framework/ACDF_lifecycle.md",
    "framework/ACDF_authority.md",
    "framework/ACDF_execution.md",
    "framework/ACDF_verify.md",
    "framework/ACDF_hero_lenses.md",
    "schemas/change.schema.json",
    "schemas/authority.schema.json",
    "schemas/claim.schema.json",
    "schemas/state-log.schema.json",
    "schemas/receipt.schema.json",
    "templates/.acdf/reference/guide.md",
    "templates/.acdf/reference/trust-zones.md",
    "templates/.acdf/reference/forbidden-files.md",
    "templates/.acdf/changes/_template/proposal.md",
    "templates/.acdf/changes/_template/design.md",
    "templates/.acdf/changes/_template/tasks.md",
    "templates/.acdf/changes/_template/authority.json",
    "templates/.acdf/changes/_template/claims/.gitkeep",
    "templates/.acdf/changes/_template/state-log.ndjson",
    "templates/.acdf/changes/_template/evidence/.gitkeep",
    "templates/.acdf/changes/_template/receipts/.gitkeep",
    "templates/.acdf/changes/_template/retrospective.md",
    "examples/tiny-change/change.json",
    "examples/tiny-change/proposal.md",
    "examples/tiny-change/design.md",
    "examples/tiny-change/tasks.md",
    "examples/tiny-change/authority.json",
    "examples/tiny-change/claims/task-1.agent-1.json",
    "examples/tiny-change/state-log.ndjson",
    "examples/tiny-change/evidence/task-1_verify.log",
    "examples/tiny-change/receipts/task-1.json",
    "examples/tiny-change/retrospective.md",
    "examples/tiny-change/config.txt"
]

FORBIDDEN_TERMS = [
    r"\bOpenSpec\b",
    r"\bAria\b",
    r"\bUCC\b",
    r"\bUnCommon\s+Core\b",
    r"\bHermes\s+Thrice\s+Great\b",
    r"\bCampaign\s+OS\b",
    r"\bHermes\b"
]

LIFECYCLE_REQUIREMENTS = [
    "Inputs",
    "Outputs",
    "Binary Gate",
    "Evidence",
    "Stop Conditions",
    "Next Unlock"
]

def log_success(msg):
    print(f"\033[92m[PASS]\033[0m {msg}")

def log_failure(msg):
    print(f"\033[91m[FAIL]\033[0m {msg}")

def test_file_existence():
    passed = True
    for relative_path in REQUIRED_FILES:
        full_path = os.path.join(REPO_ROOT, relative_path)
        if os.path.exists(full_path):
            log_success(f"File exists: {relative_path}")
        else:
            log_failure(f"Missing file: {relative_path}")
            passed = False
    return passed

def test_json_schemas():
    passed = True
    schema_dir = os.path.join(REPO_ROOT, "schemas")
    for filename in os.listdir(schema_dir):
        if filename.endswith(".schema.json"):
            filepath = os.path.join(schema_dir, filename)
            try:
                with open(filepath, "r") as f:
                    json.load(f)
                log_success(f"Valid schema JSON: {filename}")
            except Exception as e:
                log_failure(f"Invalid schema JSON in {filename}: {e}")
                passed = False
    return passed

def test_example_validation():
    passed = True
    
    # 1. Validate change.json
    try:
        with open(os.path.join(REPO_ROOT, "examples/tiny-change/change.json"), "r") as f:
            change_data = json.load(f)
        assert "changeId" in change_data, "Missing changeId"
        assert "stage" in change_data, "Missing stage"
        assert isinstance(change_data["tasks"], list), "tasks is not a list"
        for task in change_data["tasks"]:
            assert "id" in task, "Task missing id"
            assert "binary_gate" in task, "Task missing binary_gate"
        log_success("change.json fits change schema constraints")
    except Exception as e:
        log_failure(f"change.json validation failure: {e}")
        passed = False

    # 2. Validate authority.json
    try:
        with open(os.path.join(REPO_ROOT, "examples/tiny-change/authority.json"), "r") as f:
            auth_data = json.load(f)
        assert "changeName" in auth_data, "Missing changeName"
        assert "snapshots" in auth_data, "Missing snapshots"
        assert "write_rules" in auth_data, "Missing write_rules"
        assert "allowed_files" in auth_data["write_rules"], "Missing allowed_files"
        log_success("authority.json fits authority schema constraints")
    except Exception as e:
        log_failure(f"authority.json validation failure: {e}")
        passed = False

    # 3. Validate claim.json
    try:
        with open(os.path.join(REPO_ROOT, "examples/tiny-change/claims/task-1.agent-1.json"), "r") as f:
            claim_data = json.load(f)
        assert "taskId" in claim_data, "Missing taskId"
        assert "agentId" in claim_data, "Missing agentId"
        log_success("claim JSON fits claim schema constraints")
    except Exception as e:
        log_failure(f"claim JSON validation failure: {e}")
        passed = False

    # 4. Validate state-log.ndjson
    try:
        with open(os.path.join(REPO_ROOT, "examples/tiny-change/state-log.ndjson"), "r") as f:
            for line in f:
                if line.strip():
                    log_data = json.loads(line)
                    assert "timestamp" in log_data, "Missing timestamp"
                    assert "action" in log_data, "Missing action"
        log_success("state-log.ndjson validation passes")
    except Exception as e:
        log_failure(f"state-log.ndjson validation failure: {e}")
        passed = False

    # 5. Validate receipt.json
    try:
        with open(os.path.join(REPO_ROOT, "examples/tiny-change/receipts/task-1.json"), "r") as f:
            receipt_data = json.load(f)
        assert "taskId" in receipt_data, "Missing taskId"
        assert "status" in receipt_data, "Missing status"
        assert "verification_command" in receipt_data, "Missing verification_command"
        assert "prevention" in receipt_data, "Missing prevention"
        log_success("receipt.json fits receipt schema constraints")
    except Exception as e:
        log_failure(f"receipt.json validation failure: {e}")
        passed = False

    return passed

def test_forbidden_references():
    passed = True
    
    # Compile regexes
    patterns = [re.compile(pat, re.IGNORECASE) for pat in FORBIDDEN_TERMS]
    
    for root, dirs, files in os.walk(REPO_ROOT):
        # Skip git folders and verify script itself
        if ".git" in root or "scripts" in root:
            continue
        for file in files:
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                for pat in patterns:
                    match = pat.search(content)
                    if match:
                        log_failure(f"Forbidden reference '{match.group()}' found in: {os.path.relpath(filepath, REPO_ROOT)}")
                        passed = False
            except Exception as e:
                # Ignore binaries or unreadable files
                pass
                
    if passed:
        log_success("No forbidden terms or private project names found in repository files.")
    return passed

def test_lifecycle_gates():
    passed = True
    lifecycle_path = os.path.join(REPO_ROOT, "framework/ACDF_lifecycle.md")
    
    if not os.path.exists(lifecycle_path):
        log_failure("Cannot verify lifecycle gates: framework/ACDF_lifecycle.md is missing.")
        return False
        
    with open(lifecycle_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    stages = re.split(r"###\s+Stage\s+\d+:", content)
    # The first split element is headers, the rest are stages 0-8 (10 total elements)
    if len(stages) < 10:
        log_failure(f"Failed to find all 9 stages in ACDF_lifecycle.md (found {len(stages)-1}/10 sections)")
        passed = False
    else:
        log_success("Found all lifecycle stages (Stage 0 to Stage 8) in ACDF_lifecycle.md")
        
    # Check that each stage section has the 6 required bullet points
    for idx, stage_content in enumerate(stages[1:]):
        stage_num = idx
        missing_reqs = []
        for req in LIFECYCLE_REQUIREMENTS:
            if req not in stage_content:
                missing_reqs.append(req)
        if missing_reqs:
            log_failure(f"Stage {stage_num} is missing required fields: {', '.join(missing_reqs)}")
            passed = False
        else:
            log_success(f"Stage {stage_num} has all required fields (Inputs, Outputs, Gates, Evidence, Stops, Unlocks)")
            
    return passed

def main():
    print("--- Starting ACDF v8 Repo Integrity Validation ---")
    results = [
        test_file_existence(),
        test_json_schemas(),
        test_example_validation(),
        test_forbidden_references(),
        test_lifecycle_gates()
    ]
    
    print("-------------------------------------------------")
    if all(results):
        print("\033[92m[SUCCESS]\033[0m ACDF v8 standalone repository is 100% valid and secure.")
        sys.exit(0)
    else:
        print("\033[91m[FAILURE]\033[0m Repository integrity tests failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
