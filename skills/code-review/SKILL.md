---
name: code-review
description: "Review a diff or repository, prepare a review request, or evaluate incoming review feedback."
---

# code-review

## Inputs and scope

Mode, base/head, requirements, changed code and test evidence.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Choose diff-review, repository-audit, request-review or feedback mode. A repository audit expands inspection only when requested.

2. For review, follow changed inputs into connected code and identify concrete failure conditions and user impact. Cite precise source locations and distinguish confirmed defects from questions.

3. For requests, provide scope, base/head and acceptance criteria to an available reviewer. For feedback, reproduce or reason through each claim, accept or rebut with evidence and verify fixes.

4. Keep severity tied to impact. Draft external replies unless sending is explicitly authorized.

## Deliverable and verification

Actionable findings or reviewed feedback ledger, evidence and remaining review scope.

Unavailable independent review must be labeled self-review; avoid inventing defects or accepting feedback merely because it sounds authoritative.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Review a queue retry change for duplicate work and resource leaks.
