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

## Requirements

**Claim-to-Command Mapping**: Every claim maps to specific proving commands. See `references/claim-to-command-mapping.md`.

**Execution Standards**: Run full commands, capture exit status, read complete output. Fresh execution required.

**Reporting**: Report factual status with command evidence and failure counts. See `references/evidence-reporting.md`.

**When Verification Fails**: State failures clearly, no false completion. See `references/failure-communication.md`.

## No Exceptions

Time pressure, simple changes, or previous success do not justify skipping verification.

## References

- `references/claim-to-command-mapping.md` - Mapping claims to proving commands
- `references/evidence-reporting.md` - Evidence reporting templates
- `references/failure-communication.md` - Failure reporting patterns
