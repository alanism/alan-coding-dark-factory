# Council evaluation protocol

Status: protocol only; no benchmark runs or measured improvements yet. Obtain an approved task set, budget, environment, and acceptance criteria before execution. This document does not authorize production actions or additional agents.

## Comparison design

Compare the same approved tasks from the same starting snapshot under:

- No hero lens: project instructions, approved plan, specification, and required safety context remain loaded.
- One relevant lens: the same baseline plus the selected card.
- A justified pairing: the same baseline plus a second card owning a different concern.

Hold model/version, effort, tools, permissions, verifier, task limits, and acceptance checks constant. Use fresh isolated state for each run; do not let later runs inherit earlier solutions. Record ordering and repeat counts agreed before starting. Vary or counterbalance order where practical and report stochastic variation. Judge artifacts without lens labels where feasible. Document deviations and blocked runs rather than silently dropping them.

Test selective loading separately from lens count: compare the same lens with the relevant context versus broader library loading. Otherwise savings cannot be attributed to loading strategy. Never drop mandatory context.

## Run record template

```text
Run ID / task ID / task class / risk:
Plan version / approval evidence / spec version:
Starting artifact revision or hash:
Condition / lens / card revision or hash / loaded sections:
Model version / effort / harness / tools / permissions:
Budget / run order / elapsed time:
Artifact / raw command outputs / verifier identity:
Required checks passed / total required / checks unavailable:
Human rework (recorded effort and cause):
Reviewer findings: confirmed / rejected / unresolved:
Escaped defects: observation window / observed defects / unknowns:
Tokens and cost: measured values or unavailable:
Outcome: completed / failed / blocked:
Confounders / limitations:
```

## Interpretation

Report check completion as passed checks divided by required checks; a task is complete only when all required gates pass. Report confirmed finding precision as confirmed findings divided by adjudicated findings; with no adjudicated findings, report not applicable. Keep unresolved findings visible. Do not infer recall unless a known defect set exists. Do not treat an unobserved escaped defect as proof of absence; name the observation window.

Compare quality, rework, elapsed time, and cost together. Do not select a lens on verbosity or raw output count. Missing cost data stays unavailable, not zero. Agree task-specific adoption criteria before trials; this protocol supplies no invented quality thresholds. A small pilot supports a provisional decision, not a universal ranking.

## Learning and promotion

Link each repeated failure to its run evidence, proposed documentation/check change, authorized revision, and follow-up run. Keep an unchanged holdout for validation. Adopt, revise, or retire guidance based on outcomes; preserve rejected alternatives and unresolved attribution questions. No automatic edits to cards or project policy.
