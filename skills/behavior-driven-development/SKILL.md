---
name: behavior-driven-development
description: Use when implementing features or bugfixes from behavior-focused requirements (Given/When/Then scenarios in design docs), before writing implementation code
argument-hint: (no arguments - provides reference guidance)
user-invocable: false
version: 2.1.0
---

# Behavior-Driven Development

This skill runs BDD-guided TDD in the active agent conversation: parse behavior scenarios from design docs, write tests, execute loops, and align implementation without process-artifact files.

## Core Concept

Behavior scenarios are executable specifications. TDD implements them through RED -> GREEN -> REFACTOR.

## Required Inputs

- Design entrypoint: `docs/plans/YYYY-MM-DD-<topic>-design/_index.md`
- Scenario source: `bdd-specs.md` (preferred, standard Gherkin) or `bdd-scenarios.md` (legacy) linked from `_index.md`

Scenario format:

1. **Standard Gherkin** (in `bdd-specs.md`):
   ```gherkin
   Feature: User Login
     Scenario: Successful login
       Given user exists...
       When user logs in...
       Then user is redirected...
   ```

2. **Legacy Format** (in `bdd-scenarios.md`):
   - `### SCN-001 <title>`
   - `Given: ...`
   - `When: ...`
   - `Then: ...`
   - optional `Tags: smoke, api, web`

## Conversation-Flow Loop (In-Memory)

For each scenario ID, keep loop state in memory:

- `scenario_id`
- `phase` (`RED`, `GREEN`, `REFACTOR`)
- `iteration`
- `last_failure_reason`
- `stalled_count`

Execution sequence:

1. Parse scenario from design docs.
2. Generate/adjust tests for that scenario.
3. Run tests (`RED` must fail first).
4. Apply minimal implementation fix (`GREEN`).
5. Re-run tests and evaluate progress.
6. Run refactor verification pass (`REFACTOR`).
7. Return final conversational result (`passed`, `failed`, `manual decision required`).

Do not generate `.feature`, `summary.json`, `events.jsonl`, or `manual_decision/*.md` in default workflow.

## Safety Controls

- Enforce max iterations per scenario.
- Trigger manual decision point when no progress repeats.
- Do not loop indefinitely.

## Test Double Discipline

- Unit tests must isolate external dependencies (DB/network/third-party APIs) via appropriate test doubles.
- BDD is behavior specification, not full-mock acceptance theater.

## Agent Team Compatibility

This skill is designed to be run by an **Implementer** teammate within an Agent Team (or by the Team Lead). 
See Skill tool load `superpowers:agent-team-driven-development` skill for orchestrating the team execution.

## Legacy Compatibility

Legacy file-based controller scripts exist for external harness compatibility (`scripts/orchestrate.sh`, `scripts/tdd_loop_controller.py`), but the preferred modern workflow is via Agent Teams.

## References

- `references/loop-contract.md` - Conversation-flow contract and scenario rules
- `references/red-phase-guide.md` - Writing effective failing tests
- `references/green-phase-guide.md` - Minimal implementation strategies
- `references/refactor-phase-guide.md` - Refactoring while maintaining green
- `references/test-design-patterns.md` - Test design patterns and granularity
- `references/anti-patterns-and-rationalizations.md` - Common pitfalls to avoid
- `references/verification-checklist.md` - Final verification steps
- `testing-anti-patterns.md` - Broader anti-pattern catalog
