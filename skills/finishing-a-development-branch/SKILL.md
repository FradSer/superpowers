---
name: finishing-a-development-branch
description: Use when you have completed all implementation and verification tasks - guides valid completion by enforcing final verification before merging, creating a PR, or cleaning up
argument-hint: (no arguments - provides reference guidance)
user-invocable: false
version: 1.1.0
---

# Finishing a Development Branch

This skill provides guidance on closing out completed work by choosing and executing the correct integration path.

## Core Concept

Use this skill when you believe the work is done. No branch operation should occur before fresh verification and explicit branch-target confirmation.

## Key Requirements

**Verification Gate**: Fresh verification required before any integration. All checks must pass. See `./references/verification-gate.md`.

**Integration Options**: Choose from merge locally, push + PR, keep as-is, or discard. See `./references/integration-options.md`.

**Base Branch Confirmation**: Never assume target branch. Explicitly confirm with user when ambiguous.

**Cleanup and Recovery**: Destructive operations require confirmation. Document rollback procedures. See `./references/cleanup-and-recovery.md`.

## References

- `./references/verification-gate.md` - Verification requirements before integration
- `./references/integration-options.md` - Option selection criteria and execution
- `./references/cleanup-and-recovery.md` - Cleanup procedures and rollback strategies
