# Common Mistakes and Red Flags (Part 2/2)

**Don't:**
- Tell them to "figure it out"
- Provide vague answers
- Skip answering
- Proceed without clarity

## If Reviewer Finds Issues

**Do:**
- Implementer (same subagent) fixes them
- Reviewer reviews again after fixes
- Repeat until approved
- Track the review loop

**Don't:**
- Skip the re-review
- Try to fix manually (context pollution)
- Accept "mostly good"
- Move forward with open issues

## If Subagent Fails Task

**Do:**
- Dispatch fix subagent with specific instructions
- Provide context about what went wrong
- Don't try to fix manually

**Don't:**
- Fix manually (causes context pollution)
- Skip the failure
- Proceed hoping it works
- Batch multiple failed tasks

## Common Rationalization

| Excuse | Reality |
|--------|---------|
| "Skip review, task is simple" | Simple tasks have issues too. Review catches them. |
| "Self-review is enough" | Self-review ≠ independent review. Both needed. |
| "Spec reviewer said mostly good" | Mostly ≠ compliant. Fix issues and re-review. |
| "Code quality can wait" | Must review before moving on. Fix now. |
| "Close enough on spec" | Spec is exact. Not negotiable. |
| "Review order doesn't matter" | Spec first, then quality. Order matters. |
| "One review for both" | Two separate concerns. Two reviews. |
| "Batch reviews at end" | Review per task. Catch issues early. |
| "Skip re-review, I trust the fix" | Reviewer must verify fixes. Always. |
