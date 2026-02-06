---
name: systematic-debugging
description: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes
argument-hint: (no arguments - provides reference guidance)
user-invocable: false
version: 1.0.0
---

# Systematic Debugging

This skill provides guidance on debugging by proving root cause first, then applying the smallest correct fix.

## Core Concept

Fixes should never be proposed before root-cause evidence is gathered and analyzed. Guessing at fixes wastes time and creates regressions.

## Workflow

**Evidence Collection**: Gather error messages, stack traces, logs, and environment details. See `references/evidence-collection.md`.

**Reproduction**: Establish reliable reproduction with minimal failing condition. See `references/reproduction-techniques.md` and `references/isolation-strategies.md`.

**Fix Design**: Apply minimal correct fix targeting root cause. Verify with fresh execution evidence. See `references/fix-design-principles.md` and `references/regression-verification.md`.

## Critical Discipline

Time pressure increases guessing risk. Systematic debugging saves time by avoiding failed attempts and regressions. See `references/debugging-anti-patterns.md` for common pitfalls.

## References

- `references/evidence-collection.md` - Evidence gathering templates and techniques
- `references/reproduction-techniques.md` - Reliable reproduction strategies
- `references/isolation-strategies.md` - Minimal failing condition isolation
- `references/fix-design-principles.md` - Designing minimal correct fixes
- `references/regression-verification.md` - Regression checking strategies
- `references/debugging-anti-patterns.md` - Common pitfalls and shortcuts to avoid
