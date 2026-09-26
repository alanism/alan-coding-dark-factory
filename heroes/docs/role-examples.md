# Worked operational examples

Council synthesis. All scenarios below are illustrative; no test results or defects are claimed. Apply the approved plan and project gates. A role does not require a separate agent.

| Role / activation | Useful deliverable and evidence | Poor application | No finding / escalation |
|---|---|---|---|
| Reviewer: an approved retry fix changes persistence behavior | Cite the exact branch that can duplicate a write; supply inputs, expected/actual state, and a reproducer or explicit reasoning if execution is unavailable | Report stylistic preferences as defects or invent file/line evidence | Say no actionable finding when none is supported; disclose untested paths. Escalate undefined retry semantics |
| Test designer: a specified transformation mishandles empty input | Derive expected output from the spec, show the test fail on the original and pass after the fix, record command outputs | Copy implementation logic into the expected result | Do not invent expected behavior when the spec is silent; request the missing decision |
| Refactorer: an approved cleanup removes duplicate parsing | Compare representative valid and invalid inputs before/after, run required checks, identify removed complexity | Change accepted inputs while calling it cleanup | Recommend no change if removal adds complexity; escalate any required behavior change |
| Exploratory QA: a dialog changes keyboard interaction | Record environment, steps, expected focus behavior, observed behavior, evidence, and retest | Treat a screenshot as proof that keyboard use works | Report no issue only for exercised journeys; mark unavailable assistive-tech checks unverified |
| Integrator: separately prepared changes are ready to combine | Inspect each artifact, reconcile interfaces, run combined gates, identify release authority and rollback evidence | Trust lane summaries or treat individual passes as a combined pass | Keep integration incomplete when required checks cannot run; escalate incompatible contracts |

A useful finding describes a supported consequence and the smallest corrective action. “No finding” is valid; it must not imply untested behavior was verified. Operational incidents and acceptance thresholds remain owned by the project, not these examples.
