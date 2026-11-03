# Defect correction acceptance

Use this procedure to plan proposed defect corrections or accept authorized corrections.
For a proposal or plan, use the regression, exception, and affected-boundary requirements below as future acceptance criteria.
Mark future checks `not run`.
Planning gives no permission for fixes or check execution.
A full comprehensive audit or its coverage matrix is not necessary for a focused fix.
Use existing task state and acceptance criteria.
This procedure gives no permission to edit source, tests, fixtures, instrumentation, configuration, data, or infrastructure.

## Diagnose before correcting

Before fixes, use the relevant `root-cause-audit` guidance to find the trigger, mechanism, contributing conditions, and alternatives.
Group defects only when evidence supports a shared mechanism.
Where applicable, use one coherent correction for that mechanism.
Do not mask symptoms, add competing fixes, or duplicate a correction without technical evidence.

For an explicitly authorized temporary mitigation, record its limits, unresolved cause, and follow-up check.
Keep it separate from a final root fix.
Do not report the root cause as resolved because the visible symptom is gone.

<a id="establish-regression-evidence"></a>
## Regression evidence

For a confirmed bug, use a reproducible regression check by default.
The check must fail on the version before the fix for the expected reason.
It must pass on the corrected version.
If an existing test finds the defect, use it again.
Authorization that covers new or changed tests or fixtures is necessary.
An audit request alone does not give that authorization.
For work other than code, use a deterministic before/after comparison of the relevant behavior or artifact.

If the prior version is unavailable or unsafe to recreate, record the exception and its evidence.
If reproduction is infeasible (impossible or impractical), record the exception and its evidence.
If the correction is trivial, also record the exception and its evidence.
For every exception, run a mandatory focused acceptance check.
Record what that check cannot prove.
Do not invent a historical failing result.
Do not weaken a check to get a passing result.
An existing observation can support a defect without proof that a new test failed before the fix.

Keep authorized software regression tests for future runs through the existing runner and CI where applicable.
Use existing test discovery and commands.
Do not invent CI.
Do not make new infrastructure mandatory or change infrastructure without authorization.

<a id="verify-the-affected-boundary"></a>
## Examine the affected boundary

Select adjacent and integration checks from the changed mechanism, contracts, shared state, and risk.
On the exact final revision, test the original failure, corrected behavior, and affected adjacent flows at the applicable boundary.
Keep root-cause findings, remediation status, and verification evidence distinct.

If you can run the behavior, get observable UI/UX evidence from the rendered artifact or running UI.
Use the relevant views and sizes.
Unit or static checks do not prove runtime or visual acceptance.
If necessary UI/UX evidence is unavailable, report that acceptance as partial.
Passing tests do not remove the gap.

Use valid evidence again for unchanged inputs and dependencies.
Do checks again only for a changed dependency, failure, contradiction, or named gap.
Without such a reason, do not do the full suite again.
Report the accepted scope, final revision, checks, exceptions, and remaining limits.
Do not give a statement of broader coverage.
