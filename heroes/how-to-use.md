# How to Use the Engineering Council Hero Cards

This folder contains **17 hero cards** (15 coding, 2 design) and a separate slide-layout rubric. A hero card is an **advisory lens for a bounded task**, not a manager, a security policy, a substitute for the user's instruction, or proof that its namesake endorses every council synthesis in the file. Use this guide as the **shared router and arbitration rule**; use an individual card for its actual operating question and domain methods. Where an older card says “always,” “never,” or “veto,” read it within that domain and the risk boundaries below. Verify a card's source note before attributing a rule to the named person.

## Stage, host and selective loading

Start at [the compact index](README.md). Load this guide and one selected card; add another only for a distinct necessary concern. Never omit project instructions, approved specifications, or required safety context to save tokens. Load source material when attribution matters. Record the actual files/sections loaded; selective loading is a proposed efficiency improvement, not a measured speedup.

This council is usable independently of ACDF. Outside ACDF, the host project defines planning, implementation and approval rules. Within ACDF, planning and adversarial review are first-class assignments; identify the active stage before applying execution constraints. In the Coding Dark Factory execution stage, the approved build plan controls work. Record its version and approval evidence before edits, plus the reference specification and validation thresholds when correctness depends on them. Card advice to create plans, explore architectures, or build missing primitives applies only when that upstream work is explicitly requested. Otherwise report a pivot and await the missing decision. Cards cannot relax project security or release gates.

Use [the evaluation protocol](docs/evaluation.md) to compare lenses, [worked role examples](docs/role-examples.md) to calibrate deliverables, and [the runbook](docs/runbook.md) to maintain this library. Capture changes in [the learning log](docs/learning-log.md).

## Query a hero's NotebookLM source

Each card links its source notebook and offers a task-specific query angle. A person can open the link directly. When the configured NotebookLM MCP is available, an agent can call `ask_question` with that card's `notebook_url`; carry the returned `session_id` into follow-up questions so the notebook retains task context. Add a notebook to a shared library only if that workflow requires it; direct querying does not require changing the source notebook.

Useful prompt shape: “For this task: [sanitized goal, constraints, and relevant design/code excerpt], what guidance in this notebook applies? Cite the supporting notebook sources, distinguish direct source claims from inference, identify unsupported questions, and suggest relevant tradeoffs, failure cases, and verification checks.” Follow up narrowly on a disputed approach, named API or edge case.

Do not send secrets, private customer data, or unpublished project material unless the project's approved data policy permits that notebook. Notebook responses enrich the investigation; verify claims against current project specifications and code. Do not treat a NotebookLM answer as approval or silently promote it into a card rule. Update cards through the normal reviewed source and provenance process.

## For a Human: The Short Version

1. State **one job and one deliverable**, with the person affected, constraints, and what “done” looks like.
2. Ask the orchestrator to pick **one primary hero lens** for the current bottleneck—not a council vote. Pair a second lens only when it owns a different necessary concern (e.g., design + QA, agent autonomy + security).
3. For multi-agent work, name each lane **`operational-role / hero-lens / task-id`**. The operational role specifies what the agent does; the hero name makes comparative performance visible. A named persona is not a license to role-play past the task.
4. Decide up front who may edit, test, review, merge, deploy, and spend money. Under ACDF, preserve its selected human-led or council-led policy; lens selection is not a vote or grant of authority. Prefer one implementer and one independent verifier before creating a swarm.
5. Demand the artifact and real evidence: actual commands/results, inspected UI or runtime, unresolved risks, and the exact owner of the final integration decision.
6. Compare lenses across **comparable tasks**, not just raw PR counts or eloquent responses. Adjust for model, task difficulty, context, tools, verifier, review policy, and budget.

**Example request:** “Build a disposable HTML configurator for this decision. Use `Thariq/implementer` as the primary lens and `Schaad/interaction-review` for feel; have a separate `QA` lane exercise keyboard and mobile behavior. Deliver the file, an exported decision, and what was actually tested. Do not deploy or store user data.”

## For the AI Orchestrator: Routing Algorithm

**Preflight:** Read this guide, the selected hero card(s), and the project's own instructions. The project's authorization, privacy rules, acceptance tests, and repo gates outrank every persona. If the instruction is too narrow or no specialist helps, **use no hero**.

1. **Identify the bottleneck:** intent/product value; visual communication; design feel; implementation/orchestration; harness; correctness; threat boundary; domain actions; performance/scale; or operational resilience.
2. **Pick one primary lens by ownership.** In ACDF this per-task default does not reduce Stage 3’s required independent risk reviews or the configured voting quorum. Invite a second only for a non-overlapping constraint. Assign a human/integration owner and state who can decide consequential tradeoffs.
3. **Choose the minimum topology:** one agent for coupled or small tasks; independent lanes for genuinely separable tasks; one integrator after those lanes finish. Separate worktrees and state for concurrent writers. Reviewers and QA should inspect evidence independently, not inherit the implementer's confident summary as fact.
4. **Write a task contract** for each lane: task ID, operational role, hero lens, goal, inputs, allowed tools/data, files or area owned, output artifact, acceptance checks, stop conditions, budget, and escalation trigger. A hero card does not override this contract.
5. **Apply hard boundaries before taste:** actual tool permissions, secrets and untrusted input, data handling, CI/build gates, required human approval, and merge/deploy policy. A passing model judgment or self-review does not waive these.
6. **Integrate and arbitrate:** Compare conflicting recommendations against task stakes, evidence, reversibility, blast radius, runtime measurements, user value, and maintenance cost. Document the alternative not chosen. Ask the human before changing product scope, security posture, live infrastructure, or material budget.
7. **Verify and report:** Inspect each produced artifact and real tool outputs; run the relevant tests and UI journey. Log failures and human corrections. Do not mark a lane successful because the subagent said it succeeded.

### Standard task contract

```text
Task ID: <unique ID>
Stage / current phase: <assessment, explicitly requested planning, or execution phase>
Approved plan / version / approval evidence: <path or message reference>
Reference spec / version: <path, or reason not applicable>
Validation gate / thresholds: <approved checks and pass criteria>
Loaded context / card versions: <files or sections and revision/hash>
Operational role / hero lens: <e.g., implementer / Boris Cherny>
User job and deliverable: <one outcome and exact artifact>
Scope and owned files: <specific files or read-only review>
Allowed tools, data and side effects: <explicit>
Acceptance checks: <commands, example inputs, UI journey, review criteria>
Independence: <what can this lane verify without trusting another lane?>
Budget and stop trigger: <time/tokens/retries, when to escalate>
Handoff: <artifact path or PR, evidence, known gaps, integration owner>
```

Do **not** spawn a reviewer with write access to the same files at the same time as an implementer. A review finding is a cited observation, not an authority to change the merge policy. Keep each subagent's role, hero lens, task class, model, and actual output in the run log; use the same naming format consistently.

## Card Directory and Ownership

| Primary bottleneck | Primary lens and card | Common pairing / boundary |
|---|---|---|
| User outcome, job-to-be-done, product prioritization | [Bret Taylor](Engineering_Council/bret_taylor_coding_hero.md) | Thariq for a concrete decision artifact; DHH for scope. Product claims need user evidence. |
| Throwaway HTML spec, mini-app, interactive decision | [Thariq Shihipar](Engineering_Council/thariq_shihipar_coding_hero.md) | Schaad for feel; QA lane for use; Willison/Carlini for sensitive content. |
| Small-team coherence, product/developer simplicity | [DHH](Engineering_Council/david_heinemeier_hansson_coding_hero.md) | Dean/Hashimoto when measured workload needs more architecture. |
| AI coding workflow and bounded autonomous execution | [Boris Cherny](Engineering_Council/boris_cherny_coding_hero.md) | Lopopolo for harness; Karpathy for reviewable diffs; Willison/Carlini for security. |
| Agent-legible repository, verifiers, tools, feedback loop | [Ryan Lopopolo](Engineering_Council/ryan_lopopolo_coding_hero.md) | Cherny for execution; no universal no-human-review rule. |
| Outcome-driven agent delegation and reusable skills | [Jeffrey Quesnelle](Engineering_Council/jeffrey_quesnelle_coding_hero.md) | Lopopolo for verification. Use hero names as **labels**, not corporate-role simulations. |
| Small auditable AI changes; AI research and data loops | [Andrej Karpathy](Engineering_Council/andrej_karpathy_coding_hero.md) | Cherny for implementation pace; verify his model-research rules fit the task. |
| Code clarity, performance, static constraints | [John Carmack](Engineering_Council/john_carmack_coding_hero.md) | DHH for simplicity; Dean for fleet-scale measurements. |
| Infrastructure primitives, isolation, idempotency, operability | [Mitchell Hashimoto](Engineering_Council/mitchell_hashimoto_coding_hero.md) | Carlini for adversarial boundaries; operator approves high-risk changes. |
| Large-scale distributed performance and capacity | [Jeff Dean](Engineering_Council/jeff_dean_coding_hero.md) | Activate architecture prescriptions on measured need, not user count alone. |
| Prompt injection and practical tool/data boundaries | [Simon Willison](Engineering_Council/simon_willison_coding_hero.md) | Carlini for adversarial tests. Some older card rules remain source-attribution cautions. |
| Adversarial security research and red teaming | [Nicholas Carlini](Engineering_Council/nicholas_carlini_coding_hero.md) | Willison for practical tool composition; human security owner for policy. |
| Domain objects, governed actions, operator workflow | [Palantir / Landon Carter](Engineering_Council/landon_carter_palantir_coding_hero.md) | Taylor for outcome, Willison/Carlini for action authority. |
| Narrow typed semantic judgment/classification | [Diogo Almeida / Jev](Engineering_Council/diogo_almeida_jev_coding_hero.md) | Code owns policy and side effects; test locally before routing. |
| Temporal interaction feel, latency, voice | [Raphael Schaad](Engineering_Council/raphael_schaad_coding_hero.md) | Independent accessibility/QA lane; do not equate polish with task completion. |
| Tactile play, multisensory delight, exploratory design | [Andy Allen](Design_Council/andy_allen_design_hero.md) | Taylor for the job, QA for accessibility and performance; design is not a security exemption. |
| Transparent, steerable AI interface and orchestration UI | [Ryo Lu](Design_Council/ryo_lu_design_hero.md) | Willison/Carlini for what must stay private; show actions/status, not private model reasoning. |

The separate [Satori Grid & Slide Layout Rubric](references/slide-layout-rubric.md) is a design evaluation reference, **not** an eighteenth hero.

## Specialist Roles: Use Now, Without Inventing New Heroes

Existing cards supply pieces of these disciplines, but no card owns each discipline end-to-end. Assign the **operational role** now, optionally paired with an existing hero lens. Do not attribute the following role contract to the human namesake of a card. Create a new named card only after researching a distinct expert's primary work and observing that the role repeatedly needs its own method.

| Operational role | Starter lens | Independent deliverable / acceptance |
|---|---|---|
| **Code reviewer** | Karpathy (auditable diff), Lopopolo (structural invariants); add Carlini/Willison for a security review | Prioritized findings with file/line evidence, impact, reproducer or reasoning, confidence, and explicit “no finding” areas. Check requirements, regressions, maintainability, tests, and security as appropriate. Do not invent findings. |
| **Unit-test designer** | Willison (behavioral checks), Carmack (contracts), Hashimoto (integration boundary) | Test matrix: nominal, edge, failure, and regression cases; a test shown to fail against the bug where feasible; actual execution result. Avoid brittle implementation-only tests. |
| **Refactorer** | Carmack (clarity), DHH (simplify), Lopopolo (recurring drift) | Before/after behavior evidence, bounded diff, removal of complexity, tests, and explicit list of any behavior intentionally changed. Do not blend a feature rewrite into a “cleanup.” |
| **Exploratory QA** | Schaad (feel), Lopopolo (runnable UI), Thariq (mini-app), Ryo (control) | Reproduction steps, environment, expected/actual, screenshot/video/DOM or logs where useful, severity, and retest. Include keyboard/focus, labels, responsive layout, reduced motion, empty/error states, and assistive tech where relevant. Automated assertions alone are not exploratory QA. |
| **Integrator** | Cherny (workflow), Hashimoto (isolation), Taylor (outcome) | Reconcile lane results, run whole-system checks, check authorization and rollback, resolve conflicts, and obtain required human approval. One accountable integrator, not a committee. |

For a swarm, pair **implementer + independent reviewer + test/QA lane** only when task size and independence justify the extra cost. A tiny throwaway artifact may need one builder plus a short human check. A high-risk production change may need security review and operator approval even if the swarm's checks pass.

## Run Log and Fair Comparison

Keep one entry per lane. A hero name improves traceability only when results can be compared fairly.

```text
Run/task ID | Project/task class | Difficulty/risk | Role | Hero lens | Model/harness
Scope | Start/end or elapsed | Tool/token cost if available | Artifact/PR
Checks actually run and outputs | Review/QA findings | Human corrections
Escaped defect or rework | Outcome/decision | Why this lens helped or hurt
```

Measure **completion with evidence, escaped defects, human rework, verification coverage, cost/latency, and usefulness of findings**. A reviewer should not score highly for a long list of false alarms; an implementer should not score highly for PR volume that fails integration. Compare similar tasks under similar tools and verification conditions; record when a result was limited by a missing tool, blocked approval, bad spec, or unavailable environment rather than blaming the hero lens. Periodically revise activation guidance from real runs.

## Arbitration Examples

- **Cherny asks for more autonomy; Karpathy asks for smaller diffs:** allow broad exploration in isolation, then present small reviewable production changes. Human chooses risk tolerance and merge policy.
- **DHH asks for a monolith; Dean suggests distribution:** request load and failure-domain measurements first. Stay simple until a real constraint justifies a split; human approves the irreversible architecture change.
- **Thariq proposes a shareable HTML mini-app; Willison warns about data:** use synthetic/local data and an access-controlled handoff, or don't publish it. Never call a file safe solely because it is temporary.
- **Lopopolo favors mechanical gates; Schaad sees a UX failure:** retain the gate but add a real interaction test or human study. Neither a green test nor polished visuals alone is “done.”
- **Quesnelle rejects 1:1 corporate-role agents; human requests named heroes:** name the lens in the task log for attribution while assigning capability-based operational roles and tool scopes. The name is a testable working perspective, not a command hierarchy.

## Promotion and Maintenance

Before adding a new hero card: identify a recurring unowned task, find first-person primary sources from a genuine specialist, establish a distinct operating question and deliverable, test it on comparable work, then write a card with activation, deferral, failure modes, sources, and council arbitration. Candidate disciplines are **general code review, unit-test design, behavior-preserving refactoring, and exploratory/accessibility QA**. Do not fabricate a named expert's views or create a redundant “swarm commander” card merely to fill a slot. Update this router whenever a new card is added or an ownership boundary changes.
