# Causal and branch analysis

Read the parts needed for the current audit. Scale the record to the system and risk.

## Build the scope from behavior

Start with the user's expected result and observable failure. Keep these separate from a suspected implementation cause. Obtain requirements from current contracts, configuration, domain rules, and confirmed user expectations. A historical implementation is a comparison, not proof of correct behavior.

Model the smallest useful area as states and transitions. For each entry point, enumerate reachable state/event pairs, their guards, outputs, state changes, and next states. Mark impossible combinations and the reason they are impossible. Add relevant invalid-event behavior and dependency failures. Record uncertainties rather than silently pruning them.

Select adjacent paths by shared dependencies: a cache writer and reader; multiple callers of one function; event registration and teardown; retry and cancellation; load and refresh; permission checks and error handling. Consider order and timing when state persists between operations. Bound sequences by an explicit lifecycle, depth, or scenario set. An unbounded event history cannot be covered by a finite test claim.

Use risk and symptom links to prioritize. If the scope is too large, retain the full known inventory and identify the subset selected for checking. Pairwise combinations can reduce work, but do not establish all higher-order or sequence interactions. Distinguish transition coverage, sequence coverage, input coverage, and runtime environment coverage.

## Construct and test explanations

For each symptom, build a chain:

`observable result <- failure mechanism <- trigger + enabling conditions <- upstream sources`

Label each link with evidence or an open question. A shared upstream dependency is a candidate shared cause only if a mechanism connects it to the symptoms. Compare with separate causes that happen to occur together. One confirmed defect can coexist with another.

For interacting causes, use a small timeline or causal graph when it clarifies event order, persistent conditions, and failed or missing barriers. Explain each edge. Do not replace evidence with the diagram. Examine system and process conditions rather than assigning blame to an individual.

For material candidates, record:

- What should be observable if the explanation is correct?
- Which alternative predicts a different result?
- What observation would contradict the explanation?
- Which variables or sources could confound the comparison?
- What is the smallest permitted check that separates these predictions?

Use existing logs, traces, call sites, state snapshots, and version comparisons first when sufficient. Match clocks and request or event identities before connecting records. An absent log is useful only if that event would reliably have been captured. A source path must be shown to execute before it explains runtime behavior.

When permitted, change one causal factor at a time in an isolated environment. Compare with an unchanged control. Check that the intervention reached the intended factor and did not alter a relevant confounder. For intermittent behavior, record attempts, outcomes, timing conditions, and uncertainty; zero observed failures does not prove impossibility. A changed reproduction rate can support a claim without proving the full chain.

Do not replay operations with external effects, alter live configuration, add logs, or inject failures under audit-only permission. A hypothetical intervention is a proposed check, not performed evidence. Preserve useful evidence before any separately authorized repair.

During an active incident, follow the authorized incident procedure. Urgent containment can precede full diagnosis when it is within that authority. Record what changed and preserve available evidence without delaying required containment. A successful containment action does not establish a root cause or validate a permanent fix.

## Interpret results and stop

Update the claim status when new evidence changes it. Keep rejected explanations with the observation that rejected them. If a failed check did not reach the target path, classify it as a check failure rather than a refutation.

Separate a symptom workaround from removal of the mechanism. For example, a reload can clear stale state while leaving the faulty invalidation path intact. A proposed correction must explain why the causal chain will break and which other consumers can be affected.

Stop when the agreed finite scope has been assessed to the stated evidence level, or when the remaining checks need unavailable access, permission, or artifacts. Report the unresolved gap and next useful check. Do not treat a tool limit as proof that the system is correct.

Passing checks show the observed results for those conditions. They do not establish absence of defects or fitness for user needs outside the assessed behavior.
