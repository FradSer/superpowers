---
name: executing-plans
description: Use when you have a written implementation plan to execute in a separate session with review checkpoints
user-invocable: true
version: 1.0.0
---

# Executing Plans

Execute written implementation plans in predictable batches. Supports **Serial Execution** (single subagent) or **Parallel Execution** (Agent Teams).

## Core Principles

Review before execution, batch verification, explicit blockers, evidence-driven approach.

## Workflow

**Phase 1 - Plan Review**: Read plan, identify ambiguities, clarify before proceeding. See `./references/blocker-and-escalation.md`.

**Phase 2 - Task Setup**: Use `TaskCreate` tool to create tasks from the plan. Identify batch boundaries, verify prerequisites.

**Phase 3 - Batch Execution**: Execute to scope.
- **Serial**: Standard BDD loop.
- **Parallel**: Create Agent Team using Skill tool load `superpowers:agent-team-driven-development` skill, assign tasks, wait for completion.
See `./references/batch-execution-playbook.md`.

**Phase 4 - Verification & Feedback**: Publish evidence, confirm with user, update tracker. Repeat Phase 3-4 until complete.

## Exit Criteria

All tasks executed and verified, evidence captured, no blockers, user approval received, final verification passes.

## References

- `./references/blocker-and-escalation.md` - Guide for identifying and handling blockers
- `./references/batch-execution-playbook.md` - Pattern for batch execution
