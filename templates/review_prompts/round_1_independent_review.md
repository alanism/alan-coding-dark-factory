# ACDF Multi-Model Review: Round 1 Blind Critique Prompt

You are performing an independent, blind adversarial review of the proposed system change. Do not assume other reviewers are correct. Audit the change packet using strict systems thinking.

## Input Review Packet
[Insert review_packet.md content here]

## Instructions
Review the packet and identify issues in the following categories:
1. **Core Risks**: Architectural weaknesses, race conditions, bottlenecks.
2. **Hidden Assumptions**: Unstated dependencies or configurations.
3. **Failure Modes**: What happens when network calls time out, or state transitions fail?
4. **Security Gaps**: Trust boundary crossings and potential privilege leaks.
5. **Test Gaps**: Missing scenarios or gates on the task list.

## Output Format
Generate your report using these markdown sections:
* ## Key Risks
* ## Architecture Critique
* ## Missing Specifications
* ## Recommended Task Gate Updates
* ## Questions for the Human Governor
