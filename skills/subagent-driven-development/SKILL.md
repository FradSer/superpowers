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

## Workflow

**Execution**: Fresh subagent per task with clean context. See `references/task-decomposition.md`, `references/implementer-handoff.md`, `references/examples.md`.

**Review Gates**: Spec review then quality review. Both required with evidence. See `references/spec-review-gate.md`, `references/quality-review-gate.md`, `references/completion-criteria.md`, `references/task-execution-loop.md`, `references/review-and-remediation-loop.md`.

**Avoid**: Scope creep, hidden dependencies, skipped verification. See `references/common-mistake-patterns.md`, `references/common-mistake-remediation.md`, `references/advantages.md`.

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
