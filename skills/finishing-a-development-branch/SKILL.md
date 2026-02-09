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

## Key Requirements

**Verification Gate**: Fresh verification required before any integration. All checks must pass. See `./references/verification-gate.md`.

**Integration Options**: Choose from merge locally, push + PR, keep as-is, or discard. See `./references/integration-options.md`.

**Base Branch Confirmation**: Never assume target branch. Explicitly confirm with user when ambiguous.

**Cleanup and Recovery**: Destructive operations require confirmation. Document rollback procedures. See `./references/cleanup-and-recovery.md`.

## References

- `./references/verification-gate.md` - Verification requirements before integration
- `./references/integration-options.md` - Option selection criteria and execution
- `./references/cleanup-and-recovery.md` - Cleanup procedures and rollback strategies
