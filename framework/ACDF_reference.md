# ACDF v9 Reference Specifier — Implementation Contract

This document governs the format, creation, and compilation of the **Stage 1 Project Reference Guide** (`.acdf/reference/guide.md`).

---

## 1. Specifications as the Source of Truth

In ACDF, specifications are not advisory documentation; they are strict implementation contracts. If a feature behavior, API endpoint, or database column is not declared in the Reference Guide, it cannot be implemented.

The Reference Guide must contain:
1. **API Endpoints**: Input/output schemas, authorization headers, and error payload structures.
2. **Data Schemas**: Database table constraints, column data types, and primary/foreign key relationships.
3. **System Invariants**: Strict rules (e.g. "Negative transaction amounts are forbidden").
4. **Trust Zones**: Network boundaries and permission containment rules.
5. **Knowledge Provenance**: NotebookLM title, ID, public share URL, MCP access mode, extraction rounds, and source gaps for every imported guide or Hero Lens.
6. **Approval Policy**: The selected human-led or council-led mode, eligible council members, quorum, majority rule, and hard-stop decisions that always require a human.

---

## 2. Ingestion & Stress-Testing Workflow

To ensure the Reference Guide is robust, it must be compiled and stress-tested using these core workflows:

### A. NotebookLM Ingestion
New spec invariants and heuristics are extracted from public shared notebooks listed in [`docs/notebooklm-inventory.md`](../docs/notebooklm-inventory.md) using the read-only NotebookLM MCP workflow in [`docs/coding-reference-guide-process.md`](../docs/coding-reference-guide-process.md). The extracted principles become rules in `.acdf/reference/guide.md` only after source gaps and provenance are recorded.

### B. Multi-Model Adversarial Review
Before the spec is finalized, the selected approval mode runs the [Multi-Model Adversarial Review Workflow](ACDF_multimodel_review.md) to stress-test the schemas, state limits, and trust zones against multiple independent frontier models and the individual council cards under [`heroes/`](../heroes/).

---

## 3. The Spec Audit Checklist (The "Ten No's")

Every Reference Guide update must satisfy the following checklist before transition to Stage 2:
1. **No TBD Placeholders**: All variables and constants must be fully defined.
2. **No Implicit Behaviors**: Do not assume the model knows how an external provider behaves.
3. **No Unbounded Strings**: Every text input must have a character size limit.
4. **No Untested Error States**: Every API call must define failure responses.
5. **No Blind Trust**: Any input crossing a trust zone must be sanitized.
6. **No Undocumented Constants**: Port numbers, paths, and timeouts must be hardcoded.
7. **No Multi-Actor Ambiguity**: Define transaction locks for concurrent users.
8. **No Orphaned States**: Define recovery states for interrupted operations.
9. **No Code Without Test Coverage**: Every invariant must be mapped to a binary gate.
10. **No Forbidden Writes**: Ensure files in the forbidden list are untouched.
11. **No Unrecorded Decisions**: Every delegated council decision has a voter-by-voter record, quorum proof, strict-majority result, dissent, and rationale; hard stops have human approval.
