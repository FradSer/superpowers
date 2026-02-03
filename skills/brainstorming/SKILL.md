---
name: brainstorming
description: "You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation."
argument-hint: (no arguments - provides process guidance)
user-invocable: true
version: 1.0.0
---

# Brainstorming Ideas Into Designs

Turn rough ideas into implementation-ready designs through structured collaborative dialogue.

## Core Principles

- **Converge in order**: Clarify constraints → compare options → choose intentionally → document
- **Incremental validation**: Present design in small sections (200-300 words) and validate each
- **YAGNI ruthlessly**: Remove features not required by current constraints
- **Context first**: Build context from existing code/docs before asking questions

## Process Phases

**Phase 1: Discovery**

Understand what you're building by exploring the current project state and clarifying requirements.

- Check out the current project state first (files, docs, recent commits)
- Use `AskUserQuestion` tool to ask one focused question at a time
- Prefer multiple choice questions when possible
- Only one question per message - break complex topics into multiple questions
- Focus on: purpose, constraints, success criteria
- See `references/discovery-questions.md` for question patterns

**Phase 2: Option Analysis**

Evaluate different architectural approaches before committing to one.

- Propose 2-3 viable approaches with explicit trade-offs
- Present options conversationally with your recommendation and reasoning
- Lead with your recommended option and explain why
- Use structure in `references/option-analysis.md`

**Phase 3: Design & Documentation**

Create the actionable design artifact through incremental validation.

- Present design in sections of 200-300 words
- Ask after each section whether it looks right so far
- Cover: architecture, components, data flow, error handling, testing
- Be ready to go back and clarify if something doesn't make sense
- Write validated design to `docs/plans/YYYY-MM-DD-<topic>-design.md`
- **Load `superpowers:elements-of-style` skill** using the Skill tool for writing guidelines
- Commit the design document to git

**Phase 4: Transition to Implementation**

Set up for implementation if continuing.

- Use `AskUserQuestion` tool to ask: "Ready to set up for implementation?"
- Use superpowers:using-git-worktrees to create isolated workspace
- Use superpowers:writing-plans to create detailed implementation plan

## Exit Criteria

- [ ] Design document created at `docs/plans/YYYY-MM-DD-<topic>-design.md`
- [ ] Requirements and constraints explicitly listed
- [ ] At least 2 options compared with trade-offs (or clear "No Alternatives" rationale)
- [ ] Failure modes and testing strategies defined
- [ ] User approval received for the final design

## References

- `references/discovery-questions.md` - Question bank for requirements gathering
- `references/option-analysis.md` - Template for comparing architectural options
