# ACDF v9 Lifecycle — Gated Sequential Stages

This document defines the sequential stages of the ACDF v9 engineering lifecycle. Stages are execution milestones. Transitioning between stages requires binary verification of inputs and outputs. No phase gates can be bypassed. Independent tasks may run concurrently within the currently unlocked stage when the approved dependency graph allows it. Agents entering execution verify the completed upstream handoff rather than repeating upstream work. Standalone council use follows the host workflow instead of imposing these stages.

---

## The Gated Stages

### Stage 0: Intent Capture
* **Inputs**: Human brief or raw bug description, plus the user's selected approval mode (`human-led` or `council-led`).
* **Outputs**: `STAGE0_INTENT.md`, `ROUGH_MAP.mmd`, `REFERENCE_RESEARCH_NOTES.md`, `OPEN_QUESTIONS.md`, and `APPROVAL_POLICY.md`.
* **Binary Gate**: STAGE0_INTENT.md contains validated Job-to-be-Done (JTBD), primary user definition, and open research questions are mapped.
* **Evidence**: Stage 0 artifacts successfully committed to the repository (no application source code modified).
* **Stop Conditions**: The brief lacks a clear user metric or the agent cannot define what success means.
* **Next Unlock**: Stage 0.5 (Architectural Modeling).

### Stage 0.5: Architectural Modeling
* **Inputs**: `STAGE0_INTENT.md`, research notes, active project code, and the canonical [ACDF workflow model](ACDF_workflow.mmd).
* **Outputs**: Validated Mermaid diagrams located in `.acdf/changes/<change-id>/models/` (e.g. flowcharts, sequence diagrams, state diagrams, ER schemas, dependency graphs, or C4 container mappings), including the approval path used by the change.
* **Binary Gate**: Every dynamic system element, component interface, and state transition is represented. Mermaid script syntax compiles clean with zero errors.
* **Evidence**: Validated Mermaid code snippets verified by markdown parsing tools.
* **Stop Conditions**: State transitions are left unmapped or components mentioned in intent docs are missing from the diagrams.
* **Next Unlock**: Stage 1 (Reference Guide Specification).

### Stage 1: Reference Guide Specification
* **Inputs**: Stage 0.5 Architectural models, research notes, APIs, public NotebookLM sources selected from `docs/notebooklm-inventory.md`, read-only NotebookLM MCP outputs, and synthesized expert source packs from the [NotebookLM Ingestion Workflow](ACDF_multimodel_review.md).
* **Outputs**: Updated `.acdf/reference/guide.md` (schemas, constants, invariants, trust zones, forbidden files).
* **Binary Gate**: Core schemas and interfaces are compiled. The guide satisfies the "Ten No's" check list.
* **Evidence**: Compiler/linter exits 0 when building schema definitions.
* **Stop Conditions**: Interfaces contain TBD place-holders or undocumented constants.
* **Next Unlock**: Stage 2 (Change Setup & Tasking).

### Stage 2: Change Setup & Tasking
* **Inputs**: Stage 0.5 Models and Stage 1 Reference Guide (`.acdf/reference/guide.md`).
* **Outputs**: `.acdf/changes/<change-id>/` directory containing `proposal.md`, `design.md`, and `tasks.md`, plus task contracts and a coordination manifest when using the v9 coordination profile.
* **Binary Gate**: Topological sort of tasks is resolved. Every task has a whitelisted `allowed_files` array and a designated `binary_gate` test command. Coordinated lanes also declare role/lens, ownership, workspace, context, budget, evidence and integration owner; validate their manifest before dispatch.
* **Evidence**: Successful JSON validation of `change.json` metadata against `change.schema.json`.
* **Stop Conditions**: A task requires modifying a file declared in `forbidden-files.md`.
* **Next Unlock**: Stage 3 (Adversarial Review).

### Stage 3: Adversarial Review
* **Inputs**: Stage 0.5 Architectural models, `proposal.md`, `design.md`, `tasks.md`, and the selected individual Engineering/Design Council cards under `heroes/`.
* **Outputs**: `.acdf/changes/<change-id>/risk_review.md` and, when council-led, an approval record generated via the [Multi-Model Adversarial Review Workflow](ACDF_multimodel_review.md).
* **Binary Gate**: At least 3 independent advisory risk lenses have evaluated and challenged the models, sequence mappings, and task list; any council approval has a recorded quorum and strict majority.
* **Evidence**: Signed check-offs from each lens inside the risk review log or risk register, plus the human or council decision record.
* **Stop Conditions**: A critical security, scaling, or database migration risk is flagged in the models without a mitigation task.
* **Next Unlock**: Stage 4 (Execution Readiness).

### Stage 4: Execution Readiness (Snapshot)
* **Inputs**: Locked tasks, design, models, Reference Guide, and valid approval record.
* **Outputs**: `.acdf/changes/<change-id>/authority.json` with the approval record attached.
* **Binary Gate**: Content-hashed snapshot of the Reference Guide, architectural diagrams, task board, and approval record is sealed.
* **Evidence**: Validation of `authority.json` against `authority.schema.json`.
* **Stop Conditions**: File hashes do not match the current working copy on disk.
* **Next Unlock**: Stage 5 (Implementation).

### Stage 5: Bounded Implementation
* **Inputs**: Locked snapshot, claimed task from `tasks.md`.
* **Outputs**: Code diff in whitelisted allowed files, task claim lockfile `.acdf/changes/<change-id>/claims/<task-id>.<agent-id>.json`, and entry in `.acdf/changes/<change-id>/state-log.ndjson`.
* **Binary Gate**: Claim file matches the active schema. Bounded loop runs under budget (default 2 cycles, hard maximum 5 only with recorded approval, max 3 files edited).
* **Evidence**: File writes restricted to whitelisted zones. Write events appended to the audit NDJSON log.
* **Stop Conditions**: Implementation requires scope expansion, touching forbidden files, or loop budget overrun.
* **Next Unlock**: Stage 6 (Binary Verification).

### Stage 6: Binary Verification
* **Inputs**: Completed task code diff, compiler/test runner commands.
* **Outputs**: `.acdf/changes/<change-id>/evidence/<task-id>_verify.log` and `.acdf/changes/<change-id>/receipts/<task-id>.json`.
* **Binary Gate**: Code compiles clean, types check successfully, linters exit 0, and all unit/integration tests pass.
* **Evidence**: Validated `receipt.json` against `receipt.schema.json` containing the exact verification commands and raw shell outputs.
* **Stop Conditions**: Compiler warnings are generated, or a test run fails.
* **Next Unlock**: Stage 6.5 (Live Smoke Testing) or Stage 7 (Stabilization).

### Stage 6.5: Live Smoke Testing
* **Inputs**: Compiled application build, E2E browser test scripts.
* **Outputs**: `.acdf/changes/<change-id>/smoke_report.md` with E2E outputs and screenshots.
* **Binary Gate**: The primary user E2E path executes successfully in a headless browser or live sandbox.
* **Evidence**: Smoke report matches E2E path log criteria with visual artifacts.
* **Stop Conditions**: Renders misaligned elements, misses loading/error states, or crashes on token retrieval.
* **Next Unlock**: Stage 7 (Stabilization).

### Stage 7: Stabilization & Runbook
* **Inputs**: All tasks marked DONE, task receipts and verify reports, and checks run against the combined artifact by the named integrator. Individual lane passes alone do not establish integration success.
* **Outputs**: `.acdf/changes/<change-id>/RUNBOOK.md` detailing cold-start deployment, configuration, and rollback.
* **Binary Gate**: A clean agent environment can successfully deploy, boot, and verify the app using only the runbook.
* **Evidence**: Exit 0 on runbook validation checks.
* **Stop Conditions**: The runbook requires implicit parameters or manual intervention steps.
* **Next Unlock**: Stage 8 (Retrospective).

### Stage 8: Retrospective
* **Inputs**: Completed change container, receipts, and ledger log.
* **Outputs**: `.acdf/changes/<change-id>/retrospective.md` containing learning cards, actual role/lens/context records, and links from failures to prevention evidence. Do not claim lens or swarm gains without comparable runs.
* **Binary Gate**: At least one static enforcement check (lint check, AST validator, or unit check) is added to the active Reference Guide to prevent recurrence of any observed failures.
* **Evidence**: Delta sync commit merging change specs into project specifications and archiving the change container to `.acdf/archive/`.
* **Stop Conditions**: Failure logs contain unresolved bugs or no static prevention rules are written.
* **Next Unlock**: Transition complete.
