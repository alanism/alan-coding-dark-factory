# AGENTS.md — ACDF v8 Entry Point

Welcome, Agent. This repository contains the protocol rules and validation schemas for **Alan Coding Dark Factory (ACDF) v8**. 

Read this routing guide before executing tasks or modifying files in this workspace.

---

## File Routing Map

| Target Phase | Framework Document | Purpose |
|---|---|---|
| Main operating principles | [ACDF_kernel.md](file:///Users/alannguyen/Documents/Vibe%20Code/alan-coding-dark-factory/framework/ACDF_kernel.md) | Canonical doctrine binding. Read first. |
| Stage Progression | [ACDF_lifecycle.md](file:///Users/alannguyen/Documents/Vibe%20Code/alan-coding-dark-factory/framework/ACDF_lifecycle.md) | Gated progression map for Stages 0–8. |
| Multi-Model Review | [ACDF_multimodel_review.md](file:///Users/alannguyen/Documents/Vibe%20Code/alan-coding-dark-factory/framework/ACDF_multimodel_review.md) | Human-guided blind review & NotebookLM pipeline. |
| Authority snaps | [ACDF_authority.md](file:///Users/alannguyen/Documents/Vibe%20Code/alan-coding-dark-factory/framework/ACDF_authority.md) | Content-hashed snaps locking change limits. |
| Execution / claims | [ACDF_execution.md](file:///Users/alannguyen/Documents/Vibe%20Code/alan-coding-dark-factory/framework/ACDF_execution.md) | Task board claim locks, loops, and runbooks. |
| Binary gates / smoke testing | [ACDF_verify.md](file:///Users/alannguyen/Documents/Vibe%20Code/alan-coding-dark-factory/framework/ACDF_verify.md) | Compilers, test logs, and headless browser evidence. |
| Advisory lenses | [ACDF_hero_lenses.md](file:///Users/alannguyen/Documents/Vibe%20Code/alan-coding-dark-factory/framework/ACDF_hero_lenses.md) | Curated expert heuristics (advisory check). |
| Learning Curriculum | [learn/README.md](file:///Users/alannguyen/Documents/Vibe%20Code/alan-coding-dark-factory/learn/README.md) | Curriculum for engineering thinking. |

---

## Directives for AI Agents

1. **Gated, Not Fluid**: You must walk stages 0 to 8 sequentially. Do not create tasks or implement code changes unless the preceding gates are locked.
2. **Read-Only Lock**: You can only modify files explicitly whitelisted in the active `authority.json` for your claimed task.
3. **No Spec Hallucination**: If a configuration parameter, API interface type, or validation threshold is missing from the project's Reference Guide, STOP and write the spec gap to the change ledger.
