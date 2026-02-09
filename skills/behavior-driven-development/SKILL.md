---
name: behavior-driven-development
description: Use when implementing features or bugfixes from behavior-focused requirements (Given/When/Then scenarios in design docs), before writing implementation code
argument-hint: (no arguments - provides reference guidance)
user-invocable: false
version: 2.1.0
---

# Behavior-Driven Development

This skill runs BDD in the active agent conversation: parse behavior scenarios from design docs, write tests, execute loops, and align implementation without process-artifact files.

## Core Concept

Behavior scenarios are executable specifications. BDD implements them through RED -> GREEN -> REFACTOR.

## Required Inputs

- Design entrypoint: `docs/plans/YYYY-MM-DD-<topic>-design/_index.md`
- Scenario source: `bdd-specs.md` (Standard Gherkin) linked from `_index.md`

Scenario format:

**Standard Gherkin** (in `bdd-specs.md`):

### Keywords

- **Feature**: High-level description of a software feature. Groups related scenarios.
- **Rule**: (Optional) Represents one business rule. Groups scenarios belonging to this rule.
- **Example** (or **Scenario**): Concrete example illustrating a business rule. Consists of steps.
- **Given**: Initial context/scene setup (past tense).
- **When**: Event or action (interaction).
- **Then**: Expected outcome or result (assertion).
- **And / But**: Connects multiple steps of the same type.
- **Background**: Shared Given steps run before each scenario in a feature.
- **Scenario Outline**: Runs the same scenario with different values from an Examples table.

### Example Usage

```gherkin
Feature: User Login
  Background:
    Given the user database is initialized

  Scenario: Successful login
    Given user "Alice" exists with password "password123"
    When she logs in with "Alice" and "password123"
    Then she is redirected to the dashboard

  Scenario Outline: Invalid login
    Given user "Alice" exists with password "password123"
    When she logs in with "<username>" and "<password>"
    Then she sees an error message "<error>"

    Examples:
      | username | password    | error            |
      | Alice    | wrong       | Invalid password |
      | Bob      | password123 | User not found   |
```

For full details, see [Cucumber Gherkin Reference](./references/cucumber-gherkin-reference.md).


## Conversation-Flow Loop (Detailed Contract)

**Input sources:**
- `docs/plans/YYYY-MM-DD-<topic>-design/_index.md`
- `bdd-specs.md` (Standard Gherkin) linked from `_index.md`

**In-Memory State Fields:**
Track per scenario in conversation state: `scenario_id`, `phase` (`RED`, `GREEN`, `REFACTOR`), `iteration`, `last_failure_reason`, `stalled_count`.

**Loop Behavior:**
1. Parse scenario from design docs.
2. Generate/update tests from scenario intent.
3. Run verification (`RED` must fail first).
4. Implement minimal fix (`GREEN`).
5. Re-run and evaluate progress.
6. Run refactor verification pass (`REFACTOR`).

**Safety Thresholds:**
- Cap max iterations per scenario.
- Escalate to manual decision point on repeated no-progress.
- Never run unbounded loops.

## Red Phase Strategy

**Goal:** Write a failing test that strictly proves the absence of the feature or the presence of the bug.

**The Iron Law:** NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST.
- Verify that the test fails (not errors).
- Confirm failure message is expected (e.g., "Expected 200, got 404").
- If test passes immediately, you are testing existing behavior or your test is broken. Fix the test.

**Key Action:**
```bash
npm test path/to/test.test.ts
# Confirm FAIL
```

## Green Phase Strategy

**Goal:** Write the minimal code necessary to make the test pass.

**Requirements:**
- Do not add features not tested.
- Do not refactor other code yet.
- "YAGNI" - You Ain't Gonna Need It.

**Key Action:**
```bash
npm test path/to/test.test.ts
# Confirm PASS
```

## Refactor Phase Strategy

**Goal:** Clean up the code without changing behavior.

**Checklist:**
- Remove duplication.
- Improve naming.
- Extract helpers.
- **CRITICAL:** Tests must remain GREEN throughout.

## Anti-Patterns & Rationalizations (STOP if you see these)

- **"I'll write tests after":** Tests written after are biased by implementation and miss edge cases.
- **"Too simple to test":** Simple code breaks. If it's simple, the test takes 30 seconds.
- **"Already manually tested":** Manual testing is ad-hoc and unrepeatable. Automated tests are assets.
- **"Deleting code is wasteful":** Keeping unverified code is technical debt. Delete it and start over with BDD.
- **"Tests pass immediately":** You learnt nothing. You don't know if the test is capable of failing.

## Agent Team Compatibility

This skill is designed to be run by an **Implementer** teammate within an Agent Team (or by the Team Lead). 
Load the `superpowers:agent-team-driven-development` skill for orchestrating team execution.
