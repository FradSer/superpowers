---
name: subagent-driven-development
description: Use when executing implementation plans with independent tasks in the current session
argument-hint: (no arguments - provides reference guidance)
user-invocable: false
version: 1.0.0
---

# Subagent-Driven Development

This skill provides guidance on executing implementation plans in-session using fresh subagents with two review gates per task.

## Core Concept

One task → one fresh implementer → spec gate → quality gate → verified completion. This pattern avoids context pollution and ensures consistent quality gates.

## Pattern Overview

**Fresh Implementer Per Task**: Each task gets a new subagent with clean context. Reusing stale implementer context leads to assumption carryover and scope creep.

**Two Review Gates**: Spec-compliance review first, then code-quality review. Skipping either gate compromises quality.

**Verified Completion**: Tasks are complete only after both gates pass and verification evidence is captured.

For trade-offs and why this pattern tends to outperform single-agent execution, see `references/advantages.md`.

## Task Decomposition

**One-Task Units**: Plans should be split into single-task units with explicit success criteria. Multi-task handoffs confuse scope.

**Independence**: Tasks should be mostly independent to allow parallel execution. Tightly coupled tasks require sequential execution.

**Clear Criteria**: Each task needs unambiguous success criteria. Ambiguous criteria lead to incomplete implementations.

See `references/task-decomposition.md` for decomposition strategies and success criteria templates.

## Implementer Handoff

**Handoff Format**: Implementers receive task specification, relevant context, and success criteria. Missing context leads to assumptions.

**Scope Clarity**: Handoff should clearly define what's in-scope and out-of-scope. Scope ambiguity causes scope creep.

**Examples**: Concrete examples in handoffs reduce misinterpretation. Abstract specifications lead to implementation variance.

See `references/implementer-handoff.md` for handoff templates and `references/examples.md` for concrete examples.

## Spec Review Gate

**First Gate Purpose**: Verify implementation matches specification before reviewing code quality. Spec mismatches invalidate quality review.

**Gap Closure**: All spec gaps must be closed before proceeding to quality review. Partial spec compliance compounds with quality issues.

**Evidence**: Spec compliance requires evidence (test outputs, behavior verification). Claims need supporting proof.

See `references/spec-review-gate.md` for spec review criteria and gap closure workflows.

## Quality Review Gate

**Second Gate Purpose**: Verify code quality, maintainability, and best practices after spec compliance is confirmed.

**Finding Resolution**: Quality findings should be resolved before marking task complete. Technical debt accumulates from deferred quality issues.

**Consistency**: Quality standards should be applied consistently across tasks. Inconsistent standards create technical debt variance.

See `references/quality-review-gate.md` for quality criteria and resolution workflows.

## Completion Criteria

**Both Gates Required**: Tasks cannot be marked complete until both spec and quality gates pass. Skipping gates under time pressure creates quality debt.

**Verification Evidence**: Completion requires verification evidence (test runs, checks passing). No completion without proof.

**No Gate Skipping**: Time pressure does not justify skipping review gates. Skipped gates create rework later.

See `references/completion-criteria.md`, `references/task-execution-loop.md`, and `references/review-and-remediation-loop.md` for detailed completion workflows.

## Common Mistake Patterns

**Scope Creep**: Implementers expanding beyond task boundaries. Fixed by clear handoff scope definition.

**Hidden Dependencies**: Tasks assumed independent but actually coupled. Fixed by better task decomposition.

**Skipped Verification**: Marking complete without running checks. Fixed by enforcing completion criteria.

See `references/common-mistake-patterns.md` and `references/common-mistake-remediation.md` for comprehensive mistake patterns and remediations.

## When This Pattern Applies

**Appropriate Contexts**:
- Tasks are decomposed and mostly independent
- Fast iteration without context pollution is needed
- Quality gates must be applied consistently

**Pattern Advantages**:
- Fresh context per task avoids assumption carryover
- Consistent review gates ensure quality
- Parallel execution where tasks are independent

## References

- `references/advantages.md` - Pattern trade-offs and benefits
- `references/task-decomposition.md` - Decomposition strategies
- `references/implementer-handoff.md` - Handoff format and templates
- `references/examples.md` - Concrete handoff examples
- `references/spec-review-gate.md` - Spec compliance review
- `references/quality-review-gate.md` - Quality review criteria
- `references/completion-criteria.md` - Task completion requirements
- `references/task-execution-loop.md` - Execution workflow
- `references/review-and-remediation-loop.md` - Review and fix workflow
- `references/common-mistake-patterns.md` - Known failure patterns
- `references/common-mistake-remediation.md` - Remediation strategies
