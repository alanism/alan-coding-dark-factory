# ACDF learning log

## acdf-v9-20260926

- **Changed:** lifecycle-wide and standalone council routing; 17 maintained cards with provenance; stage-aware task handoffs; coordination protocol, fixtures and declaration checker; migration/runbook/curriculum; portable navigation and narrower verifier claims.
- **Initial failure:** the user's original checkout lacked a tracked tiny-change evidence log and was one commit behind upstream. Its baseline verifier failed; no implementation occurred there.
- **Root cause:** local worktree state differed from the clean upstream snapshot. The deletion's intent was unknown and was preserved.
- **Resolution:** used an isolated worktree at upstream eceaa7491baa2d8912fcfb44a2fcc8b68718e479; clean baseline passed.
- **Test-first evidence:** coordination tests initially failed because the new validator did not yet exist. After implementation, the 15 initial tests passed. This was an intentional red stage, not a production failure.
- **Prevention:** validate a clean baseline while preserving user changes; inspect actual execution limits instead of treating prose or a green repository check as a security guarantee.
- **Harness update:** negative tests for concurrent ownership, dependencies, reviewer writes, missing handoffs, budgets, malformed paths and command non-execution; provenance/link checks to catch documentation drift.
- **Reference-guide recommendation:** keep runtime-specific limits and source claims versioned; distinguish host-enforced permissions from declaration checks.
- **Build-plan recommendation:** separate protocol validation, source verification, runtime integration and performance evaluation. Specify pilot tasks/budgets/adoption criteria before benchmarking.
- **Unresolved:** primary notebook claims not reverified; no live swarm benchmark, independent multi-model review, runtime sandbox/claim implementation or full legacy schema-validation upgrade. Existing approval arithmetic and schemas remain unchanged.

Actual final command evidence is recorded in the change ledger. This log does not claim deployment, publication or measured productivity gains.
