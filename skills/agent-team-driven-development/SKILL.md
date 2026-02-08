---
name: agent-team-driven-development
description: Orchestrate development using Claude Code Agent Teams (requires CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1)
user-invocable: false
version: 2.0.0
---

# Agent Team Driven Development

This skill provides guidance on orchestrating development tasks using Claude Code's native **Agent Teams** feature.

## Core Concept
Instead of manually simulating subagents, you leverage the `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` feature to spawn real, parallel agent instances. You act as the **Team Lead**, coordinating specialized teammates.

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
