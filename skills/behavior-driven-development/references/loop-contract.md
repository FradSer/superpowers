# Conversation-Flow Loop Contract

## Default Execution Mode

`behavior-driven-development` executes in agent conversation flow, not as a file-artifact pipeline.

Input sources:

- `docs/plans/YYYY-MM-DD-<topic>-design/_index.md`
- `bdd-specs.md` (Standard Gherkin) linked from `_index.md`

## Required Scenario Grammar

Scenarios must follow **Standard Gherkin** format (`Feature` / `Scenario` / `Given` / `When` / `Then`).

For full syntax reference, see [Cucumber Gherkin Reference](cucumber-gherkin-reference.md).

If ID or any Given/When/Then line is missing, stop and request document correction.

## In-Memory State Fields

Track per scenario in conversation state:

- `scenario_id`
- `phase` (`RED`, `GREEN`, `REFACTOR`)
- `iteration`
- `last_failure_reason`
- `stalled_count`

## Loop Behavior

1. Parse scenario from design docs.
2. Generate/update tests from scenario intent.
3. Run verification (`RED` must fail first).
4. Implement minimal fix (`GREEN`).
5. Re-run and evaluate progress.
6. Run refactor verification pass (`REFACTOR`).

## Safety Thresholds

- Cap max iterations per scenario.
- Escalate to manual decision point on repeated no-progress.
- Never run unbounded loops.

## Output Rules

Default mode returns conversational status only:

- `passed`
- `failed`
- `manual decision required`

Do not generate `.feature`, `summary.json`, `events.jsonl`, or `manual_decision/*.md` by default.

