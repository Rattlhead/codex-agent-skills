---
name: task-model-router
description: Выбирай модель и уровень усилия для задачи или её части. Используй для выбора модели, бюджета или делегирования. Сравнивай возможности и полную стоимость до приёмки. Сохраняй роль руководителя, делегирование по умолчанию и исключение для короткой цели целиком. Не запускай субагентов только для оценки задачи.
---

# Task Model Router

Use this skill independently for each task or slice. Keep explicit user choices, quality requirements, and budgets.
If the requested model is unavailable, record the limitation. Do not silently substitute another model.
Without authorization, do not change global defaults, account, credentials, or tariff. A recommendation does not change the current chat's model.

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

Before a cost estimate, read the saved [rate reference](references/rates.md).
It contains rates, speed multipliers, payment units, sources, and group dates.
A rate group identifies a model and payment mode. A multiplier group identifies a speed and payment mode.
Without a change trigger, use each necessary group without online lookup.
Its own check date must be no more than 30 days old.
If a necessary group is missing, undated, or older than 30 days, get current values from official sources.
Also get current values from official sources for affected necessary groups when any of these triggers applies:

- The user reports a change.
- An official source shows a rate change.
- The payment mode changes.

Update `references/rates.md` only with values validated against those sources and their actual group check dates.
Assign a check date only after validation of every value in that group.
Split partially validated groups. Keep other values and dates.
Use one effective rate reference for all comparisons and assignments in this assessment.
Do not refresh unchanged current groups per subagent without a change trigger.
If the directory is read-only, save one dated assessment rate record. Report that the saved reference could not be updated.
Use the environment's documentation rules for official sources.
For API USD, use the applicable [official API rates](https://developers.openai.com/api/docs/pricing).
Do not calculate API USD from credits.

## Subagent availability

Observation date: **2026-10-27**. Source: this session's `collaboration.spawn_agent` schema.
This observation is for this runtime only. It gives no assurance of availability for an account or another runtime.
Before each assignment, examine the actual delegation tool schema. If it differs from this table, use the schema.

| Model | Model override | Supported reasoning effort |
| --- | --- | --- |
| gpt-6.1-sol | Available | low, medium, high, xhigh, max, ultra |
| gpt-6.1-terra | Available | low, medium, high, xhigh, max, ultra |
| gpt-6-sol | Available | low, medium, high, xhigh, max, ultra |
| gpt-6-luna | Available | low, medium, high, xhigh, max |
| gpt-6-astra | Available | low, medium, high, xhigh, max, ultra |

If the actual schema lists permitted model IDs or efforts, keep those limits.
If it does not list them, find other applicable evidence of support in the actual tool and environment.
A parameter with type `string` alone does not prove support for a model ID or effort.
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
- **Exceptional**: concrete evidence shows that an otherwise sufficient strong model cannot do the work satisfactorily.

A score alone cannot show that the exceptional class is necessary.
Do not use file count, reviewer role, or roadmap length to select the class.
Missing facts, access, or verification are blockers or limitations. They do not make the most expensive model necessary.

## Select who does the work

Record one whole-task decision: `execution_mode=primary_only` or `execution_mode=delegate`.
The primary is the director by default. Start from `delegate`; primary execution needs the confirmed short-whole-goal exception below.
Reassess after a material change or new independent-review requirement. Use complexity for configuration selection, not agent count.

First, examine primary capability for every necessary slice against requirements, observed failures, and relevant capability evidence.
Model names, raw prices, and unknown facts alone cannot prove insufficient capability.
A known capability gap needs no failed attempt first.
If any necessary slice exceeds primary capability, select `delegate`. Select and start a sufficient available worker through the applicable delegation workflow.
This applies to a single coherent slice. A recommendation alone is insufficient; cost cannot justify known insufficient primary execution.
Keep coordination and acceptance with the primary. Do not add a manager layer.

Next, examine expected whole-goal context, even if primary capability is sufficient.
Select `delegate` for substantive stage sequences, such as investigation, implementation, and integration, or substantial research, artifact, dependency, or verification context.
Decide before full research. Do not wait for context overload. Describe context burden qualitatively, without invented numerical thresholds.
A long connected chain is not a short goal. Assign it to one worker where permitted by scope and permissions.
Also select `delegate` for mandatory separate review or explicit user agent requests. Possible parallelism alone does not make delegation necessary.

Use `primary_only` only after affirmative assessment of all these conditions:

- The entire goal is short and self-contained.
- Primary capability is sufficient.
- Context is bounded.
- There is no substantive stage sequence or other required delegation.

Supporting inspection, a small patch, and focused verification within one short local correction do not themselves constitute substantive stages.
Do not extract a pending substep from an already delegated larger goal to claim the exception.
Do not count commands or assign one worker per action.
If eligibility is uncertain, use minimal bounded clarification or discovery. Do not start a classification agent.
Uncertainty grants no primary-execution permission. If the exception remains unconfirmed, keep `delegate`.

Optimize cost only among eligible configurations. After validation of the exception, compare optional delegation with primary execution through acceptance.
Price alone cannot validate the exception or make primary execution the default. If both modes qualify, select the lower-cost mode.
For unknown costs, record uncertainty and qualitative evidence. Do not claim a cost advantage without evidence.
If optional delegation has no supported cost advantage and the whole goal qualifies, select `primary_only`.

Keep explicit user restrictions, permissions, and budgets. If they prevent a required worker configuration or start, record the blocker.
Stop dependent work. Continue independent work within authorization, selected mode, and role.
Do not substitute insufficient primary execution, change the global model, or expand authorization.
The primary keeps responsibility for the shared contract, integration coordination, and final acceptance.
In `delegate`, workers execute integration. In `primary_only`, the primary performs work and integration.

Before a start, obtain facts necessary for task correctness or mandatory budget compliance.
Record other unknowns and their decision effects without invented costs.
Record the mode and basis, primary model and effort, and each delegated slice's worker model and effort.
Forecast total cost through acceptance. Do not start an agent only for classification or model selection.
Let workers delegate only when the primary assigns that role and slice.

## Find permitted configurations

Compare capability requirements with the actual tool's model IDs, supported efforts, and current-generation candidates above.
Keep explicit whitelists.
Before selection of a model, make sure that capability and tool availability are supported.
Use the effective rate reference from `Verified prices`.
Do not automatically include older generations that user policy excludes.

Luna is an initial candidate for focused, repeatable work with direct acceptance.
For complex work, compare 6.1 Sol with Astra against capability, cost, and acceptance evidence.
For writing, visual understanding, or computer use, consider 6.1 Terra when the applicable runtime offers it.
Assign a model and effort to a subagent only after confirming that the delegation tool and environment support both.
Use the current schema and, where it does not list permitted values, other applicable evidence as specified in `Subagent availability`.
These candidates do not give a universal model ranking. Comparable accepted work can change the permitted candidates.
[Official model information](https://learn.chatgpt.com/docs/models) describes Astra for the most demanding work and 6.1 Sol for complex cost-sensitive work.
It describes Terra for writing, visual, or computer-use work, and Luna for focused repeatable tasks.
Compare 6 Sol with rates and acceptance evidence from comparable tasks when the runtime offers it.
Do not select a candidate that evidence already shows is insufficient.
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

Use the effective rate reference from `Verified prices`.

Record the date, payment unit, account, payment mode, speed, and rates for permitted candidates.
Do not mix API USD, purchased credits, and included subscription allowance.
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
Select the least expensive sufficient configuration within the budget.
If data are incomplete, record the qualitative basis and uncertainty. Do not claim an exact least-cost result.
An output-length limit does not limit total spend. A numerical forecast is not an enforced cost limit.

## Use the forecast before each start

Before a new or repeated agent start, examine the remaining work and cost.
Recheck the model and effort for each affected slice.
Use the whole-team forecast as a condition for the start decision.
After acceptance failure or cost beyond the forecast, make this decision again before further starts.
Compare the remaining forecast with the budget and quality requirements.
If the forecast has changed, record the cause and the revised basis.
A forecast overrun alone does not make user approval necessary.

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
If evidence shows insufficient capability, revise the estimate and retry allocation. A low initial estimate does not justify another insufficient attempt.
Include prior spend, remaining work, handoff, and acceptance in the revised forecast. Continue the same slice within existing permissions.
Do not increase without limit or jump to the most expensive model.
If a sufficient attempt exceeds an explicit cap, stop dependent paid starts. Ask only for the necessary cap change.
Usually, change one parameter at a time. Do not select candidates again if evidence already shows insufficient capability.
Keep the least expensive configuration with an accepted result.
After a material change to the assessment, use this skill again.

Do not give model recommendations or questions before every task.
After an explanation, put recommendations for subsequent work at the end.
For a roadmap, include a model and effort for the whole roadmap and each step.
In each step, show any necessary change to the model or effort.
For creation or change of a test, include a model and effort recommendation for that test.
Do not write that a recommendation changed the primary chat's model.
