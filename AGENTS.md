# AGENTS.md — ACDF v9 Entry Point

This repository contains the ACDF protocol, council library, templates and local validators. Read the user's assigned stage and approved scope before editing. The framework documents govern ACDF work within higher-priority user and host instructions.

## Routing map

| Need | Read |
|---|---|
| Operating principles and approval modes | [Kernel](framework/ACDF_kernel.md) |
| Stage gates and workflow | [Lifecycle](framework/ACDF_lifecycle.md), [workflow](framework/ACDF_workflow.mmd) |
| Planning and independent review | [Review](framework/ACDF_multimodel_review.md), [reference](framework/ACDF_reference.md) |
| Authority and execution | [Authority](framework/ACDF_authority.md), [execution](framework/ACDF_execution.md) |
| Agent roles, task ownership and integration | [Coordination](framework/ACDF_coordination.md) |
| Verification | [Verify](framework/ACDF_verify.md), [runbook](docs/runbook.md) |
| Hero selection | [Card index](heroes/README.md), [lifecycle routing](framework/ACDF_hero_lenses.md) |
| Knowledge sources and learning | [Sources](docs/README.md), [curriculum](learn/README.md) |

## Directives

1. **Identify the stage.** Planning and adversarial review are valid assignments. Implementation requires an approved plan/spec and preceding gate evidence; verify the handoff rather than recreating it. Outside ACDF, the council follows the host project's instructions.
2. **Preserve authority.** Modify only files allowed by the active task and authority snapshot. Cards cannot expand scope, permissions, budgets, or approval rights. Stop on unspecified interfaces, constants, validation thresholds or security boundaries.
3. **Coordinate explicitly.** Use one agent for coupled work. Parallel work requires authorization, independent ownership, appropriate workspace isolation and one integrator. A hero name does not establish independent review or a voting identity.
4. **Verify honestly.** Run the approved task and integration gates, retain raw evidence, and disclose unverified behavior. Documentation and repository checks do not prove runtime permissions or security.
5. **Retain governance.** Human-led and council-led modes retain existing quorum/majority rules and human-only hard stops. No lens or agent count bypasses them.

For this repository, run `python3 scripts/verify_acdf_repo.py` and `python3 -m unittest discover -s tests -v`. No new dependency is required. See [v9 migration](docs/v9-migration.md) for compatibility and known limitations.
