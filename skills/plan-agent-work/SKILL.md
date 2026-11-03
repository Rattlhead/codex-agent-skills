---
name: plan-agent-work
description: Создавай, проверяй и возобновляй исполнимые дорожные карты для сложных задач. Определяй зависимости, ответственных, доказательства для приёмки и порядок восстановления работы. Не применяй полный процесс к вопросу в одно действие или стратегической дорожной карте продукта.
---

# Plan agent work

Convert the requested outcome into work that an agent can start, validate, and resume.
This method combines engineering practices. It is not a joint vendor standard.

## Select the mode first

Use the user's intent and existing authorization. State the mode briefly when ambiguity could affect actions.

- **PLAN ONLY:** Produce assignments, configurations, and future checks. Write authorized plan files, including the index and step files.
  Planning grants no implementation permission. Do not start execution workers, change source or tests, or run execution checks.
  Mark future checks **not run**. The manager may delegate substantial planning within permitted source and plan-file scope.
  That child produces the plan, not its future outputs.
- **PLAN+EXECUTE:** Plan and execute authorized work. Keep authorization across turns without redundant approval requests.
  Obtain applicable approval for material scope changes or actions outside authorization.
- **REVIEW:** Examine an existing plan against the requested outcome and observed constraints. Report concrete gaps and corrections.
  Plan review grants no execution permission.
- **RESUME:** Restore the prior mode and authorization. Examine current state.
  Run relevant safe checks only within existing authorization and mode. In plan-only mode, describe checks without execution.

## Main sequence

Make sure the outcome and authorization are clear. Select the smallest useful route below.
For substantial work, use the available manager and router before full research. Use their current whole-goal assessment and execution mode.
The primary is the director by default; `primary_only` needs their confirmed short-whole-goal exception.
Plan worker ownership and essential context before execution. Start only ready authorized assignments.
Accept outputs and update the canonical plan within the active mode.

## Choose the smallest useful route

A small task needs an action and its check. Answer a one-step question directly. Related outcomes need a compact plan. Long work needs explicit ownership, dependencies, state, decisions, and a resume point.

For a short plan-only request, give the outcome, action or actions, and future check. Stop there unless a persisted roadmap is requested; then use the package layout in [planning.md](references/planning.md). Do not load delegation, execution, or sources references automatically.

A persisted roadmap is one canonical package: a compact index and one file per defined step.
Keep authoritative task status, global constraints, and authorization in the index. Load only necessary step files.
Use [planning.md](references/planning.md) for layout and selective reading. Use [execution.md](references/execution.md) for safe updates and recovery.

For substantial planning or plan review, read [planning.md](references/planning.md). It contains outcome contracts, requirement coverage, dependencies, uncertainty, and templates. It also covers research and non-code work.

For substantial roadmaps, also read [delegation.md](references/delegation.md), even before execution. It defines the executor/context map: owners and their essential context.
Find the actual `subagent-manager` and `task-model-router`. Use their execution-mode, assignment, configuration, and cost procedures; do not make substitutes.
If either is missing, label the plan provisional. Record unresolved decisions without invented models, prices, agent IDs, or capabilities.
Stop dependent execution when required delegation is unavailable.

Read [execution.md](references/execution.md) only for relevant execution, evidence, integration, or recovery work.
In plan-only review or resume, read applicable guidance without running checks or changing implementation artifacts.
Use available implementation or verification skills where applicable.

Read [sources.md](references/sources.md) only to examine provenance or reassess a workflow choice. It is not required reading for each task.

Keep user constraints and the shared execution mode.
This skill alone grants no Goal-creation, worker-start, background-action, or additional permission.
Obey the selected mode, existing authorization, and tool contracts. Do not invent runtime state.
