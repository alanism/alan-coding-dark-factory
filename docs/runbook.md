# ACDF v9 repository runbook

## Start and check

This repository is a protocol and artifact library. No application server, deployment command, hosted service, environment variables or credentials are required for local validation. Python 3.9 or later is sufficient; the checks use only the standard library. Start with [README](../README.md).

From the repository root:

```sh
python3 scripts/verify_acdf_repo.py
python3 -m unittest discover -s tests -v
python3 scripts/verify_coordination.py examples/coordination/single.json
python3 scripts/verify_coordination.py examples/coordination/parallel.json
```

Healthy: all commands exit 0, changed documentation links resolve, 17 cards match the recorded shipped hashes, and negative contract tests reject invalid declarations. This is not evidence that a target application works or that runtime access controls exist.

## Regular maintenance

After changing routing/cards/contracts, run both the repository verifier and test suite. Review scope, attribution and approval-policy consistency. Update provenance only for an intentional reviewed card change; keep original source hashes and explain adaptations. Keep task run evidence in approved locations without secrets or private raw data. Compare lens effectiveness using the evaluation protocol; do not optimize for PR count or eloquence.

## Failures and recovery

| Failure | Response |
|---|---|
| Missing file or broken link | Inspect the actual change and restore/correct the intended artifact; rerun the affected check |
| Card hash differs | Review the edit; either restore the pinned card or deliberately update its shipped hash and adaptation record |
| Coordination collision or cycle | Correct ownership/dependencies in the plan before dispatch; do not bypass the check |
| Missing/invalid authority or approval | Stop target-project execution and obtain the decision required by its policy |
| Runtime claim conflict or stale claim | Use the host's coordinator and existing escalation procedure; never delete another agent's claim automatically |
| Combined checks fail | Preserve individual and integration evidence, block dependents, diagnose and fix within scope |
| Source attribution cannot be verified | Label it unresolved; do not convert it into mandatory project policy |

The responsible owner is Alan or the target project's named integration owner. No alert service, scheduled monitor or alternate on-call rotation is configured here. For a security incident, stop further exposure and follow the affected host/project procedure; this repository does not supply incident infrastructure.

## Release and rollback

Review the v9 diff, checks, migration notes and unresolved limitations before merging/publishing under the existing approval policy. There is no automatic release command. Preserve the original checkout and unrelated edits. Roll back using a known prior revision in an isolated checkout, then verify the project's approved references and authority; do not reset or overwrite uncommitted user work.

## Verification boundaries

The coordination checker never executes contract commands or authenticates approvals. The documentation checker verifies local link targets (not remote URLs or anchor fragments), card coverage/hashes and selected routing fields. The legacy repository verifier checks JSON syntax and selected example fields, not full JSON Schema semantics. Mermaid rendering, live swarm behavior, source notebooks, host permissions and performance benchmarks are separate validations; none is implied by these checks.
