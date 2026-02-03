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

- **Explicit over implicit**: Plans must be explicit about files, sequencing, tests, and verification evidence
- **Granular tasks**: Decompose into small tasks with clear done criteria
- **Verification-driven**: Include concrete verification commands for each task
- **Context independence**: Never assume executor has implicit project context

## When to Use

- Work spans multiple files or phases
- Handoff quality matters (another agent or future session)
- Hidden assumptions would be costly

## Process Phases

**Phase 1: Plan Structure**

Define the overall goal, architecture direction, and constraints.

- Review the spec or requirements document
- Use `./references/plan-structure-template.md` for structure
- Define success criteria and constraints
- Identify architectural patterns and dependencies
- Use `AskUserQuestion` tool if critical requirements are ambiguous

**Phase 2: Task Decomposition**

Break down the work into granular, executable tasks.

- Decompose into small tasks with clear done criteria
- List exact files to create/modify/test for each task
- Add TDD steps per task using `./references/task-granularity-and-verification.md`
- Include concrete verification commands (test runs, lint checks, build commands)
- Define commit boundaries and rollback notes
- Order tasks by dependencies

**Phase 3: Validation & Documentation**

Review and finalize the plan for execution.

- Verify each task has explicit verification steps
- Check that no assumptions are left implicit
- Ensure task granularity allows incremental progress
- Use `AskUserQuestion` tool to confirm plan approach with user
- Save plan to `docs/plans/YYYY-MM-DD-<topic>-plan.md`
- Commit the plan document to git

## Exit Criteria

- [ ] Plan document created at `docs/plans/YYYY-MM-DD-<topic>-plan.md`
- [ ] Goal, architecture direction, and constraints clearly defined
- [ ] Tasks decomposed with explicit file lists and verification commands
- [ ] TDD steps included for each implementation task
- [ ] Commit boundaries and rollback notes specified
- [ ] No vague tasks like "implement feature" - all tasks are concrete
- [ ] User approval received for the plan

## References

- `references/plan-structure-template.md` - Template for plan structure
- `references/task-granularity-and-verification.md` - Guide for task breakdown and verification
