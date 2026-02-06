---
name: code-review-guidance
description: Use when requesting or processing code reviews - encompasses defining clear review scope (Requesting) and rigorously triaging feedback (Receiving)
argument-hint: (no arguments - provides reference guidance)
user-invocable: false
version: 1.0.0
---

# Code Review Guidance

This skill provides unified guidance for the entire code review lifecycle: from requesting focused reviews to rigorously processing feedback.

## Core Concept

Code review is a two-way technical contract, not a social performance.

- **Requesting**: Define clear boundaries (BASE..HEAD) and risk areas. Context-free requests waste time.
- **Receiving**: Verify technically before accepting. No performative agreement. Severity matters.

## Workflow: Requesting Review

**1. Define Scope**: Identify the exact commit range (BASE_SHA → HEAD_SHA).
**2. Provide Context**: Summarize what changed, why, and specific risk areas.
**3. Dispatch Agent**: Use `code-reviewer` agent with explicit template.

See `references/review-request-template.md` for the request structure.

## Workflow: Receiving Feedback

**1. Triage**: Classify by severity (Critical/Major/Minor). Critical issues block merge.
**2. Verify**: Don't blindly implement. Check against requirements and codebase reality.
**3. Respond**: Technical acknowledgment or reasoned pushback with evidence.
**4. Implement**: One item at a time, verifying each change.

See `references/feedback-triage.md` for detailed triage and response patterns.

## Quality Gate

- **Critical Findings**: Must be resolved before merge.
- **Pushback**: Valid and encouraged when supported by technical evidence.

## References

- `references/review-request-template.md` - Templates for requesting reviews
- `references/feedback-triage.md` - Classification and response workflows
