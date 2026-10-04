---
name: task-model-router
description: Select supported model and reasoning effort for a task or slice using complexity, capability, rates, workload, and total cost through acceptance. Use for model recommendations, budget decisions, or assignments; works without a manager and never spawns agents for classification.
---

# Task Model Router

Apply independently to each task/slice. Preserve explicit user choices, quality, and budget; disclose an unavailable explicit model instead of silently substituting. Never change global defaults, account, credentials, or tariff without authorization. Recommendations do not switch the current chat.

## Таблица цен / Verified prices

Verified **2026-10-04**: Codex **Standard purchased credits per 1M tokens**, from [official token rates](https://learn.chatgpt.com/docs/pricing#token-rates). Only current-generation routing candidates are retained.

| Model ID | Input | Cached input | Output |
| --- | ---: | ---: | ---: |
| gpt-6-luna | 2.5 | 0.25 | 12.5 |
| gpt-6.1-sol | 50 | 2.5 | 250 |
| gpt-6-sol | 50 | 5 | 250 |
| gpt-6-astra | 250 | 25 | 1250 |

Purchased-credit speed multipliers: Fast ×2; Astra Ultrafast ×6, where supported. Included subscription allowance has different multipliers; this table cannot calculate it. API USD uses separate [official API pricing](https://developers.openai.com/api/docs/pricing). Do not convert credits to USD without an applicable verified account rate.

## Доступность субагентам / Subagent availability

Observed **2026-10-04** in this session's `collaboration.spawn_agent` schema; not an account-wide guarantee. Recheck the actual spawning tool before each assignment; current schema overrides this snapshot.

| Model | Subagent model override | Supported reasoning effort |
| --- | --- | --- |
| gpt-6.1-sol | Available | low, medium, high, xhigh, max, ultra |
| gpt-6-sol | Available | low, medium, high, xhigh, max, ultra |
| gpt-6-luna | Available | low, medium, high, xhigh, max |
| gpt-6-astra | Available | low, medium, high, xhigh, max, ultra |
| Daybreak Blue / Red | Unavailable: absent from spawn schema | — |
| GPT-Rosalind-Research | Unavailable: absent from spawn schema | — |
| GPT-Image-2 | Unavailable: absent from spawn schema | — |

Any other ID absent from the actual spawn schema is unavailable for that tool; presence in pricing or a chat picker proves neither spawn access nor account access. Older generations are excluded from automatic routing by user policy, even if a tool still accepts them; exclusion is not technical unavailability. Preserve a subsequent explicit user model request and verify its availability.

## Classify

This local heuristic is not an official benchmark. Score four axes 0/1/2:

| Axis | 0 | 1 | 2 |
| --- | --- | --- | --- |
| U: uncertainty | Known contract/cause | Bounded alternatives | Unresolved cause/requirements |
| C: coupling | Local independent change | Known dependencies | Interacting states/modules, concurrency |
| R: error impact | Minor, easily reversed | Material but contained | Severe or difficult recovery |
| V: verification gap | Direct reliable check | Partial/indirect check | Weak oracle, major coverage gap |

S=U+C+R+V. **Light:** S≤2 and no axis=2. **Ordinary:** S≤4 and C,R<2, excluding light. **Complex:** otherwise. **Exceptional:** only concrete evidence that an adequate strong model is insufficient, never score alone. File count, reviewer role, and roadmap length do not determine class. Missing required facts/access/verification are blockers or limitations, not grounds for the most expensive model.

## Establish eligibility

Intersect capability needs with the **actual tool schema's model IDs and per-model efforts** and current-generation candidates above. Respect explicit whitelists. New generations require verified capability, rates, and tool eligibility before selection; do not restore removed legacy candidates automatically.

Luna may handle light and bounded ordinary work with direct acceptance; Sol is a complex-work candidate. These are starting candidates, not a universal ranking: comparable accepted work can change eligibility. Official [guidance](https://learn.chatgpt.com/docs/models) positions 6.1 Sol for complex/agentic work and Luna for narrow repeatable work. Evaluate 6.1 Sol before 6 Sol as the initial strong candidate, then compare rates and comparable same-task acceptance evidence. Skip proven inadequate candidates. Exceptional requires the insufficiency evidence above; unknown causes or missing fixtures do not justify Astra.

Choose supported effort: none/minimal for extraction; low for mechanical/local work; medium for ordinary reasoning; high for multiple hypotheses, interacting states, or substantial risk. Code/tool work starts at least low. xhigh/max/ultra require demonstrated benefit; delegation alone warrants no increase. If overrides are unknown, use supported inheritance and disclose limitations. Where `fork_turns` exists, full `"all"` forks inherit settings and cannot override; use supported `"none"` or numeric forks with sufficient context. Verify whether follow-up configuration can change.

## Compare cost through acceptance

Use the price table above before the first assignment/recommendation in a task. Reuse its verified snapshot; refresh after one day or account/tariff/model/speed changes. Check official sources under environment documentation rules. Keep fresh data in memory or agreed task scratch; never automatically rewrite global files.

Record date, payment unit, account/mode, speed, and a correct rate table for eligible candidates. Never mix API USD, purchased credits, and included subscription allowance. Fetch official API rates for API mode. Unknown rates/counters/volume remain `unknown` or qualitative; invent no availability, success probabilities, or precise savings.

Estimate nonoverlapping ranges for noncached input, cached input, and billed output; include billed reasoning in output where applicable **without double counting**. With rates per million, `C_run=(T_uncached*P_input + T_cached*P_cached + T_billed_output*P_output)/1e6`. Compare forecast ranges for comparable eligible candidates while preserving the quality gate. Total cost includes execution/context transfers + manager + review + bounded retry reserve and incurred task spend when in scope. Lowest token rate alone is insufficient. Select the cheapest adequate configuration within budget; incomplete data require a stated qualitative basis/uncertainty, not an exact cheapest-cost claim. A numerical forecast is not a hard cap without an enforcing limiter.

For strict caps define unit/accounting scope and reserve; check remaining budget before paid launches. Per-agent counters and goal token budgets may not cover the team. Without shared accounting/enforcement, an exact monetary cap cannot be guaranteed. If compliance is mandatory and unprovable, block dependent paid launches until that condition changes; unknown spending is not zero.

## Accept and reassess

Record class/decisive axes → eligible model/effort → cost basis/reserve → acceptance gate. Comparable accepted work is evidence, never a universal ranking; create no classification agent or per-choice benchmark.

On failure distinguish reasoning weakness from unclear contract, tool/harness failure, or missing environment. Increase effort for deeper tracing, model for insufficient capability; normally change one parameter, skip proven inadequate intermediates, retain the cheapest accepted configuration. Reapply on material reassessment.

Do not ask or recommend models before every task. Put recommendations for subsequent execution after explanation. Roadmaps include model/effort for the whole roadmap and each step, marking changes. Creating/changing a test requires its own model/effort recommendation. Never claim a recommendation changed the main chat's model.
