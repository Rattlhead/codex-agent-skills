---
name: root-cause-audit
description: Audit a bounded system area for defects and causal mechanisms across related symptoms, adjacent flows, and event branches. Use for evidence-based cause analysis and coverage reports; this skill does not authorize fixes.
---

# Root Cause Audit

Find the conditions and mechanisms that produce an observed failure. Test whether related symptoms have a shared upstream cause. Do not assume that they do. Deliver findings that distinguish evidence, explanation, coverage, and uncertainty. For provenance questions, read [sources.md](references/sources.md); routine use does not require a web refresh.

## Scope and permission

Default to an audit. Inspect sources and run authorized checks that do not change system state. Create requested report artifacts in the permitted location. Check the side effects of commands, fixtures, replays, and tests before running them. A command called a test can still change data or contact a live service.

Do not change source, configuration, instrumentation, persistent data, or external systems without permission for that change. A request to diagnose is not permission to fix. Use existing observations and isolated authorized experiments when a live intervention is not permitted. Report the resulting evidence limit.

Read applicable project instructions and the relevant source of truth. Use existing canonical task state and reports. Do not create a second tracker or edit `AGENTS.md`. Discover other skills only when the task needs them: coordination for delegated work, planning for substantial execution, focused diagnosis for an established repro, or verification for checks. Their availability is not a requirement to load them all. Do not import a fixed hypothesis count or a mandatory reproducible-failure gate into this area audit.

## Work from a finite audit boundary

1. State the requested area, expected behavior, observed symptoms, environment, and access limits. Identify the exact revision or artifact under examination. Include relevant dirty changes, runtime build identity, configuration, and data versions. Do not expose secrets.
2. Enumerate the in-scope entry points, states, events, valid reachable transitions, and important adjacent dependencies. Include invalid inputs, error paths, retries, cancellation, concurrency, and recovery where they affect the area. Record exclusions and unknowns. Use [methodology.md](references/methodology.md) when building this inventory or selecting causal probes.
3. Build a branch matrix from that inventory. Trace each symptom through its trigger, mechanism, contributing conditions, and possible upstream sources. Add nearby paths that share state, data, callbacks, services, or lifecycle boundaries. Expand only when evidence connects them to the scope; record each expansion.
4. Compare plausible explanations. For each material candidate, state a prediction, a distinguishing observation or safe experiment, and a result that would weaken it. Use controls and counterexamples. Prefer the next check that best separates the remaining explanations at reasonable cost.
5. Assign evidence status to each claim and coverage status to each branch. Reuse evidence while its revision, environment, assumptions, and measured path remain valid. Rerun only checks affected by changed conditions or unresolved questions.
6. Report the causal explanation, alternatives, coverage, limitations, and next action. Use [report-templates.md](references/report-templates.md) for larger audits. Record durable verified findings and prevention in an existing canonical source when that write is authorized; otherwise propose the exact addition in the report.

## Evidence and completion

Use `confirmed` when direct observations or controlled comparisons establish the claimed mechanism within the stated boundary. Use `supported` for a coherent explanation with material alternatives or links still untested. Use `unresolved` when evidence cannot distinguish explanations. Use `rejected` when a valid observation contradicts the candidate's prediction; state the conditions of rejection.

Static reachability, temporal order, correlation, a passing test, and removal of a visible symptom are each limited evidence. Explain what the check establishes. Trace the causal chain to a useful actionable boundary; do not claim an ultimate cause outside the evidence. Distinguish the initiating trigger, failure mechanism, contributing conditions, and organizational or process factors when supported.

An audit can finish with partial coverage, an intermittent symptom, or no reproduction. State what was observed, attempted, blocked, and not run. Give the most useful next discriminating check and its access needs. Do not invent certainty or continue a loop without a concrete information gain.

Do not call a sample, pairwise combination set, or selected path list exhaustive. Claim complete coverage only against an enumerated finite scope with evidence for each included branch. Name remaining gaps. Keep a mitigation separate from a proposed root fix; neither is validated by diagnosis alone. If fixes are later authorized, verify the mechanism, original symptoms, affected adjacent branches, and relevant regression behavior against the changed version.
