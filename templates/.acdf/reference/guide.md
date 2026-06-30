# REFERENCE_GUIDE.md — Project Specifications

This guide is the canonical contract for all system schemas, constants, behavioral invariants, and API paths. 

If a rule or value is not explicitly documented here, it does not exist. Do not guess or infer.

---

## 1. System Constants

* `CONST_NAME`: Value (Sourced explanation)

---

## 2. API & Data Schemas

Include explicit types or schemas:

```typescript
// Define interfaces here
```

---

## 3. Core Invariants

* `INV-01`: Absolute rule that cannot be violated under any execution state.

---

## 4. Operational Invariants

* `OP-01`: Logging, retry, timeout, or circuit-breaker behaviors.
