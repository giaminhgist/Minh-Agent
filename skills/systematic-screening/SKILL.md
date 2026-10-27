---
name: systematic-screening
description: "Screen records for a systematic review with explicit eligibility and adjudication."
---

# systematic-screening

## Inputs and scope

Protocol, records/full texts, inclusion criteria and reviewer arrangement.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Choose protocol, quick exploration, pilot, title/abstract, full-text, adjudication, audit or report mode. Freeze operational eligibility rules before production screening.

2. Pilot ambiguous records and refine rules transparently; record record-ID, stage, decision, criterion and reason.

3. Treat missing full text as unresolved rather than an exclusion based on guessed content. Resolve disagreements through a recorded adjudication process.

4. Deduplicate and reconcile counts across stages, preserving exclusions and audit trail.

## Deliverable and verification

Screening ledger, decisions with reasons, disagreement record and flow counts.

One model reviewing twice is not two independent reviewers; exploratory screening is not a completed systematic review.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Screen a pilot set against explicit eligibility rules and explain ambiguous decisions.
