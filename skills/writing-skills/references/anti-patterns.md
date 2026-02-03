# Anti-Patterns in Skill Writing

## ❌ Narrative Example
"In session 2025-10-03, we found empty projectDir caused..."

**Why bad:** Too specific, not reusable

## ❌ Multi-Language Dilution
example-js.js, example-py.py, example-go.go

**Why bad:** Mediocre quality, maintenance burden

## ❌ Code in Flowcharts
```dot
step1 [label="import fs"];
step2 [label="read file"];
```

**Why bad:** Can't copy-paste, hard to read

## ❌ Generic Labels
helper1, helper2, step3, pattern4

**Why bad:** Labels should have semantic meaning

## What is a Skill?

A **skill** is a reference guide for proven techniques, patterns, or tools. Skills help future Claude instances find and apply effective approaches.

**Skills are:** Reusable techniques, patterns, tools, reference guides

**Skills are NOT:** Narratives about how you solved a problem once

## When to Create a Skill

**Create when:**
- Technique wasn't intuitively obvious to you
- You'd reference this again across projects
- Pattern applies broadly (not project-specific)
- Others would benefit

**Don't create for:**
- One-off solutions
- Standard practices well-documented elsewhere
- Project-specific conventions (put in CLAUDE.md)
- Mechanical constraints (if it's enforceable with regex/validation, automate it—save documentation for judgment calls)

## Skill Types

### Technique
Concrete method with steps to follow (condition-based-waiting, root-cause-tracing)

### Pattern
Way of thinking about problems (flatten-with-flags, test-invariants)

### Reference
API docs, syntax guides, tool documentation (office docs)
