# Detailed Workflow: Subagent-Driven Development (Part 1/2)

## Complete Process Flow

### Initial Setup

**Read plan, extract all tasks with full text, note context, create TodoWrite**

Read the plan file once, extract ALL tasks with their complete text and surrounding context. Create TodoWrite with all tasks upfront so you have the complete picture.

### Per-Task Loop

For each task in the plan:

#### Step 1: Dispatch Implementer Subagent

Use `./implementer-prompt.md` template. Provide:
- Full task text (already extracted)
- Context about where this task fits
- Any dependencies or prerequisites
- Expected output format

**Key principle:** Controller provides full text - subagent doesn't read plan file.

#### Step 2: Implementer Asks Questions?

**If YES:**
- Answer questions clearly and completely
- Provide additional context if needed
- Don't rush them into implementation
- Re-dispatch with answers

**If NO:**
- Proceed to implementation

#### Step 3: Implementer Implements

Subagent:
- Implements feature following TDD
- Adds tests (all passing)
- Self-reviews their work
- Commits changes

**Controller monitors but doesn't interfere.**

#### Step 4: Dispatch Spec Compliance Reviewer

Use `./spec-reviewer-prompt.md` template. Get git SHAs and provide:
- What was implemented
- Original task requirements
- BASE_SHA (before task)
- HEAD_SHA (after task)

**Reviewer checks:**
- All requirements met?
- Nothing extra added?
- Spec compliance only (not code quality yet)

#### Step 5: Spec Reviewer Response

**If ✅ Spec Compliant:**
- Proceed to Step 6

**If ❌ Issues Found:**
- List specific gaps or extras
- Implementer (same subagent) fixes issues
- Re-dispatch spec reviewer
- Repeat until ✅

**Critical:** Don't move to code quality review until spec compliance is ✅

#### Step 6: Dispatch Code Quality Reviewer

Use `./code-quality-reviewer-prompt.md` template. Provide same git SHAs.

**Reviewer checks:**
- Code quality and best practices
- Test coverage and quality
- Architecture and design
- Performance considerations

#### Step 7: Code Quality Reviewer Response

**If ✅ Approved:**
- Mark task complete in TodoWrite
- Move to next task
