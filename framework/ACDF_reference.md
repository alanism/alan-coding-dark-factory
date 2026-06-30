# ACDF v8 Reference Specifier — Implementation Contract

This document governs the format, creation, and compilation of the **Stage 1 Project Reference Guide** (`.acdf/reference/guide.md`).

---

## 1. Specifications as the Source of Truth

In ACDF, specifications are not advisory documentation; they are strict implementation contracts. If a feature behavior, API endpoint, or database column is not declared in the Reference Guide, it cannot be implemented.

The Reference Guide must contain:
1. **API Endpoints**: Input/output schemas, authorization headers, and error payload structures.
2. **Data Schemas**: Database table constraints, column data types, and primary/foreign key relationships.
3. **System Invariants**: Strict rules (e.g. "Negative transaction amounts are forbidden").
4. **Trust Zones**: Network boundaries and permission containment rules.

---

## 2. Ingestion & Stress-Testing Workflow

To ensure the Reference Guide is robust, it must be compiled and stress-tested using these core workflows:

### A. NotebookLM Ingestion
New spec invariants and heuristics are extracted from expert engineering literature using the [NotebookLM Ingestion Workflow](file:///Users/alannguyen/Documents/Vibe%20Code/alan-coding-dark-factory/framework/ACDF_multimodel_review.md). The extracted principles become rules in `.acdf/reference/guide.md`.

### B. Multi-Model Adversarial Review
Before the spec is finalized, the human governor runs the [Multi-Model Adversarial Review Workflow](file:///Users/alannguyen/Documents/Vibe%20Code/alan-coding-dark-factory/framework/ACDF_multimodel_review.md) to stress-test the schemas, state limits, and trust zones against multiple independent frontier models.

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
