---
name: autonomous-decision-agent
description: Resolve nontrivial choices during authorized long tasks through a bounded read-only decision child under the existing subagent-manager. Use when a routine in-scope choice would otherwise interrupt the user. Preserve human approvals, current permissions, and the canonical task state. Do not use as a second manager or for trivial settled questions.
---

# Автономное принятие решений при выполнении длительных задач

Choose a justified next action inside existing authority. Keep the user's goal, quality criteria, selected execution mode, and mandatory approvals. A decision is advice to the authorized execution owner; it grants no permission.

## Route the question

Search the existing decision section narrowly before new analysis. Check the decision's scope and input revision. Apply the D authority gate for the requested operation before testing whether its answer is already settled under A. The primary agent can do this preflight without a worker.

| Category | Condition | Route |
| --- | --- | --- |
| A | Current requirements, authoritative documentation, tests, a valid prior decision, or accepted completion uniquely determine the answer, including an obvious mechanically settled choice | Apply that determined answer. Skip the decision child. Use `NO_DECISION_NEEDED` when a structured result is requested. |
| B | A nontrivial choice is inside the current goal and authority | By default, obtain one read-only specialist decision child through the existing manager role. |
| C | A material fact is missing | Obtain the smallest authorized observation through the child or its existing owner. Then request the automatic choice with current inputs. Use `NEED_EVIDENCE` while that fact is missing. |
| D | Authority is missing, the goal changes materially, or a mandatory human approval is pending | Use `ESCALATE_TO_USER`. Block dependent action. Continue independent authorized work. No choice vote can supply authority. |

A small or reversible action alone does not make a choice A. Multiple admissible options can still require a nontrivial B choice. Use `DEFER` when a named dependency or future trigger is not ready. Do not mistake it for missing authority. A stale prior decision can become B or C. Irreversibility alone does not create D when explicit existing authorization is sufficient and all mandatory checks are met.

## Apply only the needed guidance

- Before a B/C specialist decision, read [decision-policy.md](references/decision-policy.md). It defines selection, authority limits, and evidence quality.
- To assign, accept, log, or resume a decision, read the relevant section of [integration.md](references/integration.md). Discover the installed `subagent-manager` and `task-model-router` by their available skill names and actual paths. Keep their execution mode, assignment, reuse, configuration, and acceptance rules. Do not start an extra manager agent.
- For a structured request or reply, read [decision-contract.md](references/decision-contract.md). Use its exact ten input fields and twelve output fields. The decision child returns only the JSON object.
- Read [evaluation.md](references/evaluation.md) only to evaluate or change this decision architecture. Do not load test fixtures or evaluation material for ordinary decisions.

Do not ask the user to select a routine B option merely because alternatives exist. Do not send covered trivial questions to a child. Bundle only tightly related choices with the same scope and evidence. A missing child capability does not authorize a silent substitute or a new permission: use the fallback rules in integration.md.
