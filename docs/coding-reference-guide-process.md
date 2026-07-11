# Coding Reference Guide — Build Process

> How we actually extract NotebookLM notebooks into structured .md reference guides for AI coding agents.

---

## Overview

We produce reference guides by querying NotebookLM notebooks with 2 rounds of 9 project-specific questions, then consolidating the answers into a structured markdown file. The guide becomes the authoritative reference for an AI coding agent working on a specific build plan.

**Total time per guide:** ~15-20 minutes (auth + 2 rounds + consolidation)
**NotebookLM queries per guide:** 18 (2 rounds × 9 questions)
**Output:** Single `.md` file at `docs/{framework}-coding-reference-guide.md`

---

## Step 0: Select a Public Notebook and Connect Through MCP

Start with [notebooklm-inventory.md](notebooklm-inventory.md). Select the public shared URL that best matches the framework or project domain, then pass that URL to the configured NotebookLM MCP server in read-only mode.

The MCP request must preserve the notebook identity and provenance:

```text
notebook_title: {title from inventory}
notebook_id: {id from inventory}
share_url: https://notebooklm.google.com/notebook/{id}
access: read-only public share link
project: {project name and build-plan scope}
```

Do not provide private source files, credentials, tokens, production data, or unpublished requirements to a public notebook. If a notebook is not publicly shared or the MCP connection cannot verify the selected URL, stop and record the gap.

## Step 1: Receive Context

Every extraction starts with two inputs:

1. **NotebookLM URL or ID** — The source notebook to query
2. **Build plan or project context** — Determines what questions to ask

The build plan is essential. Questions must be project-specific. Generic "teach me React" questions produce shallow answers. Questions tied to specific build-plan needs (e.g., "CSP for zero-egress renderer in Tauri") produce actionable patterns.

**Example build-plan signals that shape questions:**
- Security constraints mentioned → CSP, credential isolation, sandboxing
- Specific libraries named → targeted pattern questions
- Architecture diagrams → component hierarchy, state management
- Non-goals listed → what NOT to ask about

---

## Step 2: Craft 2 Rounds of 9 Questions

### Round 1 — Foundation

Covers the essential patterns an AI coding agent needs to build correctly in this domain:

| Question Type | Example |
|--------------|---------|
| Architecture & composition | Component hierarchy, module organization |
| State management | Reducers, context, stores |
| Security patterns | CSP, input validation, credential handling |
| Error handling | Error boundaries, discriminated unions |
| Testing | Unit, integration, E2E patterns |
| Performance | Memoization, virtualization |
| Accessibility | Keyboard nav, focus management |
| Styling | CSS approach, design tokens |
| Type safety | TypeScript config, branded types |

Each question must specify: "Include concrete code examples, invariants, forbidden patterns, and acceptance tests."

### Round 2 — Depth

Covers advanced implementation patterns specific to the build plan's core flows:

| Question Type | Example |
|--------------|---------|
| Async workflows | AbortController, cancellation, retry |
| State machines | useReducer for multi-step flows |
| File handling | Import/export, drag-and-drop |
| Feature-specific | Text selection, virtualization, lazy loading |
| Performance profiling | React Profiler, DevTools |
| Context optimization | Context splitting for settings |
| Framework-specific | React 18/19 features |
| Integration patterns | IPC, bridge, cross-boundary |
| Advanced testing | Async component tests, mocked providers |

### Question Writing Rules

1. **Be specific to the build plan** — reference the actual component names, panel structures, and flows from the build plan
2. **Always include the constraint prefix** — `"Answer only from the uploaded source material. Extract reusable principles. Be technical and citation-backed."`
3. **Request concrete code** — never accept prose-only answers
4. **Request invariants + forbidden patterns** — "what to do" is half the answer; "what to never do" is the other half
5. **Request acceptance tests** — every invariant should have a mechanical test

---

## Step 3: Write Prompt Files

For long questions (anything over ~200 characters), write to a `.txt` prompt file:

```
C:\Users\alani\AppData\Local\Temp\{framework}_round{N}.txt
```

The prompt file includes:
- The instruction prefix
- All 9 questions (numbered Q1-Q9)
- Sub-questions and specific asks

Short questions can be passed inline with `notebooklm ask "QUESTION" --json`, but all our reference guide questions are complex enough to need prompt files.

---

## Step 4: Run Queries Against NotebookLM

### Auth Check First

```bash
notebooklm -p alanism auth check --test --json
```

Returns `status: "ok"` + `token_fetch: true`. If auth is expired, run `notebooklm -p alanism login`.

### Run via delegate_task (preferred)

Run both rounds in parallel using `delegate_task` with `terminal` + `file` toolsets:

```python
delegate_task(tasks=[
    {"goal": "Round 1 foundation questions", "toolsets": ["terminal", "file"]},
    {"goal": "Round 2 depth questions", "toolsets": ["terminal", "file"]},
])
```

Each subagent:
1. Reads the prompt file
2. Runs `notebooklm -p alanism ask -n {notebook_id} --prompt-file {file} --json`
3. Saves the answer to `extra/round1/{framework}_round1.md`

### Fallback: Direct terminal queries

If `delegate_task` is unavailable or the subagent is timing out, run directly:

```bash
notebooklm -p alanism ask -n {notebook_id} --prompt-file /c/Users/alani/AppData/Local/Temp/{file}.txt --json 2>&1
```

### Batch Execution Pattern

Each round is 9 questions. NotebookLM processes them as a single prompt via `--prompt-file`. The model returns a single answer addressing all 9 questions sequentially. We do NOT ask questions one at a time.

---

## Step 5: Save Raw Answers

Save each round's answer to a structured location:

```
extra/
├── round1/{framework}_reference_round1.md
├── round2/{framework}_reference_round2.md
```

These are intermediate files. They capture the full NotebookLM response including any gap warnings ("source material lacked coverage on X").

---

## Step 6: Consolidate Into Final Guide

Read both round files. Synthesize into a single structured reference guide.

### Guide Structure

```markdown
# {Framework} — Coding Reference Guide

> Source: NotebookLM notebook `{id}`
> Extraction: 2 rounds of 9 questions — foundation + depth
> Target: AI coding agent building {project}

## 1. {Section Title}

### {Pattern or Principle}

- Concrete code examples (TypeScript/Rust/React/etc.)
- Forbidden patterns marked with ❌
- Acceptance tests where applicable
- Failure behavior

### Invariant

{One-sentence architectural rule that must never be violated}
```

### Guide Sections (typical)

| # | Section | Source |
|---|---------|--------|
| 1 | Architecture & Component Design | R1 Q1-Q2 |
| 2 | State Management | R1 Q3 |
| 3 | State Machines & Complex Flows | R2 Q2 |
| 4 | Security & CSP | R1 Q4 |
| 5 | Error Handling & Boundaries | R1 Q6, R2 Q1 |
| 6 | Async Patterns & Cancellation | R2 Q1 |
| 7 | Performance | R1 Q9, R2 Q5 |
| 8 | Accessibility & Keyboard | R1 Q7 |
| 9 | Testing | R1 Q8, R2 Q9 |
| 10 | Styling & Design Tokens | R1 Q9 |
| 11 | File & Import Handling | R2 Q3 |
| 12 | Quick Reference — Codex Rules | All sections consolidated |

### Mark Notebook Gaps

If the notebook lacked coverage on a topic, note it explicitly:

```markdown
**Note:** Notebook source had limited coverage on {topic}. Patterns below
are standard {framework} practice verified against official docs.
```

---

## Step 7: Save & Name Convention

Save final guides to `docs/` with a descriptive filename:

```
docs/{framework}-coding-reference-guide.md
```

Examples:
- `docs/tauri-v2-coding-reference-guide.md`
- `docs/nextjs-react-coding-reference-guide.md`
- `docs/react-coding-reference-guide.md`
- `docs/rust-coding-reference-guide.md`

---

## Real Examples From This Session

| Guide | Notebook | Rounds | Key Build Plan Signals |
|-------|----------|--------|----------------------|
| Tauri v2 | `3d7578dd` | 9 questions each (single round of 9 detailed multi-part) | Zero-egress renderer, Rust IPC, credential vault, EPUB ingestion |
| Next.js/React | `bd77a6f5` | 2 × 9 | CSP, component hierarchy, async hooks, error boundaries, testing |
| React | `89f89c37` | 2 × 9 | Component composition, state management, custom hooks, portals, performance |
| Rust | `2c9ca62e` | 2 × 9 | Arc/Mutex, error handling, serde, async Tokio, filesystem safety |

---

## Common Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Auth expired mid-extraction | Subagent hits "Authentication expired" error | Run `notebooklm login` before launching delegate_task |
| Notebook has no coverage on key topic | Answer says "source material lacks X" | Note the gap in the guide; supplement with standard practices |
| Questions too generic | Shallow answers that don't map to build plan | Tighten questions — reference specific components, flows, constraints |
| One round's answer is much larger than the other | Both rounds merged into a single response | Verify the prompt file has clear Q1-Q9 separation |
| Answers contain speculative content | "Not in sources — answering from general knowledge" | Strip speculative sections; only keep source-backed content |

---

## Quality Checklist

Before delivering the final guide:

- [ ] Both rounds successfully extracted (verify files exist in `extra/round1/` and `extra/round2/`)
- [ ] Auth was working at time of extraction
- [ ] Notebook gaps are marked in the guide
- [ ] Each section has concrete code examples (not prose-only)
- [ ] Forbidden patterns are marked with ❌ or explicit "Do not" language
- [ ] Invariants are stated as single-sentence architectural rules
- [ ] Codex rules table at the end (10-12 rules)
- [ ] File saved to `docs/{framework}-coding-reference-guide.md`
