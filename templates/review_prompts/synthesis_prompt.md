# ACDF Multi-Model Review: Synthesis Guidelines (Human & Synthesis Agent)

You are synthesizing multiple independent risk registers into the canonical `risk_review.md` for this change. 

## Inputs
[Insert Round 3 model outputs here]

## Synthesis Rules
1. **Merge Duplicates**: Consolidate overlapping risks under single descriptive titles.
2. **Preserve Minority Warnings**: High-severity warnings (especially regarding security, database race conditions, or state transitions) must never be averaged away or deleted just because only one model flagged them.
3. **Evidence-First**: Prioritize concrete compiler/test/AST assertions over subjective design advice.
4. **Convert Objections to Gates**: If a model flags a risk, it must become a binary test gate in `tasks.md`.
5. **Convert Ambiguity to Stop Conditions**: If a model notes that a behavior is unspecified, it must be flagged as a Stage 4 execution blocker until defined.

## Output Target
Produce the final `.acdf/changes/<change-id>/risk_review.md` listing the prioritized register.
