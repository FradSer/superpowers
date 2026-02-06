# Phase 3: Detailed Design - Detailed Guidance

## Goal

Create complete design document with all technical details through Planning Subagent.

## Primary Agent: Delegation Instructions

### Prepare Delegation Context

Summarize all information gathered in Phases 1-2:

**Requirements Package**:

- User requirements and constraints from Phase 1
- Success criteria and non-functional requirements
- Chosen approach and rationale from Phase 2
- Alternative approaches considered with trade-offs
- Relevant files and patterns discovered during exploration

### Delegate to Planning Subagent

Launch the `Plan` agent and provide complete context:

**Delegation Message Template**:

```
Create detailed design document for [topic].

Requirements:
- [Requirement 1 from Phase 1]
- [Requirement 2 from Phase 1]
- [Constraints from Phase 1]

Chosen approach: [Approach from Phase 2 with rationale]

Alternatives considered:
- [Alternative 1 with trade-offs]
- [Alternative 2 with trade-offs]

Relevant files:
- [File 1: brief description of relevance]
- [File 2: brief description of relevance]

Use `superpowers:elements-of-style` skill for writing guidelines.
Explore the codebase to ground the design in existing patterns.

Create complete design document content following this structure:
- Overview and requirements
- Chosen approach and rationale
- Alternative approaches considered (brief)
- Detailed design with component breakdown
- Error handling and edge cases
- Testing strategy
- Open questions or risks

Return the complete design document content.
```

## Planning Subagent: Design Creation Instructions

When Primary Agent delegates to you with requirements package:

### 1. Load Writing Guidelines

Use `Skill` tool to load `superpowers:elements-of-style` for document quality standards.

### 2. Explore Codebase

Build deep understanding of implementation context:

- Use `Read` to examine relevant files mentioned in delegation
- Use `Grep` to find similar patterns and implementations
- Use `Glob` to discover related components
- Use `Bash` for git history or project structure exploration

### 3. Draft Complete Design

Create comprehensive design document with all required sections:

**Required Structure**:

#### Overview and Requirements

- Brief summary of what's being built
- Core requirements from Phase 1
- Success criteria and constraints

#### Chosen Approach and Rationale

- Detailed description of chosen approach
- Why this approach fits the requirements
- How it aligns with existing codebase patterns
- Reference specific files and patterns

#### Alternative Approaches Considered

- Brief summary of alternatives from Phase 2
- Key trade-offs that led to rejection
- Don't need full details (Primary Agent already discussed)

#### Detailed Design

- Component breakdown with responsibilities
- Data structures and interfaces
- Integration points with existing code
- Sequence diagrams or flow descriptions (text-based)
- File structure and organization

#### Error Handling and Edge Cases

- Expected error scenarios and handling strategy
- Edge cases identified and mitigation
- Recovery and rollback strategies

#### Testing Strategy

- Unit test approach and key test cases
- Integration test requirements
- Manual testing checklist if needed

#### Open Questions or Risks

- Unresolved technical decisions
- Known risks and mitigation plans
- Dependencies on external systems

### 4. Ground in Reality

Throughout the design:

- Reference specific files: "Similar to the pattern in `src/users/service.ts`"
- Cite existing patterns: "Following the repository pattern used in data access layer"
- Show concrete examples: "The API endpoint will look like: `POST /api/v1/...`"

### 5. Return to Primary Agent

Provide complete design document content in your response. Primary Agent will save it to file.

## Tools Available to Planning Subagent

- `Read`, `Grep`, `Glob`, `Bash` - for exploration
- `Skill` - to load writing guidelines
- `AskUserQuestion` - if critical decisions need user input

## Tools NOT Available to Planning Subagent

- `Edit`, `Write`, `NotebookEdit` - Primary Agent handles all file operations

## Key Principle

**Planning Subagent prepares content; Primary Agent writes files.** This separation keeps file operations in one place and prevents coordination issues.
