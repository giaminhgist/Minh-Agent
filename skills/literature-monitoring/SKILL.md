---
name: literature-monitoring
description: "Design or run an authorized literature watch and produce a deduplicated digest."
---

# literature-monitoring

## Inputs and scope

Topics, queries, sources, date window, cadence and notification preferences.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Define reproducible queries and inclusion rules; preserve last-seen identifiers and source dates.

2. For a requested one-time check, search and compare with the prior ledger; summarize genuinely new relevant work.

3. For recurring monitoring, configure an actual host scheduler only when authorized, with explicit trigger and notification scope.

4. Produce a digest with links and reasons for relevance, recording unavailable sources.

## Deliverable and verification

Query configuration, last-seen ledger, digest and actual scheduler status.

A saved schedule template is not an active monitor. No scheduler means recurring execution is unavailable.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Create a weekly literature-watch configuration and run an initial deduplicated scan.
