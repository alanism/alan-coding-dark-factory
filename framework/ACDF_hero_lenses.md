# ACDF v8 Hero Lenses — Evolving Knowledge Modules

Hero Lenses in ACDF are living engineering knowledge modules. They are **not** role-playing personas, and they are **not** authority sources.

---

## 1. Governance Rule

> “Hero Lenses may propose risks, questions, test ideas, and implementation heuristics. They cannot grant authority, expand scope, waive gates, override user instructions, or justify touching forbidden files.”

---

## 2. Model-First Challenging Process (Stage 3)

During Stage 3 (Adversarial Review), Hero Lenses are invoked to review and challenge the Mermaid diagrams generated in Stage 0.5. They analyze:
* Flowcharts: Search for unhandled decision paths or looping errors.
* Sequence Diagrams: Inspect for trace concurrency issues, unhandled API call timeouts, or security zone crossings.
* State machines: Audit for unreachable states, missing recovery states, or invalid state transitions.
* ER schemas: Identify column duplication, missing constraints, or bad decoupling.

A change plan cannot be signed off if any lens identifies structural flaws in the models without a corresponding task in `tasks.md` to resolve them.

---

## 3. NotebookLM Ingestion Model

A Hero Lens is synthesized from a curated, living expert engineering corpus (e.g. papers, codebase audits, technical talks). The framework evolves continuously without modifying its underlying architecture by updating the NotebookLM source material.

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

---

## 4. Generic Hero Lenses

ACDF v8 defines seven canonical advisory lenses:

### 4.1 Systems Builder Lens
* **Focus**: Modular decoupling, type safety, type-driven designs, and clean interface boundaries.
* **Model Critique**: Challenges C4 boundaries, entity relationships, schemas, and public API interfaces.
* **Evidence Required**: Complete data schemas, TypeScript interfaces, and API payload definitions.

### 4.2 Security Red-Team Lens
* **Focus**: Threat modeling, white-box penetration checks, data boundary containment, and sanitization of untrusted input.
* **Model Critique**: Challenges sequence diagrams for secret leakage, privilege escalation, or unauthenticated pathways across trust zones.
* **Evidence Required**: Validated sanitization checks and white-box test cases for input parameters.

### 4.3 Runtime Truth Lens
* **Focus**: Empiricism over compilation. Direct validation against running processes, E2E curl outputs, and latency statistics.
* **Model Critique**: Challenges state machines for deadlocks, race conditions, or unhandled runtime edge states.
* **Evidence Required**: Telemetry logs and system resource footprint outputs from E2E runs.

### 4.4 Developer Ergonomics Lens
* **Focus**: One-command developer setups, codifying tribal configurations, clean runbooks, and token efficiency.
* **Model Critique**: Challenges complex sequence diagrams for bloated orchestration and setup overhead.
* **Evidence Required**: Validation of a clean environmental cold-start setup via automated scripts.

### 3.5 Simplicity Lens
* **Focus**: Surgical code changes, removing speculative abstractions, minimizing line diffs, and keeping a short leash.
* **Model Critique**: Challenges large, monolithic Mermaid diagrams, rejecting over-engineered loops or speculative abstractions.
* **Evidence Required**: Git diff statistics showing exactly which lines of code were modified.

### 3.6 Infrastructure Reliability Lens
* **Focus**: Error thresholds, exponential backoff, jitter, circuit breakers, terminal states, and database rollback steps.
* **Model Critique**: Challenges sequence flows for missing timeout, backoff, retry, or recovery nodes.
* **Evidence Required**: Configured timeouts and simulated circuit-breaker failure logs.

### 3.7 Product Judgment Lens
* **Focus**: Metric-driven features, anti-reward hacking checks (e.g. preventing agents from deleting tests to force a pass), and JTBD alignment.
* **Model Critique**: Challenges flowcharts and sequences against user stories and core Job-to-be-Done (JTBD) requirements.
* **Evidence Required**: Metric success validation checklists.
