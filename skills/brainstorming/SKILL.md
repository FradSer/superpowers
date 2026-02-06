---
name: brainstorming
description: |
  A structured 4-phase workflow to turn ideas into implementation-ready designs.
  Phases:
  1. Discovery: Explore codebase and clarify requirements (Primary Agent).
  2. Option Analysis: Evaluate approaches and get user approval (Primary Agent).
  3. Detailed Design: Create comprehensive design document (Planning Subagent).
  4. Save & Setup: Commit design and prepare for implementation (Primary Agent).
  MANDATORY: Use this skill before creating features or modifying complex behavior.
---

# Brainstorming Ideas Into Designs

Turn rough ideas into implementation-ready designs through structured collaborative dialogue.

**Primary Agent**: Discovery and option analysis (Phase 1-2), then save and setup (Phase 4)
**Planning Subagent**: Detailed design creation (Phase 3)

See `references/roles-and-principles.md` for complete role descriptions and core principles.

## Phase 1: Discovery (Primary Agent)

Explore codebase, review project context, identify gaps, and ask focused questions to understand requirements.

See `references/phase1-discovery.md` for detailed exploration patterns and question guidelines.

## Phase 2: Option Analysis (Primary Agent)

Research existing patterns, propose 2-3 viable approaches, present conversationally with trade-offs, and get user approval.

See `references/phase2-option-analysis.md` for option comparison patterns and presentation guidelines.

## Phase 3: Detailed Design (Delegate to Planning Subagent)

Primary Agent delegates to Planning Subagent with complete context. Planning Subagent explores codebase and creates comprehensive design document.

See `references/phase3-detailed-design.md` for delegation format and design structure requirements.

## Phase 4: Save & Setup (Primary Agent)

Receive design content, save to `docs/plans/YYYY-MM-DD-<topic>-design/_index.md`, commit to git, and optionally set up for implementation.

See `references/phase4-save-setup.md` for file naming, git commit patterns, and implementation setup.

## Exit Criteria

Check `references/exit-criteria.md` for complete checklists ensuring each phase is fully complete before proceeding.

## References

- `references/phase1-discovery.md` - Detailed exploration patterns and question guidelines
- `references/phase2-option-analysis.md` - Option comparison and presentation patterns
- `references/phase3-detailed-design.md` - Delegation format and design structure
- `references/phase4-save-setup.md` - File operations and implementation setup
- `references/exit-criteria.md` - Complete checklists for all phases
