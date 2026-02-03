---
name: test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code
argument-hint: (no arguments - provides reference guidance)
user-invocable: false
version: 1.0.0
---

# Test-Driven Development

This skill provides guidance on implementing behavior through strict red-green-refactor cycles.

## Core Concept

No production code should be written before a failing test proves the behavior gap exists.

## The Red-Green-Refactor Cycle

**Red Phase**: Writing a focused failing test that specifies the next behavior increment. The test should fail for the right reason, proving the behavior gap exists.

**Green Phase**: Writing the minimum code needed to make the test pass. This phase prioritizes speed to green over code quality - optimization comes in refactor.

**Refactor Phase**: Improving code structure while keeping all tests green. This phase addresses technical debt, removes duplication, and improves design without changing behavior.

See `references/red-phase-guide.md`, `references/green-phase-guide.md`, and `references/refactor-phase-guide.md` for detailed guidance on each phase.

## When TDD Applies

**Appropriate Contexts**:
- New behavior implementation
- Bug fixes requiring behavior verification
- Meaningful refactors where correctness must be demonstrated
- Changes prone to rationalization shortcuts

**Test Design Considerations**:
- Tests should be focused enough to diagnose failures quickly
- Test granularity should match the smallest verifiable behavior increment
- Tests should avoid being too broad or testing multiple concerns

See `references/test-design-patterns.md` for common patterns and anti-patterns.

## Common Anti-Patterns

**Skipping Red**: Writing implementation before the test, then writing tests that already pass. This defeats the purpose of proving the behavior gap.

**Too-Broad Tests**: Writing tests that cover too much functionality, making failures hard to diagnose.

**Keeping Pre-Written Code**: Having implementation already written and retrofitting tests to it.

See `references/anti-patterns-and-rationalizations.md` for comprehensive coverage.

## Verification

After completing TDD cycles, verification ensures the implementation is complete and correct. This includes running the full test suite, checking coverage, and validating edge cases.

See `references/verification-checklist.md` for detailed verification steps.

## References

- `references/red-phase-guide.md` - Writing effective failing tests
- `references/green-phase-guide.md` - Minimal implementation strategies
- `references/refactor-phase-guide.md` - Refactoring while maintaining green
- `references/test-design-patterns.md` - Test design patterns and granularity
- `references/anti-patterns-and-rationalizations.md` - Common pitfalls to avoid
- `references/verification-checklist.md` - Final verification steps
