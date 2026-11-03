# Causal and branch analysis

Read the parts necessary for the current audit.
Adjust the record to the system and risk.

## Build the scope from behavior

Start with the user's expected result and observable failure.
Keep these separate from a suspected implementation cause.
Get requirements from current contracts, configuration, domain rules, and confirmed user expectations.
A historical implementation gives a comparison. It does not prove correct behavior.

Model the smallest useful area as states and transitions.
For each entry point, list reachable state/event pairs, their guards, outputs, state changes, and next states.
Mark impossible combinations and their reasons.
Add relevant invalid-event behavior and dependency failures.
Record uncertainties. Do not silently remove them.

Select adjacent paths by shared dependencies.
Examples include cache writers and readers, callers of one function, event registration and teardown, retries and cancellation, load and refresh.
Permission checks and error handling can also share dependencies.
If state persists between operations, examine their order and timing.
Limit sequences by an explicit lifecycle, depth, or scenario set.
A finite test claim cannot cover an unlimited event history.

Use risk and symptom links to set priorities.
If the scope is too large, keep the full known inventory.
Mark the selected subset for checks.
Pairwise combinations can decrease work. They do not prove all higher-order or sequence interactions.
Distinguish transition coverage, sequence coverage, input coverage, and runtime environment coverage.

## Construct and test explanations

For each symptom, build a chain:

`observable result <- failure mechanism <- trigger + enabling conditions <- upstream sources`

Give each link evidence or an open question.
A shared upstream dependency is a candidate shared cause only if a mechanism connects it to the symptoms.
Compare with separate causes that occur together.
One confirmed defect can coexist with another.

For interacting causes, use a small timeline or causal graph if it clarifies their relationship.
Include relevant event order, persistent conditions, and failed or missing barriers.
Give the reason for each edge.
Do not replace evidence with the diagram.
Examine system and process conditions. Do not give blame to an individual.

For material candidates, record:

- What should be observable if the explanation is correct?
- Which alternative predicts a different result?
- What observation would contradict the explanation?
- Which variables or sources could confound the comparison?
- What is the smallest permitted check that separates these predictions?

If sufficient, first use existing logs, traces, call sites, state snapshots, and version comparisons.
Before you connect records, compare their clocks and request or event identities.
A missing log is useful only if the logging system would reliably record that event.
Before a source path can account for runtime behavior, show that it runs.

When permitted, change one causal factor at a time in an isolated environment.
Compare with an unchanged control.
Make sure that the intervention reached the intended factor and did not change a relevant confounder.
For intermittent behavior, record attempts, outcomes, timing conditions, and uncertainty.
No observed failures does not prove that failure is impossible.
A changed reproduction rate can support a claim without proof of the full chain.

Under audit-only permission, do not replay operations with external effects.
Do not change live configuration, add logs, or inject failures.
A hypothetical intervention is a proposed check. It gives no evidence of a performed action.
Before a separately authorized repair, keep useful evidence.

During an active incident, obey the authorized incident procedure.
If that authority permits it, urgent containment can come before full diagnosis.
Record changes.
Keep available evidence without delay to mandatory containment.
A successful containment action does not prove a root cause or validate a permanent fix.

## Interpret results and stop

When new evidence changes a claim, update its status.
Keep rejected explanations with the observation that rejected them.
If a failed check did not reach the target path, report a check failure.
Do not report a refutation of the explanation.

Keep a symptom workaround separate from removal of the mechanism.
For example, a reload can clear stale state but leave the defective invalidation path unchanged.
For a proposed correction, give the reason that the causal chain will break.
List other consumers that the correction can change.

Stop when the agreed finite scope has evidence at the agreed level.
Also stop if necessary access, permission, or artifacts for remaining checks are unavailable.
Report the unresolved gap and next useful check.
Do not use a tool limit as proof that the system is correct.

Passing checks show the observed results for those conditions.
They do not prove that no defects exist or that behavior outside the audit meets user needs.
