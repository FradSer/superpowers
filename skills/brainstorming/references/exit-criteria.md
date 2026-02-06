# Exit Criteria - Complete Checklists

## After Phase 1: Discovery (Primary Agent)
Before proceeding to Phase 2, verify:

- [ ] **Explored codebase thoroughly**
  - Checked relevant files with Read/Glob/Grep
  - Reviewed existing patterns and conventions
  - Examined similar implementations
  - Checked docs/, README.md, CLAUDE.md for context
  - Reviewed recent git commits for development focus

- [ ] **Requirements explicitly clarified**
  - Used AskUserQuestion to fill gaps codebase couldn't answer
  - Asked questions one at a time (not bundled)
  - Preferred multiple choice questions when possible
  - Clarified purpose, constraints, and success criteria

- [ ] **Mental model built**
  - Clear understanding of what's being built
  - Known constraints and non-functional requirements
  - Success criteria defined
  - Relevant existing patterns identified

- [ ] **Ready for option analysis**
  - Have enough context to propose viable approaches
  - Know which existing patterns to follow or adapt
  - Understand trade-offs that matter for this project

## After Phase 2: Option Analysis (Primary Agent)
Before delegating to Planning Subagent, verify:

- [ ] **At least 2 options compared with trade-offs**
  - OR clear "No Alternatives" rationale provided
  - Options grounded in codebase reality, not abstract possibilities
  - Trade-offs explained (complexity, maintainability, performance, etc.)
  - Referenced specific files/patterns from codebase

- [ ] **User approval received**
  - Presented options conversationally (not formal tables)
  - Led with recommended option and reasoning
  - Used AskUserQuestion to confirm chosen approach
  - User explicitly approved the direction

- [ ] **Respected existing architecture**
  - Proposals align with established patterns
  - Use existing libraries and frameworks when possible
  - Follow project's architectural style

- [ ] **All context ready to delegate**
  - Requirements summary from Phase 1
  - Chosen approach with rationale
  - Alternatives considered with trade-offs
  - Relevant files and patterns to reference

## After Phase 3: Detailed Design (Planning Subagent)
Before returning to Primary Agent, verify design document content includes:

- [ ] **Overview and requirements section**
  - Brief summary of what's being built
  - Core requirements and constraints
  - Success criteria

- [ ] **Chosen approach and rationale section**
  - Detailed description of chosen approach
  - Explanation of why it fits the requirements
  - References to existing codebase patterns

- [ ] **Alternative approaches section**
  - Brief summary of alternatives considered
  - Key trade-offs that led to rejection

- [ ] **Detailed design section**
  - Component breakdown with responsibilities
  - Data structures and interfaces
  - Integration points with existing code
  - File structure and organization

- [ ] **Error handling and edge cases section**
  - Expected error scenarios and handling strategy
  - Edge cases identified and mitigation
  - Recovery and rollback strategies

- [ ] **Testing strategy section**
  - Unit test approach and key test cases
  - Integration test requirements
  - Manual testing checklist if needed

- [ ] **Open questions or risks section**
  - Unresolved technical decisions
  - Known risks and mitigation plans
  - Dependencies on external systems

- [ ] **Design grounded in existing codebase**
  - References specific files and patterns throughout
  - Shows concrete examples and interfaces
  - Aligns with project's architectural style

- [ ] **Content returned to Primary Agent**
  - Complete document content in response
  - No files written (Primary Agent handles that)

## After Phase 4: Save & Setup (Primary Agent)
Before marking brainstorming complete, verify:

- [ ] **Design document written**
  - Saved to `docs/plans/YYYY-MM-DD-<topic>-design/_index.md`
  - Created `docs/plans/YYYY-MM-DD-<topic>-design/` directory if needed
  - Used correct date format (YYYY-MM-DD)

- [ ] **Design document committed**
  - Used `git add` and `git commit` with proper message
  - Commit message starts with `docs:` prefix
  - Subject line under 50 characters and lowercase
  - Included Co-Authored-By line with model name

- [ ] **User asked about next steps**
  - Used AskUserQuestion to ask: "Design document saved. Ready to set up for implementation?"
  - Confirmed file location in the question

- [ ] **If requested: implementation setup started**
  - Used superpowers:using-git-worktrees to create isolated workspace
  - Used superpowers:writing-plans to create implementation plan
  - Ready to begin implementation with clear task list

## Success Indicators

**High Quality Brainstorming Session**:
- Explored codebase before asking questions
- Asked focused questions based on exploration gaps
- Proposed options grounded in existing patterns
- Got user buy-in before creating detailed design
- Design document is comprehensive and actionable
- Committed design as checkpoint before implementation

**Common Pitfalls to Avoid**:
- Asking questions without exploring codebase first
- Proposing abstract options not grounded in reality
- Creating design without user approval of approach
- Skipping alternatives without clear rationale
- Design document missing key sections
- Jumping to implementation without committing design
