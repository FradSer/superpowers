# BDD Mapping for Skills

Writing skills IS Behavior-Driven Development applied to process documentation. You write behavior scenarios (pressure scenarios with subagents), watch them fail (baseline behavior), write the skill (documentation), watch scenarios pass (agents comply), and refactor (close loopholes).

## The Mapping

| BDD Concept | Skill Creation |
|-------------|----------------|
| **Behavior Scenario** (Test case) | Pressure scenario with subagent |
| **Production code** | Skill document (SKILL.md) |
| **Scenario fails (RED)** | Agent violates rule without skill (baseline) |
| **Scenario passes (GREEN)** | Agent complies with skill present |
| **Refactor** | Close loopholes while maintaining compliance |
| **Define Scenario First** | Run baseline scenario BEFORE writing skill |
| **Watch it fail** | Document exact rationalizations agent uses |
| **Minimal guidance** | Write skill addressing those specific violations |
| **Watch it pass** | Verify agent now complies |
| **Refactor cycle** | Find new rationalizations → plug → re-verify |

The entire skill creation process follows RED-GREEN-REFACTOR, strictly driven by BDD scenarios (BDD driving TDD).

## The Iron Law

```
NO SKILL WITHOUT A FAILING SCENARIO FIRST
```

This applies to NEW skills AND EDITS to existing skills.

Write skill before testing? Delete it. Start over.
Edit skill without testing? Same violation.

**No exceptions:**
- Not for "simple additions"
- Not for "just adding a section"
- Not for "documentation updates"
- Don't keep untested changes as "reference"
- Don't "adapt" while running tests
- Delete means delete
