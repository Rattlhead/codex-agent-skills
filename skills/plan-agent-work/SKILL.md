---
name: plan-agent-work
description: Build, review, or resume executable agent roadmaps for complex code, research, analysis, and other work with checkable outcomes. Use for task dependencies, ownership, acceptance evidence, and recovery. Do not apply a large planning process to a one-step question or a strategic product roadmap.
---

# Plan agent work

Convert the requested outcome into work that an agent can start, check, and resume. This method is an engineering synthesis. It is not a joint vendor standard.

## Select the mode first

Use the user's intent and existing authorization. State the mode briefly when ambiguity could affect actions.

- **PLAN ONLY:** Produce the requested plan. A request to “make a plan” does not authorize implementation. Read instructions and relevant artifacts as needed. Do not change source or tests, perform implementation, or run real execution checks. Describe future checks as **not run**.
- **PLAN+EXECUTE:** Plan and carry out work already authorized by the user. Preserve that authorization across turns. Do not ask for it again. Seek appropriate approval for a material scope change or an action outside that authorization.
- **REVIEW:** Assess an existing plan against the requested outcome and observed constraints. Report concrete gaps and corrections. Review does not grant execution permission.
- **RESUME:** Restore the prior mode and authorization before work continues. Inspect current state. Run a safe, relevant check only if already authorized and allowed by that mode. A plan-only resume describes the check without running it.

## Main sequence

Confirm the outcome and authorization. Inspect the minimum existing state and inputs. Plan the work and assign only ready tasks when delegation is authorized. Accept outputs and run checks only within the active mode. Update the canonical tracker and leave a checkpoint when continued work needs one.

## Choose the smallest useful route

A small task needs an action and its check. Answer a one-step question directly. Related outcomes need a compact plan. Long work needs explicit ownership, dependencies, state, decisions, and a resume point.

For a short plan-only request, give the outcome, action or actions, and future check. Stop there. Do not load delegation, execution, or sources references automatically.

For substantial planning or plan review, read [planning.md](references/planning.md). It contains outcome contracts, requirement coverage, dependencies, uncertainty, and templates. It also covers research and non-code work.

Read [delegation.md](references/delegation.md) only when worker selection, assignments, shared resources, or independent review matters. For model and effort selection, discover and use `task-model-router` when installed. For actual coordination, discover and use `subagent-manager` when installed. Use their actual locations and current tool schemas; do not assume relative paths, model rates, or available capabilities. Missing optional skills do not prevent planning. If required delegation is unavailable, stop the dependent work and report the missing capability.

Read [execution.md](references/execution.md) when authorized execution, evidence assessment, integration, or recovery requires it. Ordinary future-plan drafting uses planning.md alone. For a concrete question about existing evidence or recovery, including a plan-only review or resume, read the relevant execution guidance without running checks or changing implementation artifacts. Do not load it automatically. Use implementation or verification skills when they suit the task and are available.

Read [sources.md](references/sources.md) only to examine provenance or reassess a workflow choice. It is not required reading for each task.

Keep user constraints and the shared execution mode in force. Selecting this skill alone does not authorize Goal creation, worker starts, background actions, or new permissions. Actual actions depend on the chosen mode, current authorization, and tool contracts. Do not invent runtime state.
