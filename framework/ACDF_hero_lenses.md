# ACDF v8 Hero Lenses — Evolving Knowledge Modules

Hero Lenses in ACDF are living engineering knowledge modules. They are **not** role-playing personas, and they are **not** authority sources.

---

## 1. Governance Rule

> “Hero Lenses may propose risks, questions, test ideas, and implementation heuristics. They cannot grant authority, expand scope, waive gates, override user instructions, or justify touching forbidden files.”

---

## 2. NotebookLM Ingestion Model

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

## 3. Generic Hero Lenses

ACDF v8 defines seven canonical advisory lenses:

### 3.1 Systems Builder Lens
* **Focus**: Modular decoupling, type safety, type-driven designs, and clean interface boundaries.
* **Evidence Required**: Complete data schemas, TypeScript interfaces, and API payload definitions.

### 3.2 Security Red-Team Lens
* **Focus**: Threat modeling, white-box penetration checks, data boundary containment, and sanitization of untrusted input.
* **Evidence Required**: Validated sanitization checks and white-box test cases for input parameters.

### 3.3 Runtime Truth Lens
* **Focus**: Empiricism over compilation. Direct validation against running processes, E2E curl outputs, and latency statistics.
* **Evidence Required**: Telemetry logs and system resource footprint outputs from E2E runs.

### 3.4 Developer Ergonomics Lens
* **Focus**: One-command developer setups, codifying tribal configurations, clean runbooks, and token efficiency.
* **Evidence Required**: Validation of a clean environmental cold-start setup via automated scripts.

### 3.5 Simplicity Lens
* **Focus**: Surgical code changes, removing speculative abstractions, minimizing line diffs, and keeping a short leash.
* **Evidence Required**: Git diff statistics showing exactly which lines of code were modified.

### 3.6 Infrastructure Reliability Lens
* **Focus**: Error thresholds, exponential backoff, jitter, circuit breakers, terminal states, and database rollback steps.
* **Evidence Required**: Configured timeouts and simulated circuit-breaker failure logs.

### 3.7 Product Judgment Lens
* **Focus**: Metric-driven features, anti-reward hacking checks (e.g. preventing agents from deleting tests to force a pass), and JTBD alignment.
* **Evidence Required**: Metric success validation checklists.
