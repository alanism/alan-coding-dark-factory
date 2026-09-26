# ACDF v9 Hero Lenses — Lifecycle Advisory Methods

Hero lenses inform engineering judgment throughout ACDF. They are neither authority sources nor separate job titles. Use the [maintained cards](../heroes/README.md) and [shared router](../heroes/how-to-use.md) for methods; this document owns only their ACDF integration. The council may also be used independently under a host project's instructions.

## Role, lens, model and authority

- **Role:** the work assigned, such as planner, implementer, reviewer, test designer, QA or integrator.
- **Lens:** an optional expert-inspired method for a specific bottleneck.
- **Model/agent:** the executor, with actual tools, context and limits.
- **Authority:** the approved scope and selected human-led or council-led policy.

Label work `operational-role / hero-lens-or-none / task-id`. Multiple lenses do not create multiple independent reviewers or additional votes. Record actual reviewer/model identity and what each independently inspected.

## Routing by stage

| Stage | Role / useful lens examples | Required outcome / boundary |
|---|---|---|
| 0 | Outcome assessment / Taylor, DHH | Human-owned objective and scope; no invented product demand |
| 0.5–2 | Planner / Cherny; domain actions / Carter; visual decision artifact / Thariq | Models, reference specification, task graph and acceptance checks; planning must be explicitly assigned |
| 3 | Adversarial reviewer / Carlini, Willison, or another relevant lens | Cited risks, mitigation evidence and unresolved questions; existing minimum three independent risk lenses remains |
| 4 | Readiness / Hashimoto, Lopopolo | Approved plan/spec versions, runnable gates and valid authority; a lens cannot approve its own permissions |
| 5 | Implementer / Karpathy, Cherny, Carmack, or none | Bounded diff following the approved plan; performance work needs measurements |
| 6–6.5 | Reviewer, test designer, exploratory QA / Carmack, Willison, Schaad, Ryo | Actual test and interaction evidence; disclose untested behavior |
| 7 | Integrator / Hashimoto, Cherny | Combined checks, runbook and release authority; individual passes are insufficient |
| 8 | Learning / Lopopolo, Quesnelle | Failure-to-prevention record and follow-up evidence; no automatic policy promotion |

Choose one primary lens per bounded task, adding one only for a distinct necessary concern. This context-loading default does not reduce Stage 3's existing independent-review requirements or a configured voting quorum. Different stage participants can each load only their assigned card.

## Standalone and ACDF use

Outside ACDF, use the host's task and approval rules. Within ACDF, upstream planning/review roles may create or challenge plans when assigned; Stage 5 implementers verify approved artifacts and stop on material gaps. Do not recreate approved upstream work or interpret a card's planning advice as permission to change the plan.

[Task contracts](../templates/agent_task_contract.md) connect the role and lens to the plan, scope, context, budget and evidence. [Coordination](ACDF_coordination.md) separates task dependencies from lifecycle gates. No topology is authorized merely because a card describes swarms.

## Governance and source maintenance

Under council-led policy, eligible reviewers use selected cards as advisory methods and record actual votes. The existing quorum, majority calculation and human-only hard stops remain binding. Operational role selection is not a council vote. An implementer's confidence is not independent review.

The maintained 17-card library replaces the duplicated v8 mini-doctrines and unverified ingestion counts in this file. V8's Wood summary has no corresponding maintained card in this snapshot; its removal from routing is not a claim that protocol review is unnecessary. Assign that operational review with approved domain references when needed.

Use [the card process](../docs/hero-lens-card-process.md), record primary-source support versus Council synthesis, and update [provenance](../heroes/SOURCE_MANIFEST.json) deliberately. Source material does not become an execution constraint until the responsible owner adopts it into the project specification. See [evaluation](../heroes/docs/evaluation.md) and [role examples](../heroes/docs/role-examples.md).
