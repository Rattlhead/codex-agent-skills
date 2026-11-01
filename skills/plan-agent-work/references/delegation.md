# Delegation and ownership

## Choose delegation for a concrete benefit

Delegate when independent parallel work, bounded context, isolated tools, or independent review has enough benefit to pay for assignment, coordination, and integration. Otherwise keep one owner. Specialization helps when it changes the method or evidence quality; a role name alone does not do this. Confirm that each worker has adequate tools and permissions.

Keep tightly coupled planning, implementation, and the owner's tests with one owner. Make research questions and change scopes disjoint. Different files or worktrees do not prove independence: check interfaces, databases, ports, browser sessions, the Git index, and external systems. Assign one owner or serialize access to each shared resource. Record the boundary before dispatch.

The primary agent owns the goal, decisions, canonical state, integration accountability, and final acceptance. It may do useful non-overlapping work only when the current execution mode permits it. If `subagent-manager` reserves production changes and integration to workers in delegate mode, preserve that restriction. The primary may then perform only its permitted bounded checks of named gaps. Accountability does not grant permission to implement or integrate personally. Do not introduce a default hierarchy or grant recursive delegation by default.

## Assign only ready work

Check preconditions before starting a worker. Do not occupy a worker while a required artifact, decision, permission, or dependency is missing. Dispatch ready tasks as dependencies clear; use waves only when their shared boundary helps coordination.

Inspect the actual agent API. Verify how context inheritance works and whether clean or inherited context is supported. Choose the supported form that fits the task. Explicitly pass critical constraints even when context is inherited. Do not assume a fork includes tools, runtime state, files, or permissions that its schema does not promise.

## Assignment template

```text
Task ID: stable ID from the canonical plan
Role and goal:
Inputs: verified artifacts and minimum relevant context
Bounds: owned changes, shared resources, exclusions
Dependencies: accepted inputs and readiness conditions
Output: artifact and interface contract
Acceptance: criteria and required evidence
Report: result template below and delivery route
If relevant: permitted tools/actions, authorization limits, stop conditions
No recursive delegation unless explicitly authorized
```

Use `task-model-router` for model and effort decisions when available, as routed by SKILL.md. Do not copy its algorithms or price tables into an assignment.

## Receipts and review

Require a result that connects the real artifact to its criterion and evidence. Accept that evidence at its actual scope. Do not repeat the worker's whole task. Inspect a named gap, changed dependency, or unsupported claim when needed.

```text
Task ID and state:
Output artifacts and content identity:
Criteria: pass / fail / not run / unknown, with evidence links
Changes and affected dependencies:
Decisions, limits, blockers, and next step:
Shared resources released or still in use:
```

Use independent review when required or when its expected benefit justifies its cost. Give the reviewer criteria, relevant artifacts, and adequate tools. Do not prescribe the desired verdict. Require concrete mismatches with evidence and their connection to acceptance. A reviewer receipt supports the primary's acceptance decision; it does not replace it.
