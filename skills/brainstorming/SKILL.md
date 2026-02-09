---
name: brainstorming
description: |
  A structured workflow to turn ideas into implementation-ready designs.
  Phases:
  1. Discovery: Explore codebase and clarify requirements.
  2. Option Analysis: Evaluate approaches and get user approval.
  3. Design & Commit: Create design document and commit to git.
  MANDATORY: Use this skill before creating features or modifying complex behavior.
user-invocable: true
---

# Brainstorming Ideas Into Designs

Turn rough ideas into implementation-ready designs through structured collaborative dialogue.

## Core Principles

1. **Converge in Order**: Clarify → Compare → Choose → Design → Commit
2. **Context First**: Explore codebase before asking questions
3. **Incremental Validation**: Validate each phase before proceeding to the next
4. **YAGNI Ruthlessly**: Only include what's explicitly needed
5. **Test-First Mindset**: Always include BDD specifications (Given-When-Then)

See `./references/core-principles.md` for detailed explanations.

## Workflow Overview

**Phase 1**: Explore → Ask → Understand
**Phase 2**: Research → Propose → Get approval
**Phase 3**: Design with BDD → Save → Commit

## Phase 1: Discovery

**Goal**: Understand what you're building by exploring current state and clarifying requirements.

**Actions**:
1. **Explore codebase first** - Use Read/Grep/Glob to find relevant files and patterns
2. **Review project context** - Check docs/, README.md, CLAUDE.md, recent commits
3. **Identify gaps** - Determine what's unclear from codebase alone
4. **Ask focused questions** - Use AskUserQuestion tool with exactly 1 question per call
   - **Prefer multiple choice** with 2-4 options (A, B, C) to reduce user cognitive load
   - Ask one at a time, never bundle questions
   - Base questions on exploration gaps

**Output**:
- Clear requirements and constraints
- Success criteria defined
- Relevant existing patterns identified

See `./references/phase1-discovery.md` for exploration patterns and question guidelines.

## Phase 2: Option Analysis

**Goal**: Evaluate different approaches and get user buy-in on the chosen direction.

**Actions**:
1. **Research existing patterns** - Search for similar implementations in codebase
2. **Identify viable approaches** - Propose 2-3 options grounded in codebase reality
   - OK to say "No Alternatives" if the path is obvious/constrained, but must explain why
3. **Present conversationally** - Write naturally as if explaining to a colleague (**Do NOT use formal tables**)
   - Lead with recommended option
   - Explain trade-offs (complexity, maintainability, performance)
   - Reference specific files from codebase
4. **Get user approval** - Use AskUserQuestion with exactly 1 question per call
   - Ask one at a time, never bundle questions
   - Continue asking single questions until the approach is fully clear and agreed upon

**Output**:
- User-approved approach with rationale
- Alternatives considered (brief summary)
- Trade-offs and constraints understood

See `./references/phase2-option-analysis.md` for option comparison and presentation patterns.

## Phase 3: Design & Commit

**Goal**: Create comprehensive design document and commit to git.

**Actions**:
1. **Create design document**:
   - Use `_index.md` as the main filename
   - Include: Context, Requirements, Rationale, Detailed Design
   - **MANDATORY**: Include BDD specifications in a separate `bdd-specs.md` file

2. **Write BDD Specifications** (in `bdd-specs.md`):
   - At least 3 scenarios in Given-When-Then format (Gherkin syntax)
   - Cover happy path, edge cases, and error conditions
   - Reference specific API endpoints or methods

   **Example Gherkin**:
   ```gherkin
   Feature: User Login
     Scenario: Successful login
       Given a user with email "user@example.com"
       When the user submits valid credentials
       Then they should be redirected to the dashboard
   ```

3. **Save to folder structure**:
   - `docs/plans/YYYY-MM-DD-<topic>-design/{_index.md, bdd-specs.md, architecture.md}`

4. **Commit to git**:
   ```bash
   git add docs/plans/YYYY-MM-DD-<topic>-design/
   git commit -m "docs: add design for <topic>

   <User's original request or context>

   - <Specific action taken>
   - <Specific action taken>

   <Brief summary of the design approach>
   
   Co-Authored-By: <Model Name> <noreply@anthropic.com>"
   ```

**Output**:
- Design folder created and committed
- **Ready for `writing-plans`**: `bdd-specs.md` is now the contract for task planning
- **Ready for `behavior-driven-development`**: Specs are compatible with BDD skill execution
- Ready for implementation

See `./references/phase3-design-commit.md` for design structure, BDD format, file operations, and git commit patterns.

See `./references/exit-criteria.md` for complete checklists and success indicators.

## References

Detailed guidance for each phase:

- `./references/core-principles.md` - Core principles guiding the workflow
- `./references/phase1-discovery.md` - Exploration patterns and question guidelines
- `./references/phase2-option-analysis.md` - Option comparison and presentation patterns
- `./references/phase3-design-commit.md` - Design structure, BDD format, file operations, git commit
- `./references/exit-criteria.md` - Complete checklists and success indicators
