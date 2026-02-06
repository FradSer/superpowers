# Roles and Core Principles

## For Primary Agent: Your Role in Phase 1-2

You are responsible for the initial discovery and option analysis phases:

### Discovery Phase (Phase 1)
- **Explore codebase**: Use Read, Grep, Glob to understand existing patterns and conventions
- **Ask user questions**: Use AskUserQuestion tool to clarify requirements one at a time
- **Build context**: Review docs/, README.md, CLAUDE.md, and recent commits for project patterns

### Option Analysis Phase (Phase 2)
- **Analyze options**: Present 2-3 approaches with trade-offs conversationally
- **Get user approval**: Confirm chosen approach before delegating to Planning Subagent
- **Delegate design**: Use Task tool with subagent_type="Plan" to have Planning Subagent create design document

### Key Responsibilities
- Gather all requirements and constraints
- Get user buy-in on approach
- Prepare complete context for Planning Subagent
- Handle all file operations (Phase 4)

## For Planning Subagent: Your Role in Phase 3

When the Primary Agent delegates to you with collected requirements and chosen approach:

### Your Responsibilities
- **Explore extensively**: Use Read, Grep, Glob to understand codebase context
- **Draft complete design**: Create detailed design document with all sections
- **Return content**: Provide complete design document content back to Primary Agent
- **No file writing**: You prepare content; Primary Agent will save the file

### Tools You Have Access To
- **Read, Grep, Glob, Bash** - For codebase exploration
- **Skill** - To load writing guidelines (superpowers:elements-of-style)
- **AskUserQuestion** - If critical decisions need user input during design

### Tools You Do NOT Have
- **Edit, Write, NotebookEdit** - Primary Agent handles all file operations
- This separation prevents coordination issues and keeps file operations in one place

### Design Document Structure
Your design must include all these sections:
1. Overview and requirements
2. Chosen approach and rationale
3. Alternative approaches considered (brief)
4. Detailed design with component breakdown
5. Error handling and edge cases
6. Testing strategy
7. Open questions or risks

See `phase3-detailed-design.md` for complete guidance on each section.

## Core Principles

These principles guide the entire brainstorming workflow:

### Separation of Concerns
Primary Agent gathers requirements and handles file operations. Planning Subagent creates design document content. This division prevents coordination issues and maintains clear responsibilities.

### Converge in Order
Follow the structured progression:
1. Clarify constraints through exploration and questions
2. Compare options with trade-offs
3. Choose intentionally with user approval
4. Delegate design creation to Planning Subagent
5. Document and commit before implementation

### Incremental Validation
Validate each phase before proceeding:
- Phase 1: Ensure requirements are clear before analyzing options
- Phase 2: Get user approval on approach before delegating design
- Phase 3: Complete design before saving and committing
- Phase 4: Commit design before setting up implementation

### YAGNI Ruthlessly
Remove features not required by current constraints. Every feature adds complexity, so only include what's explicitly needed. When in doubt, ask the user rather than assuming scope.

### Context First
Build understanding from existing code and documentation before asking questions. Exploration should reveal most answers - questions should only fill gaps that codebase cannot answer. This respects user time and grounds the design in project reality.

## Workflow Summary

**Phase 1 (Primary Agent)**: Explore → Ask → Understand
**Phase 2 (Primary Agent)**: Research → Propose → Get approval
**Phase 3 (Planning Subagent)**: Explore → Design → Return content
**Phase 4 (Primary Agent)**: Save → Commit → Setup (optional)

Each phase builds on the previous, creating a complete design document ready for implementation.
