# Task Granularity & Verification

## BDD Granularity

**1 Task = 1 BDD Scenario.**

Do not group multiple scenarios into one task unless they are trivial variations.
Do not split a single scenario across multiple tasks unless it involves distinct architectural layers that must be implemented sequentially (e.g., "Backend for Scenario X", "Frontend for Scenario X").

## Verification Strategy

**Verification is strictly tied to the BDD Scenario.**

1. **Red (Failing Test):**
   - The task must start by creating/enabling a test case that maps 1:1 to the BDD scenario.
   - It must fail with a meaningful error (e.g., `AssertionError: Expected X, got None`, not `ImportError`).

2. **Green (Passing Test):**
   - Implement the minimal code to satisfy the scenario.
   - Run the specific test case again.
   - It must pass.

3. **Refactor:**
   - Clean up code while keeping the test passing.
   - Ensure no regressions.

## Task Output

Every task in the plan must result in:
1. A committed BDD test case (in `tests/`).
2. Implementation code (in `src/`).
3. A green test run.

## Example Task Description

> **Task: Implement 'User logs in successfully' Scenario**
>
> **Spec:** `bdd-specs.md` -> Scenario: "User logs in successfully"
>
> **Steps:**
> 1. **Test**: Create `tests/features/login_test.py`.
>    - Implement test mapping to scenario steps (Given user exists, When logs in, Then success).
> 2. **Red**: Run test -> FAIL.
> 3. **Impl**: Update `auth_service.py`.
>    - Implement `login` method to validate credentials and return token.
> 4. **Green**: Run test -> PASS.

## Execution Handoff

After saving the plan, offer execution choice via Agent Teams:

**"Plan complete and saved to `docs/plans/<filename>.md`. Execution options:**

**1. Orchestrated Execution (Recommended)** - Use Skill tool load `superpowers:executing-plans` skill to manage execution (it will spawn an Agent Team for parallel work).

**2. Direct Agent Team** - Use Skill tool load `superpowers:agent-team-driven-development` skill to spawn a team immediately (Architecture/Implementation/Review).

**3. Manual / Serial** - Execute tasks one by one in this session (slower)."

