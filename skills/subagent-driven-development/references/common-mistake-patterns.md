# Common Mistakes and Red Flags (Part 1/2)

## Red Flags - Never Do These

**Don't start on main/master:**
- Never start implementation on main/master branch without explicit user consent
- Use git worktrees for isolation

**Don't skip reviews:**
- Never skip spec compliance review
- Never skip code quality review
- Both are required for every task

**Don't proceed with unfixed issues:**
- If reviewer found problems, implementer must fix
- Don't move to next task with open issues
- Don't skip the re-review

**Don't dispatch multiple implementers in parallel:**
- Will cause merge conflicts
- Sequential per task only
- One implementer at a time

**Don't make subagent read plan:**
- Controller reads plan once
- Provides full text to subagent
- Don't waste subagent context on file I/O

**Don't skip scene-setting context:**
- Subagent needs to understand where task fits
- Provide dependencies and prerequisites
- Explain how this relates to overall feature

**Don't ignore subagent questions:**
- Answer before letting them proceed
- Provide complete information
- Don't rush them into implementation

**Don't accept "close enough" on spec:**
- Spec reviewer found issues = not done
- Must fix and re-review
- Exact compliance required

**Don't skip review loops:**
- Reviewer found issues
- Implementer fixes
- Reviewer reviews again
- Repeat until approved

**Don't let self-review replace actual review:**
- Self-review is first pass
- Still need spec compliance review
- Still need code quality review
- Both are needed

**Don't start code quality before spec compliance:**
- Wrong order
- Spec compliance must be ✅ first
- Then code quality review

**Don't move to next task with open issues:**
- Complete current task fully
- Both reviews approved
- Then and only then move forward

## If Subagent Asks Questions

**Do:**
- Answer clearly and completely
- Provide additional context if needed
- Don't rush them into implementation
- Re-dispatch with answers
