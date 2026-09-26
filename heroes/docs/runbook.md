# Council library runbook

## Start and verify

This folder is a Markdown library. There is no application startup, deployment, or release command defined here. Start with [README](../README.md), then the shared guide and selected card. No environment variables or external services are required to read the local library. Notebook/source access is needed only for attribution verification; access has not been verified.

Within ACDF, run `python3 scripts/verify_acdf_repo.py` from the repository root. For a standalone copy, use host-provided documentation checks. For documentation changes, inspect the changed text, resolve relative Markdown links, confirm all 17 cards appear in the index, and check that task handoff fields remain present. Use Python 3 if available for local checks; do not install a runtime without approval. The maintenance record belongs in [the learning log](learning-log.md). Runtime tests belong to each target project's approved plan.

## Regular maintenance and healthy state

After a card or routing change, check links, scope, examples, attribution labels, and conflicts with the execution contract. Review actual run evidence before changing routing guidance. Healthy means required handoffs are complete, document links resolve, source claims are distinguishable from council synthesis, and outcome claims have run evidence. No automated monitor or alert is configured.

## Failure response and recovery

- Broken link: correct the documented path and rerun the link check.
- Conflicting instruction: retain the project gate, record the conflict, and request a decision if resolution changes approved scope or security policy.
- Unverifiable attribution: label it unresolved; do not present it as a verified expert rule.
- Poor trial outcome: preserve the evidence, inspect the cause, and propose a bounded correction before rerunning.
- Incorrect edit: restore the affected text from a verified prior copy or version history, preserving unrelated edits. This folder's backup/version-control arrangement has not been verified.

Escalate material decisions to Alan or the named project integration owner. No alternate on-call owner is configured. Never place secrets or sensitive raw task data in run records; use approved evidence locations. If such data is exposed, stop further sharing and follow the affected project's incident procedure. No incident-response infrastructure is established by this library.

Outcome measures: acceptance completion, human rework, confirmed review findings, escaped defects over a stated window, elapsed time, and measured cost. See [evaluation](evaluation.md); no targets have been set.
