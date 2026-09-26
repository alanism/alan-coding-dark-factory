# Upgrading ACDF v8 to v9

V9 extends council use across the lifecycle and introduces explicit coordination artifacts. It is a protocol/templates/validation upgrade, not a scheduler release. It preserves human-led and council-led approval modes, existing quorum/majority rules, hard stops, default two-cycle budget (hard maximum five with recorded approval), three-file task limit and the existing JSON schemas.

## Adopt in order

1. Finish an active v8 change under its sealed v8 authority, or obtain the existing explicit approval to replan/reseal it. Never silently replace pinned cards, specs or authority snapshots mid-run.
2. Read the [v9 kernel](../framework/ACDF_kernel.md) and identify the assigned stage. Upstream planning and adversarial review remain valid; a Stage 5 builder consumes the approved handoff without recreating it.
3. Select cards from [the index](../heroes/README.md). Record their version/hash and loaded context. The 17-card snapshot adds DHH, Almeida/Jev, Carter and Thariq to the previously shipped 13 cards. Design and engineering cards retain their directories.
4. Use [task contracts](../templates/agent_task_contract.md). If using the coordination profile, fill the companion manifest, validate its declarations and add it to the authority snapshot before dispatch. The template is a synthetic example, not a real approval packet.
5. Keep existing claim, receipt, state-log, change and authority JSON formats. The coordination manifest has its own `contract_version: 1`; it is not a replacement schema and is not mandatory for completing an already-sealed v8 task.
6. Run the repository checks and then the target project's actual gates. Require evidence from the combined artifact before integration is complete.

## Compatibility and corrections

- Framework routing now points to maintained cards instead of duplicating miniature doctrines, unverified ingestion counts and broad prescriptions. Primary notebook claims were not reverified in this release.
- The earlier Wood summary had no maintained card in the imported collection. It is no longer a routed card; assign protocol/domain review as an operational role with approved sources when needed.
- Local `file:///` navigation links are replaced with relative repository links.
- A hero lens is advisory. A reviewer/voter has an actual identity and explicit eligibility under the selected policy. Adding personas does not add independent reviews or votes.
- One primary lens per task does not waive Stage 3's minimum three independent advisory risk lenses or any configured council quorum.
- Check-then-write claim instructions are explicitly insufficient for concurrency. Atomic/serialized acquisition remains a host responsibility; no runtime locking implementation was added.
- Verifier success wording now describes its structural scope instead of claiming complete security.

## Limits and rollout

No dependencies, production permissions, approval thresholds, CI/CD configuration or automatic release behavior are added. Historical tiny-change artifacts remain compatibility examples; their illustrative hashes are not live authority evidence. The repository verifier checks selected legacy fields, not complete JSON Schema semantics or their snapshot authenticity.

Run a bounded pilot using [the evaluation protocol](../heroes/docs/evaluation.md), holding model, task, tools, budgets and checks constant. Performance and quality improvements are hypotheses until measured. Mermaid content receives structural workflow checks; rendering is a separate check when a renderer is available.

To roll back, return to the previously pinned framework/card revision and approved project configuration. Revalidate or reseal changed authority only through the existing approval process; do not blindly overwrite an active task's files. See [runbook](runbook.md).
