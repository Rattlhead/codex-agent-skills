---
name: autonomous-decision-agent
description: Выбирай решение для нетривиального вопроса в разрешённой длительной задаче через субагента без права изменений под управлением текущего subagent-manager. Используй, когда выбор иначе потребует вопроса пользователю. Сохраняй обязательные согласования, разрешения и единый источник состояния. Не создавай второго менеджера и не передавай субагенту очевидные или решённые вопросы.
---

<a id="автономное-принятие-решений-при-выполнении-длительных-задач"></a>
# Autonomous decisions during long tasks

Select a justified next action within existing authority. Keep the user's goal, quality criteria, execution mode, and mandatory approvals.
A decision advises the authorized execution owner; it grants no permission.

## Route the question

Before new analysis, search the relevant existing decision section. Examine decision scope and input revision.
Apply the D authority gate before the A settled-answer test. The primary may do this preflight without a worker.

| Category | Condition | Route |
| --- | --- | --- |
| A | Current requirements, authoritative documentation, tests, a valid prior decision, or accepted completion uniquely determine the answer. Mechanically settled choices qualify. | Apply the determined answer. Skip the decision child. For structured results, use `NO_DECISION_NEEDED`. |
| B | A nontrivial choice is inside the current goal and authority | By default, obtain one read-only specialist decision child through the existing manager role. |
| C | A material fact is missing | Obtain the smallest authorized observation through the child or existing owner. Then request the automatic choice with current inputs. Until then, use `NEED_EVIDENCE`. |
| D | Authority is missing, the goal changes materially, or a mandatory human approval is pending | Use `ESCALATE_TO_USER`. Block dependent action. Continue independent authorized work. No choice vote can supply authority. |

Small or reversible actions do not automatically qualify for A. Multiple admissible options can need a nontrivial B choice.
For an unready named dependency or future trigger, use `DEFER`. This does not mean missing authority.
A stale decision can become B or C.
Irreversibility alone does not mean D if explicit existing authorization is sufficient and all mandatory checks pass.

## Apply only the needed guidance

- Before a B/C specialist decision, read [decision-policy.md](references/decision-policy.md). It defines selection, authority limits, and evidence quality.
- To assign, accept, log, or resume a decision, read the relevant [integration.md](references/integration.md) section.
  Find the installed `subagent-manager` and `task-model-router` by catalog names and actual paths.
  Keep their execution-mode, assignment, reuse, configuration, and acceptance rules. Do not start another manager.
- For a structured request or reply, read [decision-contract.md](references/decision-contract.md). Use its exact ten input fields and twelve output fields. The decision child returns only the JSON object.
- Read [evaluation.md](references/evaluation.md) only to evaluate or change this decision architecture. Do not load test fixtures or evaluation material for ordinary decisions.

Do not ask users to select routine B options only because alternatives exist. Do not send settled trivial questions to children.
Bundle only tightly related choices with the same scope and evidence.
Missing child capability grants no substitution or additional permission. Use the fallback rules in integration.md.
