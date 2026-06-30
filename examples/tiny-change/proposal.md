# Change Proposal: Tiny Harmless Change

- **Status**: APPROVED
- **Problem**: Need to verify that the ACDF v8 protocol kernel executes correctly.
- **Job-to-be-Done (JTBD)**: Validate ACDF sequential stages with harmless configuration data.

---

## 1. Scope Boundaries

### Whitelisted (In-Scope)
* Modifying `config.txt` inside the example directory.

### Non-Goals (Explicitly Out-of-Scope)
* Modifying any actual project production source files.

---

## 2. Rollback Procedure

To roll back, delete the `config.txt` file.
