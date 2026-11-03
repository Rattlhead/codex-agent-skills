# Defect correction acceptance

Use this procedure to plan proposed defect corrections or accept authorized corrections. For a proposal or plan, carry the relevant regression, exception, and affected-boundary requirements below as future acceptance criteria. Mark future checks `not run`; planning grants no permission to fix or execute checks. A focused fix needs neither a full comprehensive audit nor its coverage matrix. Use existing task state and acceptance criteria. This procedure grants no permission to edit source, tests, fixtures, instrumentation, configuration, data, or infrastructure.

## Diagnose before correcting

Use the relevant `root-cause-audit` guidance to establish the trigger, mechanism, contributing conditions, and alternatives before fixes. Group defects only when evidence supports a shared mechanism. Assign one coherent correction for that mechanism where appropriate. Do not mask symptoms, add competing fixes, or duplicate a correction without technical grounds.

An explicitly authorized temporary mitigation must state its limits, unresolved cause, and follow-up check. Keep it separate from a final root fix. Do not report the root cause as resolved because the visible symptom is gone.

## Establish regression evidence

For a confirmed bug, default to a reproducible regression check that fails on the pre-fix version for the expected reason and passes on the corrected version. Reuse an existing test when it already detects the defect. Creating or changing tests or fixtures requires authorization that covers them; an audit request alone is insufficient. For non-code work, use a deterministic before/after comparison of the relevant behavior or artifact.

If a prior version is inaccessible or cannot be safely recreated, reproduction is infeasible, or the correction is trivial, record the evidence-based exception. Run a mandatory focused acceptance check and state what it cannot establish. Do not fabricate a historical red result or weaken a check to obtain green. An existing observation can support a defect without proving that a new test failed before the fix.

Preserve authorized software regression tests for future runs through the existing runner and CI when applicable. Use established test discovery and commands. Do not invent CI, require new infrastructure, or change it without authorization.

## Verify the affected boundary

Select adjacent and integration gates from the changed mechanism, contracts, shared state, and risk. Verify the original failure, corrected behavior, and affected neighboring flows on the identified final revision at the appropriate boundary. Keep root-cause findings, remediation status, and verification evidence distinct.

UI/UX claims require observable evidence from the rendered artifact or running UI at the relevant views and sizes when the behavior can be exercised. Unit or static checks do not establish runtime or visual acceptance. If required UI/UX evidence is unavailable, report that acceptance as partial; green tests do not close the gap.

Reuse valid evidence for unaffected inputs and dependencies. Repeat checks only for a changed dependency, failure, contradiction, or named gap. Do not rerun the full suite without such a reason. Report the accepted scope, final revision, checks, exceptions, and remaining limits without claiming broader coverage.
