---
name: subagent-manager
description: Coordinate delegated work through scoped assignments, resource ownership, evidence-based acceptance, and integration. Use for large or multi-stage work, roadmap execution, or explicit delegation requests; short standalone tasks and roadmap prose edits may stay inline.
---

# Subagent Manager

Enter manager mode before full implementation research. The manager owns scope, dependencies, assignments, blockers, acceptance, integration, and existing status. Workers research, produce, and verify their slices; do not repeat their research. Respect project rules, authorization, and environment limits. If delegation is unavailable, disclose it and continue feasible work. Do not import another project's paths or tools.

Before **every new assignment and material reassessment**, apply [$task-model-router](../task-model-router/SKILL.md). It owns classification, model/effort selection, pricing, and budget gates; do not duplicate its algorithm. Install both skills in sibling directories. If the router is missing, report the dependency; do not invent a replacement selection procedure.

## Assign and execute

Choose independently acceptable slices, not an agent per command or a mandatory research/development/review chain. Explicit delegation requests require a worker even for sequential work. Otherwise a short known task may stay inline when delegation costs more than execution. Begin with one worker; parallelize only useful independent slices within actual concurrency and total-budget limits, including descendants.

Send a compact, self-contained assignment:

- Stable slice ID recorded in the existing brief/plan; keep it unchanged for the lifetime of that slice.
- Outcome/purpose, working directory, owner.
- Exact writable paths or read-only scope, exclusions, applicable rules/contracts, essential evidence.
- Dependencies/shared resource ownership, process handles and artifact paths when needed.
- Router decision, observable acceptance gate and appropriate verification.
- Return: verdict, owned changes, verification/results, evidence, risk/blocker.

Workers do not inherit the manager role. Nested delegation requires an explicitly assigned independent slice, shared budget, and no further recursive delegation.

Assign file ownership in shared checkouts; databases, browser state, servers, builds, lockfiles, and report directories also need ownership or serialized access. Distinct source files alone do not establish independence. Resolve overlapping edits first; never revert others' work. Do not create a worktree or user chat per slice. For user flows specify initial state → action → expected state; confirm fixtures and readiness before execution.

## Reuse within the original slice

Use native agent tools. A worker may continue only its original slice in the same context. Before any follow-up or task-bearing message, confirm the stable slice ID and that the original result/acceptance contract, scope, project/checkout, role, permissions and ownership, and source artifacts/fixtures are still current and match. If any item differs or is uncertain, start a fresh worker with a compact, verified handoff; never use follow-up or send_message to change an assignment to another domain or outcome. Diagnose → implement → verify may be phases of one slice only when all phases were included in its original scope and authorized by its permissions.

Follow-up is appropriate for completing or refining the worker's own result, clarifying missing facts, or checking the original acceptance criteria. A new independent result, another subsystem, or an independent review of the worker's own work requires a fresh worker, even in the same repository or file. Ordinary changes made within the slice do not by themselves invalidate reuse; a material change to its contract, branch, or context does. Idleness or completion does not make a worker available for other work. Apply task-model-router to fresh workers and pass only the short, verified handoff, not another worker's full history. If required model/effort changes are unsupported on follow-up, create a fresh worker for the same slice. Wait through native mechanisms without polling unchanged state. Continue independent work and communicate meaningful changes; require no empty periodic reports.

## Communication budget

Apply this rule to manager and workers; include it in each worker's brief. Send only the context needed for the owned slice; prefer compact handoffs when they preserve required facts. Reference file/line, diff, or saved log rather than copying whole files, histories, or successful tool output. Inter-agent updates are event-driven: blocker, decision needed, scope change, or consequential finding. Avoid acknowledgments, repeated instructions, and duplicate summaries; return one concise acceptance report. User-facing updates follow required cadence and convey useful progress. Preserve contracts, essential evidence, failures, and material uncertainty when shortening messages.

## Accept and integrate

Require done/partial/blocked, owned paths or read-only findings, exact checks/results (command and exit code when applicable), skipped checks, up to three evidence references, and remaining risk. Report available counters accurately: `unknown` or `lower-bound` where appropriate.

Compare against acceptance; inspect relevant diff/artifact and evidence gaps. Self-report alone is insufficient. Request missing facts from the same worker first when the request still satisfies the reuse policy above. Repeat checks only for a named gap or contradiction. Independent review suits material risk, disputed decisions, or explicit requests; provide criteria/artifacts without steering conclusions. Avoid duplicate review without new changes or evidence gaps.

After two unsuccessful corrections of the same gate, stop blind retries. Distinguish result defect, unclear contract, harness failure, and environment blocker; preserve failure artifacts and hand off contract, expected/actual, case, artifact, attempts. Apply the router before material escalation. Recheck the relevant gate after a demonstrated fix.

Maintain one accepted result per slice in existing plan/status; avoid redundant logs/dashboards. Complete the overall user goal after integration. Resume from the last handoff; never reconstruct missing counters or close others' tasks. Report outcome, verification, and material limitations without claiming unmeasured savings.
