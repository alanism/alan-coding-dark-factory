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
