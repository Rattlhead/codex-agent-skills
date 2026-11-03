---
name: root-cause-audit
description: Проверять причины сбоев в указанной области системы, связанные симптомы, смежные потоки и ветви событий. Применять для анализа причин по доказательствам и отчёта о покрытии. Аудит не разрешает исправления.
---

# Root Cause Audit

Find the conditions and mechanisms that cause an observed failure.
Test whether related symptoms have a shared upstream cause.
Do not assume that they do.
Give findings that distinguish evidence, explanation, coverage, and uncertainty.
For provenance questions, read [sources.md](references/sources.md).
Do not refresh web sources for routine use without a reason.

## Scope and permission

Default to an audit.
Examine sources.
Run authorized checks that do not change system state.
Put requested report artifacts in the permitted location.
Before you run commands, fixtures, replays, or tests, examine their side effects.
A command called a test can still change data or contact a live service.

Do not change source, configuration, instrumentation, persistent data, or external systems without permission for that change.
A diagnosis request does not give permission for fixes.
If live intervention is not permitted, use existing observations and isolated authorized experiments.
Report the resulting evidence limit.

Read applicable project instructions and the authoritative source for the subject.
Use the existing task record and reports.
Do not make a second tracker.
Do not edit `AGENTS.md`.
Find other skills only when they are necessary for the task.
Use coordination for delegated work, planning for substantial execution, diagnosis for a known reproducible failure, or verification for checks.
Loading all available skills is not necessary.
Do not impose a fixed hypothesis count.
Do not make reproduction of a failure a prerequisite for this area audit.

## Work from a finite audit boundary

1. Record the requested area, expected behavior, observed symptoms, environment, and access limits. Record the exact revision or artifact under examination. Include relevant uncommitted changes, runtime build identity, configuration, and data versions. Do not expose secrets.
2. List the entry points, states, events, valid reachable transitions, and important adjacent dependencies within scope. Include invalid inputs, error paths, retries, cancellation, concurrency, and recovery where they affect the area. Record exclusions and unknowns. For the inventory or causal checks, use [methodology.md](references/methodology.md).
3. Build a branch matrix from that inventory. Trace each symptom through its trigger, mechanism, contributing conditions, and possible upstream sources. Add nearby paths that share state, data, callbacks, services, or lifecycle boundaries. Expand only when evidence connects them to the scope; record each expansion.
4. Compare plausible explanations. For each material candidate, give a prediction, a distinguishing observation or safe experiment, and a result that would weaken it. Use controls and counterexamples. Select the next check that best separates the remaining explanations at reasonable cost.
5. Give each claim an evidence status. Give each branch a coverage status. Use evidence again while its revision, environment, assumptions, and measured path remain valid. Do checks again only for changed conditions or unresolved questions that affect them.
6. Report the causal explanation, alternatives, coverage, limitations, and next action. For larger audits, use [report-templates.md](references/report-templates.md). If permitted, save verified findings and prevention in the existing authoritative source. Otherwise, propose the exact addition in the report.

## Evidence and completion

Use `confirmed` when direct observations or controlled comparisons show the claimed mechanism within the stated boundary.
Use `supported` for a coherent explanation with material alternatives or links still untested.
Use `unresolved` when evidence cannot distinguish explanations.
If a valid observation contradicts the candidate's prediction, use `rejected`.
Give the conditions of rejection.

Static reachability, temporal order, correlation, a passing test, and removal of a visible symptom each give limited evidence.
Tell what the check shows.
Show the causal chain to a useful boundary for action.
Do not give an ultimate cause without evidence for it.
When evidence supports them, distinguish the initiating trigger, failure mechanism, contributing conditions, and organizational or process factors.

An audit can finish with partial coverage, an intermittent symptom, or no reproduction.
Record observations, attempts, blocked checks, and checks not run.
Give the most useful next discriminating check and its access needs.
Do not invent certainty.
Do not continue a loop without a concrete information gain.

Do not call a sample, pairwise combination set, or selected path list exhaustive.
Give a statement of complete coverage only for a listed finite scope with evidence for each included branch.
Name remaining gaps.
Keep a mitigation separate from a proposed root fix.
Diagnosis alone does not validate either one.
If fixes are later authorized, examine the mechanism, original symptoms, affected adjacent branches, and relevant regression behavior.
Use the changed version for these checks.
