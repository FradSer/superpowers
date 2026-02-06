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

## Skill Selection

**Intent Matching**: Match by intent patterns, not keywords. Load before asking questions or exploring.

**Priority**: Process skills before implementation skills.

**Red Flags**: "Just a simple question", "Need context first", "Let me explore first", "Doesn't need formal skill", "I remember this". See `references/skill-selection-heuristics.md`.

**Common Patterns**: Features → brainstorming. Implementation → behavior-driven-development. Bugs → systematic-debugging. Plans → writing-plans or executing-plans. Reviews → requesting/receiving-code-review.

## Flow

Parse intent → Identify matches → Load skills → Announce → Execute. See `references/invocation-flow-and-red-flags.md`.

## References

- `references/skill-selection-heuristics.md` - Comprehensive skill matching patterns
- `references/invocation-flow-and-red-flags.md` - Flow patterns and rationalization red flags
