---
name: requesting-code-review
description: Use when completing tasks, implementing major features, or before merging to verify work meets requirements
argument-hint: (no arguments - provides reference guidance)
user-invocable: false
version: 1.0.0
---

# Requesting Code Review

This skill provides guidance on requesting review with precise boundaries so defects are found quickly and accurately.

## Core Concept

Clear scope, clear intent, clear commit range. Context-free "review everything" requests waste reviewer time and miss critical issues.

## Review Request Structure

**Exact Review Range**: Review requests should specify exact commit boundaries (BASE_SHA → HEAD_SHA). Ambiguous ranges lead to incomplete reviews.

**Change Summary**: What changed and why. Reviewers need context about the purpose and expected behavior of changes.

**Risk Areas**: Specific areas requiring careful review. Highlighting complexity or uncertainty focuses reviewer attention where it matters.

See `references/review-request-template.md` for complete request structure and examples.

## When Code Review Applies

**Appropriate Contexts**:
- Meaningful task or feature slice is complete
- Approaching merge-sensitive milestones
- Risk level requires formal reviewer sign-off

**Review Scope Considerations**:
- Avoid context-free requests lacking change summary
- Include enough context for independent review
- Highlight areas of uncertainty or complexity

## Finding Resolution

**Severity Classification**: Findings should be classified by severity (critical, major, minor, informational). Resolution priority follows severity.

**Critical Findings**: Block merge until resolved. These represent bugs, security issues, or severe quality problems.

**Non-Critical Findings**: Can be resolved post-merge or deferred with rationale. Balance quality with delivery urgency.

See `references/finding-resolution-flow.md` for classification criteria and resolution workflows.

## Resolution Evidence

**Concrete Resolution**: Each finding needs concrete resolution status (fixed, deferred, won't-fix) with supporting evidence.

**Verification**: Fixed findings should be verified with test outputs or code references. Claims need supporting evidence.

**Communication**: Resolution status should be communicated clearly to reviewers. Ambiguous responses lead to review cycles.

## Review as Quality Gate

**Not Optional Noise**: Code review is a quality gate, not a bureaucratic checkbox. Meaningful review catches defects before production.

**Merge Discipline**: Unresolved critical findings block merge. Shipping known critical issues creates technical debt.

**Reviewer Respect**: Reviewers invest time to improve quality. Treating review as optional disrespects that investment.

## References

- `references/review-request-template.md` - Request structure and examples
- `references/finding-resolution-flow.md` - Severity classification and resolution workflows
