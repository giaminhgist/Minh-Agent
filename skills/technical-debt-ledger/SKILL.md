---
name: technical-debt-ledger
description: "Inventory intentional shortcuts and define measurable conditions for retiring them."
---

# technical-debt-ledger

## Inputs and scope

Repository paths, shortcut markers, known debt and maintenance constraints.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Locate shortcut: and ponytail: markers plus explicitly identified debt; use the bundled scanner for a read-only inventory.

2. For each real item record the affected behavior, rationale, current ceiling, failure symptom and upgrade path. Keep unverified scanner matches separate from accepted debt.

3. Prioritize by impact and likelihood; fix only when the task includes remediation.

## Deliverable and verification

Debt ledger with source lines, owner when known and measurable upgrade triggers.

Ignore generated/vendor content unless explicitly requested; do not classify every TODO as a confirmed defect.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

For the bundled executable adapter, read [local helper usage and limits](references/local-helper.md) before running it. Resolve scripts relative to this Skill directory, not the user's project.

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

List shortcut markers and identify which limits will be exceeded by the next release.
