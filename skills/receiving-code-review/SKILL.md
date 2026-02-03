---
name: receiving-code-review
description: Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation
argument-hint: (no arguments - provides reference guidance)
user-invocable: false
version: 1.0.0
---

# Receiving Code Review

This skill provides guidance on processing review feedback with technical rigor before changing code.

## Core Concept

Understand and verify first; implement or push back with evidence. Performative agreement and blind implementation lead to poor outcomes.

## Feedback Triage

**Severity and Dependency**: Feedback should be triaged by severity (critical/major/minor) and dependency (blocking/independent). Resolution order follows this classification.

**Ambiguous Items**: Unclear feedback requires clarification before implementation. Guessing at reviewer intent leads to misdirected effort.

**Conflict Detection**: Feedback may conflict with architectural constraints or other comments. Conflicts need explicit resolution before implementation.

See `references/feedback-triage.md` for classification criteria and triage workflows.

## Clarification Patterns

**When Clarification Is Needed**:
- Feedback is ambiguous about what to change
- Suggested approach conflicts with constraints
- Impact or scope is unclear

**Effective Clarification**:
- Reference specific code locations
- Explain current implementation rationale
- Ask targeted questions about suggestions

See `references/clarification-patterns.md` for clarification templates and examples.

## Verification Before Implementation

**Test Against Requirements**: Suggestions should be verified against code, tests, and requirements. Not all suggestions improve the codebase.

**Architecture Consistency**: Changes should maintain architectural consistency. Localized improvements shouldn't violate system-wide patterns.

**Evidence-Based Decisions**: Accept/defer/pushback decisions need concrete rationale. Opinion-based responses lack credibility.

## Implementation Loop

**Incremental Implementation**: Accepted feedback should be implemented incrementally with verification after each change. Batch implementation obscures which change caused failures.

**Verification After Changes**: Each implemented suggestion needs verification. Assumed correctness leads to introduced bugs.

**Evidence Capture**: Implementation results should be captured as evidence. "Fixed" claims need supporting test outputs.

See `references/implementation-loop.md` for implementation patterns and verification strategies.

## Pushback with Evidence

**When Pushback Is Appropriate**:
- Suggestion conflicts with architectural constraints
- Change would introduce bugs or regressions
- Cost outweighs benefit given current priorities

**Effective Pushback**:
- Concrete rationale with code references
- Evidence from tests or existing patterns
- Alternative approaches when available

See `references/pushback-examples.md` for pushback templates and examples.

## Common Anti-Patterns

**Blanket Agreement**: "You're absolutely right, I'll fix all of these" - Performative agreement without understanding.

**Blind Implementation**: Implementing without verifying suggestions against requirements. Not all feedback improves code.

**Closing Without Evidence**: Marking items resolved without verification outputs. Claims need supporting evidence.

**Coupled Changes**: Implementing multiple coupled feedback items simultaneously. Obscures which change caused issues.

## References

- `references/feedback-triage.md` - Severity classification and triage workflows
- `references/clarification-patterns.md` - Clarification templates and examples
- `references/implementation-loop.md` - Implementation patterns and verification
- `references/pushback-examples.md` - Pushback templates and rationale examples
