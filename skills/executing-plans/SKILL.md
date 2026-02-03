---
name: executing-plans
description: Use when you have a written implementation plan to execute in a separate session with review checkpoints
argument-hint: (no arguments - provides process guidance)
user-invocable: true
version: 1.0.0
---

# Executing Plans

Execute written implementation plans in predictable batches with review checkpoints.

## Core Principles

- **Review before execution**: Understand the full plan and surface ambiguities first
- **Batch verification**: Verify each batch before moving to the next
- **Explicit blockers**: Stop and escalate when blockers invalidate assumptions
- **Evidence-driven**: Capture verification outputs for each batch

## When to Use

- A plan already exists and should be executed as written
- Work is risky enough to require staged checkpoints
- Blocker handling must be explicit

## Process Phases

**Phase 1: Plan Review**

Read and validate the plan before starting execution.

- Read the full implementation plan document
- Use `./references/blocker-and-escalation.md` to identify ambiguities
- Surface unclear requirements or missing context immediately
- Use `AskUserQuestion` tool to clarify ambiguities before proceeding
- Do not silently reinterpret unclear requirements

**Phase 2: Task Setup**

Prepare for batch execution.

- Convert plan items into a task tracker (use TaskCreate tool)
- Identify natural batch boundaries based on dependencies
- Verify test environment is ready
- Ensure all prerequisites are satisfied

**Phase 3: Batch Execution**

Execute tasks in batches with verification checkpoints.

- Execute the next batch exactly to scope using `./references/batch-execution-playbook.md`
- Follow TDD workflow: write test → implement → verify
- Run required checks and capture outputs (test results, lint, build)
- Do not batch so large that feedback comes too late
- Stop immediately if blockers invalidate assumptions

**Phase 4: Verification & Feedback**

Verify batch completion and gather feedback before continuing.

- Publish batch evidence (test outputs, verification results)
- Use `AskUserQuestion` tool to confirm: "Batch N complete. Ready to proceed?"
- Wait for user feedback before continuing
- Update task tracker to mark completed tasks
- Repeat Phase 3-4 until all tasks complete

## Exit Criteria

- [ ] All plan tasks executed and verified
- [ ] All verification commands passed with evidence captured
- [ ] No unresolved blockers remaining
- [ ] All batches reviewed and approved by user
- [ ] Task tracker shows all tasks completed
- [ ] Final verification run passes (all tests, lint, build)

## References

- `references/blocker-and-escalation.md` - Guide for identifying and handling blockers
- `references/batch-execution-playbook.md` - Pattern for batch execution
