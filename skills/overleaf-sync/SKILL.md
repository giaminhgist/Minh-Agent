---
name: overleaf-sync
description: "Set up or reconcile synchronization between a local LaTeX project and Overleaf."
---

# overleaf-sync

## Inputs and scope

Project identity, local Git state, supported bridge and requested direction.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Inspect remotes and uncommitted work without exposing credentials.

2. For pull/status compare local and remote history; preserve local edits before reconciliation.

3. Resolve conflicts explicitly in sources and rebuild affected documents.

4. Push only when authorized and report the actual resulting revision. Retain credentials in the host's secure mechanism.

## Deliverable and verification

Sync status, reconciled files, revision evidence and unresolved conflicts.

If the account lacks Git bridge access, provide export/import guidance and label live sync unavailable; never overwrite remote work blindly.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Pull an Overleaf project and resolve a bibliography conflict without losing local edits.
