---
name: dispatching-parallel-agents
description: Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies
argument-hint: (no arguments - provides reference guidance)
user-invocable: false
version: 1.0.0
---

# Dispatching Parallel Agents

This skill provides guidance on using parallel agents for truly independent work streams.

## Core Concept

Parallel agents should only be used when work streams have no shared state or sequential dependencies. Partition by domain first, then dispatch one focused agent per domain.

## Independence Assessment

**True Independence Indicators**:
- Failures are independent by subsystem or root cause
- Work can be integrated after isolated fixes without coordination
- No shared state mutations between tasks
- Domain boundaries are clear and non-overlapping

**False Independence Warning Signs**:
- Tightly coupled failures requiring coordinated fixes
- Shared data structures or state requiring synchronization
- Unclear domain boundaries leading to overlap
- Integration conflicts likely after parallel work

See `references/independence-assessment.md` for detailed assessment criteria.

## Dispatch Patterns

**Task Contract Definition**: Each agent needs clear scope, evidence requirements, and done conditions. Ambiguous contracts lead to integration conflicts.

**Domain Clustering**: Problems should be clustered into independent domains before dispatch. Each domain gets one focused agent to avoid ownership conflicts.

**Concurrent Execution**: Agents execute in parallel only after contracts are defined. Premature dispatch without clear boundaries wastes effort.

See `references/dispatch-patterns.md` for contract templates and dispatch strategies.

## Integration Considerations

**Output Consolidation**: After parallel execution, outputs must be consolidated and overlaps resolved. This requires reviewing all domain results together.

**Integrated Verification**: Domain-only success is insufficient. End-to-end verification ensures the integrated system works correctly.

**Overlap Resolution**: When agents produce overlapping changes, conflicts must be resolved with full context of both domains.

See `references/integration-checks.md` for verification strategies and conflict resolution patterns.

## When Parallel Dispatch Applies

**Appropriate Contexts**:
- Multiple subsystem failures with clear isolation
- Independent feature development in separate modules
- Parallel bug fixes with no shared code paths

**Inappropriate Contexts**:
- Coupled failures requiring coordinated investigation
- Shared state requiring synchronization
- Ambiguous boundaries leading to ownership conflicts

## Benefits and Trade-offs

**Lower Cycle Time**: Independent tasks complete faster when parallelized, reducing overall execution time.

**Coordination Overhead**: Parallel work requires upfront contract definition and post-execution integration, adding coordination cost.

**Risk of Rework**: Poor independence assessment leads to integration conflicts and wasted parallel effort.

## References

- `references/independence-assessment.md` - Criteria for assessing task independence
- `references/dispatch-patterns.md` - Task contract templates and dispatch strategies
- `references/integration-checks.md` - Integration verification and conflict resolution
