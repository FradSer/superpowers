---
name: agent-team-driven-development
description: Use when you need to orchestrate complex, multi-step development tasks that can be parallelized across multiple specialized agents (e.g., Implementer, Reviewer, Architect) - best for large features or refactors where dividing work speeds up execution
user-invocable: false
version: 2.1.0
---

# Agent Team Driven Development

This skill provides guidance on orchestrating development tasks using Claude Code's native **Agent Teams** feature.

## Core Concept

Use this skill to spawn real, parallel agent instances for complex work. Instead of manually simulating subagents, you leverage the `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` feature to act as the **Team Lead**, coordinating specialized teammates. This is ideal for tasks that benefit from separation of concerns (e.g., implementation vs. review) or parallel execution.

## Roles

- **Implementer**: Focuses on BDD, testing, and isolated implementation.
  - See `roles/implementer.md`
- **Reviewer**: Focuses on spec compliance and strict code quality.
  - See `roles/reviewer.md`
- **Architect**: Focuses on high-level design and breaking down complex plans.
  - See `roles/architect.md`

## Workflow

1. **Initiate Team**: Spawn a team based on your needs.
   - See `workflows/initiate-team.md`
2. **Assign Tasks**: Delegate precise tasks to teammates.
   - See `workflows/manage-team.md`
3. **Monitor & Review**: Act as the Lead. Review teammate outputs (plans, code) before approving.
   - Use `teammateMode` (in-process or tmux) to observe progress.
4. **Merge & Verify**: Once teammates complete their work, verify integration and merge.

## References

- [Agent Teams Documentation](https://code.claude.com/docs/en/agent-teams)
