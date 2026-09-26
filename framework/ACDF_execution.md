# ACDF v9 Execution — Task Claims and Bounded Loops

This document governs **Stage 5 (Implementation)** and **Stage 7 (Stabilization & Runbooks)**.

---

## 1. Task Claims and Audit Logging

To coordinate multiple independent agents without task collision, ACDF v9 requires claim records and NDJSON state logging. This repository does not implement atomic claim acquisition; the host coordinator must serialize acquisition or supply an atomic claim service. A check-then-write sequence alone is not collision-safe.

### 1.1 Claiming a Task
Before modifying any files:
1. Validate the approved plan/spec and authority versions, assigned role/lens, allowed context, write boundary and gate evidence. Confirm the task status in `tasks.md` is `TODO` and all dependencies are `DONE`.
2. Through the host's serialized or atomic claim mechanism, write a JSON lockfile to `.acdf/changes/<change-id>/claims/<task-id>.<agent-id>.json`.
3. Append a claim event to the NDJSON log: `.acdf/changes/<change-id>/state-log.ndjson`.

### 1.2 Collision Rule
If a claim lockfile already exists for `<task-id>`, do not overwrite it. Skip the task. If a claim lockfile is stale (longer than the agent timeout limit), escalate to the human—do not delete it autonomously.

---

## 2. Bounded Implementation Loop

Agents execute within strict execution budgets.

### 2.1 The Cycle
```text
Observe (Read state) ──► Diagnose (Isolate cause) ──► Act (Edit code) ──► Verify (Test gate) ──► Decide
```

### 2.2 Loop Budgets
* **Max Cycles**: Default 2 cycles; extending beyond 2 requires recorded approval, with the existing hard maximum of 5. A subagent inherits the task budget; delegation does not reset it.
* **Max Files Modified**: 3 files.
* **Stop Conditions**: Halt and write to `BUILD_LEDGER.md` if:
  - Allowed files whitelist is violated.
  - The root cause is unclear or speculative.
  - Code changes require altering schemas not defined in the Reference Guide.

---

## 3. The Task Receipt Contract

Every completed task must write a receipt to `.acdf/changes/<change-id>/receipts/<task-id>.json` validating against `receipt.schema.json`.

```json
{
  "taskId": "task-01",
  "agentId": "agent-runner-x",
  "timestamp": "2026-06-30T16:00:00Z",
  "status": "PASS",
  "planned_change": "Write validation functions",
  "actual_change": "Implemented validation helpers inside utils.js",
  "verification_command": "npm run test:validate",
  "evidence_file": "evidence/task-01_verify.log",
  "prevention": "Added lint check enforcing parameter definitions."
}
```

---

## 4. Stage 7 Runbooks
When all tasks in `tasks.md` are marked DONE, compile `.acdf/changes/<change-id>/RUNBOOK.md`. The runbook must cover:
* Environment specifications and setup checks.
* Single-command deployment paths.
* Rollback procedures to revert database migrations, system configurations, or feature flags.

## 5. V9 role and handoff contract

Use [the task contract](../templates/agent_task_contract.md) and [coordination profile](ACDF_coordination.md). Record operational role, optional lens, actual model/agent, plan/spec versions, context, owned files, dependencies, limits, acceptance checks, output artifact, evidence and one integration owner. Plan generation belongs to explicitly assigned upstream work; implementers stop on material plan gaps.

One agent is appropriate for coupled tasks. Parallel writers need separate workspaces and non-overlapping ownership or explicit dependency ordering. Reviewers inspect an immutable artifact and cannot write the implementation under review. When a lane blocks, preserve its evidence and block dependents; unrelated approved lanes may continue. Never silently reclaim another agent's stale claim.

Before Stage 7, the integrator inspects each result, applies changes in dependency order and runs the approved checks on the combined artifact. Conflicting interfaces or new scope return to the plan owner. A task receipt or coordination-check pass is not merge/deploy approval.
