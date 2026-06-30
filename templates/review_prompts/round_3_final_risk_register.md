# ACDF Multi-Model Review: Round 3 Final Risk Register Prompt

You are generating the final prioritized Risk Register for the proposed change. 

## Inputs
[Insert Round 2 summaries and original packet data]

## Instructions
Synthesize all confirmed risks into a prioritized markdown register table. For each risk, you must explicitly declare:
1. **Risk Name & Description**
2. **Severity (High / Medium / Low)**
3. **Evidence Basis**: The specific sequence node, state path, or interface that creates the vulnerability.
4. **Proposed Prevention**: The code heuristic or change needed.
5. **Gate / Test / Receipt Requirement**: The binary check that must be added to `tasks.md` to prevent this risk.
6. **Reference Guide Invariant**: The strict rule that must be appended to the project's Reference Guide.
7. **Blocker Status**: Does this risk block execution until resolved?

## Output Format
Generate your report as a markdown table using these exact columns:
`| Risk | Severity | Evidence | Prevention | Task Gate Check | Reference Invariant | Blocks Build? |`
