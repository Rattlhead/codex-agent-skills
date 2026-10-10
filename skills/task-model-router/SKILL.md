---
name: task-model-router
description: Select a model and reasoning effort for a task or slice. Decide whether the primary agent should work alone or delegate. Compare capability, workload, rates, and total cost through acceptance. Use for model, budget, or delegation decisions. Do not start agents for classification.
---

# Task Model Router

Use this skill independently for each task or slice. Keep the user's explicit choices, quality requirements, and budget limits.
If the user's specified model is unavailable, record that limitation. Do not silently select a different model.
Without authorization, do not change global defaults, the account, credentials, or the tariff.
A recommendation does not change the current chat's model.

## Technical nouns

These subject terms have the same meaning throughout this skill:

- **Model**: an AI configuration with a specific model ID.
- **Reasoning effort**: the tool parameter that controls the model's reasoning work.
- **Slice**: a defined part of a task with its own result and acceptance criteria.
- **Acceptance criteria**: the conditions for acceptance of a result.
- **Token**: the unit that the applicable service uses to measure model input or output.
- **Billed output**: output tokens that the service charges, including reasoning tokens where applicable.
- **Forecast**: an estimate of total cost through acceptance.
- **Effective rate reference**: saved rates that are current, or rates checked during this assessment.
- **Subagent**: an agent that receives a slice from another agent. A descendant is a subagent of a subagent.
- **Tool schema**: the tool's current specification of parameters and permitted values.

Exact model IDs, parameter names, payment units, and API names are technical names.

## Verified prices

Read the saved [rate reference](references/rates.md) before a cost estimate.
It gives the rates, speed multipliers, payment unit, sources, and check date.
Use it without an online lookup while it is no more than 30 days old.
Check rates when the reference is more than 30 days old.
Also check when the user reports a change.
Check rates when an official source shows a rate change.
Check rates when the payment mode changes.
Check only missing rates when the reference does not include a model or payment mode.
After a check, update `references/rates.md` with the rates and the new date.
Use the updated reference for all assignments in this assessment.
Do not check the same rates again for each subagent.
If the skill directory is read-only, save one dated rate record for this assessment.
Report that you could not update the saved reference.
For API USD, use the applicable [official API rates](https://developers.openai.com/api/docs/pricing).
Do not calculate API USD from credits.

## Subagent availability

Observation date: **2026-10-08**. Source: this session's `collaboration.spawn_agent` schema.
This observation is for this runtime only. It gives no assurance of availability for an account or another runtime.
Before each assignment, examine the actual tool schema. Use that schema if it differs from this table.

| Model | Model override | Supported reasoning effort |
| --- | --- | --- |
| gpt-6.1-sol | Available | low, medium, high, xhigh, max, ultra |
| gpt-6-sol | Available | low, medium, high, xhigh, max, ultra |
| gpt-6-luna | Available | low, medium, high, xhigh, max |
| gpt-6-astra | Available | low, medium, high, xhigh, max, ultra |
| Daybreak Blue / Red | Unavailable: absent from schema | — |
| GPT-Rosalind-Research | Unavailable: absent from schema | — |
| GPT-Image-2 | Unavailable: absent from schema | — |

If an ID is absent from the actual schema, it is unavailable for that tool.
A price table or chat picker does not show tool access or account access.
User policy does not include older generations in automatic selection. This exclusion does not mean technical unavailability.
For a subsequent explicit model request, keep the user's choice. Make sure that the requested model is available.

## Classify the work

This local method is not an official benchmark. Give each axis a score of 0, 1, or 2.

| Axis | 0 | 1 | 2 |
| --- | --- | --- | --- |
| U: uncertainty | Known contract or cause | Limited alternatives | Unknown cause or requirements |
| C: coupling | Local independent change | Known dependencies | Interactions between states or modules, or concurrency |
| R: error impact | Minor and easy to reverse | Material but contained | Severe or difficult recovery |
| V: verification gap | Direct reliable check | Partial or indirect check | Weak comparison basis or large coverage gap |

Use `S=U+C+R+V`.

- **Light**: `S≤2` and no axis equals 2.
- **Ordinary**: `S≤4` and `C,R<2`, except light work.
- **Complex**: all other work.
- **Exceptional**: concrete evidence shows that an otherwise adequate strong model cannot do the work satisfactorily.

A score alone cannot show that the exceptional class is necessary.
Do not use file count, reviewer role, or roadmap length to select the class.
Missing facts, access, or verification are blockers or limitations. They do not make the most expensive model necessary.

## Select who does the work

For the whole task, record `execution_mode=primary_only` or `execution_mode=delegate`.
The primary agent must make this decision once for the whole task.
Use task complexity to select a model and effort. Do not use it to select the number of agents.
Choose `delegate` if one or more of these conditions apply:

- Separate slices can run in parallel.
- A worker can do a required task that the primary cannot do.
- A separate review is required.
- The user requests agents.

For optional delegation, compare the total cost with primary-only work.
If both modes meet the task requirements, choose the lower-cost mode.
Choose `primary_only` when no delegation condition or explicit request applies and the primary agent can complete the task.
Keep the shared contract, integration, and final acceptance with the primary agent.
Honor an explicit request to delegate unless tool access, permissions, or budget limits prevent it.
Do not start an agent to classify the task or select models.
If an unknown fact can change this decision, find it before an agent starts.
Record the mode and its reason.
For `primary_only`, record the primary model and its effort.
For `delegate`, name each slice. Select a model and an effort level for each worker.
Forecast the total cost through acceptance.
Do not let a worker start another agent unless the primary agent assigns the role and slice.

## Find permitted configurations

Compare capability requirements with the actual tool's model IDs, supported efforts, and current-generation candidates above.
Keep explicit whitelists.
Before selection of a model, make sure that capability and tool availability are supported.
Use the effective rate reference defined in `Calculate the forecast`.
Do not automatically include older generations that user policy excludes.

Luna is an initial candidate for light work and limited ordinary work with direct acceptance.
Sol is an initial candidate for complex work.
These candidates do not give a universal model ranking. Comparable accepted work can change the permitted candidates.
[Official model information](https://learn.chatgpt.com/docs/models) gives 6.1 Sol for complex agent work and Luna for narrow, repeatable work.
First, examine 6.1 Sol as the strong candidate. Then compare 6 Sol with rates and acceptance evidence from comparable tasks.
Do not select a candidate that evidence already shows is inadequate.
Without evidence of insufficient capability, do not select Astra for unknown causes or missing fixtures.

Select only an effort available in the applicable tool:

- `none` or `minimal`: extraction.
- `low`: mechanical or local work.
- `medium`: ordinary reasoning.
- `high`: multiple hypotheses, state interactions, or substantial risk.
- `xhigh`, `max`, or `ultra`: demonstrated benefit only.

For code or tool work, start with at least `low`.
Delegation alone does not make more effort necessary.
If override support is unknown, use supported inheritance. Record the limitation.
Where `fork_turns` exists, a full `"all"` fork inherits settings and cannot use overrides.
For overrides, use supported `"none"` or numeric forks. Give the worker sufficient context.
Make sure that the tool has the parameters necessary for a proposed change to a follow-up configuration.

## Calculate the forecast

At the start of an assessment, read the saved rate reference.
If it is current and covers the model and payment mode, use it.
Otherwise, check only rates that are old or missing.
Update the saved reference after you check rates.
Use the updated reference for all model comparisons and assignments in this assessment.
Do not check the same rates again for each subagent.
For a long assessment, update the reference if its rates become more than 30 days old.
Also update it if a change trigger applies.
Use the environment's documentation rules for official sources.

Record the date, payment unit, account, payment mode, speed, and rates for permitted candidates.
Do not mix API USD, purchased credits, and included subscription allowance.
For API mode, get the applicable official API rates.
If rates, counters, or volumes are unknown, record `unknown` or a range with its basis.
Do not invent availability, success probabilities, exact costs, or precise savings.

For each participant, make separate estimates of noncached input, cached input, and billed output.
If the input counter includes cached input, use `T_uncached=total_input−T_cached`.
If the input counter gives only noncached input, do not subtract cached input again.
Include the primary agent, every subagent, and every descendant.
Include context transfers, review, integration, and a reserve for a limited number of retries.
Record assumptions, incomplete components, and the basis for the reserve. Do not use a universal fixed percentage.
Where applicable, include billed reasoning in billed output. Do not count it twice.
With rates per million, use:

`C_run=(T_uncached*P_input + T_cached*P_cached + T_billed_output*P_output)/1e6`

Use the applicable speed multiplier for each run.
Calculate the team forecast from all runs through acceptance. Include incurred task cost when it is within the accounting scope.
If a count is unknown, keep that uncertainty in the total. Unknown cost is not zero.
Compare forecast ranges for comparable permitted configurations. Keep the quality requirements.
The lowest token rate alone does not show the lowest total cost.
Select the least expensive adequate configuration within the budget.
If data are incomplete, record the qualitative basis and uncertainty. Do not claim an exact least-cost result.
An output-length limit does not limit total spend. A numerical forecast is not an enforced cost limit.

## Use the forecast before each start

Before a new or repeated agent start, examine the remaining work and cost.
Recheck the model and effort for each affected slice.
Use the whole-team forecast as a condition for the start decision.
After acceptance failure or cost beyond the forecast, make this decision again before further starts.
Compare the remaining forecast with the budget and quality requirements.
If the forecast has changed, record the cause and the revised basis.
A forecast overrun alone does not create a user-approval requirement.

For a strict user cap, record the unit, accounting scope, reserve, and remaining budget.
Before paid starts, make sure that shared accounting and enforcement can keep the work within that cap.
Per-agent counters and goal token budgets might not include the whole team.
Without shared accounting and enforcement, do not give an assurance of an exact monetary cap.
If you cannot show mandatory cap compliance, stop dependent paid starts until that condition changes.

## Accept and reselect

Record the class, its decisive axes, the execution mode, and its reason.
Record the primary model and effort.
For delegation, record each worker model and effort.
Record the cost basis, reserve, and acceptance criteria.
Use comparable accepted work as evidence. Do not treat it as a universal ranking.
Do not start a classification agent or make a benchmark for each choice.

After failure, find the cause: reasoning weakness, unclear contract, tool failure, test-system failure, or missing environment.
For deeper analysis, increase effort. For insufficient capability, select a model with sufficient capability.
Usually, change one parameter at a time. Do not select candidates again if evidence already shows insufficient capability.
Keep the least expensive configuration with an accepted result.
After a material change to the assessment, use this skill again.

Do not give model recommendations or questions before every task.
After an explanation, put recommendations for subsequent work at the end.
For a roadmap, include a model and effort for the whole roadmap and each step.
In each step, show any necessary change to the model or effort.
For creation or change of a test, include a model and effort recommendation for that test.
Do not write that a recommendation changed the primary chat's model.
