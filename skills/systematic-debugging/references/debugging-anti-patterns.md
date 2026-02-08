# Systematic Debugging Details (6/6)

- **`root-cause-tracing.md`** - Trace bugs backward through call stack to find original trigger
- **`defense-in-depth.md`** - Add validation at multiple layers after finding root cause
- **`condition-based-waiting.md`** - Replace arbitrary timeouts with condition polling

**Related skills:**
- **Behavior Driven Development** - Use Skill tool load `superpowers:behavior-driven-development` skill for creating failing test case (Phase 4, Step 1)
- **Verification Before Completion** - Use Skill tool load `superpowers:verification-before-completion` skill to Verify fix worked before claiming success

## Real-World Impact

From debugging sessions:
- Systematic approach: 15-30 minutes to fix
- Random fixes approach: 2-3 hours of thrashing
- First-time fix rate: 95% vs 40%
- New bugs introduced: Near zero vs common
