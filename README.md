# Alan Coding Dark Factory (ACDF) v9

ACDF is a governed engineering protocol for moving from intent and build plans through adversarial review, bounded implementation, verification, and learning. V9 makes the Engineering Council useful throughout that lifecycle, including single-agent tasks and coordinated subagent work.

This repository contains documentation, templates, example artifacts, and local validators. It does **not** ship a swarm scheduler, runtime permission sandbox, atomic task-claim service, or automatic deployment engine. A target project's tooling must enforce its actual permissions and execution gates.

## Start here

- **Using ACDF:** read [the kernel](framework/ACDF_kernel.md), [lifecycle](framework/ACDF_lifecycle.md), and [workflow diagram](framework/ACDF_workflow.mmd).
- **Using the council:** start with [the 17-card index](heroes/README.md) and [routing guide](heroes/how-to-use.md). The council also works independently of ACDF under the host project's instructions.
- **Planning or reviewing:** use [hero routing by stage](framework/ACDF_hero_lenses.md) and [multi-model review](framework/ACDF_multimodel_review.md).
- **Executing an approved plan:** read [execution](framework/ACDF_execution.md), [coordination](framework/ACDF_coordination.md), and [the task contract](templates/agent_task_contract.md).
- **Upgrading from v8:** follow [migration notes](docs/v9-migration.md). Existing approval modes, hard stops, schemas, and budgets are preserved.

## What changes in v9

| Area | V9 behavior |
|---|---|
| Hero use | Advisory methods for intent, planning, adversarial review, implementation, tests, QA, integration and learning |
| Agent identity | Operational role / optional hero lens / task ID; a hero name grants no permissions |
| Context | Shared instructions plus selected cards and task evidence; no automatic whole-library loading |
| Coordination | Explicit owners, dependencies, write boundaries, workspaces, budgets, handoffs and one integration owner |
| Verification | Individual task evidence followed by checks on the combined artifact |
| Learning | Recorded failures and comparison against a no-lens baseline; no claimed speedup without measurements |

A role, a lens, a model, and a voter are different things. One agent can perform several sequential roles. Independent review requires independent evidence inspection; changing the persona name does not establish independence. Additional agents are appropriate only when the work is separable and authorized.

## Lifecycle and stage boundaries

| Stage | Deliverable |
|---|---|
| 0 | Intent, success criteria and selected approval policy |
| 0.5 | Architectural models |
| 1 | Reference specification and source-backed context |
| 2 | Build plan, task graph and coordination contracts |
| 3 | Adversarial review, mitigation tasks and decision evidence |
| 4 | Approved, content-hashed execution authority |
| 5 | Claimed tasks and bounded implementation |
| 6 | Verification evidence and receipts |
| 6.5 | Relevant live smoke testing |
| 7 | Integrated result and operational runbook |
| 8 | Retrospective and prevention work |

Lifecycle gates remain ordered. Independent tasks may run concurrently **within the unlocked stage** when the approved task graph and permissions allow it. A build agent receiving a valid Stage 4 handoff verifies that handoff; it does not recreate upstream plans. When explicitly asked to plan or review upstream, an agent may perform those roles without treating implementation-only restrictions as a ban on planning. Missing or changed requirements return to the responsible owner.

## Human and council governance

The user selects **human-led** or **council-led** approval. Council-led mode requires the existing recorded quorum and strict-majority rule for routine, in-scope decisions. Authority comes from that explicit delegation, not from a hero card or the number of agents running.

Ties, missing quorum, unresolved critical dissent, scope expansion, and changed success criteria block work. Security, privacy, legal, production-release, credential, and external-data-boundary decisions retain explicit human approval. Votes cannot waive lifecycle gates, expand permissions, or replace tests. See [approval policy](templates/APPROVAL_POLICY.md) and [authority](framework/ACDF_authority.md).

## Knowledge and evidence

Curated primary material and [public NotebookLM sources](docs/notebooklm-inventory.md) inform the cards. Card updates require review; they do not automatically change project policy. [Provenance](heroes/SOURCE_MANIFEST.json) records the imported card snapshot and local adaptations. Unverified historical claims remain labeled; ingestion is not source verification.

Try the [single-agent and parallel coordination examples](examples/coordination/README.md). Use [the evaluation protocol](heroes/docs/evaluation.md) before claiming that a lens or a swarm improves quality, cost, or latency.

## Local checks

Python 3.9 or later, standard library only:

```sh
python3 scripts/verify_acdf_repo.py
python3 -m unittest discover -s tests -v
```

These are repository and contract checks, not a security certification or production acceptance suite. See [the runbook](docs/runbook.md), [learning log](docs/learning-log.md), and [learning curriculum](learn/README.md).
