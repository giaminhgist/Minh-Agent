---
name: reviewer-calibration
description: "Calibrate a review rubric against labeled examples and report limits of agreement."
---

# reviewer-calibration

## Inputs and scope

Rubric, reference reviews, labels, sample definition and calibration objective.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Define what labels measure and separate training examples from held-out assessment.

2. Apply the rubric to examples with anchored rationales and compare against references.

3. Analyze disagreement by criterion; revise unclear anchors and reevaluate without leaking held-out answers.

4. Report sample size, agreement metrics when appropriate and limits of generalization.

## Deliverable and verification

Calibrated rubric, example judgments, disagreement analysis and measured evaluation.

Do not claim calibrated live review merely because a profile file exists; calibration is NOT_RUN without labeled evidence.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Evaluate a reviewer rubric against a small labeled manuscript set.
