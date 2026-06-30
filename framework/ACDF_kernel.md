# ACDF v8 Kernel — Canonical Binding Doctrine

This is the canonical binding doctrine of the **Alan Coding Dark Factory (ACDF) v8** execution protocol. It overrides all other guides, agent configurations, and session memories.

---

## 1. Philosophical Foundations (Six Axioms + Model-First)

All agent operations are governed by these core axioms:

1. **Model-First System Execution**: In ACDF, diagrams are not post-hoc documentation—they are executable mental models that drive specifications, authority, and implementation. Before compiling types or writing task boards, every non-trivial change must model system dynamics, sequence states, and trust zones in Mermaid format.
2. **Authority over Ambiguity**: If a requirement, parameter, rule, or validation boundary is not written down in the project's Reference Guide, it does not exist. Do not guess. Stop and request a spec update.
3. **Evidence over Assumptions**: Assertions that code "should work" or "looks complete" are rejected. Every task completion requires binary evidence (test runner logs, compilation logs, headless browser screenshots).
4. **Gates over Self-Assessment**: Agents cannot self-certify completion. Done is declared solely when a deterministic verify tool executes and returns a clean pass (exit 0).
5. **Receipts over Chat Memory**: Agent context windows are volatile. All execution decisions, reproduction steps, patches, and preventions must be recorded in version-controlled receipt logs.
6. **Runtime Truth over Planning Confidence**: A highly detailed plan that fails to boot in a clean environment is a failure. Empiricism and runtime metrics override planning confidence.
7. **Retrospective Learning over Repeated Failure**: Operational failures must compound into future security, compiler, or linter rules. Every bug patch must include a prevention rule in the Reference Guide.

---

## 2. Target Project Workspace Layout

A project running ACDF v8 must maintain the following file tree layout:

```text
.acdf/
├── reference/                  # Core Project Specifications (ReadOnly to build agents)
│   ├── guide.md                # Strict schemas, TypeScript interfaces, constants, and API paths
│   ├── trust-zones.md          # Trusted/untrusted system components and network boundaries
│   └── forbidden-files.md      # Whitelist of files agents are blocked from writing or reading
└── changes/                    # Change-scoped Execution Containers
    └── <change-id>/            # Unique subdirectory per change (e.g. add-dark-mode)
        ├── models/             # Stage 0.5: Architectural models (flow, sequence, ER, C4, etc.)
        ├── proposal.md         # Stage 2: Intent, out-of-scope non-goals, rollback procedure
        ├── design.md           # Stage 2: Technical architecture and sequence mappings
        ├── tasks.md            # Stage 2: Task board checklist with allowed write zones and gates
        ├── authority.json      # Stage 4: Locked content-hashed snapshot of specs & graph
        ├── BUILD_LEDGER.md     # Stage 5: Append-only execution history and blocked gaps
        ├── claims/             # Stage 5: Agent task claim lockfiles
        ├── state-log.ndjson    # Stage 5: NDJSON log auditing claim/release/complete events
        ├── evidence/           # Stage 6: Console outputs, compile logs, test runner files
        ├── receipts/           # Stage 6: Machine-readable JSON receipts per completed task
        └── retrospective.md    # Stage 8: Learning cards and Reference Guide updates
```

---

## 3. The Philosophy Test

Every proposed change to the framework, the project specs, or the codebase must run the following test:

> **Does this make ACDF v8 more usable without weakening authority, evidence, or runtime truth?**

If **yes**, keep it.  
If **no**, reject it.
