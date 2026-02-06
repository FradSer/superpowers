# Phase 4: Save & Setup - Detailed Guidance

## Goal
Save design document and optionally set up for implementation.

## Primary Agent Actions

### 1. Receive Design Content
Planning Subagent returns complete design document content in their response. You now have the full text ready to save.

### 2. Save Design Document
Save to standardized location with date prefix:

**File Location Pattern**: `docs/plans/YYYY-MM-DD-<topic>-design/_index.md`

**Examples**:
- `docs/plans/2025-01-15-user-authentication-design/_index.md`
- `docs/plans/2025-01-15-payment-processing-design/_index.md`
- `docs/plans/2025-01-15-api-rate-limiting-design/_index.md`

**Directory Creation**: Ensure both `docs/plans/` and `docs/plans/YYYY-MM-DD-<topic>-design/` exist.

### 3. Commit Design
Use `Bash` to commit the design document to git:

**Git Workflow**:
```bash
git add docs/plans/YYYY-MM-DD-<topic>-design/
git commit -m "docs: add design for <topic>

Co-Authored-By: <Model Name> <noreply@anthropic.com>"
```

**Example**:
```bash
git add docs/plans/2025-01-15-user-authentication-design/
git commit -m "docs: add design for user authentication

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

**Commit Message Guidelines**:
- Use `docs:` prefix for documentation
- Keep subject line under 50 characters and lowercase
- Brief description of what was designed
- Always include Co-Authored-By line with model name

### 4. Ask About Next Steps
Use `AskUserQuestion` to check if user wants to proceed:

**Question Template**:
```
Design document saved to docs/plans/YYYY-MM-DD-<topic>-design/_index.md and committed to git.

Ready to set up for implementation?
```

### 5. If Yes, Proceed With Implementation Setup

#### Implementation Setup
Use `superpowers:writing-plans` skill to create detailed implementation plan:
- Breaks design into executable tasks
- Defines task dependencies and order
- Creates checklist for tracking progress

**Typical Flow**:
```
1. Load superpowers:writing-plans skill
2. Create detailed implementation plan from design document
3. Begin implementation with clear task list
```

## Output
- Design document saved at `docs/plans/YYYY-MM-DD-<topic>-design/_index.md`
- Design document committed to git with proper message
- User informed and asked about next steps
- If requested: implementation plan started

## Key Principle
**Complete the brainstorming phase before jumping into implementation.** The design document is a checkpoint - commit it before proceeding to ensure you can refer back to the original plan.
