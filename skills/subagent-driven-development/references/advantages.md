# Advantages and Comparison

## vs. Manual Execution

**Subagents follow TDD naturally:**
- Fresh instance follows the discipline
- No accumulated bad habits
- Clean adherence to test-first

**Fresh context per task:**
- No confusion from previous tasks
- Clear mental model for each component
- No context pollution

**Parallel-safe:**
- Each subagent independent
- No interference between tasks
- Clean separation of concerns

**Can ask questions:**
- Before starting work
- During implementation if needed
- Controller provides clarity

## vs. Executing Plans (Parallel Session)

**Same session:**
- No context handoff needed
- Controller has full picture
- No human-in-loop for continuation

**Continuous progress:**
- No waiting between batches
- Flow from task to task
- Faster overall completion

**Review checkpoints automatic:**
- After each task, not each batch
- Catch issues immediately
- Fix before they compound

## Efficiency Gains

**No file reading overhead:**
- Controller reads plan once
- Provides full text to subagents
- Subagent doesn't waste context on file I/O

**Controller curates context:**
- Exactly what's needed for task
- Scene-setting information
- Dependencies explicitly noted

**Subagent gets complete information upfront:**
- Full task text
- Context about where it fits
- Prerequisites and dependencies

**Questions surfaced before work:**
- Not after implementation
- Prevents wasted work
- Clearer requirements

## Quality Gates

**Self-review catches issues before handoff:**
- Implementer reviews own work
- Catches obvious mistakes
- Reduces reviewer burden

**Two-stage review:**
- Spec compliance prevents over/under-building
- Code quality ensures well-built implementation
- Separate concerns, separate reviews

**Review loops ensure fixes work:**
- Reviewer finds issues
- Implementer fixes
- Reviewer verifies fixes
- No "close enough"

**Spec compliance prevents scope creep:**
- Catches extra features early
- Ensures requirements met
- Nothing missing, nothing extra

**Code quality ensures maintainability:**
- Well-structured code
- Good test coverage
- Follows best practices

## Cost Considerations

**More subagent invocations:**
- Implementer per task
- Spec reviewer per task
- Code quality reviewer per task
- 3+ subagents per task

**Controller does more prep:**
- Extract all tasks upfront
- Curate context for each
- Manage review loops

**Review loops add iterations:**
- Issue found → fix → re-review
- Can cycle multiple times
- Adds invocations

**But catches issues early:**
- Cheaper than debugging later
- Prevents cascading problems
- Faster overall to fix immediately

**Net benefit:**
- Higher upfront cost
- Lower total cost (including fixes)
- Better quality output
