---
name: task-token-retrospective
description: После крупной задачи или по запросу кратко разбирать лишний расход токенов, поиск документов и неэффективные правила. Предлагать предотвращение повторной работы и сохранять проверенные решения с условиями применения. Правки инструкций проекта требуют явного одобрения конкретного изменения.
---

# Task Token Retrospective

Use the findings to help later tasks use verified project knowledge again and prevent repeated work.
After the task result and necessary checks are available, examine the completed task once.
Use this skill after work with several phases, delegated slices, or substantial rework.
Do not do the retrospective again after each command or minor step.
For an explicit request, examine the specified task even if it was small.
Keep the retrospective brief.
Do not do completed work again for this retrospective.
Use the primary agent unless the user requests a separate reviewer.

## Use the available evidence

Start with the task's existing summary, decisions, tool results, and agent reports.
Read more only to get necessary evidence for a specific finding.
Keep the retrospective within this task and project.
Do not search all session histories or other projects.
Use `unknown` for record fields that the task evidence does not show.
Do not infer a past event's date from the current date or a file timestamp.
For a quotation, copy the exact source text.
Otherwise, mark it as a paraphrase.

Use available token counters and the original forecast, if recorded.
Separate measured tokens, estimates, and unknown values.
Do not infer task usage from account-wide limits or file length.
Without a baseline, do not give a budget overrun as measured.
Without counters, report unnecessary actions from the task record and their likely effect.
Do not invent exact wasted tokens, percentages, costs, or savings.
Do not add totals whose measurement intervals overlap.

Distinguish token volume from monetary cost.
If a cost comparison is necessary, use the available `$task-model-router` and its saved rates.
If it is unavailable, report the limitation.
Do not make another price table.
Do not assume that every input token had the full input rate.
Use measured cache information where available.

## Find avoidable work

Select the few findings with the greatest actual effect.
For each finding, give the action, evidence reference, cause, and a practical correction.
For each proposed improvement, specify a prevention plan:

- The condition that makes the improvement relevant to a future task.
- Its storage path, discovery entry point, and condition for reading it.
- The executing agent's action and the unnecessary work it replaces.
- A short check of the expected result.

General advice without these details is not a complete prevention plan.
Before you propose a prevention plan, show the route for one matching future task from its entry point.
If a read condition does not cover that task, include the necessary route change in the proposal.
Consider these patterns only when the task evidence supports them:

- Repeated reads or checks with unchanged inputs and no identified gap.
- Large context transfers, duplicate reports, or excessive tool output.
- Retries without a new hypothesis or changed conditions.
- Rework caused by missed requirements, ownership conflicts, or unstable interfaces.
- Delegation with no useful result from coordination or duplicate work.

Judge each action using the information available when it occurred.
A failed attempt can provide necessary evidence.
Changed inputs, unreliable checks, and explicit user requests can justify repeated work.
Do not label such work as waste without a supported reason.
Distinguish a cause with evidence from an unconfirmed explanation.
If no avoidable work is supported, say so.
Propose a prevention change only for a supported finding or verified reusable solution.

<a id="check-context-load-and-document-discovery"></a>
## Examine context load and document discovery

For the primary agent and workers, compare loaded material with the information necessary for their assigned work.
Examine whether assignments, instructions, or contracts combined unrelated areas and caused unnecessary reading.
Look for irrelevant sections, repeated context transfers, lost decisions, and repeated reconstruction of the same facts.
Document length alone does not prove overload. Required reading is not waste because it is long.
Before you propose decomposition, specify the unnecessary material and its actual effect.

If decomposition can prevent the cause, propose focused documents with clear responsibilities.
Keep shared requirements and acceptance criteria intact.
Keep the entry document short, with links and conditions for reading each document.
Do not make every linked document mandatory for every task.

Find the instruction or contract that should have guided unnecessary document searches.
Examine it for missing, broken, or outdated links, unclear document names, and missing read conditions.
Show the search evidence, the needed document, and the entry point that lacked a usable reference.
If they can prevent the demonstrated search cost, propose a tested link and a clear read condition.
Do not propose more agent roles or files unless they address the observed cause.

## Preserve reusable solutions

Select verified solutions that can remove similar work from a future task.
Include environment fixes, document locations, reliable checks, contract dependencies, and confirmed tool limitations when relevant.
Keep useful verified solutions even when the original diagnosis was necessary and was not waste.
Record only a solution with evidence for its result.
Mark a verified workaround as a workaround.
Do not report failed attempts or untested guesses as reusable solutions.

Make a short record with these items:

- The problem and known cause, or `cause=unknown`.
- The project scope, relevant input or environment versions, prerequisites, and date of the successful check.
- The working steps or reference, with necessary commands, directory, and configuration where applicable.
- The verification evidence and observed result.
- The prevention plan and conditions that make a new check necessary.

For a port problem, record the selection method and affected configuration.
Do not use a temporarily free port as a permanent project setting.
In the record, make a check of current port availability mandatory before reuse.
Keep secret values and temporary process identifiers out of the record.

Use the existing project document for that subject when possible.
Keep one authoritative source instead of duplicate records or task journals.
Update the existing entry when new verified evidence changes the solution.
Remove obsolete instructions only within the authorized edit.
Show the exact entry and target path.
Save it only with authorization that covers that document.
If authorization is absent, include the ready-to-save entry in the report and request approval.
Explicit approval of the proposed edit is still necessary for changes to project agent instructions.
In the record, make a check of applicability mandatory before reuse.
Do diagnosis again only when conditions differ, the saved procedure fails, or a specific evidence gap remains.

<a id="check-the-project-rules"></a>
## Examine the project rules

For each supported finding, examine the instructions that applied to its paths and role.
Read the relevant project `AGENTS.md` and referenced instructions only as necessary.
Use the version in force during the task when available.
If that version is unknown, record this limit.

If a rule is missing, propose one only when a supported finding or verified solution justifies it.
If a rule already exists, give its reference.
Do not add a duplicate.
Find why it did not apply or did not change the action.
A statement that a rule was partly followed describes the failure. It does not explain the cause.
Examine whether the executing agent could find the rule and whether evidence shows that it received the rule.
Examine scope, trigger clarity, instruction conflicts, and the worker's received context.
Do not assume that an agent received a rule because the rule exists in a file.
Distinguish a justified exception from a failure to obey the rule.
If the cause is unknown, use the smallest relevant existing artifact that can show it.
If available evidence cannot show the cause, record the missing evidence and the smallest next check.
Do not do the whole task again for this investigation.
Do not assert an unconfirmed cause.
Keep that cause marked as unresolved.
Do not use a rule's existence alone to conclude that no correction is necessary.

Correct the demonstrated cause, such as an unclear trigger or a missing instruction reference.
Prefer one local correction to a new general rule.
Keep project proposals compatible with higher-priority instructions and necessary verification.
Use the applicable language rules for English and Russian technical text.
Keep one action per procedure step and one term per concept.
Make a full ASD-STE100 conformance statement only after the normative rule and dictionary checks.
Do not give an ASD-STE100 conformance statement for Russian text.

## Report and request approval

Give a short report in the user's language:

- Measurement coverage: what is known, estimated, or unavailable.
- Up to three supported findings, with evidence, cause, and correction.
- Rule status: missing, present but ineffective, justified exception, or unknown.
- If an edit is useful, the exact project path and proposed diff or replacement text.
- Reusable solutions, their prevention plans, and status: `proposed`, `saved`, or `ready_for_reuse`.

If no edit is proposed, give the supported reason or the unresolved evidence gap.
Do not use an unresolved cause as proof that no instruction correction is necessary.
For decomposition, show source and target paths, content to move, and links to update.
Unless requested, do not make a separate report file.
Keep the task result visible.
Do not replace it with the retrospective.
If a rule edit is proposed, ask for explicit approval of that edit.
Before approval, do not make, change, or delete project agent instruction files.
This includes `AGENTS.md`, referenced rule files, and project agent configuration.
Do not split, move, or rewrite instruction or contract documents before approval of the proposed restructuring.
Approval of the original task or this retrospective does not authorize these edits.
Do not add automatic approval or automatic rule-writing behavior.

After approval, read the current target and apply only the approved change.
If the target changed materially, show the revised edit and get approval again.
Keep unrelated instructions unchanged.
Examine the diff for duplicates, conflicts, and scope changes.
After an authorized save, examine the relevant links and read conditions.
Show the route for one matching scenario from the agent's entry point to the solution and necessary action.
If the solution is necessary for workers, make sure that saved instructions make its inclusion mandatory in relevant assignments.
Use existing artifacts or a small isolated check.
Do not do the original task again for this check.
Keep necessary verification and acceptance criteria unchanged.
Use `ready_for_reuse` only after successful checks of storage, discovery, applicability, and the necessary action.
An entry awaiting approval remains `proposed`.
Report the applied path, prevention status, and check result.
Report actual savings only after evidence from subsequent comparable work supports them.
Do not extend project approval to global rules or another project.
