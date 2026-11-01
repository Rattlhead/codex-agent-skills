# Evaluate the decision architecture

Read this reference only for explicit architecture evaluation or changes. Ordinary decisions do not load tests, scores, or holdout material. This procedure is a local engineering method, not an official joint vendor standard or evidence of measured improvement.

## Freeze before trials

Define measurable acceptance criteria, exact request/result contracts, route labels, risk cases, and an independent rubric before drafting the first tested skill. Freeze case inputs, separate oracles, development/holdout split, checker, and rubric before trials. Preserve timestamps and hashes. The skill author may receive public contracts and development inputs only; withhold holdout inputs and all oracles. Keep evaluation ownership separate from authorship. Never change an oracle to make an answer pass. Use a versioned erratum and a fresh equivalent case for a proven fixture defect.

Compare a neutral baseline, the exact original manager snapshot, and this component under the same actual model, effort, task wrapper, tools, inputs, and batch sizes. Record each arm's real instructions, actor/context ID, revision, and exposure. Use fresh contexts across arms and batches. Freeze the revised skill after development evaluation, then release the untouched holdout once. Further tuning cannot retain that holdout's untouched label.

Use the study's own predeclared counts and gates, not a universal sample size from this skill. Include A/B/C/D, dependency deferral, valid and stale prior decisions, authorized irreversible work, missing approval, insufficient facts, malformed or lost worker replies, prompt injection, false completion, duplicate owners, and resume. Predeclare repeat cases, paraphrase equivalents, and one-condition route flips. Do not call a valid route flip an inconsistency or treat repeated related cases as independent tasks.

## Score actual outputs

Preserve raw replies and parsed objects separately. Use a deterministic checker for shape, IDs, enums, offered options, and status invariants. Do not use reason keyword matching as semantic grading. An independent scorer applies the frozen oracle and rubric to reasoning quality, constraints, authorization, evidence, risks, and the next action. Require a concrete reply span and violated criterion for deductions. Retain disagreement and adjudication. Accept multiple defensible architectures when they satisfy criteria.

Count missing or malformed replies as failures in denominators. Report development and untouched holdout separately before aggregates, and first runs separately from repeats. Report route counts, D detection, false autonomy, unnecessary B escalation, C evidence follow-through, A child skips, constraint and authorization adherence, and independent quality/evidence scores with their denominators. Report consistency for repeats, paraphrases, and condition flips separately.

Distinguish an unsafe recommendation from an actual unauthorized external effect. Actual effects require tool/audit telemetry and a known authority boundary; absent telemetry means UNKNOWN. Record native request wall time, native token counts, and actual billing only where exposed. Do not infer per-task tokens, prices paid, or savings from model prose or public rate estimates. Report observed counts, mean, median, and maximum where meaningful. A small clustered study does not justify statistical confidence or broad safety claims.

## Test the real controller separately

Component JSON scores cannot establish actual manager adoption, child dispatch, runtime tool isolation, stopping, or resume. After component freeze, trace real native manager-to-child calls for A skip, B child, C fact check then automatic decision, D dependent block and user-facing escalation, decision log linkage, and resumed authorized work. Include failed, malformed, lost, stale, duplicate-owner, injection, and false-completion paths. Record actor IDs, prompts, replies, tool events, state transitions, permitted effects, and blocked effects.

Use bounded reversible authorized fixtures. Do not use real payment, secrets, destruction, or production writes merely to prove a guard. Supplied reply strings and dry runs can establish parser behavior only. Label a path UNSUPPORTED when the native runtime cannot exercise it. Preserve real native pending-call state where required; a text checkpoint does not simulate restoration. Report compatibility gaps and partial evidence without replacing them with a component score.

## Source basis

Reviewed 2026-11-01: OpenAI [Eval Skills](https://developers.openai.com/blog/eval-skills) supports independent structured rubrics and realistic skill evaluation. Anthropic [Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) supports measurable criteria and held-out evaluation. OpenAI [Skills guidance](https://developers.openai.com/api/docs/guides/tools-skills) supports progressive skill instructions; local discovery and metadata still depend on the actual product. These sources inform this method. They do not define the local frozen protocol, validate its scores, or guarantee this runtime's approval enforcement.
