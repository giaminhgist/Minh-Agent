---
name: research-evidence-audit
description: "Analyze experiment results or audit manuscript claims against raw research evidence."
---

# research-evidence-audit

## Inputs and scope

Mode, raw outputs, evaluation code, manuscript and provenance records.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Choose results-analysis, experiment-integrity or manuscript-claim mode. Keep statistical analysis distinct from forensic verdicts.

2. Trace datasets, splits, metrics and aggregation back to their implementation and raw records. Check missing runs, duplicate seeds and incompatible denominators.

3. For each manuscript number or claim locate supporting evidence, recompute when possible and flag unsupported generalization.

4. Report exclusions, uncertainty and unresolved integrity issues without filling missing data.

## Deliverable and verification

Reproducible analysis or claim ledger with source anchors and severity-ranked discrepancies.

Missing raw outputs prevents confirmation; an audit with limited access cannot establish that no manipulation occurred.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Check a paper's reported average against per-seed CSV outputs.
