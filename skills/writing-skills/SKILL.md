---
name: writing-skills
description: Use when creating new skills, editing existing skills, or verifying skills work before deployment
argument-hint: (no arguments - provides reference guidance)
user-invocable: false
version: 1.0.0
---

# Writing Skills

This skill provides guidance on authoring and refining skills with a test-first approach so behavior change is proven, not assumed.

## Core Concept

Baseline failure → minimal guidance → verification → loophole hardening. Skills should be tested against scenarios to prove they change behavior.

For the exact mapping between TDD concepts and skill authoring artifacts, see `references/tdd-mapping.md`.

## Skill TDD Lifecycle

**Baseline Scenarios**: Before writing skill guidance, run baseline scenarios without the skill and record failures. This proves the behavior gap exists.

**Minimal Guidance**: Write the minimum guidance targeting observed failure modes. Over-specification makes skills brittle.

**Verification**: Re-run scenarios with the skill loaded and verify improved behavior. Assumed improvements without testing are invalid.

**Loophole Hardening**: When new loopholes are found, harden wording against rationalization patterns.

See `references/skill-tdd-lifecycle.md` for detailed lifecycle phases.

## Skill Structure

**Canonical Format**: Skills follow a standard structure with frontmatter metadata, core concept, topic sections, and references.

**Token Budget**: Frequently-loaded skills should stay small (~500 tokens) by moving depth to references. Token bloat reduces context efficiency.

**Progressive Disclosure**: Core guidance in SKILL.md, detailed techniques in references/. This allows selective deep-diving.

See `references/skill-structure.md` for structure templates and `references/cso-token-budget-heuristics.md` for token guidance.

## Discoverability

**Description Focus**: Skill descriptions should focus on *when to use*, not *what it does*. Trigger conditions make skills discoverable.

**Keyword Strategy**: Descriptions should include common user intent patterns. "Use when implementing" maps to implementation intent.

**CSO Principles**: Claude Skill Optimization (CSO) principles guide description writing for maximum discoverability.

See `references/cso-description-principles.md` and `references/cso-keyword-strategy.md` for discoverability guidance.

## Testing Methodology

**Scenario-Based Testing**: Skills should be tested against realistic scenarios, not abstract reasoning. Real scenarios reveal rationalization patterns.

**Pressure Testing**: Skills should be tested under time pressure and ambiguity. Weak wording fails under pressure.

**Regression Testing**: After hardening, re-run previous failure scenarios. Hardening for one loophole shouldn't break previous fixes.

See `references/testing-methodology.md` and `references/pressure-testing-and-hardening.md` for testing strategies.

## Bulletproofing Against Rationalization

**Red Flag Patterns**: Skills should explicitly call out common rationalization patterns ("This is simple, I don't need the skill").

**Anti-Pattern Documentation**: Known failure modes should be documented so they can be addressed in guidance.

**Wording Precision**: Weak language like "should consider" allows rationalization. Strong language like "must verify" prevents skipping.

See `references/bulletproofing-skills.md` and `references/anti-patterns.md` for hardening techniques.

## Flowcharts and Examples

**When Flowcharts Help**: Non-obvious decision trees and loops benefit from flowcharts. Simple linear flows don't need diagrams.

**Example Quality**: Examples should be concrete and realistic, not abstract. Good examples prevent misinterpretation.

**Example Placement**: Examples belong in references/ for deep-diving, not in main SKILL.md (token efficiency).

See `references/flowcharts-and-examples.md` for guidance on visual aids.

## Deployment Checklist

**Pre-Deployment Verification**:
- Baseline scenarios recorded with failures
- Skill tested against scenarios and behavior improved
- Token count within budget for frequently-loaded skills
- Description focuses on when-to-use
- References provide depth without bloating main skill

**Post-Deployment Monitoring**:
- Watch for scenarios where skill is skipped despite applying
- Gather feedback on unclear guidance
- Iterate on hardening when new loopholes found

See `references/deployment-checklist.md` for complete deployment verification.

## When This Guidance Applies

**Appropriate Contexts**:
- Reusable behavior pattern appears repeatedly
- Existing skill fails under pressure scenarios
- Skill wording needs stronger anti-rationalization guardrails

**Skill Scope**:
- Over-scoping beyond repeatable patterns makes skills unmaintainable
- Under-scoping misses reuse opportunities
- Right scope: behavior pattern repeated across multiple scenarios

## References

- `references/tdd-mapping.md` - TDD concepts mapped to skill authoring
- `references/skill-tdd-lifecycle.md` - Lifecycle phases in detail
- `references/skill-structure.md` - Structure templates and conventions
- `references/cso-description-principles.md` - Description discoverability principles
- `references/cso-keyword-strategy.md` - Keyword strategy for triggers
- `references/testing-methodology.md` - Scenario-based testing approaches
- `references/bulletproofing-skills.md` - Hardening against rationalization
- `references/pressure-testing-and-hardening.md` - Testing under pressure
- `references/anti-patterns.md` - Common failure patterns
- `references/flowcharts-and-examples.md` - Visual aids and examples
- `references/cso-token-budget-heuristics.md` - Token budget guidance
- `references/deployment-checklist.md` - Pre and post-deployment verification
