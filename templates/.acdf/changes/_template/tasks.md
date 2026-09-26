# Execution Tasks: [Change Name]

- **Status**: GATED

---

## Phase 1: Foundations

- `[ ]` **task-1**: [Task description]
  - **Dependencies**: None
  - **Allowed Files**: `["src/path/**/*"]`
  - **Forbidden Files**: `["src/auth/**/*"]`
  - **Binary Gate**: `npm run test:foundation`

## Phase 2: Wiring

- `[ ]` **task-2**: [Task description]
  - **Dependencies**: `["task-1"]`
  - **Allowed Files**: `["src/path/**/*"]`
  - **Forbidden Files**: `["src/auth/**/*"]`
  - **Binary Gate**: `npm run test:wiring`

## V9 assignment and integration

For each task, complete [the agent task contract](../../../agent_task_contract.md). Record role/lens, actual agent, approved plan/spec versions, context, owner, workspace, budget, evidence and integration recipient. When adopting the coordination profile, replace the adjacent illustrative `coordination.json` with the actual assignments, validate it, and seal it with the approved plan.

The named integrator runs approved checks on the combined artifact. Dependency completion does not waive lifecycle gates or release approval. Keep existing task budgets; split larger work into bounded tasks.
