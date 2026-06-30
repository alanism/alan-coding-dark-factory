# Alan Coding Dark Factory (ACDF) v8

## An AI Engineering Operating System for Governing Autonomous Development

Alan Coding Dark Factory (ACDF) is an open-source engineering operating system designed to govern, constrain, and optimize autonomous software development. It provides the structured boundaries, content-hashed snapshots, and binary gates necessary to coordinate frontier AI models safely across complex, real-world codebases.

ACDF is **not** an autocomplete assistant. It is a deterministic execution container that enforces software quality, containment, and continuous organizational learning.

---

## 1. Why ACDF Exists

Software engineering is a sequence of decisions, not just a stream of characters. 

The widespread adoption of generative AI has made code synthesis cheap, but it has made engineering judgment, specification precision, and codebase safety scarce. Vague natural language instructions given directly to LLMs often result in speculative abstractions, scope sprawl, hidden technical debt, and regressions.

ACDF exists to transition AI engineering from a model of **unconstrained code generation** to a model of **governed execution**. It bounds AI agency within strict contracts, ensuring that all code modifications are structurally justified, rigorously modeled, adversarially reviewed, and programmatically verified before they are committed to the codebase.

---

## 2. Core Philosophy

ACDF is built on the following axioms:

* **Authority over Ambiguity**: If a detail is missing from the project's specification contract, execution stops. Agents are forbidden from guessing.
* **Evidence over Assumptions**: Code is only correct when empirical verification logs (compilers, test suites, E2E runners) prove it. Vibes-based assertions are rejected.
* **Gates over Self-Assessment**: Agents cannot self-certify completion. Done is declared solely by deterministic verification exit codes.
* **Receipts over Chat Memory**: Chat history is volatile context. Decisional proof is written to version-controlled receipts containing root-cause analyses and static preventions.
* **Runtime Truth over Planning Confidence**: A pristine plan that fails to compile is a failure. Empiricism and runtime metrics override planning confidence.
* **Continuous Learning over Repeated Failure**: Systemic failures must compound into future security, compiler, or linter rules to statically prevent their recurrence.

---

## 3. Why ACDF is Different

Unlike ordinary AI coding assistants that edit files directly from a chat window, ACDF introduces a structured protocol kernel:

| Dimension | Ordinary AI Coding Assistants | Alan Coding Dark Factory (ACDF) |
|---|---|---|
| **Write Scope** | Can modify any file in the workspace | Locked strictly to whitelisted files in `authority.json` |
| **Specifications** | Relies on fuzzy instructions in chat logs | Governed by a centralized, explicit `REFERENCE_GUIDE.md` |
| **Planning** | Generates code immediately | Enforces sequential gates (Stage 0 -> Stage 8) |
| **Orchestration** | Single-model generation | Multi-model review, planning, and verification |
| **Organizational Memory** | Discards chat logs after closing session | Codifies learning cards back into active project rules |
| **Diagrams & Models** | documentation artifacts | Executable mental models driving gates and tasks |

---

## 4. Multi-Model Engineering Workflows

Modern frontier models possess different reasoning strengths, latency profiles, and context-window capabilities. Betting on a single model to handle the entire software lifecycle introduces vulnerabilities.

ACDF orchestrates multiple frontier models to perform specialized engineering roles:
1. **Planning & Task Decomposition**: High-reasoning models compile specifications and trace topological task dependencies.
2. **Adversarial Review**: Critic models challenge proposed architectures and schemas.
3. **Implementation**: Surgical coding agents execute minimal diffs within whitelisted files.
4. **Verification**: Specialized testing agents execute compile loops, lint checkers, and E2E E2E runners.

This multi-model orchestration approximates the workflow benefits of a **Mixture-of-Experts (MoE) engineering pipeline**—allocating specialized tasks to models optimized for those specific roles—without requiring custom model training or specialized inference infrastructure.

---

## 5. Hero Lenses: Living Knowledge Modules

One of ACDF’s primary innovations is the **Hero Lens**—a living engineering knowledge module synthesized from curated expert engineering sources (papers, lectures, codebase audits, and technical debates).

```text
Books, Talks, Podcasts, Conference presentations, Interviews, Papers, Tweets, GitHub discussions
                                       │
                                       ▼
                                  NotebookLM
                                       │
                                       ▼
                              Knowledge Extraction
                                       │
                                       ▼
                              Engineering Doctrine
                                       │
                                       ▼
                                  Checklists
                                       │
                                       ▼
                              Evidence Requirements
                                       │
                                       ▼
                              Execution Constraints
                                       │
                                       ▼
                                   Hero Lens
```

### Living Knowledge Ingestion
* **Not Personas**: Lenses do not role-play. They are highly structured technical doctrines.
* **NotebookLM Integration**: Each lens is backed by an ingestion corpus of expert literature. As new industry standards, security vulnerabilities, or frameworks emerge, the corpus is refreshed, updating the lens heuristics without modifying ACDF itself.
* **Stage 3 Model Critique**: Lenses challenge sequence mappings, state transitions, and schemas before coding starts.
* **Advisory Governance Bounds**: *“Hero Lenses may propose risks, questions, test ideas, and implementation heuristics. They cannot grant authority, expand scope, waive gates, override user instructions, or justify touching forbidden files.”*

---

## 6. Human-in-the-Loop Responsibilities

ACDF does not aim for complete, unattended autonomy. Instead, it positions the human developer as the **governing authority** who owns critical judgment paths, while agents act as executors within bounded scopes:

* **Curating Knowledge**: Humans curate the NotebookLM ingestion sources for Hero Lenses.
* **Defining Correctness**: Humans define the project's success metrics, Job-to-be-Done (JTBD), and active trust zones.
* **Obtaining Approval**: Agents must pause and wait for explicit human approval before transitioning from planning (Stage 2/3) to execution (Stage 4).
* **Reviewing Conflicts**: When adversarial reviews flag structural contradictions, humans arbitrate the architectural decisions.

---

## 7. Repository Structure

```text
alan-coding-dark-factory/
├── README.md                   # System positioning and overview
├── AGENTS.md                   # Agent routing entry point
├── framework/                  # The core execution kernel
│   ├── ACDF_kernel.md          # Canonical binding doctrine and axioms
│   ├── ACDF_lifecycle.md       # Stage 0 to Stage 8 sequential gating rules
│   ├── ACDF_authority.md       # Content-hashed snapshots and lock rules
│   ├── ACDF_execution.md       # Claiming locks, NDJSON logs, and loop budgets
│   ├── ACDF_verify.md          # Test gate standards and smoke testing E2E reports
│   └── ACDF_hero_lenses.md     # Curated living knowledge module lens cards
├── schemas/                    # JSON Schemas enforcing machine-readable state boundaries
├── templates/                  # Scaffolds for target project workspaces
└── examples/                   # Walkthrough of a tiny golden change
```

---

## 8. Quick Start

### 1. Initialize ACDF in your project
Copy the `.acdf/` structure from the `templates/` directory to the root of your target codebase:
```bash
cp -r templates/.acdf /path/to/your/project/
```

### 2. Set the Reference Guide
Update `.acdf/reference/guide.md` with your system constants, TypeScript interfaces, and API payload definitions.

### 3. Route Your Agent
Open `AGENTS.md` in your AI coding assistant and let it route its tasks sequentially through the lifecycle.

---

## 9. Example Lifecycle Execution

ACDF enforces a sequential **Stage 0 → Stage 8** lifecycle flow:

```
[Stage 0: Explore] ──► [Stage 0.5: Model] ──► [Stage 1: Reference] ──► [Stage 2: Tasking] ──► [Stage 3: Critique]
                                                                                                    │
[Stage 8: Retro] ◄── [Stage 7: Stabilize] ◄── [Stage 6.5: Smoke] ◄── [Stage 6: Verify] ◄── [Stage 5: Claim] ◄─┘
```

1. **Stage 0 (Intent Capture)**: Run `/acdf:explore` to map out raw ideas, JTBD metrics, and research parameters.
2. **Stage 0.5 (Modeling)**: Create Mermaid flowcharts, sequence diagrams, and state transitions.
3. **Stage 1 (Reference Guide)**: Map APIs and invariants. Enforce the "Ten No's" spec checklist.
4. **Stage 2 (Tasking)**: Compile a task list with whitelistedAllowed Files and designated test commands.
5. **Stage 3 (Critique)**: Evaluate the models and tasks using the active Hero Lenses.
6. **Stage 4 (Snapshot)**: Seal a content-hashed snapshot of configuration files in `authority.json`.
7. **Stage 5 (Claim)**: Write task lockfiles to `claims/` and implement code inside bounded loops.
8. **Stage 6 (Verify)**: Run unit compilers and test commands, generating receipt files.
9. **Stage 6.5 (Smoke Test)**: Run Playwright or headless browser scripts to verify E2E states.
10. **Stage 7 (Stabilize)**: Create a cold-start deployment runbook.
11. **Stage 8 (Retrospective)**: Extract learning cards from ledger logs and update Reference Guide lint rules to prevent future failure modes.

---

## 10. Long-Term Vision

ACDF is architected to survive shifts in AI model capabilities. As models improve, the manual orchestration steps decrease, but the underlying **governance principles, gates, and authority layers remain stable**. 

By separating the **reasoning prior** (which evolves via NotebookLM updates) from the **operating protocol** (which remains locked in the kernel), ACDF represents a future-proof OS for governed software automation.
