# ACDF v8 Authority — Content-Hashed Snapshots

This document defines how execution boundaries are locked and verified in **Stage 4 (Execution Readiness)** using content-hashed snapshots.

---

## 1. Establishing Authority

To prevent agents from straying into stale design specifications, changing active code styles, or editing unapproved directories, the workspace is locked using a content-hashed state registry.

The registry is written in `.acdf/changes/<change-id>/authority.json`. It stores:
* SHA-256 hashes of all binding configuration files, specification guides, architecture layouts, and task files.
* Allowed write boundaries (whitelisted files).
* Forbidden directories (blacklisted files).

---

## 2. Generating the Snapshot

When Stage 3 (Adversarial Review) is complete, the snapshot tool generates the target `authority.json`.

For each file in the project's authority scope:
1. Read file contents.
2. Compute the SHA-256 hash.
3. Write the target file path and hash value into the `snapshots` dictionary.
4. Define the whitelist zones under `write_rules.allowed_files`.

---

## 3. Runtime Authority Verification

At the start of every execution cycle in Stage 5, the agent must verify the current working files against the authority snapshot.

```python
# Pseudo-code logic for verification:
for filepath, expected_hash in authority_snapshots.items():
    current_hash = calculate_sha256(filepath)
    if current_hash != expected_hash:
        raise AuthorityError(f"File {filepath} hash mismatch! Authority has been violated.")
```

If a mismatch is found, the agent must STOP immediately, mark the task as **BLOCKED** in the ledger, and notify the user. The snapshot can only be regenerated with explicit human confirmation.
