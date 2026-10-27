---
name: citation-verification
description: "Verify bibliographic metadata, reference existence and support for cited claims."
---

# citation-verification

## Inputs and scope

Bibliography, citation-bearing text and accessible primary records.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Separate existence, metadata accuracy and semantic support. Resolve identifiers against reliable records and inspect the cited passage when accessible.

2. Compare title, authors, year, venue and DOI field by field; normalize format without merging genuinely different versions.

3. For claim support, record source location and whether it entails, qualifies, contradicts or does not address the claim.

4. Export a discrepancy ledger; produce XLSX only when requested and spreadsheet tooling is available.

## Deliverable and verification

Reference verification table, field-level differences, claim-support findings and access limits.

An inaccessible source is unverified, not fabricated. Similar titles alone are insufficient to change a citation.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Cross-check a bibliography and flag a real paper cited for an unsupported claim.
