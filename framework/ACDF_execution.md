# ACDF v8 Execution — Task Claims and Bounded Loops

This document governs **Stage 5 (Implementation)** and **Stage 7 (Stabilization & Runbooks)**.

---

## 1. Task Claims and Audit Logging

To coordinate multiple independent agents without task collision, ACDF v8 enforces lockfiles and NDJSON state logging.

### 1.1 Claiming a Task
Before modifying any files:
1. Confirm the task status in `tasks.md` is `TODO` and all dependencies are `DONE`.
2. Write a JSON lockfile to `.acdf/changes/<change-id>/claims/<task-id>.<agent-id>.json`.
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
* **Max Cycles**: 2 cycles (hard maximum 5).
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
