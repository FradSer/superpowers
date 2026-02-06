# Writing Skills Details (1/2)

# Detailed Guidance

This file preserves the previously detailed SKILL.md guidance for deeper reference.

# Writing Skills

## Overview

**Writing skills IS Test-Driven Development applied to process documentation.**

**Personal skills live in agent-specific directories (`~/.claude/skills` for Claude Code, `~/.codex/skills` for Codex)**

You write test cases (pressure scenarios with subagents), watch them fail (baseline behavior), write the skill (documentation), watch tests pass (agents comply), and refactor (close loopholes).

**Core principle:** If you didn't watch an agent fail without the skill, you don't know if the skill teaches the right thing.

**REQUIRED BACKGROUND:** You MUST understand superpowers:behavior-driven-development before using this skill. That skill defines the fundamental RED-GREEN-REFACTOR cycle.

## When to Use

**Create skills when:**
- Technique wasn't intuitively obvious
- You'd reference this again across projects
- Pattern applies broadly (not project-specific)

**Don't create for:**
- One-off solutions or standard practices
- Project-specific conventions (use CLAUDE.md)
- Mechanical constraints (automate instead)

## Core Workflow

1. **RED: Run baseline** - Pressure scenario WITHOUT skill, document exact rationalizations
2. **GREEN: Write minimal skill** - Address those specific violations only
3. **Verify GREEN** - Run scenarios WITH skill, confirm compliance
4. **REFACTOR: Close loopholes** - Find new rationalizations, plug explicitly, re-test
5. **Deploy** - Commit to git

## Red Flags

**Never:**
- Write skill before running baseline test
- Skip testing because "obviously clear"
- Create multiple skills without testing each
- Keep untested changes as "reference"
- Move to next skill before current verified

**The Iron Law:** NO SKILL WITHOUT A FAILING TEST FIRST

## References
