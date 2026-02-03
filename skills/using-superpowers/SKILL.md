---
name: using-superpowers
description: Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions
argument-hint: (no arguments - provides reference guidance)
user-invocable: false
version: 1.0.0
---

# Using Superpowers

This skill provides guidance on how to identify, select, and apply skills at conversation start.

## Core Concept

Skills should be loaded before taking any action when there's even a 1% chance they might apply to the task.

## Skill Selection Principles

**Intent Matching**: Skills are triggered by user intent patterns, not exact keyword matches. The description field indicates when each skill applies.

**Pre-action Loading**: Skill selection happens before:
- Asking clarifying questions
- Running exploratory commands
- Making assumptions about approach
- Responding to the user

**Skill Priority**: When multiple skills could apply, process skills are loaded before implementation skills (e.g., brainstorming before domain-specific skills).

## Selection Heuristics

**Red Flags Indicating Rationalization**:
- "This is just a simple question" - Questions are tasks; check for skills
- "I need more context first" - Skill check comes before context gathering
- "Let me explore the codebase first" - Skills tell you how to explore
- "This doesn't need a formal skill" - If a skill exists, it should be used
- "I remember this skill" - Skills evolve; load current version

**Common Intent Patterns**:
- Creating/building/adding features → brainstorming
- Implementing functionality → test-driven-development
- Bug fixes or failures → systematic-debugging
- Multi-step tasks with plans → writing-plans or executing-plans
- Code review requests → requesting-code-review
- Receiving review feedback → receiving-code-review

See `references/skill-selection-heuristics.md` for comprehensive matching patterns.

## Invocation Flow

The standard flow follows this pattern:
1. Parse user request intent
2. Identify plausible skill matches
3. Load relevant skills (using Skill tool)
4. Announce selected skill(s) briefly
5. Execute under skill constraints

See `references/invocation-flow-and-red-flags.md` for detailed flow patterns and anti-patterns.

## References

- `references/skill-selection-heuristics.md` - Comprehensive skill matching patterns
- `references/invocation-flow-and-red-flags.md` - Flow patterns and rationalization red flags
