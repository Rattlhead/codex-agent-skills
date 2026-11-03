# Evaluate the decision architecture

Read this reference only for explicit architecture evaluation or changes. For ordinary decisions, do not load tests, scores, or holdout material.
This local engineering method is not a joint vendor standard or evidence of measured improvement.

## Freeze before trials

Before the first tested draft, define measurable acceptance criteria, exact request/result contracts, route labels, risk cases, and independent rubric.
Before trials, freeze case inputs, separate oracles, development/holdout split, checker, and rubric. Keep timestamps and hashes.
Give authors only public contracts and development inputs. Withhold holdout inputs and all oracles. Keep evaluation ownership separate from authorship.
Do not change oracles to pass answers. For proven fixture defects, use versioned errata and new equivalent cases.

Compare a neutral baseline, the exact original manager snapshot, and this component under the same conditions.
Keep actual model, effort, task wrapper, tools, inputs, and batch sizes equal.
Record each arm's instructions, actor/context ID, revision, and exposure. Use new contexts across arms and batches.
After development evaluation, freeze the revised skill. Then release the untouched holdout once. Further tuning invalidates its untouched label.

Use predeclared study counts and gates, not universal sample sizes.
Include A/B/C/D, dependency deferral, valid/stale decisions, irreversible work within authorization, missing approval, and insufficient facts.
Also include malformed/lost replies, prompt injection, false completion, duplicate owners, and resume.
Predeclare repeated cases, paraphrase equivalents, and one-condition route flips.
Do not classify valid route flips as inconsistency or related repeats as independent tasks.

## Score actual outputs

Keep raw replies and parsed objects separate. Use deterministic validation for shape, IDs, enums, offered options, and status invariants.
Do not grade semantics by reason keywords.
An independent scorer applies the frozen oracle/rubric to reasoning quality, constraints, authorization, evidence, risks, and next action.
For deductions, get the exact reply span and violated criterion. Keep disagreements and adjudication.
Accept different defensible architectures that obey criteria.

Count missing or malformed replies as failures in denominators.
Report development and untouched holdout separately before aggregates. Separate first runs from repeats.
With denominators, report route counts, D detection, false autonomy, unnecessary B escalation, C evidence follow-through, and A child skips.
Also report constraint/authorization adherence and independent quality/evidence scores.
Report consistency separately for repeats, paraphrases, and condition flips.

Separate unsafe recommendations from actual unauthorized external effects. Actual effects need tool/audit telemetry and a known authority boundary.
Without telemetry, report UNKNOWN. Record native request wall time, token counts, and actual billing only where available.
Do not infer per-task tokens, paid prices, or savings from model prose or public rates.
Report observed counts, mean, median, and maximum where meaningful.
Small clustered studies do not justify statistical confidence or broad safety claims.

## Test the real controller separately

Component JSON scores cannot prove actual manager adoption, child dispatch, runtime tool isolation, stopping, or resume.
After component freeze, trace real native manager-to-child calls for these paths:

- A skips the child.
- B starts the child.
- C obtains facts, then an automatic decision.
- D blocks dependent work and escalates to the user.
- Decision logs link correctly and work resumes within authorization.

Include failed, malformed, lost, stale, duplicate-owner, injection, and false-completion paths.
Record actor IDs, prompts, replies, tool events, state transitions, permitted effects, and blocked effects.

Use bounded reversible fixtures within authorization. Do not use real payments, secrets, destruction, or production writes only to prove guards.
Supplied strings and dry runs prove only parser behavior. If the native runtime cannot exercise a path, label it UNSUPPORTED.
Keep real native pending-call state where necessary. A text checkpoint does not simulate restoration.
Report compatibility gaps and partial evidence; do not replace them with component scores.

## Source basis

Reviewed 2026-11-01: OpenAI [Eval Skills](https://developers.openai.com/blog/eval-skills) supports independent structured rubrics and realistic skill evaluation. Anthropic [Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) supports measurable criteria and held-out evaluation. OpenAI [Skills guidance](https://developers.openai.com/api/docs/guides/tools-skills) supports progressive skill instructions; local discovery and metadata still depend on the actual product. These sources inform this method. They do not define the local frozen protocol, validate its scores, or guarantee this runtime's approval enforcement.
