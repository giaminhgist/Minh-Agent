---
name: test-driven-development
description: "Use a red-green-refactor loop for a requested behavior change or regression fix."
---

# test-driven-development

## Inputs and scope

Behavioral requirement, testing framework and an executable failing example.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Write a test of externally observable behavior. Run it and confirm it fails for the missing behavior rather than syntax, setup or an unrelated dependency.

2. Implement the smallest complete change that makes the test pass. Do not weaken the assertion or substitute mocks for the behavior under test.

3. Refactor while preserving the result, then run related checks. Record the red and green evidence; use a meaningful regression scenario instead of checking the implementation's wording.

## Deliverable and verification

Behavioral test, implementation and observed red/green/refactor checks.

If tests cannot execute, report NOT_RUN and the missing prerequisite. Do not fabricate the red phase after writing the code.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Fix duplicate queue launches with a failing resume test first.
