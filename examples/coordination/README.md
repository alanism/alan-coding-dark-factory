# Coordination examples

These are synthetic planning fixtures, not records of executed work or valid authority grants. Referenced source files, workspaces, approvals and evidence are illustrative and are not expected to exist. Replace them before adopting the profile.

- [Single](single.json): one agent implements a small configuration change, then integrates sequentially. It provides no independent review.
- [Parallel](parallel.json): two agents own disjoint changes, a separate reviewer inspects their pinned artifacts, and one integrator checks the combined result. Stage 3 approval/review is assumed to be supplied by real upstream evidence; this example does not replace it.

Run `python3 scripts/verify_coordination.py examples/coordination/single.json` and the corresponding `parallel.json` command from the repository root. A pass validates the declarations, not the underlying application.

## Negative cases covered by tests

| Change to fixture | Expected result / recovery |
|---|---|
| Independent writers claim the same file or workspace | Reject; split ownership or add a genuine dependency before dispatch |
| Dependency references itself, an unknown task or a cycle | Reject; return the task graph to its owner |
| Reviewer claims an implementation file | Reject; preserve review independence and route fixes to an implementer |
| Missing evidence, checks, context or handoff recipient | Reject; complete the contract |
| File count exceeds three or cycles exceed five | Reject; split tasks; do not raise existing limits |
| More than two cycles without recorded extension approval | Reject; obtain the existing required approval or use the default budget |
| Integrator does not depend on every lane | Reject; prevent premature integration |
| Absolute, traversal, glob or case-aliased owned paths | Reject; use explicit, canonical ownership declarations |

For a blocked handoff in a real run, retain the failed lane's evidence, mark dependent work blocked and notify the integration owner. Never create a replacement agent to evade the original budget. Council-led examples do not grant approval: the selected policy and its real vote record still govern.
