# Plugin Optimization - Content Migration Guide

## Overview

This guide provides step-by-step migration templates for all skills exceeding the 500-token body limit.

**Target Structure:**
- **SKILL.md**: ~500 tokens (core workflow, essential steps)
- **references/**: Detailed content (examples, rationale, tables, edge cases)

## Migration Strategy

For each skill:
1. Identify content suitable for references/
2. Create appropriate reference files
3. Update SKILL.md to reference new files
4. Maintain core workflow in SKILL.md

---

## CRITICAL: writing-skills (5558 tokens → ~500)

**Must move: 5058+ tokens**

### Content Analysis
The writing-skills SKILL.md likely contains:
- Detailed writing guidelines
- Multiple examples
- Style guides
- Common mistakes tables

### Recommended References Structure
```
skills/writing-skills/
├── SKILL.md (keep: core workflow only)
└── references/
    ├── writing-guidelines.md (detailed rules)
    ├── examples.md (code examples)
    ├── style-guide.md (formatting standards)
    └── common-mistakes.md (antipatterns)
```

### Migration Steps
1. Read current writing-skills/SKILL.md
2. Extract detailed content to references/
3. Keep only essential workflow in SKILL.md
4. Add reference links in SKILL.md

---

## Skills Requiring Migration (Ordered by Priority)

### 1. subagent-driven-development (2455 tokens → ~500)
**Must move: 1955+ tokens**

**Suggested references/**
- `workflow-details.md` - Detailed task orchestration steps
- `examples.md` - Real-world subagent usage examples
- `coordination-patterns.md` - Agent communication patterns

**Keep in SKILL.md:**
- When to use (description)
- Core workflow (3-5 steps)
- Red flags

---

### 2. test-driven-development (2431 tokens → ~500)
**Must move: 1931+ tokens**

**Suggested references/**
- `tdd-cycle.md` - Detailed RED-GREEN-REFACTOR explanation
- `examples.md` - Test case examples
- `antipatterns.md` - Common TDD mistakes
- `testing-strategies.md` - Framework-specific approaches

**Keep in SKILL.md:**
- Core TDD cycle
- When to use
- Basic workflow

---

### 3. systematic-debugging (2429 tokens → ~500)
**Must move: 1929+ tokens**

**Suggested references/**
- `phase-details.md` - Detailed explanation of all 4 phases
- `evidence-gathering.md` - Diagnostic instrumentation examples
- `common-mistakes.md` - Rationalization table
- `supporting-techniques.md` - Root cause tracing, defense-in-depth

**Keep in SKILL.md:**
- Iron Law
- Four phases (overview only)
- Red flags

---

### 4. receiving-code-review (1497 tokens → ~500)
**Must move: 997+ tokens**

**Suggested references/**
- `review-response-guide.md` - How to handle different types of feedback
- `verification-steps.md` - How to verify reviewer concerns
- `examples.md` - Good vs bad review responses

**Keep in SKILL.md:**
- Core principles
- Basic workflow
- When to push back

---

### 5. dispatching-parallel-agents (1479 tokens → ~500)
**Must move: 979+ tokens**

**Suggested references/**
- `independence-criteria.md` - How to identify independent tasks
- `examples.md` - Parallel vs sequential scenarios
- `coordination-patterns.md` - Result aggregation strategies

**Keep in SKILL.md:**
- When to use
- Core dispatch workflow
- Independence checks

---

### 6. using-git-worktrees (1345 tokens → ~500)
**Must move: 845+ tokens**

**Suggested references/**
- `worktree-setup.md` - Detailed setup instructions
- `directory-selection.md` - Smart directory selection logic
- `cleanup-procedures.md` - Worktree cleanup and maintenance

**Keep in SKILL.md:**
- When to use
- Basic workflow
- Safety checks

---

### 7. finishing-a-development-branch (992 tokens → ~500)
**Must move: 492+ tokens**

**Suggested references/**
- `integration-options.md` - Detailed merge/PR/cleanup options
- `decision-criteria.md` - How to choose integration method
- `examples.md` - Common scenarios and resolutions

**Keep in SKILL.md:**
- When to use
- Core workflow
- Option presentation

---

### 8. verification-before-completion (965 tokens → ~500)
**Must move: 465+ tokens**

**Suggested references/**
- `verification-commands.md` - Framework-specific test/lint commands
- `evidence-requirements.md` - What constitutes proof
- `common-failures.md` - Typical verification issues

**Keep in SKILL.md:**
- Iron law (evidence before claims)
- Core workflow
- Red flags

---

### 9. using-superpowers (895 tokens → ~500)
**Must move: 395+ tokens**

**Suggested references/**
- `red-flags.md` - Detailed rationalization table
- `skill-priority.md` - When to use which skills
- `examples.md` - Skill invocation examples

**Keep in SKILL.md:**
- The Rule
- Core workflow (invoke before action)
- Basic red flags (top 5)

---

## OPTIONAL: Minor Overages

### 10. writing-plans (784 tokens → ~500)
**Consider moving: 284+ tokens**

**Suggested references/**
- `plan-template.md` - Detailed plan format
- `examples.md` - Good plan examples

---

### 11. requesting-code-review (635 tokens → ~500)
**Consider moving: 135+ tokens**

**Suggested references/**
- `review-checklist.md` - What to include in review request

---

### 12. executing-plans (600 tokens → ~500)
**Consider moving: 100+ tokens**

**Suggested references/**
- `execution-details.md` - Detailed execution steps

---

### 13. brainstorming (565 tokens → ~500)
**Consider moving: 65+ tokens**

**Suggested references/**
- `brainstorming-techniques.md` - Advanced techniques

---

## General Migration Pattern

### Template: SKILL.md (After Migration)
```markdown
---
name: skill-name
description: Brief description
---

# Skill Name

## When to Use

[2-3 sentences]

## Core Workflow

1. Step 1
2. Step 2
3. Step 3

## Red Flags

- Flag 1
- Flag 2

## References

See `references/` directory for:
- `details.md` - Detailed workflow explanation
- `examples.md` - Real-world examples
- `common-mistakes.md` - Antipatterns to avoid
```

### Template: references/details.md
```markdown
# [Skill Name] - Detailed Guide

## Overview

[Detailed explanation extracted from SKILL.md]

## Advanced Techniques

[Detailed content]

## Examples

[Code examples, scenarios]

## Common Mistakes

[Tables, antipatterns]
```

---

## Migration Checklist

For each skill:
- [ ] Read current SKILL.md completely
- [ ] Identify content for references/ (tables, examples, detailed steps)
- [ ] Create references/ directory if not exists
- [ ] Create reference files with extracted content
- [ ] Update SKILL.md to ~500 tokens (core workflow only)
- [ ] Add references section to SKILL.md
- [ ] Verify links work
- [ ] Re-run validation to confirm token count

---

## Automation Script

Use this bash script to create reference directories:

```bash
#!/bin/bash
PLUGIN_ROOT="/Users/FradSer/Developer/FradSer/superpowers"

# Critical
mkdir -p "$PLUGIN_ROOT/skills/writing-skills/references"

# Recommended
mkdir -p "$PLUGIN_ROOT/skills/subagent-driven-development/references"
mkdir -p "$PLUGIN_ROOT/skills/test-driven-development/references"
mkdir -p "$PLUGIN_ROOT/skills/systematic-debugging/references"
mkdir -p "$PLUGIN_ROOT/skills/receiving-code-review/references"
mkdir -p "$PLUGIN_ROOT/skills/dispatching-parallel-agents/references"
mkdir -p "$PLUGIN_ROOT/skills/using-git-worktrees/references"
mkdir -p "$PLUGIN_ROOT/skills/finishing-a-development-branch/references"
mkdir -p "$PLUGIN_ROOT/skills/verification-before-completion/references"
mkdir -p "$PLUGIN_ROOT/skills/using-superpowers/references"

# Optional
mkdir -p "$PLUGIN_ROOT/skills/writing-plans/references"
mkdir -p "$PLUGIN_ROOT/skills/requesting-code-review/references"
mkdir -p "$PLUGIN_ROOT/skills/executing-plans/references"
mkdir -p "$PLUGIN_ROOT/skills/brainstorming/references"

echo "✅ Reference directories created"
```

---

## Next Steps

1. Run automation script to create directories
2. Migrate skills in priority order (critical → recommended → optional)
3. Re-run validation after each migration
4. Update plugin version to 4.1.2 after all migrations complete
