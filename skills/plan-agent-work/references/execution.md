# Execution, evidence, and recovery

Use this reference only within the authorization selected in SKILL.md.

## Maintain one state source

Find the canonical plan package and its status authority, normally the index. Do not create a second manual queue. Designate one status writer; workers submit receipts to that writer. Keep derived views synchronized or regenerate them from the authority. In delegate mode the manager assigns plan-file updates to existing workers within their roles; do not start a new worker only for bookkeeping. Assign non-overlapping file ownership or serialize edits to a shared file.

Write the output artifact, then record its evidence receipt in the relevant step file before the status writer records completion in the index. Accept the required proof before marking done. Batch independent file writes when safe; receipt-to-completion updates are dependent. If a write or reply fails, inspect which artifacts, receipts, and index changes actually exist. Repair the incomplete update without inventing proof or blindly repeating external actions. An index entry alone cannot establish completion.

Use its executor/context map when work becomes ready. Validate the affected assignment and current manager/router conditions before dispatch, rather than rebuilding all assignments or loading each owner's investigation into director context. Record actual starts separately from planned owner labels. Keep production and integration with workers in delegate mode.

Use the project's labels. Their logical meanings should distinguish waiting, in progress, review, done, blocked, and cancelled. A ready task has all preconditions met. A done task has accepted output and the required proof. A blocked task states the blocker and the affected scope. Continue unblocked authorized work. Do not treat a timeout, lost response, or exhausted budget as completion.

Task state is separate from check outcome. Record checks as success, failure, not run, or unknown. Do not translate unknown into success.

## Accept evidence at the right scope

For code, use relevant project checks. Choose TDD according to the user request, project rules, and risk. Do not require new tests for every trivial document edit. For UI work, verify actual user behavior: initial state, action, and expected visible result. Static inspection alone does not establish that flow. For research, inspect source content that supports the claim, not only a title or search snippet. For other artifacts, use the contract's reproducible content or visual checks.

Tie evidence to the actual content, including relevant dirty changes or a content hash, and to inputs, environment, and criterion. A commit identifier alone is insufficient. Reuse checks when the relevant content and conditions remain unchanged and the evidence is still valid. Rerun affected checks after relevant changes, for a named unresolved risk, or when project rules require them. Do not rerun unchanged work merely because another stage begins.

After separate branches join, perform the planned integration task and end-to-end flow checks. Component success does not establish system success. Report remaining limits explicitly.

## Diagnose and recover

After failure, inspect actual state before retrying. A lost reply does not imply a lost result. Locate outputs and check pending actions before overwriting work or repeating external effects.

Determine whether the failure is in the premise, dependency, approach, implementation, or integration. Replan the affected portion using that diagnosis. Preserve mandatory acceptance. Do not weaken a criterion merely to make a check pass.

Set a reachable exit criterion and a justified retry bound for the task, using risk, available resources, and evidence. Do not use a universal attempt count. Retry only after conditions change or evidence supports a transient failure. If a blocker remains, identify its impact and the action or input needed to resolve it.

## Resume checkpoint

Store large intermediate outputs as artifacts. Keep evidence receipts with their step files; link them from the index. Keep the index checkpoint compact, with links instead of copied step bodies or logs:

```text
Goal, active mode, authorization, and constraints:
Accepted outputs: links to step receipts with content identity, proof, and limits
Executor map: owner/assessment references; actual agent bindings separate from planned owners
Active work: owner, original scope, state, resources, pending actions
Artifacts and inputs required to continue:
Decisions and unresolved questions:
Blockers and their affected scope:
Next authorized action and readiness conditions:
Native tool/API state needed: handles, sessions, pending-call identifiers
```

Preserve required native API and tool state using the environment's supported mechanism. A prose checkpoint does not restore a runtime, a session, or a pending call. On resume, verify their actual status before continuing. If that state is unavailable, describe the recovery limit and rebuild only what is safe within the active mode.

On resume, read the index and the step files needed for the next authorized action. Validate affected assignments, input revisions, and readiness; do not reload every step or full histories. Preserve stable IDs, valid artifacts, accepted evidence, and owner context. Reuse current instruction/evidence bindings until a named change or gap requires refresh; reassess only the affected dependency frontier, context bindings, or model decisions. Apply the manager's original-slice reuse rules before continuing a worker; do not treat a planned label or stale agent ID as a live executor. In PLAN ONLY, update authorized plan files and describe future execution checks and worker starts without performing them.

## Evaluate the method

Assess outcome quality, elapsed time, retries, and the tokens and cost of all participants and tools when data is available. Include coordination and integration. Mark unavailable measurements unknown, not zero. Do not claim measured savings without comparison data. Use observed failures or costs to adjust the next relevant step, not to add universal process.
