# ACDF v9 Coordination — Roles, Lanes and Integration

This profile describes reviewable assignments for a single agent or multiple agents. It is a companion to the existing task board, authority, claims and receipts, not their replacement. Use it when planning coordinated work; adopting it does not grant permission to launch agents.

## Minimum useful topology

Use one agent for tightly coupled or small tasks. Parallelize only independently owned tasks after prerequisites pass. Name each lane `role / optional-lens / task-id`; record the actual agent separately. An integrator owns the combined result. The integrator may be the same person/agent in a single-agent workflow; self-checks must not be described as independent review.

Planning and review lanes can exist upstream, and implementation/QA/integration lanes downstream. The manifest describes planned assignments; `stage` names its starting stage. Later review/integration roles remain queued until their own lifecycle gates unlock. A dependency edge never unlocks a lifecycle stage; the host checks both dependencies and stage authority before dispatch. Standalone council users may use the plain [task contract](../templates/agent_task_contract.md) with their own host rules.

## Contract version 1

Copy [coordination.json](../templates/.acdf/changes/_template/coordination.json), replacing the illustrative references. Paths in `write_files`, `workspace`, `output_artifact` and handoff `evidence` are exact repository-relative POSIX paths: no absolute paths, traversal, glob patterns, empty segments or case-only aliases. Resolve broad task-board globs to explicit owned files for this profile.

| Field | Required meaning |
|---|---|
| `contract_version` | Integer `1`, independent of ACDF release version |
| `mode` | `single` or `parallel`; single has one distinct agent, parallel has at least two |
| `stage` | `planning`, `review`, `execution`, `verification`, `integration`, or `learning`; actual gate evidence lives in the approval/authority packet |
| `approval_mode`, `approval_ref` | `human` or `council` and the existing decision record reference; neither is an approval assertion |
| `plan_ref`, `spec_ref` | Nonempty versioned references to the assigned plan and specification (for upstream work, identify the approved brief/reference draft) |
| `integration_owner` | Actual agent ID present in the lanes; must own the integration-role lane |
| `lanes` | Nonempty list with unique `task_id` values in existing `task-N` form |
| Lane identity | `agent_id`, `role` and `hero_lens` (nonempty string or `null`); roles: planner, reviewer, implementer, test-designer, qa, integrator, learning |
| Lane dependencies | `dependencies`: task IDs completed before this lane can start; no unknown IDs, self-links or cycles |
| Lane ownership | `workspace`, `write_files`, `output_artifact`; output must be among owned files; artifact paths must be unique across lanes |
| Lane context | `context`: nonempty list of versioned instructions, spec, selected card and evidence references; mandatory project context is retained |
| Lane checks | `acceptance_checks` and `stop_conditions`: nonempty string lists; commands are descriptions and are never executed by the checker |
| Lane budget | `budget.max_cycles`: default 2, hard maximum 5; values above 2 need `extension_approval_ref`. `budget.max_files`: positive integer no greater than the existing maximum 3 and at least the owned file count |
| Lane handoff | `handoff.artifact`: equals output; `handoff.evidence`: nonempty expected evidence paths; `handoff.unresolved`: list of known gaps; `handoff.recipient`: integration owner |

Planning manifests name expected artifacts and evidence. They do not imply the files exist or gates have passed. Preserve actual commands/results and gaps in execution receipts. Do not mark completion based on manifest validation.

## Ownership and independence rules

Every concurrent pair must have distinct actual agents and, when both write, distinct workspaces and disjoint owned files. A dependency path orders lanes sharing files or an agent. Worktree isolation alone does not make conflicting changes independent. Paths are compared case-insensitively to catch aliases on common local filesystems.

Reviewers may write only their declared review output. QA and test-design roles may own appropriate tests/evidence under explicit task scope. Do not permit reviewers to patch implementation while claiming independent review. Give reviewers a pinned artifact and acceptance criteria, record what they independently inspected, and disclose shared model/context limitations.

The integration-role lane owned by `integration_owner` must depend transitively on every other lane. It may own files already changed by prerequisites, within the existing file limit. For larger integrations, split work into bounded tasks instead of increasing the limit. Run combined checks before declaring the change complete. One agent may implement and later integrate sequentially; this is not independent verification.

## Claim, block and recovery protocol

Validate authority and the manifest before dispatch. The host must serialize or atomically acquire claims; this repository supplies no claim service. Existing stale-claim escalation remains. Stop and preserve evidence on unknown causes, scope expansion, exceeded budgets, denied permissions or failed gates. Block dependent tasks; do not reset budgets by spawning replacements. The integrator reports interface conflicts to the plan owner and obtains any required new approval before editing the contract or resealing authority.

For a handoff, record the artifact revision, actual checks and evidence paths, remaining gaps and receiving owner. Reviewers never inherit “PASS” from another lane as fact. Role selection and orchestration do not add eligible voters or change council quorum.

## Validation and limits

```sh
python3 scripts/verify_coordination.py examples/coordination/single.json
python3 scripts/verify_coordination.py examples/coordination/parallel.json
python3 -m unittest discover -s tests -v
```

The checker validates shape, required references, budgets, ownership and dependency consistency. It does not access the network, run embedded commands, authenticate an approval, check evidence existence, resolve filesystem symlinks, acquire locks, create worktrees, enforce permissions, launch agents or establish independent review. The host must canonicalize real paths and verify all external state before granting access. No claim of runtime security follows from a pass.
