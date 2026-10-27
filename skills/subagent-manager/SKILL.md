---
name: subagent-manager
description: Choose whether to delegate work based on context, independence, permissions, review needs, and total cost. Coordinate delegated slices through scoped assignments, resource ownership, acceptance evidence, and integration. Use for explicit manager or delegation requests, execution planning for substantial work, and independent review.
---

# Subagent Manager

Before project operations or full implementation research, assess the whole current user request and select an execution mode below.
In `delegate` mode, the manager directs scope, dependencies, assignments, blockers, and acceptance, coordinates integration, and keeps brief status in the conversation.
The primary agent remains responsible for the shared contract, integration coordination, and final acceptance. Assigned workers execute integration.
Workers examine their slices, make their results, and do the necessary checks. Without a specified gap, do not repeat their research.
Keep project rules, authorization, and environment limits.
Do not use another project's paths or tools.

## Technical nouns

- **Work item**: a bounded substantive task with one coherent result and acceptance criteria.
- **Slice**: a defined part of a task with its own result and acceptance criteria.
- **Acceptance criteria**: the conditions for acceptance of a result.
- **Owner**: the agent with responsibility for a specified resource, interface, or check.
- **Shared interface**: a contract or result structure that producers and consumers use together.
- **Revision**: an identified version of an input, interface, or result.
- **Evidence**: an observation, artifact, or command result that gives a basis for an acceptance decision.
- **Handoff**: the verified information that a new worker needs to continue a slice.

Model IDs, tool parameters, file paths, and native agent tool names are technical names.

## Choose the execution mode

Assess the whole current user goal, its context, and dependencies. Prefer one agent's continuous work cycle for closely connected context and sequential work, including long tasks. Task or file counts, professional roles, and roadmap size alone do not justify delegation.

Select `execution_mode=delegate` for useful independent parallel work; necessary isolation of context, permissions, or tools; independent review; demonstrated context overload or tool-selection problems; or a model configuration justified by the router's forecast of total cost through acceptance. Potential parallelism alone does not establish a benefit. Otherwise, select `execution_mode=primary_only`. Explicit user requirements and applicable constraints take priority, including required delegation or independent review.

Use the router to assess configuration adequacy, verified rates in the applicable payment unit, and forecast cost through acceptance. Model name, generation, or raw token rate alone cannot establish the benefit. Record unknown primary model, effort, payment mode, cache use, or cost inputs; do not invent them. Unknown cost alone does not require delegation.

Where both modes meet these constraints, let the router compare total cost and select an adequate mode. Reassess the mode when new evidence changes dependencies, expected benefit, cost, or required capability. Do not use reassessment to bypass user constraints. Do not change the primary agent's global model settings.

## Select the configuration

Before selecting a mode, give [$task-model-router](../task-model-router/SKILL.md) the whole goal, context dependencies, useful independent work, and the mode criteria above. Supply mandatory delegation or review constraints explicitly. Its generic defaults must not force delegation from task count or potential parallelism alone.
Before every new assignment, repeated worker start, or material change to the assessment, use its forecast and selection procedure.
The router controls classification, model and effort selection, prices, and budget conditions within these constraints. Do not copy its algorithm here. The router also operates without this manager.
Install both skills in adjacent directories.
If the router is missing, stop mode selection and dependent project operations. Do not invent a replacement selection procedure.

## Execute within the selected mode

In `primary_only` mode, the primary agent may perform the connected work, integration, and necessary acceptance checks within the authorized scope.
In `delegate` mode, the primary agent coordinates and accepts supplied evidence. Assign production work and integration to workers. The manager may read instructions, the router, rates, and tool schemas; assess models and budgets; use coordination tools; and keep brief status. It may also perform a bounded inspection or check for a named evidence gap, contradiction, or changed input. Use the smallest necessary scope, current permissions, and explicit ownership of the check and resources. Do not repeat full research or test suites, or replace a required independent reviewer. Publication still requires the applicable authorization.
Defaults in called skills, including the router, audit, and retrospective, do not override the selected execution mode. Their standalone modes are unchanged.
User instructions, permissions, environment limits, and budget limits retain priority. This skill does not guarantee automatic invocation in every project.

If required delegation is blocked by unavailable workers, slots, tools, a strict budget, or required permissions, stop dependent operations and record the blocker. Do not silently substitute primary execution or use bounded inspection to bypass it. For optional delegation, reassess the mode against the criteria above. If a required worker operation is available only to the primary agent, request an explicit role change or worker access before that operation.

## Give assignments in delegate mode

Select slices by the context and shared interface each needs, with independent acceptance criteria.
Do not create an agent for each command or a mandatory research, implementation, and verification chain. These phases can stay with one slice owner when its scope and permissions cover them; retain any required independent review.
Give work to a worker after the router selects a configuration consistent with the selected execution mode.
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
- The slice-specific execution limits, observable acceptance criteria, and appropriate checks.
- Any slice-specific communication requirement beyond the rules below.
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
- Identity and purpose of source artifacts and fixtures.

Their revisions may change within the original scope.
Before continuation, give the worker the current revisions and relevant changes.

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
Continue independent management work and coordinate unblocked worker work. Give updates for meaningful changes without empty periodic reports.

## Limit communication

Apply these rules to the manager and workers. Do not copy this section into each assignment.
Give only the context necessary for the owned slice.
Keep shared background and general instructions in their existing sources. Reference only the relevant section when the slice needs it and the worker does not already have it.
If a required source is inaccessible, supply only the essential excerpt. Do not create a separate briefing file merely to avoid copying a short assignment.
Keep rate tables, model-selection explanations, and the team forecast with the manager. Pass only applicable resource limits unless the worker's assigned role requires pricing or budget work.
Use short handoffs that keep required facts.
Use file and line references, a diff, or a saved log instead of complete files, histories, or successful tool output.
Send inter-agent updates for blockers, necessary decisions, scope changes, or material findings.
Do not send acknowledgments, repeated instructions, or duplicate summaries.
Give one short acceptance report.
Report the result and acceptance evidence, not the full investigation history. Include a short cause only when it affects acceptance, the next action, or reusable knowledge.
On follow-up, give changed facts, new evidence, and unresolved gaps. Reference unchanged accepted facts instead of repeating them.
Expand an explanation only for a specific unresolved acceptance question or a user request.
For user updates, keep the required cadence. Give useful progress information.
When messages become shorter, keep contracts, essential evidence, failures, and material uncertainty.

## Accept and integrate

For each delegated result, get these items:

- `done`, `partial`, or `blocked`.
- Owned paths or read-only findings.
- Exact checks and results, including the command and exit code where applicable.
- The input and interface revisions for each check.
- Checks not done, up to three evidence references, and remaining risk.
- Available counters, with `unknown` or `lower-bound` where applicable.

Compare bounded actual evidence in the handoff with the acceptance criteria, including the applicable diff or artifact excerpts. A worker's statement alone is insufficient.
Assign missing evidence to its owner when the reuse conditions still hold. The manager may resolve a named gap with the bounded inspection or check permitted above; identify its scope and ownership before execution.
Accept command and result evidence only for the stable, identified revision under review.
Do not duplicate a worker's check for the same revision without a named gap or contradiction.
Before assigning a repeated check, record the changed input, failure, or evidence gap that makes it necessary.
Have the check owner start with the smallest failed or affected area.
After integration, do the necessary overall check through its assigned owner.
After a local change, have the assigned owner repeat it only for an affected dependency or a specified gap.

For material risk, disputed decisions, or explicit review requests, use independent review.
Give the reviewer the criteria and artifacts. Do not tell the reviewer which conclusions to give.
Without new changes or evidence gaps, do not duplicate review.

After two unsuccessful corrections of the same criterion, stop blind retries.
Find the cause: result defect, unclear contract, test-system failure, or environment blocker.
Keep the failure artifacts.
Give the next worker the contract, expected and actual results, case, artifact, and previous attempts.
Before a material increase in effort or model capability, use the router.
After acceptance failure or cost beyond the forecast, recheck remaining work and slice configurations before further starts.
After a demonstrated correction, have the assigned owner repeat the affected acceptance check.

Keep one accepted result per slice in the existing plan or status. In `delegate` mode, assign file-based updates to its worker owner.
Do not create duplicate logs or dashboards.
After integration, complete the overall user goal.
Continue from the last handoff. Do not invent missing counters or close another agent's tasks.
Give the outcome, verification, and material limitations. Do not claim savings without measurements.

## Evaluate architecture changes

When changing the agent architecture, compare alternatives on the same end-to-end tasks. Assess completion of the whole goal and quality, plus total cost, latency, and rework where telemetry is available. Repeat affected important cases. This comparison is for architecture changes, not a benchmark before each ordinary task. Mark missing counters as unknown; do not claim measured savings without them.
