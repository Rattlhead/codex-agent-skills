---
name: subagent-manager
description: Decide whether to delegate large or multi-step work, then coordinate scoped assignments, resource ownership, acceptance evidence, and integration. Use for explicit delegation requests and independent review. Short tasks can stay with the primary agent.
---

# Subagent Manager

Before full implementation research, use manager mode.
The manager has responsibility for scope, dependencies, assignments, blockers, acceptance, integration, and the existing status.
Workers examine their slices and make their results. Workers do the necessary checks.
Without a specified gap, do not do their research again.
Keep project rules, authorization, and environment limits.
If delegation is unavailable, record the limitation. Continue the work that is possible.
Do not use another project's paths or tools.

## Technical nouns

- **Slice**: a defined part of a task with its own result and acceptance criteria.
- **Acceptance criteria**: the conditions for acceptance of a result.
- **Owner**: the agent with responsibility for a specified resource, interface, or check.
- **Shared interface**: a contract or result structure that producers and consumers use together.
- **Revision**: an identified version of an input, interface, or result.
- **Evidence**: an observation, artifact, or command result that gives a basis for an acceptance decision.
- **Handoff**: the verified information that a new worker needs to continue a slice.

Model IDs, tool parameters, file paths, and native agent tool names are technical names.

## Select the configuration

Before every new assignment or material change to the assessment, use [$task-model-router](../task-model-router/SKILL.md).
Before every repeated worker start, use its forecast and selection procedure again.
The router controls classification, model and effort selection, prices, and budget conditions.
Do not copy its algorithm here. The router also operates without this manager.
Install both skills in adjacent directories.
If the router is missing, record the missing dependency. Do not invent a replacement selection procedure.

## Choose the execution mode

Use the router's decision for the whole task.
If it records `primary_only`, keep the work with the primary agent and do not assign workers.
If it records `delegate`, keep the primary agent responsible for shared contracts, integration, and final acceptance.
Do not treat task length, multiple steps, or a complex score alone as a reason to delegate.
For an explicit delegation request, use `delegate` unless tool access, permissions, or budget limits prevent it.

## Give assignments

Select slices with independent acceptance criteria.
Do not create an agent for each command or a mandatory research, production, and review chain.
Give work to a worker only when the router selects `delegate`.
Start with one worker.
Add workers for independent slices that justify parallel work.
Honor an explicit request for sequential workers unless tool access, permissions, or budget limits prevent it.
For useful independent slices, use parallel workers within the available concurrency and total-budget limits.
Include descendants in these limits.

Give each worker a short, independent assignment with these items:

- A stable slice ID in the existing brief or plan. Keep that ID for the slice's lifetime.
- The outcome, purpose, directory, and owner.
- Exact writable paths or read-only scope, exclusions, applicable rules, contracts, and essential evidence.
- Dependencies and owners of shared resources. Include process handles and artifact paths when necessary.
- The router decision, observable acceptance criteria, and appropriate checks.
- The communication rules below.
- The required result: verdict, owned changes, checks, evidence, and remaining risk or blocker.

Workers do not automatically receive the manager role.
For nested delegation, explicitly give the worker an independent slice and a shared budget.
Do not give authorization for further recursive delegation.

## Control shared work

Give each file one owner in a shared checkout.
Give shared resources an owner or use sequential access.
These resources include databases, browser state, servers, builds, lockfiles, and report directories.
Different source files alone do not show independence.
Before changes, make sure that edit scopes do not overlap. Do not remove another worker's changes.
Do not create a worktree or user chat for each slice.

Give each shared interface one owner.
Give each check one owner, including checks for integration and user flows.
Keep the result fields and acceptance criteria stable during acceptance.
Before a necessary interface change, give the producer and consumers the owner's instructions for that change.
Record the affected dependencies and the new revision.
While an interface changes, workers can prepare work within their assigned scope.
Before acceptance, wait for a stable, identified interface revision and input revision.
Do not accept evidence from mixed revisions.
After an interface change, accept unchanged evidence only where the change has no effect on its inputs or conclusions.

For a user flow, specify the initial state, action, and expected state.
Before execution, make sure that fixtures and necessary resources are available.
For visual work, specify necessary cases, views, and resolution before workers pass images.

## Reuse within the original slice

Use native agent tools.
A worker can continue only its original slice in the same context.
Before a follow-up or task-bearing message, make sure that these items still match the original assignment:

- Stable slice ID, result contract, and acceptance criteria.
- Scope, project, checkout, and role.
- Permissions and ownership.
- Source artifacts and fixtures.

If an item differs or is uncertain, start a new worker with a short, verified handoff.
Do not use a follow-up or `send_message` to change the assignment's domain or outcome.
Diagnosis, implementation, and verification can be phases of one slice only if its original scope and permissions include them.

Use a follow-up to complete or correct the worker's result.
Also use it to get missing facts or examine the original acceptance criteria.
For a new independent result, another subsystem, or independent review of that worker's work, use a new worker.
This rule also applies in the same repository or file.
Ordinary changes within the slice do not themselves prevent reuse.
A material change to its contract, branch, or context prevents reuse.
An idle or completed worker does not become available for other work.

For a new worker, use the router. Give only the short, verified handoff, not another worker's full history.
If the tool cannot change a follow-up configuration, use a new worker when a model or effort change is necessary.
Keep the same slice for that worker.
Use native waits. Do not get unchanged status again and again.
Continue independent work. Give updates for meaningful changes without empty periodic reports.

## Limit communication

Apply these rules to the manager and workers. Include them in each worker's assignment.
Give only the context necessary for the owned slice.
Use short handoffs that keep required facts.
Use file and line references, a diff, or a saved log instead of complete files, histories, or successful tool output.
Send inter-agent updates for blockers, necessary decisions, scope changes, or material findings.
Do not send acknowledgments, repeated instructions, or duplicate summaries.
Give one short acceptance report.
For user updates, keep the required cadence. Give useful progress information.
When messages become shorter, keep contracts, essential evidence, failures, and material uncertainty.

## Accept and integrate

For each result, get these items:

- `done`, `partial`, or `blocked`.
- Owned paths or read-only findings.
- Exact checks and results, including the command and exit code where applicable.
- The input and interface revisions for each check.
- Checks not done, up to three evidence references, and remaining risk.
- Available counters, with `unknown` or `lower-bound` where applicable.

Compare the result with the acceptance criteria.
Examine the applicable diff or artifact and evidence gaps. A worker's statement alone is insufficient.
If the reuse conditions are still true, first tell that worker to give the missing facts.
Accept command and result evidence only for the stable, identified revision under review.
Do not duplicate a worker's check for the same revision without a named gap or contradiction.
Before you do a check again, record the changed input, failure, or evidence gap that makes it necessary.
Start with the smallest failed or affected area.
After integration, do the necessary overall check through its assigned owner.
After a local change, do it again only for an affected dependency or a specified gap.

For material risk, disputed decisions, or explicit review requests, use independent review.
Give the reviewer the criteria and artifacts. Do not tell the reviewer which conclusions to give.
Without new changes or evidence gaps, do not duplicate review.

After two unsuccessful corrections of the same criterion, stop blind retries.
Find the cause: result defect, unclear contract, test-system failure, or environment blocker.
Keep the failure artifacts.
Give the next worker the contract, expected and actual results, case, artifact, and previous attempts.
Before a material increase in effort or model capability, use the router.
After acceptance failure or cost beyond the forecast, recheck remaining work and slice configurations before further starts.
After a demonstrated correction, do the affected acceptance check again.

Keep one accepted result per slice in the existing plan or status.
Do not create duplicate logs or dashboards.
After integration, complete the overall user goal.
Continue from the last handoff. Do not invent missing counters or close another agent's tasks.
Give the outcome, verification, and material limitations. Do not claim savings without measurements.
