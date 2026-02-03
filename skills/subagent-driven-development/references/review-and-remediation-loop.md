# Detailed Workflow: Subagent-Driven Development (Part 2/2)

**If ❌ Issues Found:**
- List specific quality issues
- Implementer fixes issues
- Re-dispatch code quality reviewer
- Repeat until ✅

#### Step 8: Mark Task Complete

Update TodoWrite, proceed to next task.

### After All Tasks

#### Final Review

Dispatch final code reviewer subagent for entire implementation:
- Review all changes together
- Verify cohesion across tasks
- Confirm all requirements met

#### Complete Development

**REQUIRED SUB-SKILL:** Use superpowers:finishing-a-development-branch
- Verify tests
- Present completion options
- Execute chosen workflow

## Why Two-Stage Review?

**Spec compliance first:**
- Prevents over/under-building
- Catches scope creep early
- Ensures requirements met

**Code quality second:**
- Ensures implementation is well-built
- Maintains code standards
- Prevents technical debt

**Order matters:** Don't waste time reviewing code quality if spec isn't met yet.

## Controller Responsibilities

**Extract all tasks upfront:**
- Read plan file once
- Get full text for every task
- Note context and dependencies
- Create complete TodoWrite

**Provide complete context:**
- Full task text (don't make subagent read plan)
- Scene-setting context (where this fits)
- Dependencies and prerequisites
- Answer questions before work begins

**Manage review loops:**
- Spec compliance → fixes → re-review → approved
- Code quality → fixes → re-review → approved
- Don't skip re-reviews
- Don't accept "close enough"

**Track progress:**
- TodoWrite per task
- Mark in_progress when dispatching
- Mark completed when both reviews ✅
