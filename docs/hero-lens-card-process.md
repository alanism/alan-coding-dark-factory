# Hero Lens Card — Build Process

> How we extract thinkers from NotebookLM into structured hero lens cards for Engineering and Design Councils.

---

## Overview

A hero lens card captures a thinker's engineering or design philosophy as a structured reference that an AI coding agent can consult at runtime. Each card answers: *"What would this thinker say about this situation?"*

**Time per card:** 25-40 minutes (auth + 3 rounds + synthesis)
**NotebookLM queries per card:** 27 (3 rounds × 9 questions) — or 18 (2 rounds × 9 for lighter extractions)
**Output:** Single `.md` card at `heroes/{Council}/{thinker_slug}_{domain}_hero.md`

**Cards built so far:**
- Engineering Council: 11 cards (Karpathy, Cherny, Taylor, Quesnelle, Jeff Dean, Carmack, Hashimoto, Carlini, Schaad, Lopopolo, and Willison)
- Design Council: 2 cards (Andy Allen and Ryo Lu)

The canonical ACDF copies of completed cards live in `heroes/Engineering_Council/` and `heroes/Design_Council/`. Select a source notebook from [the public inventory](notebooklm-inventory.md) and connect to its public share URL through NotebookLM MCP in read-only mode before writing extraction prompts.

---

## Step 1: Receive Thinker + Domain

Every extraction starts with:

1. **NotebookLM URL** — The thinker's source notebook
2. **Domain/council** — Engineering, Design, Marketing, Finance, etc.
3. **Role clue** — Optional hint about their domain specialty (e.g., "UI/UX", "AI loops", "Systems")

The domain determines the question templates. A design thinker gets questions about visual principles, motion, typography. An engineering thinker gets questions about architecture, patterns, testing.

---

## Step 2: Write 3 Rounds of 9 Questions

### Round 1 — Foundation (Who are they?)

Covers the thinker's core philosophy and worldview:

| # | Question Type | Engineering Example | Design Example |
|---|--------------|--------------------|----------------|
| Q1 | Core philosophy | How does X describe their engineering philosophy? | How does X describe their design philosophy? |
| Q2 | Guiding principles | What principles guide architecture decisions? | What principles guide visual/interaction decisions? |
| Q3 | Key relationships | How do they think about simplicity vs. complexity? | How do they think about beauty vs. usability? |
| Q4 | Process approach | What's their approach to building systems? | What's their approach to prototyping/iteration? |
| Q5 | Domain-specific | How do they approach performance/scale/security? | How do they approach motion/color/typography? |
| Q6 | Common mistakes | What mistakes do they identify in engineering? | What mistakes do they identify in design? |
| Q7 | Edge cases | How do they handle evolution of systems? | How do they handle edge cases/error states? |
| Q8 | Rule extraction | Convert philosophy into 10-20 enforceable rules. | Convert philosophy into 10-20 enforceable rules. |
| Q9 | Source citation | Cite sources; distinguish explicit vs. inferred. | Cite sources; distinguish explicit vs. inferred. |

### Round 2 — Depth (How do they work?)

Deep dive into the thinker's specific techniques and methods:

| # | Engineering Depth Questions | Design Depth Questions |
|---|---------------------------|----------------------|
| Q1 | Creative/technical process from concept to ship | Design process from idea to implementation |
| Q2 | Specific techniques in their domain | Color, typography, composition at micro level |
| Q3 | Patterns for complex systems/architecture | Interaction patterns for complex actions |
| Q4 | Handling scale/multi-platform | Responsive/multi-platform design |
| Q5 | Performance/optimization methods | Prototyping fidelity — low-fi vs. hi-fi vs. code |
| Q6 | Debugging/instrumentation | Animation, transitions, temporal design |
| Q7 | Tools, software, workflows | Tools, software, workflows |
| Q8 | Balance of tradeoffs | Balance of innovation vs. conventions |
| Q9 | Most counterintuitive findings | Most counterintuitive/surprising findings |

### Round 3 — Coverage (Where do they stop?)

Maps boundaries, gaps, and council positioning:

| # | Question Type |
|---|--------------|
| Q1 | What does this thinker say practitioners should NOT do? Deliberate non-goals/rejected patterns |
| Q2 | If paired with a complementary expert (from a different council), where would they defer vs. insist? |
| Q3 | What are the sharpest critiques or acknowledged limitations of their approach? |
| Q4 | What advice would they give for applying their principles specifically to AI-powered products? |
| Q5 | How should their design/engineering decisions be evaluated beyond personal taste? |
| Q6 | What do they think about systems/consistency/scale in their domain? |
| Q7 | How do they think about the relationship between their work and business outcomes? |
| Q8 | Top 5 non-negotiable rules in their domain |
| Q9 | Single most common mistake or dangerous misconception in their field |

### Question Writing Rules

1. **Domain-adapt each question** — a Q2 about "performance" for Carmack means "latency and optimization"; for Schaad it means "typography and visual hierarchy"
2. **Always include the constraint prefix:** `"Answer only from the uploaded source material. Extract reusable {engineering/design} principles. Keep answers concise, practical, and citation-backed."`
3. **The last two questions are always the same:** Q8 = extract rules, Q9 = cite sources with explicit vs. inferred classification
4. **Round 3 Q2 is the council positioning question** — it determines where the thinker fits among peers

---

## Step 3: Write Prompt Files

Long questions go to `.txt` files. All 9 questions go into a single prompt file per round:

```
C:\Users\alani\AppData\Local\Temp\{thinker}_round{N}.txt
```

The file starts with the instruction prefix, then lists Q1–Q9 with their sub-questions.

---

## Step 4: Run Queries Against NotebookLM

### Auth

```bash
notebooklm -p alanism auth check --test --json
# Expected: status: "ok", token_fetch: true
```

If expired: `notebooklm -p alanism login`

### Run Rounds in Parallel Batches

Use `delegate_task` with batches of 3 concurrent subagents:

```python
# Batch 1: first 3 thinkers
delegate_task(tasks=[
    {"goal": f"Round 1 for {thinker1}", "toolsets": ["terminal", "file"]},
    {"goal": f"Round 1 for {thinker2}", "toolsets": ["terminal", "file"]},
    {"goal": f"Round 1 for {thinker3}", "toolsets": ["terminal", "file"]},
])

# Then Rounds 2 and 3 for the same batch
# Then move to next batch of thinkers
```

### How Many Rounds?

| Card Type | Rounds | When to Use |
|-----------|--------|-------------|
| Full hero card | **3 rounds** (27 questions) | Standard — thinkers with rich source material |
| Quick card | **2 rounds** (18 questions) | When user requests 2 rounds explicitly |
| System card (no notebook) | **0 rounds** (web synthesis) | When no NotebookLM notebook exists — card marked ⚠️ |

---

## Step 5: Save Raw Extractions

```
extra/
├── round1/{thinker_slug}_round1_extraction.md
├── round2/{thinker_slug}_round2_extraction.md
├── round3/{thinker_slug}_round3_extraction.md
```

These are intermediate files for quality checking. They preserve the full NotebookLM response.

---

## Step 6: Synthesize Hero Card

Read all round files. Produce a single card with this exact format:

```markdown
# {Thinker Name} — {Engineering/Design} Hero Card

> Source: NotebookLM 3 rounds against notebook `{id}`
> (If less than 3 rounds, note: "Round 3 not extracted — gaps noted")
> (If no notebook: "⚠️ Web-synthesized — not from NotebookLM")

## Role Card

- **Mission:** {one-line — what an AI coding agent consults this hero for}
- **Core View:** {keystone principle — the one sentence that defines their philosophy}
- **Owns:** {comma-separated domains they control}
- **Defers:** {when and to whom — which other council members handle what they don't}
- **Vetoes:** {absolute prohibitions — what they will never allow, even if it seems to work}
- **Sample Phrases:** {3-5 representative quotes or paraphrases in their voice}
- **Failure Mode:** {what breaks if this hero's advice is over-applied}

## Operating Question

{One question that activates this hero — the trigger. E.g., "Are we describing outcomes or micromanaging steps?"}

## Council Position

| Dimension | Answer |
|-----------|--------|
| **Owns** | {what this hero controls in the council} |
| **Does not own** | {what they stay out of} |
| **Defers to** | {other heroes and when} |
| **Failure mode** | {what breaks if overused in a council context} |

## Top Non-Negotiable Rules (with citations)

1. **Rule 1** — Rationale. [R1 Q3, R2 Q5]
2. **Rule 2** — Rationale. [R1 Q8]
...
(10 rules maximum. Each rule cites the source round and question.)

## Quick Reference

- **Activate when:** {trigger situations}
- **Do NOT activate when:** {counter-triggers}
- **Pair with:** {complementary heroes}
- **Never pair with:** {conflicting heroes}
```

---

## Step 7: Save to Council Directory

| Council | Path |
|---------|------|
| Engineering Council | `heroes/Engineering_Council/{thinker_slug}_coding_hero.md` |
| Design Council | `heroes/Design_Council/{thinker_slug}_design_hero.md` |
| Marketing Council (future) | `heroes/Marketing_Council/{thinker_slug}_marketing_hero.md` |
| Finance Council (future) | `heroes/Finance_Council/{thinker_slug}_finance_hero.md` |

**Filename convention:** `{firstname_lastname}_{domain}_hero.md` (lowercase, underscores).

---

## Synthesis Rules (How We Actually Build the Card)

### Role Card Rules

- **Mission:** Must be one sentence. Start with a verb. E.g., "Make every AI agent assume it's already compromised — then build the architecture that survives anyway."
- **Core View:** One keystone sentence that everything else derives from. If you can't reduce it to one sentence, you haven't understood them yet.
- **Owns:** 5-8 domains. These are what makes the thinker unique. If another thinker also owns it, mark the boundary.
- **Defers:** Name specific other heroes from the same or adjacent council. E.g., "Defers to Willison on MCP composition governance."
- **Vetoes:** 5-8 absolute prohibitions. These are the lines they will never cross. Each starts with "Never."
- **Sample Phrases:** 3-5 quotes. Must be representative of their actual voice, not generic. Use actual NotebookLM-extracted phrases where possible.
- **Failure Mode:** One sentence about what goes wrong when this lens is over-applied. Every good philosophy has a failure mode.

### Council Position Rules

The council position table is cross-referenced. When you write "Defers to Carmack on compiler-enforced correctness," that should match Carmack's "Owns" field. If the target hero doesn't exist yet, note it as "[hero not yet extracted]".

### Rule Selection Rules

| Rule Source | Keep? |
|-------------|-------|
| Explicit guidance, cited in source | ✅ Always keep |
| Explicit guidance, cited in source, repeated across rounds | ✅ ✅ Top priority |
| Inferred from broader philosophy, supported by evidence | ⚠️ Keep, note as inferred |
| Speculative, extrapolated beyond source material | ❌ Reject |
| Conflicts with another hero's explicit rule | Resolve in council position; note the tension |

Each rule includes:
1. The rule statement (bold)
2. One-sentence rationale
3. Source citations in brackets: `[R1 Q3, R2 Q5]`

---

## Real Examples

### Engineering Council — Jeffrey Quesnelle

| Artifact | Content |
|----------|---------|
| Mission | "Architect agent systems that maximize emergent model intelligence by describing outcomes and success conditions — never micromanaging steps" |
| Core View | "Get out of the way of the model." |
| Operating Question | "Are we describing outcomes and success conditions, or micromanaging steps?" |
| Rules extracted | 10 — including "Describe outcomes not steps", "Never leave evaluation criteria unstated" |

### Design Council — Jayse Hansen

| Artifact | Content |
|----------|---------|
| Mission | "Design cinematic interfaces that communicate their purpose in under 24 frames at 24fps — the audience must understand before they can look away." |
| Core View | "Design for the popcorn eater, not the hero." |
| Operating Question | "Does this UI clarify the story for the audience in under 24 frames?" |
| Rules extracted | 10 — including "The 24-Frame Rule", "Design for the Audience, not the Character" |

---

## Common Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Auth expires mid-extraction (happens every ~50 queries) | Subagent hits auth error on round 2 or 3 | Run `notebooklm login` before starting a batch. Check auth every 30 min. |
| Notebook has thin material | Answers say "source material lacked coverage" | Note the gap in the card. Consider adding more sources to the notebook. |
| Round 3 missing for some thinkers | Carlini card has "Round 3 not extracted" marker | Run the round if time allows. If not, mark it. The card is still useful with 2 rounds. |
| Operating Question is too vague | "What should we build?" instead of "If an attacker controls one input, can they hijack the agent?" | Sharpen the question. It should describe a specific tension or test. |
| Rules duplicate across heroes | Both Quesnelle and Cherny have "describe outcomes" | That's fine — convergence is informative. But check if one defers to the other on that dimension. |
| Hero's voice doesn't come through | Card sounds generic | Re-read sample phrases. If they sound like any other hero, re-extract. |

---

## Quality Checklist

- [ ] Notebook successfully queried (check `extra/round*/*.md` exist)
- [ ] Auth was valid at time of extraction
- [ ] 3 rounds extracted (or marked if fewer)
- [ ] Role Card has all 7 fields filled
- [ ] Operating Question is specific and testable
- [ ] Council Position table cross-references other heroes
- [ ] Top rules are 10 maximum, each with citation
- [ ] Quick Reference has all 4 fields (activate, don't activate, pair, never pair)
- [ ] Failure mode is honest about the philosophy's limit
- [ ] Card saved to correct council directory
- [ ] Index updated at `docs/notebooklm-inventory.md`
