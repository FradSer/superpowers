---
name: writing-plans
description: Use when you have a spec or requirements for a multi-step task, before touching code
argument-hint: (no arguments - provides process guidance)
user-invocable: true
version: 1.0.0
---

# Writing Plans

Create executable implementation plans that reduce ambiguity for whoever executes them.

## Core Principles

Explicit over implicit, granular tasks, verification-driven, context independence.
**MANDATORY**: Tasks must be driven by BDD scenarios (Given/When/Then).
When plans include unit tests, require external dependency isolation with test doubles (DB/network/third-party APIs).

## Workflow

**Phase 1 - Plan Structure**: Define goal, architecture, constraints. Use `references/plan-structure-template.md`.

**Phase 2 - Task Decomposition**: Break into small tasks mapped to specific BDD scenarios. Explicit files, BDD steps, verification commands. See `references/task-granularity-and-verification.md`.

**Phase 3 - Validation & Documentation**: Verify completeness, confirm with user, save to `docs/plans/YYYY-MM-DD-<topic>-plan.md`, commit.

## Exit Criteria

Plan created with clear goal/constraints, decomposed tasks with file lists and verification, BDD steps, commit boundaries, no vague tasks, user approval.

## References

- `references/plan-structure-template.md` - Template for plan structure
- `references/task-granularity-and-verification.md` - Guide for task breakdown and verification
