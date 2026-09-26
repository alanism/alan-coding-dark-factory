# ACDF v9 Kernel — Canonical Binding Doctrine

This is the canonical binding doctrine of the **Alan Coding Dark Factory (ACDF) v9** execution protocol. It governs ACDF work within the user's approved scope and the host's instruction hierarchy; it does not override user or platform instructions.

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

### 1.1 Bounded Approval Delegation

The user selects one approval mode at Stage 0 and the choice is recorded in the change artifacts:

- **Human-led**: the human approves each decision that requires approval.
- **Council-led**: the relevant Engineering and/or Design Council reviews the decision and records individual votes, quorum, majority result, dissent, and rationale.

Council-led approval is a bounded delegation mechanism, not autonomous authority. It may approve routine, in-scope coding or design decisions only when the required quorum is met and a strict majority votes approve. A tie, missing quorum, unresolved critical dissent, scope expansion, or changed success criteria blocks the change. Security, privacy, legal, production-release, credential, and external-data-boundary decisions always require explicit human approval; a council cannot waive those hard stops or any lifecycle gate.

---

## 1.2 Stage-aware council and agent use

The council supports planning, adversarial review, implementation, verification, integration and learning. It can also be used independently of ACDF. Within ACDF, upstream work is explicitly assigned; a build agent receiving approved artifacts verifies their gate evidence without recreating them. Hero guidance remains advisory, including when used by an eligible voter under council-led policy.

Lifecycle gates remain sequential. The approved dependency graph may permit concurrent tasks within an unlocked stage. Role, hero lens, model identity and approval authority are recorded separately. The [coordination contract](ACDF_coordination.md) describes owners, dependencies, context, limits and handoffs; it grants no additional authority.

This repository supplies protocol and validation artifacts. Actual write restrictions, atomic claims, sandboxes and tool permissions require external enforcement. A passing repository check does not establish that those runtime controls exist.

## 2. Target Project Workspace Layout

A project running ACDF v9 must maintain the following file tree layout:

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

> **Does this make ACDF v9 more usable without weakening authority, evidence, or runtime truth?**

If **yes**, keep it.  
If **no**, reject it.
