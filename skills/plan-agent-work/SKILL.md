---
name: plan-agent-work
description: Build, review, or resume executable agent roadmaps for complex code, research, analysis, and other work with checkable outcomes. Use for task dependencies, ownership, acceptance evidence, and recovery. Do not apply a large planning process to a one-step question or a strategic product roadmap.
---

# Plan agent work

Convert the requested outcome into work that an agent can start, check, and resume. This method is an engineering synthesis. It is not a joint vendor standard.

## Select the mode first

Use the user's intent and existing authorization. State the mode briefly when ambiguity could affect actions.

- **PLAN ONLY:** Produce assignments, configurations, and future checks. Write authorized plan files, including the index and step files. A request to “make a plan” does not authorize implementation. Do not start execution workers, change source or tests, or run execution checks. Describe future checks as **not run**. A large planning assignment may itself be delegated through the manager to inspect permitted sources and write only its assigned plan files; that child produces the plan, not its future outputs.
- **PLAN+EXECUTE:** Plan and carry out work already authorized by the user. Preserve that authorization across turns. Do not ask for it again. Seek appropriate approval for a material scope change or an action outside that authorization.
- **REVIEW:** Assess an existing plan against the requested outcome and observed constraints. Report concrete gaps and corrections. Review does not grant execution permission.
- **RESUME:** Restore the prior mode and authorization before work continues. Inspect current state. Run a safe, relevant check only if already authorized and allowed by that mode. A plan-only resume describes the check without running it.

## Main sequence

Confirm the outcome and authorization, then choose the smallest useful route below. For substantial work, before full research use the manager and router where available; reuse a current assessment of the whole goal and execution mode. The primary is the director by default; `primary_only` requires their confirmed short whole-goal exception. Plan worker ownership and essential context before execution. Start only ready assignments within authorization. Accept outputs and update the canonical plan within the active mode.

## Choose the smallest useful route

A small task needs an action and its check. Answer a one-step question directly. Related outcomes need a compact plan. Long work needs explicit ownership, dependencies, state, decisions, and a resume point.

For a short plan-only request, give the outcome, action or actions, and future check. Stop there unless a persisted roadmap is requested; then use the package layout in [planning.md](references/planning.md). Do not load delegation, execution, or sources references automatically.

A persisted roadmap is one canonical package: a compact index with links and authoritative task status, plus one file per defined step. Keep global constraints and authorization in the index; load only the needed step files. See [planning.md](references/planning.md) for layout and selective reading, and [execution.md](references/execution.md) for safe updates and recovery.

For substantial planning or plan review, read [planning.md](references/planning.md). It contains outcome contracts, requirement coverage, dependencies, uncertainty, and templates. It also covers research and non-code work.

For substantial roadmaps, also read [delegation.md](references/delegation.md), even when execution starts later. It defines the executor and context map. Discover and use the actual `subagent-manager` and `task-model-router` for execution mode, assignments, configuration, and cost decisions; do not create another selection or coordination method. If either is missing, a clearly labelled provisional plan is still possible. Record unresolved decisions without inventing models, prices, agent IDs, or capabilities. Stop dependent execution when required delegation is unavailable.

Read [execution.md](references/execution.md) when authorized execution, evidence assessment, integration, or recovery requires it. For an evidence or recovery question in a plan-only review or resume, read the relevant guidance without running checks or changing implementation artifacts. Do not load it automatically. Use implementation or verification skills when they suit the task and are available.

Read [sources.md](references/sources.md) only to examine provenance or reassess a workflow choice. It is not required reading for each task.

Keep user constraints and the shared execution mode in force. Selecting this skill alone does not authorize Goal creation, worker starts, background actions, or new permissions. Actual actions depend on the chosen mode, current authorization, and tool contracts. Do not invent runtime state.
