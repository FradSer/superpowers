---
name: verification-before-completion
description: Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always
argument-hint: (no arguments - provides reference guidance)
user-invocable: false
version: 1.0.0
---

# Verification Before Completion

This skill provides guidance on proving claims with fresh command evidence before making any completion assertions.

## Core Concept

Evidence before assertions. Before any completion claim, fresh commands must be run that directly prove the claim.

## Claim-to-Command Mapping

**Every Claim Needs Proof**: Claims like "tests pass", "build succeeds", or "bug is fixed" each map to specific proving commands.

**Direct Mapping**: The command should directly prove the claim. Indirect evidence (e.g., unit tests for integration claim) is insufficient.

**Fresh Execution**: Stale command outputs don't prove current state. Evidence must be from the current execution environment.

See `references/claim-to-command-mapping.md` for comprehensive claim-to-command mappings.

## Verification Execution

**Run Full Command**: Verification commands should be run completely, not partially. Partial runs hide failures in unchecked portions.

**Capture Exit Status**: Exit status (success/failure) matters more than stdout text. Zero exit indicates success; non-zero indicates failure.

**Read Complete Output**: Output should be read completely to count real failures. Skimming misses important failure details.

## Evidence Reporting

**Factual Status**: Report actual verification outcomes, not expectations or assumptions. "Should pass" is not evidence.

**Command Evidence**: Include the actual command run and relevant output. Abstract summaries hide verification gaps.

**Failure Counts**: When failures exist, report actual counts from output. "Some failures" is less actionable than "3 of 47 tests failed".

See `references/evidence-reporting.md` for reporting templates and examples.

## Failure Communication

**State Failures Clearly**: When verification fails, state what failed and the actual error. Vague descriptions prevent debugging.

**Next Remediation Step**: Failed verification should be followed by next remediation action, not completion claims.

**No False Completion**: Partial verification success does not equal completion. All verification must pass.

See `references/failure-communication.md` for failure reporting patterns.

## When Verification Applies

**Before Completion Claims**:
- Before saying tests/lint/build pass
- Before commit/push/PR actions
- Before reporting a fix as complete

**Verification Discipline**:
- No "should pass" or "expected to work" language
- No reliance on stale run results
- No completion statements after partial verification

## Common Anti-Patterns

**Stale Evidence**: Relying on previous test runs without fresh execution. State may have changed.

**Assumed Success**: Claiming tests pass without running them. Assumptions are not evidence.

**Partial Verification**: Running some checks but not all required ones. Partial verification misses failures.

**Vague Claims**: "Everything looks good" without specific verification outputs. Vague claims hide verification gaps.

## Verification Rigor

**Time Pressure**: Time pressure does not justify skipping verification. Unverified work creates rework later.

**Simple Changes**: Even simple changes require verification. Simple changes often have unexpected impacts.

**Previous Success**: Previous verification success doesn't prove current success. Code may have changed since last run.

## References

- `references/claim-to-command-mapping.md` - Mapping claims to proving commands
- `references/evidence-reporting.md` - Evidence reporting templates
- `references/failure-communication.md` - Failure reporting patterns
