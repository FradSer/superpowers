# Phase 1: Discovery - Detailed Guidance

## Goal

Understand what you're building by exploring the current project state and clarifying requirements.

## Primary Agent Actions

### 1. Explore Codebase First

**Before asking any questions**, build context from existing code:

- Find relevant files matching patterns (e.g., `**/*.ts`, `src/**/*.py`)
- Search for patterns and similar implementations
- Read files to understand existing code structure and conventions
- Check for architectural patterns, naming conventions, error handling styles

### 2. Review Project Context

Understand the project's established patterns:

- Check `docs/` directory for existing documentation
- Read `README.md` for project overview and setup
- Review `CLAUDE.md` for development guidelines and constraints
- Run `git log --oneline -20` to see recent commits and development focus
- Look for similar features or components already implemented

### 3. Identify Gaps

Based on your exploration, identify what's unclear:

- Which requirements are ambiguous or missing?
- What constraints are not documented in the codebase?
- What success criteria need clarification?
- What non-functional requirements (performance, security, scalability) need discussion?

### 4. Ask Focused Questions

Use `AskUserQuestion` tool strategically:

**Question Style Preferences**:

- **Prefer multiple choice** with 2-4 options when possible
- Use open-ended only when exploring truly unknown territory
- Frame questions based on what you learned from codebase exploration

**One Question Per Message**:

- Never bundle multiple questions together
- Break complex topics into sequential questions
- Wait for answer before asking the next question

**Question Categories**:

- **Purpose**: "What problem does this solve for users?"
- **Constraints**: "Are there performance/security requirements?"
- **Success Criteria**: "How will we know this works correctly?"
- **Scope**: "Should this handle [edge case] or is that out of scope?"
- **Integration**: "Should this integrate with [existing system]?"

**Example Multiple Choice Questions**:

```
I found two existing authentication patterns in the codebase:
1. JWT tokens with 24-hour expiry (used in /api/v1)
2. Session-based auth with Redis (used in /admin)

Which approach should this feature use?
A) JWT tokens (stateless, scales better)
B) Session-based (more secure, easier revocation)
C) Different approach (please describe)
```

### 5. Build Mental Model

Synthesize exploration and user answers:

- Create clear picture of requirements and constraints
- Identify which existing patterns to follow
- Understand success criteria and edge cases
- Prepare context to pass to Phase 2 option analysis

## Key Principle

**Explore extensively before asking.** Questions should fill gaps that codebase exploration cannot answer. If you can learn it from code or docs, don't ask.

## Output for Phase 2

Provide clear understanding including:

- Explicit requirements from user answers
- Constraints discovered from codebase and user
- Success criteria and non-functional requirements
- Relevant existing patterns and files to reference
