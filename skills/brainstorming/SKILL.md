---
name: brainstorming
description: "You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation."
argument-hint: (no arguments - provides process guidance)
user-invocable: true
version: 1.0.0
---

# Brainstorming Ideas Into Designs

Turn rough intent into an implementation-ready design through structured dialogue. Uses RFC 2119 terms: REQUIRED → MUST, RECOMMENDED → SHOULD, OPTIONAL → MAY.

## Core Principles

- **Converge in Order**: MUST clarify constraints -> compare options -> choose intentionally -> document.
- **Incremental Validation**: SHOULD present design in small sections (200-300 words) and validate each.
- **YAGNI**: MUST ruthlessly remove features not required by current constraints.
- **Context First**: MUST build context from existing code/docs before asking questions.

## Process Phases

**Phase 1: Discovery**
- **Goal**: Remove ambiguity and identify constraints.
- **Action**: Use `AskUserQuestion` tool to ask one focused question at a time.
- **Reference**: See `references/discovery-questions.md` for question patterns.

**Phase 2: Option Analysis**
- **Goal**: Evaluate architectural approaches.
- **Action**: Propose 2-3 viable options with explicit trade-offs.
- **Reference**: Use structure in `references/option-analysis.md`.

**Phase 3: Design & Documentation**
- **Goal**: Create actionable design artifact.
- **Action**: Draft design incrementally, define failure modes, and save to strict path.
- **Output**: `docs/plans/YYYY-MM-DD-<topic>-design.md`.

## Interaction Guidelines

| Type | Guideline |
|------|-----------|
| **Questions** | One per message. Use `AskUserQuestion` tool to prompt user. |
| **Validation** | Check alignment after each 200-300 word design section. |
| **Refinement** | Be flexible; return to Discovery if options don't fit constraints. |
| **Transition** | Use `AskUserQuestion` tool to ask "Ready to set up for implementation?" before ending. |

## Exit Criteria

- [ ] Design document created at `docs/plans/YYYY-MM-DD-<topic>-design.md`
- [ ] Requirements and constraints explicitly listed
- [ ] At least 2 options compared with trade-offs (or clear "No Alternatives" rationale)
- [ ] Failure modes and testing strategies defined
- [ ] User approval received for the final design

## References

- `references/discovery-questions.md` - Question bank for requirements gathering
- `references/option-analysis.md` - Template for comparing architectural options
- **Load `superpowers:elements-of-style` skill** using the Skill tool for writing guidelines.
