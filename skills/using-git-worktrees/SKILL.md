---
name: using-git-worktrees
description: Use when starting feature work that needs isolation from current workspace or before executing implementation plans - creates isolated git worktrees with smart directory selection and safety verification
argument-hint: (no arguments - provides reference guidance)
user-invocable: false
version: 1.0.0
---

# Using Git Worktrees

This skill provides guidance on creating isolated workspaces for parallel development while preserving repository hygiene.

## Core Concept

Choose location by policy, validate safety constraints, then create deterministic branch/worktree pairs. Ad-hoc location choices and ambiguous naming lead to repository pollution.

## Worktree Concepts

**Isolated Workspaces**: Worktrees provide separate working directories for different branches within one repository. This allows parallel work without branch switching.

**Shared Repository**: All worktrees share the same git object database. Commits in any worktree are visible to all worktrees.

**Branch Association**: Each worktree is associated with a specific branch. The branch can only be checked out in one worktree at a time.

## Directory Selection Policy

**Policy-Driven Location**: Worktree directories should be chosen by project policy, not ad-hoc. Common policies include sibling directories or a dedicated worktrees folder.

**Ignore Verification**: Worktree directories must be git-ignored or located outside the repository. Tracked worktrees create recursive nesting issues.

**Naming Conventions**: Deterministic naming prevents collisions. Branch names or task identifiers make good directory names.

See `references/directory-selection-policy.md` for policy patterns and naming conventions.

## Safety Constraints

**Tracked Location Prevention**: Worktrees must not be created in tracked locations. This creates repository-within-repository scenarios.

**Ref Collision Avoidance**: Worktree names should not collide with existing refs (branches, tags). Ambiguous names confuse git commands.

**Cleanliness Verification**: Before worktree removal, verify no unmerged changes exist. Removing worktrees with unmerged work loses commits.

## Creation and Validation

**Creation Steps**: Worktree creation involves selecting location, creating worktree, creating/checking out branch, and validating setup.

**Validation Checks**: After creation, verify mapping is correct, branch state is clean, and directory is properly ignored.

**Deterministic Naming**: Branch and worktree names should follow deterministic patterns. Random or ambiguous names cause confusion.

See `references/creation-and-validation.md` for creation workflows and validation checklists.

## Navigation and Cleanup

**Navigation Commands**: After worktree creation, users need clear commands to navigate to the new workspace.

**Cleanup Safety**: Worktree cleanup requires verification of merge status. Unmerged changes should be explicitly confirmed before deletion.

**State Reporting**: After cleanup, repository state should be reported clearly. Users need to understand current worktrees and branch status.

See `references/cleanup-safety.md` for cleanup procedures and safety checks.

## When Worktrees Apply

**Appropriate Contexts**:
- Starting feature work that should not disturb current workspace
- Running parallel tasks on different branches
- Requiring explicit setup and cleanup safety

**Worktree Benefits**:
- No branch switching required for parallel work
- Clean isolation prevents context mixing
- Explicit cleanup prevents abandoned branches

**Worktree Limitations**:
- Cannot check out same branch in multiple worktrees
- Additional disk space for each worktree
- Requires cleanup discipline to avoid abandoned worktrees

## References

- `references/directory-selection-policy.md` - Location policies and naming conventions
- `references/creation-and-validation.md` - Creation workflows and validation
- `references/cleanup-safety.md` - Cleanup procedures and safety verification
