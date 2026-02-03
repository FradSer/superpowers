---
name: finishing-a-development-branch
description: Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup
argument-hint: (no arguments - provides reference guidance)
user-invocable: false
version: 1.0.0
---

# Finishing a Development Branch

This skill provides guidance on closing out completed work by choosing and executing the correct integration path.

## Core Concept

No branch operation should occur before fresh verification and explicit branch-target confirmation. Integration decisions require complete context about verification status and target branch.

## Verification Gate

**Fresh Verification Required**: Before any integration decision, required checks must be run fresh. Stale verification results can hide failures.

**Pass Confirmation**: All required verification must pass before proceeding. Failing checks block all integration options except discard.

**Evidence Capture**: Verification outputs should be captured as evidence. Claims of passing tests require actual command outputs.

See `references/verification-gate.md` for verification requirements and evidence standards.

## Integration Options

**Merge Locally**: Direct merge to base branch in current workspace. Appropriate when work is reviewed and ready for immediate integration.

**Push + PR**: Push to remote and create pull request. Appropriate when review is needed or team process requires PR workflow.

**Keep As-Is**: Leave branch unmerged for future work. Appropriate when work is complete but integration timing is uncertain.

**Discard**: Delete branch and abandon work. Appropriate when work is obsolete or superseded by other changes.

See `references/integration-options.md` for detailed option selection criteria and execution steps.

## Base Branch Confirmation

**Never Assume**: The target base branch must be explicitly confirmed. Assumptions about main/master/develop lead to wrong-branch merges.

**User Confirmation**: Integration target should be confirmed with the user when ambiguous. Multiple active branches require explicit direction.

**Branch Verification**: Before merge, verify the base branch exists and is up-to-date. Outdated base branches cause integration conflicts.

## Cleanup and Recovery

**Destructive Operation Safety**: Cleanup operations like branch deletion require explicit confirmation. Accidental deletions lose work.

**Rollback Capability**: Failed integrations need clear rollback procedures. Recovery steps should be documented before attempting risky operations.

**State Reporting**: After integration, final git state should be reported clearly. Users need to understand current branch, remote status, and next steps.

See `references/cleanup-and-recovery.md` for cleanup procedures and recovery strategies.

## When This Guidance Applies

**Appropriate Contexts**:
- Implementation work is complete and verified
- Integration decision point has been reached
- Branch operation requires safety verification

**Critical Safety Points**:
- Stop immediately on failing verification
- Require explicit confirmation before destructive cleanup
- Never assume the default base branch

## References

- `references/verification-gate.md` - Verification requirements before integration
- `references/integration-options.md` - Option selection criteria and execution
- `references/cleanup-and-recovery.md` - Cleanup procedures and rollback strategies
