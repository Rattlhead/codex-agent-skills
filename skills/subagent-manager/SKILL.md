---
name: subagent-manager
description: Управляй разрешённой работой как главный агент. Делегируй выполнение, координируй проверки и принимай результаты по доказательствам. Используй при запросе управления или делегирования и для задач за пределами подтверждённого исключения для короткой самостоятельной цели целиком.
---

# Agent Orchestrator

Keep the skill name `subagent-manager` and its manager role. Use the routes below without a second manager or a mandatory specialist chain.

The primary agent is the director by default. Use `delegate` unless the whole current goal qualifies for the short-task exception below.
The manager controls scope, dependencies, assignments, blockers, quality, and acceptance. It manages integration and gives brief status updates.
Workers investigate, produce, and validate their slices, including integration. The primary keeps responsibility for the shared contract and final acceptance.
Do not do worker research again without a named gap. Obey project rules, authorization, and environment limits.
Do not use another project's paths or tools.

## Route the current goal

Before project operations or full research, record one routing decision in the existing brief or conversation:

- Intent, deliverable type, finite scope, and revision.
- Authorization, material risks, and acceptance evidence.
- `execution_mode=delegate` or `execution_mode=primary_only`, with its basis.

For `primary_only`, record the affirmative whole-goal assessment against the criteria below.
Execution mode specifies who executes. Task modes such as `PLAN ONLY`, `AUDIT`, and `RESUME` do not determine execution mode.
On resume, restore these facts from canonical state and examine changed inputs. Include the mode and basis in continuation or acceptance handoffs as needed.
Do not make another tracker. Ask only for missing facts that prevent safe or correct progress. Continue independent work within authorization.

Distinguish answers, plans, audits, diagnosis, implementation, verification, and resume. Select checks for the deliverable's domain.
Risk controls depth and boundaries; it grants no edit permission and does not make a full audit necessary.
Use `task-model-router` for complexity, model, effort, mode, and cost decisions. Do not add another scoring method.

Load only the selected skill and the sections needed for the current phase:

| Need | Route and boundary |
| --- | --- |
| Execution mode, configuration, or budget | [$task-model-router](../task-model-router/SKILL.md); use a current assessment unless its inputs change. |
| Complex plan, roadmap review, or resume | [$plan-agent-work](../plan-agent-work/SKILL.md); keep its plan-only and execution modes separate. A short task needs only an action and check. |
| Comprehensive audit of a bounded result or system | [$comprehensive-audit](../comprehensive-audit/SKILL.md); select domain and risk coverage. A narrow question needs only its relevant check. |
| Defect diagnosis, related symptoms, or cause before fixes | [$root-cause-audit](../root-cause-audit/SKILL.md); compare mechanisms and alternatives before grouping defects. |
| Software review or verification | Find the installed `code-verification` skill by its actual catalog name and path. Use relevant checks. For other artifacts, use available domain verification skills. |
| Nontrivial decision within authorized work | [$autonomous-decision-agent](../autonomous-decision-agent/SKILL.md), under the decision procedure below. |
| Instruction audit or review of instruction changes | [$agent-instructions-audit](../agent-instructions-audit/SKILL.md); keep its approval boundary. |
| Completed substantial work or requested token review | [$task-token-retrospective](../task-token-retrospective/SKILL.md), once the result and checks are available. |

For source changes within authorization, use an available implementation skill. Find external skills in the current catalog; do not guess paths.
If a selected dependency is missing, record the limit. Continue only valid independent work, subject to the required-router stop below.
These routes do not make every skill necessary for each goal or guarantee automatic invocation.

An audit or diagnosis alone grants no permission to fix, add tests, or add instrumentation.
Keep existing authorization for those changes. Do not add a redundant approval gate.

## Technical nouns

- **Work item**: a bounded substantive task with one coherent result and acceptance criteria.
- **Slice**: a defined part of a task with its own result and acceptance criteria.
- **Acceptance criteria**: the conditions for acceptance of a result.
- **Owner**: the agent with responsibility for a specified resource, interface, or check.
- **Shared interface**: a contract or result structure that producers and consumers use together.
- **Revision**: an identified version of an input, interface, or result.
- **Evidence**: an observation, artifact, or command result that gives a basis for an acceptance decision.
- **Handoff**: validated information that a new worker needs to continue a slice.

Model IDs, tool parameters, file paths, and native agent tool names are technical names.

## Choose the execution mode

Before full research, use the router to examine the whole goal, expected context, substantive stages, and dependencies. Start from `delegate`.
Make sure the mode is eligible before cost optimization.
Start the necessary worker through the configuration and assignment procedure below. A recommendation alone is insufficient.
The primary remains the manager and acceptance owner. Do not add a manager layer.

Use `primary_only` only if the entire goal is short and self-contained, primary capability is sufficient, and context is bounded.
There must be no series of substantive stages or other required delegation. Use the router's distinction between substantive stages and supporting local actions.
If eligibility is uncertain, use minimal bounded discovery or clarification. Do not start a classification agent or treat uncertainty as permission for primary execution.
If the exception remains unconfirmed, keep `delegate`. Do not extract a pending substep from a delegated larger goal to claim the exception.
Do not wait for context overload or classify a long connected chain as short.
Keep coupled stages with one worker where that assignment is permitted by scope and permissions.
Task counts, file counts, professional roles, and possible parallelism alone do not justify additional workers.

Use the router's capability, rate, and total-cost assessment. Model name, generation, and raw token rate alone cannot prove a benefit.
Record unknown model, effort, payment, cache, or cost inputs. Unknown cost alone does not make delegation necessary.
Compare optional delegation with primary execution only after validation of the short-task exception.
Reassess before further substantive work if context, stages, dependencies, cost, or capability requirements change.
Keep user constraints and the primary agent's global model settings.

## Select the configuration

Give [$task-model-router](../task-model-router/SKILL.md) the whole goal, expected context, substantive stages, dependencies, independent work, and mode criteria above.
State mandatory delegation and review constraints. Do not derive worker count from task count or possible parallelism alone.
Before each assignment, repeated start, or material assessment change, use its forecast and selection procedure.
The router controls classification, configuration, prices, and budget conditions. It can also operate independently; do not copy its algorithm here.
Install both skills in adjacent directories. If the router is missing, stop mode selection and dependent project operations. Do not invent a replacement procedure.

## Execute within the selected mode

In `primary_only`, the primary may complete the eligible short whole goal and its acceptance checks within authorization.
In `delegate`, workers perform production and integration. The primary manages work and accepts supplied evidence.
The manager may read instructions, the router, rates, and tool schemas.
It may examine configuration and budgets, use coordination tools, and give brief status.
It may examine or do a bounded check for a named evidence gap, contradiction, or changed input.
Use the smallest necessary scope.
Assign explicit ownership of that check and its resources. Keep current permissions.
Do not do full research or suites again, or replace mandatory independent review. Publication needs applicable authorization.

In `delegate`, the assigned worker owns writes to canonical project state, roadmaps, and file-based status.
Manager inspection and coordination permissions exclude these writes.
If no eligible owner is available, report the proposed or blocked update in conversation.
Do not start a child only for bookkeeping.
Called skills keep their standalone modes, but their defaults cannot override the selected execution mode.
User instructions, permissions, environment limits, and budgets have priority. Automatic invocation is not guaranteed.

If worker, slot, tool, budget, permission, or user restrictions prevent required delegation, record the blocker and stop dependent operations.
Continue independent authorized work within the selected mode and role. Do not substitute primary execution, misuse bounded inspection, or expand authorization.
Do not change global model settings. For optional delegation, reassess against the criteria above.
If only the primary can perform a necessary worker operation, first obtain an explicit role change or worker access.

## Resolve nontrivial in-scope decisions

If a nontrivial unresolved choice would interrupt work within authorization, find `autonomous-decision-agent` in the current catalog.
If installed, load its actual entrypoint.
Use its A/B/C/D preflight, authority gate, read-only contract, acceptance, decision log, resume, and missing-capability rules.
Keep this manager and the selected execution mode. Assign any decision child through the normal manager/router procedure.
Read-only scope is an instruction contract unless the runtime enforces it. The optional skill cannot change permissions or worker availability.
If absent, keep this manager's rules and record the missing capability when relevant.

## Give assignments in delegate mode

Select slices by their context, shared interfaces, and independent acceptance criteria.
Do not assign one agent per command or make a research–implementation–verification chain mandatory.
One owner can perform these phases within its scope and permissions. Keep mandatory independent review.
Assign work after router selection within the selected mode. Start with one worker; add workers only for useful independent slices.
Honor explicit sequential-worker requests unless tools, permissions, or budgets prevent them.
Use useful parallel work within concurrency and total-budget limits, including descendants.

Give each worker a short, independent assignment with these items:

- Stable slice ID in the existing brief or plan; keep it throughout the slice.
- Outcome, purpose, directory, and owner.
- Exact writable paths or read-only scope, exclusions, rules, contracts, and essential evidence.
- Exact required source paths and sections; the base directory for relative paths.
- Dependencies and shared-resource owners; necessary process handles and artifact paths.
- Execution limits, observable acceptance criteria, and checks.
- Report language, separate deliverable language, and user overrides, even when defaults apply.
- Required location format. Numeric references must use tool-produced numbering for the exact file and revision, including blank lines.
- Verdict, owned changes, checks, evidence, and remaining risks or blockers.
- `Completion route`: `final response` if automatically forwarded; otherwise the actual destination and delivery channel.

Use supplied source paths; do not reconstruct them from basenames.
After a missing-source error, compare the attempted and assigned paths. Correct only that error; do not guess a relocated file.
If the source remains inaccessible, report the blocker. Do not claim dependent work complete. The manager may supply the essential excerpt under the rules below.

Workers do not automatically receive the manager role.
For nested delegation, explicitly give the worker an independent slice and a shared budget.
Do not give authorization for further recursive delegation.

## Control shared work

Use single-writer ownership: one owner per file in a shared checkout.
Assign shared-resource ownership or serialize access. Include databases, browser state, servers, builds, lockfiles, and report directories.
Different source files do not prove independence. Before edits, make sure scopes do not overlap. Keep other workers' changes.
Do not make a worktree or user chat per slice.

Assign one owner per shared interface and check, including integration and user-flow checks.
Keep result fields and acceptance criteria stable during acceptance.
Before an interface change, give producers and consumers the owner's instructions. Record affected dependencies and the new revision.
Workers may prepare assigned work during the change. Accept only stable, identified interface and input revisions; reject mixed-revision evidence.
Use earlier evidence only if the change cannot affect its inputs or conclusions.

For a user flow, specify the initial state, action, and expected state.
Before execution, make sure that fixtures and necessary resources are available.
For visual work, specify necessary cases, views, and resolution before workers pass images.

## Reuse within the original slice

Use native agent tools. A worker may continue only its original slice in the same context.
Before a follow-up or task-bearing message, make sure these original assignment properties are unchanged:

- Stable slice ID, result contract, and acceptance criteria.
- Scope, project, checkout, and role.
- Permissions and ownership.
- Identity and purpose of source artifacts and fixtures.

Their revisions may change within the original scope.
Before continuation, give the worker the current revisions and relevant changes.

If a property differs or is uncertain, start a new worker with a short validated handoff.
Do not change domain or outcome through follow-up or `send_message`.
Diagnosis, implementation, and verification belong to one slice only when its original scope and permissions include them.

Use follow-up for completion, corrections, missing facts, or the original acceptance criteria.
Use a new worker for an independent result, another subsystem, or independent review, even in the same repository or file.
Ordinary in-slice changes do not prevent reuse; material contract, branch, or context changes do.
Idle or completed workers remain bound to their original slices.

Route each new worker through the router. Supply a short validated handoff, not another worker's full history.
If follow-up cannot change configuration, start a new worker for a necessary model or effort change. Keep the slice.
Use native waits without repeated unchanged-status requests. Manage independent management tasks and unblocked worker work; report meaningful changes.

## Limit communication

Apply these rules to managers and workers. In assignments, include only the required language, source bindings, and location format.
Write user-facing messages in Russian, with clear technical language. Use short sentences, active voice, one main idea per sentence, and consistent terms.
ASD-STE100 applies to English; do not claim Russian conformity.
Write all inter-agent messages in English. Apply ASD-STE100 to assignments, updates, handoffs, and reports.
A worker's final report to the manager is inter-agent communication. Source language alone cannot override report language.
Use the requested deliverable language for a separate artifact and the report language for its handoff.
Keep exact quotations, identifiers, commands, code, paths, and diagnostic evidence, including their original language.
These rules do not prescribe internal reasoning language. Explicit user language requirements take priority.
For a requested ASD-STE100 conformance review, use the standard's rules and dictionary. Claim full conformity only after that review.
Do not add a separate review to each message.

Supply only essential slice context. Reference relevant existing background and instructions when the worker needs them and lacks them.
If a necessary source is inaccessible, supply its essential excerpt. Do not make a briefing file only to avoid a short assignment.
Keep rate tables, selection analysis, and team forecasts with the manager. Supply applicable resource limits, unless the worker owns budget work.
Use concise handoffs with file references, diffs, or saved logs instead of full files, histories, or successful tool output.

For numeric references, use tool-produced line numbers for the exact file and revision, including blank lines.
Number the source before selecting an excerpt. Do not infer source lines from combined output or diff positions.
Use valid numbered evidence; otherwise read only the necessary range.
When numeric lines are unnecessary, use a stable identifier or exact quotation. After source changes, refresh affected references.

Send inter-agent updates for blockers, necessary decisions, scope changes, material findings, or necessary peer coordination.
Give one completion handoff through the assigned route.
If the runtime automatically forwards final responses, use that route unless the assignment explicitly names another destination or channel.
The phrase "send the manager a handoff" alone does not change the route.
Omit acknowledgments of delivery, repeated instructions, and duplicate summaries.
Report results and acceptance evidence. Include causes only when they affect acceptance, next actions, or reusable knowledge.
On follow-up, report changes, new evidence, and unresolved gaps. Reference unchanged accepted facts.
Expand explanations only for unresolved acceptance questions or user requests. Keep the required user-update cadence with useful progress information.
Keep contracts, essential evidence, failures, and material uncertainty when shortening messages.

## Accept and integrate

For each delegated result, get these items:

- `done`, `partial`, or `blocked`.
- Owned paths or read-only findings.
- Exact checks and results, including the command and exit code where applicable.
- The input and interface revisions for each check.
- Checks not done, up to three evidence references, and remaining risk.
- Available counters, with `unknown` or `lower-bound` where applicable.

Compare actual handoff evidence with acceptance criteria, including relevant diffs or artifact excerpts. A worker statement alone is insufficient.
Assign missing evidence to its owner when reuse remains valid.
For manager gap checks permitted above, identify the bounded scope and ownership before execution.
Accept evidence only for the stable, identified revision under review.
Do checks again only for a named gap, contradiction, changed input, or failure. Record that reason before assignment.
Have the check owner start with the smallest affected area. After integration, assign the necessary overall check to its owner.
After a local change, do it again only for an affected dependency or named gap.

### Accept defect corrections

Before fixes, use relevant `root-cause-audit` guidance. Do not assume related symptoms share a cause.
For correction planning or authorized fixes, load only [remediation.md](../comprehensive-audit/references/remediation.md).
Use its regression evidence, mitigation limits, adjacent checks, and acceptance rules.
In plans, record future acceptance criteria and checks as `not run`. Planning grants no fix or execution permission.
A focused fix does not need the comprehensive workflow or coverage matrix.

If remediation guidance is unavailable, keep this manager's acceptance rules and causal route. Report the missing procedure.
Withhold dependent correction acceptance until necessary checks are specified. Continue unaffected work within authorization. Keep regression requirements.

For material risk, disputed decisions, or explicit review requests, use independent review.
Give the reviewer the criteria and artifacts. Do not tell the reviewer which conclusions to give.
Without new changes or evidence gaps, do not duplicate review.

After two unsuccessful corrections of the same criterion, stop blind retries.
Find the cause: result defect, unclear contract, test-system failure, or environment blocker.
Keep the failure artifacts.
Give the next worker the contract, expected and actual results, case, artifact, and previous attempts.
Before a material increase in effort or model capability, use the router.
After acceptance failure or cost beyond the forecast, recheck remaining work and slice configurations before further starts.
After a demonstrated correction, have the assigned owner do the affected acceptance check again.

Keep one accepted result per slice in the existing plan or status.
Do not make duplicate logs or dashboards.
After integration, complete the overall user goal.
Continue from the last handoff. Do not invent missing counters or close another agent's tasks.
Give the outcome, verification, and material limitations. Do not claim savings without measurements.

## Choose local checkpoints

Select a local checkpoint when a significant coherent result benefits review, handoff, or recovery.
Useful boundaries include completed substantial work, important contract or architecture changes, and integration.
Use value, not command, edit, or task counts. Routine small actions do not each need a commit.

Select the checkpoint before assignment where practical, or at an accepted milestone.
At each accepted significant milestone and before goal closure, resolve the checkpoint decision in the existing brief or status.
Record no commit with its reason, or select a checkpoint under the rules below.
For a selected checkpoint, issue the Git assignment to its authorized owner after acceptance; recording an owner or intent alone is insufficient.
Before goal closure, obtain its commit receipt or record an explicit deferred or blocked outcome with its reason and remaining action.
In the existing brief or status, record its owner, exact scope, trigger, required acceptance, and existing local-commit authority.
Use an authorized existing executor or integration owner. In `delegate`, assign Git work; the manager does not commit.
Do not start a bookkeeping worker. Serialize shared Git-index access. Do not request approval again for checkpoints already within authorization.

A worker completion report does not prove manager acceptance.
Release a checkpoint only after manager acceptance of its outputs and checks, unless an explicit preauthorized mechanism covers that decision.
Use a same-slice follow-up for a planned post-acceptance commit where necessary.
The worker's original scope and permissions must cover the checkpoint. Do not expand its permissions or domain.

Find the actual `plan-agent-work` installation. Load only `Local milestone commits` in its `references/execution.md`.
Do not load the full planning workflow or make a roadmap for a commit. Without a roadmap, use existing brief or status.
If unavailable, use a validated existing project checkpoint procedure.
If no procedure is available, report the checkpoint blocked. Also block it if authority or an eligible owner is missing.
Continue independent work within authorization.
Do not invent authority or silently install a skill. Keep the Git procedure in one place.

## Evaluate architecture changes

When changing agent architecture, compare alternatives on the same end-to-end tasks.
Examine whole-goal completion and quality, plus total cost, latency, and rework where telemetry is available.
Do affected important cases again. This comparison applies to architecture changes, not each ordinary task.
Mark missing counters unknown. Do not claim measured savings without them.
