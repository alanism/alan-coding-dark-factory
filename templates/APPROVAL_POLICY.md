# Approval Policy

## Selected Mode

Set exactly one:

- `human-led` — the named human approves every required decision.
- `council-led` — selected Engineering and/or Design Hero Cards vote on bounded, in-scope decisions.

## Council Rules

- Required quorum: `{integer}` eligible voters.
- Approval threshold: strict majority of the quorum.
- Valid votes: `APPROVE`, `REJECT`, `ABSTAIN`.
- Record the proposal hash, selected cards, every vote, rationale, dissent, and final result.
- A tie, missing quorum, unresolved critical dissent, scope change, changed success criteria, or hard-stop concern blocks the change.

## Human-Only Hard Stops

Explicit human approval is required for security, privacy, legal, production-release, credential, external-data-boundary, and scope-expansion decisions. Council votes cannot waive lifecycle gates or authority constraints.
