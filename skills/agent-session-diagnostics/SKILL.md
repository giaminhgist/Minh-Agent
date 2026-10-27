---
name: agent-session-diagnostics
description: "Analyze agent session logs for repeated work, wasted calls and workflow failures."
---

# agent-session-diagnostics

## Inputs and scope

Selected session exports, timing/usage fields and redaction requirements.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Identify supported log schema and inspect only relevant records. Remove credentials, private payloads and unnecessary user content from the report.

2. Build an event timeline and group retries, repeated reads, task switches and failed checks. Separate measured token/time fields from estimates.

3. Connect costly sequences to a reproducible cause and propose a targeted adjustment. Produce a minimal scrubbed reproduction when requested.

## Deliverable and verification

Redacted timeline, measured versus estimated costs, root causes and actionable recommendations.

Missing logs or usage fields limit conclusions; do not infer performance gains without a comparable baseline.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Explain why a debugging session repeatedly read the same files without making progress.
