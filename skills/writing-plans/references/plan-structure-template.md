# Writing Plans Details (1/2)

# Detailed Guidance

This file preserves the previously detailed SKILL.md guidance for deeper reference.

# Writing Plans

## Overview

Write comprehensive implementation plans assuming the engineer has zero context for our codebase and questionable taste. Document everything they need to know: which files to touch for each task, code, testing, docs they might need to check, how to test it. Give them the whole plan as bite-sized tasks. DRY. YAGNI. BDD. Frequent commits.
For unit-test tasks, explicitly require test doubles to isolate external dependencies (databases, networks, third-party services).

Assume they are a skilled developer, but know almost nothing about our toolset or problem domain. Assume they don't know good test design very well.

**Announce at start:** "I'm using the writing-plans skill to create the implementation plan."

**Context:** This should be run in a dedicated worktree (created by brainstorming skill).

**Save plans to:** `docs/plans/YYYY-MM-DD-<feature-name>.md`

## Bite-Sized Task Granularity

**Each task corresponds to implementing one BDD Scenario:**
- Step 1: Ensure Scenario exists in `bdd-specs.md`
- Step 2: Implement the Test Case (translating Given/When/Then to code)
- Step 3: Run Test (`RED`)
- Step 4: Implement Logic (`GREEN`)
- Step 5: Verify (Run tests) & Refactor

## Plan Document Header

**Every plan MUST start with this header:**

```markdown
# [Feature Name] Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use Skill tool load `superpowers:executing-plans` skill to implement this plan task-by-task.

**Goal:** [One sentence describing what this builds]

**Architecture:** [2-3 sentences about approach]

**Tech Stack:** [Key technologies/libraries]

---
```

## Task Structure

```markdown
### Task N: [Scenario Name]

**Files:**
- Create: `exact/path/to/file.py`
- Modify: `exact/path/to/existing.py:123-145`
- Test: `tests/exact/path/to/test.py`
- Spec: `docs/plans/.../bdd-specs.md` (Scenario: [Scenario Name])

**Step 1: Verify Scenario**
- Ensure `[Scenario Name]` exists in `bdd-specs.md`.

**Step 2: Implement Test Case**

- File: `tests/exact/path/to/test.py`
- Action: Create/Update test function `test_scenario_name`
- Logic:
  - **Given**: Initialize [State/Context]
  - **When**: Trigger [Action]
  - **Then**: Assert [Expected Result]

**Step 3: Run test (Red)**

Run: `pytest tests/path/test.py::test_scenario_name -v`
Expected: FAIL

**Step 4: Implement Logic (Green)**

- File: `exact/path/to/file.py`
- Action: Implement method/function to satisfy the test
- Details: [Brief description of logic if needed]

**Step 5: Verify & Refactor**

Run: `pytest tests/path/test.py::test_scenario_name -v`
Expected: PASS
```
