---
name: brainstorming
description: |
  A structured 3-phase workflow to turn ideas into implementation-ready designs.
  Phases:
  1. Discovery: Explore codebase and clarify requirements.
  2. Option Analysis: Evaluate approaches and get user approval.
  3. Design & Commit: Create design document with BDD specs and commit to git.
  MANDATORY: Use this skill before creating features or modifying complex behavior.
user-invocable: true
---

# Brainstorming Ideas Into Designs

Turn rough ideas into implementation-ready designs through structured collaborative dialogue.

## Core Principles

Five principles guide the entire workflow:

1. **Converge in Order**: Clarify → Compare → Choose → Design → Commit
2. **Incremental Validation**: Validate each phase before proceeding to the next
3. **YAGNI Ruthlessly**: Only include what's explicitly needed
4. **Context First**: Explore codebase before asking questions
5. **Test-First Mindset**: Always include BDD specifications (Given-When-Then)

See `references/core-principles.md` for detailed explanations.

## Workflow Overview

**Phase 1**: Explore → Ask → Understand
**Phase 2**: Research → Propose → Get approval
**Phase 3**: Design with BDD → Save → Commit

## Phase 1: Discovery

**Goal**: Understand what you're building by exploring current state and clarifying requirements.

**Key Actions**:
1. **Explore codebase first** - Use Read/Grep/Glob to find relevant files and patterns
2. **Review project context** - Check docs/, README.md, CLAUDE.md, recent commits
3. **Identify gaps** - Determine what's unclear from codebase alone
4. **Ask focused questions** - Use AskUserQuestion tool with exactly 1 question per call
   - Prefer multiple choice over open-ended
   - Ask one at a time, never bundle questions
   - Base questions on exploration gaps

**Output**:
- Clear requirements and constraints
- Success criteria defined
- Relevant existing patterns identified
- Foundation for option analysis

See `references/phase1-discovery.md` for exploration patterns and question guidelines.

## Phase 2: Option Analysis

**Goal**: Evaluate different approaches and get user buy-in on the chosen direction.

**Key Actions**:
1. **Research existing patterns** - Search for similar implementations in codebase
2. **Identify viable approaches** - Propose 2-3 options grounded in codebase reality
   - OK to say "No Alternatives" with clear rationale
3. **Present conversationally** - Write naturally, not formal tables
   - Lead with recommended option
   - Explain trade-offs (complexity, maintainability, performance)
   - Reference specific files from codebase
4. **Get user approval** - Use AskUserQuestion with exactly 1 question to confirm

**Output**:
- User-approved approach with rationale
- Alternatives considered (brief summary)
- Trade-offs and constraints understood
- Complete context for design creation

See `references/phase2-option-analysis.md` for option comparison and presentation patterns.

## Phase 3: Design & Commit

**Goal**: Create comprehensive design documents (split into multiple files) with BDD specifications, save to folder structure, and commit to git.

**Key Actions**:
1. **Create multi-file design** with all required sections:
   - `_index.md`: Overview, requirements, rationale
   - `architecture.md`: Component breakdown, integration points
   - `data-models.md`: Data structures, schemas
   - `api-spec.md` (optional): API endpoints if applicable
   - **`bdd-specs.md`** (MANDATORY): All BDD scenarios must be in this separate file

2. **Save to folder structure**:
   - **Required path**: `docs/plans/YYYY-MM-DD-<topic>-design/` containing multiple files
   - Main document: `_index.md` (with underscore prefix) linking to other files
   - Supporting docs: `bdd-specs.md`, `architecture.md`, etc.
   - Example: `docs/plans/2025-01-15-user-authentication-design/{_index.md, bdd-specs.md, architecture.md}`

3. **Commit to git**:
   ```bash
   git add docs/plans/YYYY-MM-DD-<topic>-design/
   git commit -m "docs: add design for <topic>

   Includes BDD specifications for test-first development.

   Co-Authored-By: <Model Name> <noreply@anthropic.com>"
   ```

**BDD Specifications** (MANDATORY in `bdd-specs.md`):
- At least 3 scenarios in Given-When-Then format
- Cover happy path, edge cases, and error conditions
- Reference specific API endpoints or methods
- Provide clear acceptance criteria

**Output**:
- Design folder created at `docs/plans/YYYY-MM-DD-<topic>-design/`
- Multiple design files (`_index.md`, `bdd-specs.md`, etc.) created
- Main document `_index.md` links to supporting files
- Committed to git with proper message
- Ready for implementation

See `references/phase3-design-commit.md` for design structure, BDD format, file operations, and git commit patterns.

## Exit Criteria

Each phase has a checklist to ensure completeness before proceeding:

**After Phase 1**:
- Explored codebase thoroughly
- Requirements explicitly clarified
- Mental model built
- Ready for option analysis

**After Phase 2**:
- At least 2 options compared (or clear "No Alternatives" rationale)
- User approval received
- Respected existing architecture
- Ready to create design document

**After Phase 3**:
- All design sections complete (including MANDATORY BDD specifications)
- Design grounded in existing codebase
- Saved to correct folder structure (`_index.md` + supporting files)
- Committed to git with proper message
- User informed and ready for implementation
- **Next Step**: Use Skill tool load `superpowers:writing-plans` skill to convert this design into a detailed implementation plan.

See `references/exit-criteria.md` for complete checklists and success indicators.

## References

Detailed guidance for each phase:

- `references/core-principles.md` - Core principles guiding the workflow
- `references/phase1-discovery.md` - Exploration patterns and question guidelines
- `references/phase2-option-analysis.md` - Option comparison and presentation patterns
- `references/phase3-design-commit.md` - Design structure, BDD format, file operations, git commit
- `references/exit-criteria.md` - Complete checklists and success indicators
