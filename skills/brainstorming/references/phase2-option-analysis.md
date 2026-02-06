# Phase 2: Option Analysis - Detailed Guidance

## Goal

Evaluate different architectural approaches and get user buy-in on the chosen approach.

## Primary Agent Actions

### 1. Research Existing Patterns

Ground your options in codebase reality:

- Search for similar implementations in the codebase
- Look for established architectural patterns (MVC, layered, microservices, etc.)
- Identify libraries and frameworks already in use
- Check for coding conventions and style patterns

### 2. Identify Viable Approaches

Based on codebase exploration, propose 2-3 approaches:

**When to propose alternatives**:

- When there are genuinely different architectural choices
- When trade-offs exist between competing goals (speed vs. maintainability)
- When existing patterns suggest multiple valid paths

**When "No Alternatives" is acceptable**:

- When codebase has one clear established pattern
- When requirements strongly constrain to single approach
- When alternatives would violate project constraints
- **Must explicitly state rationale**: "No alternatives considered because [reason]"

### 3. Present Conversationally

**Don't use formal tables.** Write naturally as if explaining to a colleague:

**Structure**:

1. Lead with your recommended option
2. Explain why it fits best given the requirements and codebase
3. Describe alternative approaches with trade-offs
4. Reference specific files/patterns from the codebase

**Example Presentation**:

```
I recommend using the existing event-driven pattern (like we use in src/notifications/)
because it keeps the payment processing decoupled from order management. This means:
- Payment failures won't block order creation
- Easy to add payment providers later
- Consistent with how we handle other async operations

Alternative approach would be synchronous payment processing (direct API calls in the
order controller). This is simpler to understand but creates tight coupling - if the
payment service is down, orders can't be created at all. This is how the legacy
/checkout endpoint works, and we've had reliability issues with it.

Another option is using a job queue (Sidekiq/Celery), which gives us retry logic out
of the box. But we don't currently use background jobs anywhere, so this adds a new
infrastructure dependency just for this feature.
```

### 4. Respect Existing Architecture

Your proposals should:

- Align with established patterns found during exploration
- Use existing libraries and frameworks when possible
- Follow the project's architectural style (monolith, microservices, etc.)
- Reference specific files to show grounding in reality

**Example**: "This follows the same layered approach we use in `src/users/` where
controllers call service classes that handle business logic."

### 5. Get User Approval

Use `AskUserQuestion` to confirm the chosen approach:

**Simple approval**:

```
Does the event-driven approach sound good, or would you prefer one of the alternatives?
```

**Clarifying trade-offs**:

```
The event-driven approach is more complex to debug but more reliable. The synchronous
approach is simpler but less robust. Which trade-off matters more for this feature?
```

## Key Principle

**Options should be grounded in codebase reality, not abstract possibilities.** Don't propose approaches that would require major architectural changes unless the requirements demand it.

## Output for Phase 3

Provide Planning Subagent with:

- User-approved approach with clear rationale
- Alternative approaches considered (brief summary)
- Relevant files and patterns to reference in design
- Trade-offs and constraints to keep in mind
