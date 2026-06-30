# ACDF v8 Multi-Model Review — Long-Horizon Workflow

This document governs the **ACDF Multi-Model Long-Horizon Review Workflow**. It is a manual, human-driven process that orchestrates multiple frontier AI models across blind critique rounds and integrates expert knowledge databases. 

---

## 1. Operating Doctrine

> **Humans govern. Models argue. Evidence decides.**

This workflow does not eliminate human judgment—it amplifies it. The human engineer acts as the governor who guides the models, compiles Objections, prevents cross-contamination, resolves conflicts, and seals the final specifications.

---

## 2. Workflow A: Three-Round Adversarial Review

This workflow runs during **Stage 3 (Adversarial Review)** to stress-test designs and task structures before implementation.

### Step 0: Prepare the Review Packet
Compile `.acdf/changes/<change-id>/review_packet.md` containing:
* Core problem description and user JTBD criteria.
* Proposed Mermaid models (Stage 0.5 flow, sequence, and state diagrams).
* Reference Guide spec draft.
* Allowed write boundaries and whitelisted files.

### Round 1: Independent Blind Reviews
Send the review packet independently to 3–5 different frontier models (e.g. Claude, GPT, Gemini, Llama).
* **Isolation Rule**: Models must not see other models' reviews.
* **Review Prompt**: Use the [round_1_independent_review.md](file:///Users/alannguyen/Documents/Vibe%20Code/alan-coding-dark-factory/templates/review_prompts/round_1_independent_review.md) template.
* **Output**: Save reviews under `.acdf/changes/<change-id>/reviews/round_1/<model_name>.md`.

### Round 2: Cross-Examination
Merge Round 1 critiques into an anonymized summary. Send this summary back to each model.
* **Cross Prompt**: Use the [round_2_cross_examination.md](file:///Users/alannguyen/Documents/Vibe%20Code/alan-coding-dark-factory/templates/review_prompts/round_2_cross_examination.md) template.
* **Output**: Save under `.acdf/changes/<change-id>/reviews/round_2/<model_name>.md`.

### Round 3: Final Risk Register
Ask each model to compile its finalized, prioritized risk register mapping gates and mitigation strategies.
* **Register Prompt**: Use the [round_3_final_risk_register.md](file:///Users/alannguyen/Documents/Vibe%20Code/alan-coding-dark-factory/templates/review_prompts/round_3_final_risk_register.md) template.
* **Output**: Save under `.acdf/changes/<change-id>/reviews/round_3/<model_name>.md`.

### Synthesis
The human governor synthesizes the final outputs using the [synthesis_prompt.md](file:///Users/alannguyen/Documents/Vibe%20Code/alan-coding-dark-factory/templates/review_prompts/synthesis_prompt.md) to generate the active `.acdf/changes/<change-id>/risk_review.md`.
* **Rules**:
  - Convert repeated critiques into task gates.
  - Convert unresolved ambiguities into stop conditions.
  - Do not average away security or consistency warnings.

---

## 3. Workflow B: NotebookLM Ingestion Workflow

This workflow is used during **Stage 1 (Reference Specification)** to build and update Hero Lens doctrines from expert sources.

```text
Source Collection ──► NotebookLM Ingestion ──► Three Ingestion Rounds ──► Doctrine Update
```

### Step 1: Source Collection
Human collects primary source materials (talk transcripts, papers, blog posts, codebase audits) for the target expert.

### Step 2: Load into NotebookLM
Human uploads source materials into a dedicated NotebookLM session (e.g. `lenses/carmack/`).

### Step 3: Ask Three Rounds of Nine Questions
Ask the 27 questions defined in [notebooklm_9_questions.md](file:///Users/alannguyen/Documents/Vibe%20Code/alan-coding-dark-factory/templates/review_prompts/notebooklm_9_questions.md):
1. **Round 1 (Extraction)**: Distills core heuristics, failure patterns, and rules.
2. **Round 2 (Application)**: Critiques current model architectures.
3. **Round 3 (Synthesis)**: Exposes the final distilled engineering doctrine.

Save outputs to `.acdf/reference/lenses/<expert_name>/synthesis_date.md`. Use these synthesized doctrines to update the canonical `framework/ACDF_hero_lenses.md`.
