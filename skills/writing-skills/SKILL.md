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

**MANDATORY**: Test-First (Red-Green) workflow. You must demonstrate the model failing the task *without* the skill (Red) before writing or editing the skill.
Baseline failure → minimal guidance → verification → loophole hardening. Skills should be tested against scenarios to prove they change behavior.

## Workflow

**Behavior-Driven Lifecycle**: 
1. **Red**: create a test case/prompt where the model currently fails. 
2. **Green**: Write/Edit the skill to handle that case. 
3. **Verify**: Run the prompt again to prove the skill fixed it. 
See `./references/bdd-mapping.md` and `./references/skill-bdd-lifecycle.md`.

**Structure**: Frontmatter, core concept, sections, references. Stay ~500 tokens. See `./references/skill-structure.md`, `./references/cso-token-budget-heuristics.md`, `./references/cso-description-principles.md`, `./references/cso-keyword-strategy.md`.

**Testing**: Test under pressure against realistic scenarios. See `./references/testing-methodology.md`, `./references/pressure-testing-and-hardening.md`, `./references/bulletproofing-skills.md`, `./references/anti-patterns.md`.

**Examples**: Concrete examples in references. See `./references/flowcharts-and-examples.md`.

**Deployment**: Verify baseline, testing, token budget. See `./references/deployment-checklist.md`.

## References

- `./references/bdd-mapping.md` - BDD concepts mapped to skill authoring
- `./references/skill-bdd-lifecycle.md` - Lifecycle phases
- `./references/skill-structure.md` - Structure templates
- `./references/cso-description-principles.md` - Discoverability principles
- `./references/cso-keyword-strategy.md` - Keyword strategy
- `./references/testing-methodology.md` - Testing approaches
- `./references/bulletproofing-skills.md` - Hardening techniques
- `./references/pressure-testing-and-hardening.md` - Pressure testing
- `./references/anti-patterns.md` - Failure patterns
- `./references/flowcharts-and-examples.md` - Visual aids
- `./references/cso-token-budget-heuristics.md` - Token budget
- `./references/deployment-checklist.md` - Deployment verification
