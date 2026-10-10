---
name: task-token-retrospective
description: After a completed substantial task, briefly review avoidable token use, overloaded agent context, and document discovery. Check project rules, explain why applicable rules failed, and propose corrections or document decomposition. Change project agent instructions only after explicit user approval of the proposed edit. Also use for a requested token-waste review.
---

# Task Token Retrospective

Review the completed task once, after its result and required checks are available.
Use this skill after work with several phases, delegated slices, or substantial rework.
Do not repeat the review after each command or minor step.
For an explicit request, review the specified task even if it was small.
Keep the review brief. Do not repeat completed work for this review.
Use the primary agent unless the user requests a separate reviewer.

## Use the available evidence

Start with the task's existing summary, decisions, tool results, and agent reports.
Read more only to resolve a specific finding.
Keep the review within this task and project.
Do not search all session histories or other projects.

Use available token counters and the original forecast, if recorded.
Separate measured tokens, estimates, and unknown values.
Do not infer task usage from account-wide limits or file length.
Without a baseline, do not claim a measured budget overrun.
Without counters, report observed unnecessary actions and their likely effect.
Do not invent exact wasted tokens, percentages, costs, or savings.
Do not add totals whose measurement intervals overlap.

Distinguish token volume from monetary cost.
If a cost comparison is necessary, use the available `$task-model-router` and its saved rates.
If it is unavailable, report the limitation. Do not create another price table.
Do not assume that every input token had the full input rate.
Use measured cache information where available.

## Find avoidable work

Identify the few findings with the greatest observed effect.
For each finding, give the action, evidence reference, cause, and a practical correction.
Consider these patterns only when the task evidence supports them:

- Repeated reads or checks with unchanged inputs and no identified gap.
- Large context transfers, duplicate reports, or excessive tool output.
- Retries without a new hypothesis or changed conditions.
- Rework caused by missed requirements, ownership conflicts, or unstable interfaces.
- Delegation whose coordination or duplicate work had no useful result.

Judge each action using the information available when it occurred.
A failed attempt can provide necessary evidence.
Changed inputs, unreliable checks, and explicit user requests can justify repeated work.
Do not label such work as waste without a supported reason.
Distinguish an observed cause from an unconfirmed explanation.
If no avoidable work is supported, say so and propose no new rule.

## Check context load and document discovery

For the primary agent and workers, compare loaded material with the information needed for their assigned work.
Check whether assignments, instructions, or contracts combined unrelated areas and forced unnecessary reading.
Look for irrelevant sections, repeated context transfers, lost decisions, and repeated reconstruction of the same facts.
Document length alone does not prove overload. Required reading is not waste because it is long.
Identify the unnecessary material and its observed effect before you propose decomposition.

If decomposition can prevent the cause, propose focused documents with clear responsibilities.
Keep shared requirements and acceptance criteria intact.
Keep the entry document short, with links and conditions for reading each document.
Do not make every linked document mandatory for every task.

Trace unnecessary document searches to the instruction or contract that should have guided discovery.
Check for absent, broken, or outdated links, unclear document names, and missing read conditions.
Show the search evidence, the needed document, and the entry point that lacked a usable reference.
Propose a verified link and a clear read condition when they can prevent the demonstrated search cost.
Do not propose more agent roles or files unless they address the observed cause.

## Check the project rules

For each supported finding, check the instructions that applied to its paths and role.
Inspect the relevant project `AGENTS.md` and referenced instructions only as necessary.
Use the version in force during the task when available.
If that version is unknown, state this limit.

If a rule is missing, propose a short rule only when it can prevent the demonstrated cause.
If a rule already exists, cite it. Do not add a duplicate.
Find why it did not apply or did not change the action.
Check discovery, scope, trigger clarity, instruction conflicts, and the worker's received context.
Distinguish a justified exception from a failure to follow the rule.
If the cause is unknown, state the missing evidence instead of asserting a cause.

Correct the demonstrated cause, such as an unclear trigger or a missing instruction reference.
Prefer one local correction to a new general rule.
Keep project proposals compatible with higher-priority instructions and required verification.
Use clear technical language in English and Russian.
Keep one action per procedure step and one term per concept.
Do not claim that Russian text conforms to the English ASD-STE100 standard.

## Report and request approval

Give a short report in the user's language:

- Measurement coverage: what is known, estimated, or unavailable.
- Up to three supported findings, with evidence, cause, and correction.
- Rule status: missing, present but ineffective, justified exception, or unknown.
- If an edit is useful, the exact project path and proposed diff or replacement text.

For decomposition, show source and target paths, content to move, and links to update.
Do not create a separate report file unless requested.
Keep the task result visible. Do not replace it with the review.
If a rule edit is proposed, ask for explicit approval of that edit.
Until approval arrives, do not create, change, or delete project agent instruction files.
This includes `AGENTS.md`, referenced rule files, and project agent configuration.
Do not split, move, or rewrite instruction or contract documents before approval of the proposed restructuring.
Approval of the original task or this review does not authorize these edits.
Do not add automatic approval or automatic rule-writing behavior.

After approval, read the current target and apply only the approved change.
If the target changed materially, show the revised edit and get approval again.
Preserve unrelated instructions. Check the diff for duplicates, conflicts, and scope changes.
Report the applied path and the check result.
Do not extend project approval to global rules or another project.
