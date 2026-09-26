# Imported council learning record

The entry below describes the earlier standalone library maintenance, not the ACDF v9 verification run. See [ACDF learning log](../../docs/learning-log.md) for this integration.

# Learning log

## council-docs-20260926-01

- Authorization: user approved the assessment recommendations in this conversation (“ok proceed with your recommendations”). Scope: documentation improvements, examples, and evaluation preparation.
- Changed: compact index; execution boundaries and worked examples in 17 cards; compiler/memory qualifications; handoff fields; role examples; evaluation protocol; maintenance runbook.
- Failure observed in assessment: older universal prescriptions conflicted with conditional guidance and the post-plan execution contract. No command failures during editing.
- Root cause: card-local wording and historical runtime examples were not consistently reconciled with the shared router.
- Resolution: put the execution boundary in each card, repair the identified compiler/memory conflicts, and label new examples as Council synthesis.
- Prevention: review card-local headings, rules, and summaries together; record approved plan/spec/card versions in handoffs.
- Suggested harness update: automate relative-link, card-index coverage, and handoff-field checks if future maintenance volume justifies it. Semantic conflicts still require review.
- Suggested reference-guide update: maintain source date/version and verification status for numeric or universal prescriptions; underlying sources were not reverified in this task.
- Suggested build-plan improvement: distinguish documentation completion from evaluation execution and define trial budgets and adoption criteria before benchmarking.
- Unresolved risks: remaining historical attributions need source review; no demonstrated performance gain; no runtime or connected harness assessed. No project security policy or AGENTS.md was changed.
- Validation: local Python checks cover relative Markdown links, 17-card index/example/boundary coverage, handoff fields, and the specific compiler/memory conflicts. Two identical runs passed; this is structural validation, not a complete semantic or source audit.
