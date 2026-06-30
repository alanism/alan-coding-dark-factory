# ACDF NotebookLM Ingestion Prompt Set

This is the canonical 27-question prompt set (3 rounds of 9 questions) used to extract, apply, and synthesize expert engineering doctrines from a curated NotebookLM source corpus.

---

## Round 1 — Extraction

Ask these questions to extract raw expert heuristics:
1. What are the core engineering principles emphasized by the expert in these sources?
2. What repeated heuristics or rules of thumb does the expert cite?
3. What common failure modes, bugs, or anti-patterns does the expert warn against?
4. What are the expert's recommended best practices for code architecture and layout?
5. What design patterns does the expert explicitly prefer or enforce?
6. What are the expert's evidence standards for verifying correct behavior?
7. What conditions does the expert define as stop conditions or blockers to development?
8. What are the most useful code examples, algorithms, or snippets mentioned in the sources?
9. What are the key quotes or source anchors that define this expert's engineering doctrine?

---

## Round 2 — Application

Ask these questions to apply the expert's doctrine to our active project modeling:
1. How would this expert review or critique our current architectural models (Mermaid flowcharts, sequences, state transitions)?
2. What specific elements, nodes, or states would the expert object to or flag as risk zones?
3. What components or API orchestration would the expert recommend simplifying or removing?
4. What runtime evidence or logs metrics would the expert demand before approving this build?
5. What specific unit, integration, or E2E tests would the expert add to the validation check list?
6. What risks regarding scale, security, or data integrity would the expert prioritize first?
7. What files, libraries, or architectures would the expert refuse to build or allow in the workspace?
8. What constraints should become binary gates in the active task board?
9. What rules should be added to the project's Reference Guide based on this expert's feedback?

---

## Round 3 — Synthesis

Ask these questions to synthesize the final active doctrine cards:
1. What are the top reusable doctrines that should govern all future builds in this domain?
2. What are the distilled principles that belong in this expert's ACDF Hero Lens card?
3. What interfaces, invariants, or constants belong in the project's Reference Guide?
4. What checklist items should populate the adversarial risk review guide?
5. What are the exact verification gates that must be programmatically enforced?
6. What are the specific stop conditions that must automatically block implementation?
7. What guidance in the sources is outdated, uncertain, or context-specific?
8. How does this expert's advice conflict with or differ from other industry standards?
9. What is the final, single-paragraph distilled operating doctrine for this expert?
