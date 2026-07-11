# Council Decision Record

Use the same bounded proposal, evidence packet, and proposal hash for every selected Hero Card. Each card responds independently before the result is synthesized.

```yaml
decision_id: {change-id}-{decision-id}
proposal_hash: {sha256}
mode: council-led
hard_stop: false
eligible_voters:
  - {hero-card-path}
quorum: {integer}
votes:
  - voter: {hero-card-path}
    decision: APPROVE | REJECT | ABSTAIN
    rationale: {source-backed rationale}
approval_count: {integer}
result: APPROVED | BLOCKED
dissent: {minority concerns or none}
human_approval: {required only for hard stops, scope changes, or escalation}
```

Approve only when quorum is met and `approval_count` is greater than half of the quorum. A tie, no quorum, hard stop, or unresolved critical dissent is `BLOCKED`.
