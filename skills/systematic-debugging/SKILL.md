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

## Evidence-Driven Debugging

**Evidence Collection**: The foundation of systematic debugging is comprehensive evidence gathering. This includes error messages, stack traces, logs, environment details, and reliable reproduction steps.

**Reproduction**: Reliable reproduction is essential for proving the bug exists and verifying fixes. The minimal failing condition should be isolated to understand what triggers the issue.

**Root Cause Analysis**: With reliable reproduction, the root cause can be identified through controlled experiments and hypothesis testing. The fix should directly target the verified trigger.

See `references/evidence-collection.md`, `references/reproduction-techniques.md`, and `references/isolation-strategies.md` for detailed techniques.

## Fix Design Principles

**Minimal Correct Fix**: The fix should be the smallest change that addresses the root cause. Over-engineering or defensive fixes often introduce new issues.

**Evidence-Based Verification**: Success should never be declared without fresh execution evidence. The original failure must be resolved in the actual environment.

**Regression Protection**: Adjacent behavior should be checked for regressions. High-impact areas require thorough regression verification.

See `references/fix-design-principles.md` and `references/regression-verification.md` for detailed guidance.

## When Systematic Debugging Applies

**Appropriate Contexts**:
- Any failing test, bug report, or unstable behavior
- Cases where prior quick fixes failed or caused regressions
- High time pressure situations where guessing risk increases

**Common Anti-Patterns**:
- Proposing fixes before isolation is complete
- Declaring success without fresh execution outputs
- Skipping regression checks for high-impact areas
- Multiple simultaneous changes obscuring which fixed the issue

See `references/debugging-anti-patterns.md` for comprehensive anti-pattern coverage.

## Debugging Under Pressure

Time pressure often leads to guessing and shortcut-taking. Systematic debugging is especially important when deadlines are tight, as failed guesses compound time loss.

The discipline of evidence → reproduction → isolation → fix → verification actually saves time by avoiding failed attempts and regressions.

## References

- `references/evidence-collection.md` - Evidence gathering templates and techniques
- `references/reproduction-techniques.md` - Reliable reproduction strategies
- `references/isolation-strategies.md` - Minimal failing condition isolation
- `references/fix-design-principles.md` - Designing minimal correct fixes
- `references/regression-verification.md` - Regression checking strategies
- `references/debugging-anti-patterns.md` - Common pitfalls and shortcuts to avoid
