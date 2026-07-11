# ACDF v8 Verification — Gates & Smoke Testing

This document governs **Stage 6 (Verification)** and **Stage 6.5 (Live Smoke Testing)**.

---

## 1. Stage 6: Binary Gates

Every task must pass a strict verification gate. Gates are binary. No partial passes are permitted. If any verification check fails, the task is **FAILED** and the execution state transitions to **BLOCKED**.

### 1.1 Gate Check Order
1. **Compilation Check**: Assert that the build process exits 0.
2. **Typecheck & Linter Check**: Assert that TS typecheck is clean and eslint/prettier exit 0.
3. **Unit & Integration Tests**: Run tests whitelisted in the task board.
4. **Approval Record Check**: Confirm the authority snapshot contains a valid human or council decision record; council approvals must show quorum and strict majority, and hard stops must show human approval.

### 1.2 Telemetry Logging
Write all terminal outputs and test logs to `.acdf/changes/<change-id>/evidence/<task-id>_verify.log`. Do not truncate error stacks or stack traces.

---

## 2. Stage 6.5: Headless E2E Smoke Testing

Unit tests run in simulated node processes. Real browser bugs (token isolation, layout alignment, storage syncs) must be verified through E2E smoke tests.

### 2.1 Smoke Test Requirements
* **Runtime Verification**: The application server must be booted locally in a background process.
* **Interaction Flow**: Run headless browser automation (Playwright/Puppeteer) to walk the primary user path.
* **Capture Evidence**: Save network logs, console trace maps, and E2E screenshots.
* **Approval evidence**: Preserve the decision record and proposal hash alongside the change evidence so the approval is reproducible.

### 2.2 Smoke Report Format
Save E2E results to `.acdf/changes/<change-id>/smoke_report.md`. The report must list all tested paths, verified console warnings, and relative paths to screenshots stored under `.acdf/changes/<change-id>/evidence/`.
