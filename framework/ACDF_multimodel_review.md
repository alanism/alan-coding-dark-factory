# ACDF v9 Multi-Model Review — Long-Horizon Workflow

This document governs the **ACDF Multi-Model Long-Horizon Review Workflow**. It orchestrates multiple frontier AI models across blind critique rounds and integrates public NotebookLM knowledge sources. The user chooses whether required approvals remain human-led or use bounded Council voting.

---

## 1. Operating Doctrine

> **Humans set the boundary. Models argue. Evidence decides. A configured Council may approve bounded decisions.**

This workflow does not eliminate human judgment—it removes the human from routine approval bottlenecks when the user explicitly selects Council-led mode. The human still defines intent, trust zones, hard stops, and the approval policy. Agents compile objections, prevent cross-contamination, record votes, resolve only bounded conflicts, and seal specifications only after the applicable decision record is valid.

### 1.1 Approval Modes

At Stage 0, record exactly one mode in `APPROVAL_POLICY.md`:

| Mode | Use | Approval rule |
|---|---|---|
| `human-led` | Current explicit-approval workflow | The named human approves every required decision. |
| `council-led` | User wants routine decisions to proceed without being the bottleneck | The relevant Engineering and/or Design Council votes independently; quorum and strict majority must be recorded. |

Council-led mode applies only to routine, in-scope coding and design decisions. A tie, no quorum, unresolved critical dissent, changed success criteria, scope expansion, security/privacy/legal concern, production release, credential change, or external-data-boundary change is `BLOCKED` until a human explicitly approves or the proposal is revised. Council votes never waive a lifecycle gate.

### 1.2 Council Vote Record

Every council decision records: decision ID, proposal hash, selected Hero Cards, eligible voters, each `APPROVE`/`REJECT`/`ABSTAIN` vote, rationale, quorum, approval count, dissent, hard-stop assessment, and final result. The record is attached to `authority.json` before Stage 5 begins.

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
* **Review Prompt**: Use the [round_1_independent_review.md](../templates/review_prompts/round_1_independent_review.md) template.
* **Output**: Save reviews under `.acdf/changes/<change-id>/reviews/round_1/<model_name>.md`.

### Round 2: Cross-Examination
Merge Round 1 critiques into an anonymized summary. Send this summary back to each model.
* **Cross Prompt**: Use the [round_2_cross_examination.md](../templates/review_prompts/round_2_cross_examination.md) template.
* **Output**: Save under `.acdf/changes/<change-id>/reviews/round_2/<model_name>.md`.

### Round 3: Final Risk Register
Ask each model to compile its finalized, prioritized risk register mapping gates and mitigation strategies.
* **Register Prompt**: Use the [round_3_final_risk_register.md](../templates/review_prompts/round_3_final_risk_register.md) template.
* **Output**: Save under `.acdf/changes/<change-id>/reviews/round_3/<model_name>.md`.

### Synthesis
The selected approval mode synthesizes the final outputs using the [synthesis_prompt.md](../templates/review_prompts/synthesis_prompt.md) to generate the active `.acdf/changes/<change-id>/risk_review.md`; human-led mode uses the human governor, while council-led mode records the council result and escalates only blocked or hard-stop decisions.
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
Select a public shared notebook from [`docs/notebooklm-inventory.md`](../docs/notebooklm-inventory.md) and record its title, ID, and URL. If a new expert source is needed, the user must explicitly curate it before it enters the inventory.

### Step 2: Connect Through NotebookLM MCP
Pass the inventory's public share URL to the configured NotebookLM MCP server in read-only mode. Do not send private project files, credentials, production data, or unpublished requirements to a public notebook. Follow [`docs/coding-reference-guide-process.md`](../docs/coding-reference-guide-process.md) for the coding-guide path and [`docs/hero-lens-card-process.md`](../docs/hero-lens-card-process.md) for the card path.

### Step 3: Ask Three Rounds of Nine Questions
Ask the 27 questions defined in [notebooklm_9_questions.md](../templates/review_prompts/notebooklm_9_questions.md):
1. **Round 1 (Extraction)**: Distills core heuristics, failure patterns, and rules.
2. **Round 2 (Application)**: Critiques current model architectures.
3. **Round 3 (Synthesis)**: Exposes the final distilled engineering doctrine.

Save outputs to `.acdf/reference/lenses/<expert_name>/synthesis_date.md` and publish source-safe final cards under [`heroes/Engineering_Council/`](../heroes/Engineering_Council/) or [`heroes/Design_Council/`](../heroes/Design_Council/). Update the maintained card and its provenance record; update the routing document only if ownership changes. Do not duplicate card doctrine in the framework integration guide.

### 2.1 Engineering and Design Council Review

For a council-led decision, select the smallest relevant set of individual cards, present the same proposal and evidence to each card independently, then record the vote. Engineering cards own coding and architecture decisions; Design cards own interaction and visual decisions. Mixed decisions use both councils. A majority is a decision signal, not a bypass around the Reference Guide, authority snapshot, or verification evidence.

## 4. Independence and lifecycle use in v9

Stage 3 retains its existing review requirements. One primary lens per individual task does not reduce the number of required independent risk reviews. Preserve the same proposal snapshot for reviewers, record actual model/agent identities and disclose shared context. Renaming one model's sequential self-review as several heroes does not establish independent review or multiple eligible voters.

Hero-informed review also applies to implementation diffs, tests, user journeys and integration; it does not replace upstream adversarial review. [Task contracts](../templates/agent_task_contract.md) distinguish role, lens and permissions. The selected approval policy alone determines voting eligibility and authority.
