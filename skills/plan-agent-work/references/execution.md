# Execution, evidence, and recovery

Use this reference only within the authorization selected in SKILL.md.

## Maintain one state source

Find the canonical package and status authority, normally the index. Do not make a second manual queue.
Use single-writer ownership for status. Workers submit receipts to that writer.
Keep derived views synchronized or regenerate them from the authority.
In delegate mode, assign plan-file updates to existing workers within their roles. Do not start bookkeeping workers.
Assign non-overlapping files or serialize shared-file edits.

Write the output artifact. Then record its evidence receipt in the step file, before index completion.
Accept necessary proof before marking done. Batch safe independent writes; order receipt-to-completion updates.
After write or reply failure, examine actual artifacts, receipts, and index changes.
Repair incomplete updates without invented proof or blind repetition of external actions. An index entry alone cannot prove completion.

When work is ready, use its executor/context map.
Before dispatch, validate the affected assignment and current manager/router conditions.
Do not rebuild all assignments or load owner investigations into director context.
Record actual starts separately from planned owner labels. In delegate mode, keep production and integration with workers.

Use project labels that distinguish waiting, in progress, review, done, blocked, and cancelled.
A ready task has all prerequisites. A done task has accepted output and necessary proof.
For blocked tasks, state the blocker and affected scope. Continue unblocked authorized work.
Do not interpret timeouts, lost responses, or exhausted budgets as completion.

Task state is separate from check outcome. Record checks as success, failure, not run, or unknown. Do not translate unknown into success.

## Accept evidence at the right scope

For code, use relevant project checks. Select TDD from user requirements, project rules, and risk.
Do not make new tests mandatory for every trivial document edit.
For UI work, validate the actual flow: initial state, action, and expected visible result. Static inspection alone is insufficient.
For research, examine source content as evidence for claims. Titles and search snippets alone are insufficient.
For other artifacts, use the contract's reproducible content or visual checks.

Bind evidence to actual content, inputs, environment, and criteria. Include relevant dirty changes or a content hash.
A commit identifier alone is insufficient. Use valid evidence while relevant content and conditions remain unchanged.
Run affected checks again after relevant changes, for named unresolved risks, or under project rules.
A new stage alone does not justify unchanged checks.

After separate branches join, do the planned integration task and end-to-end flow checks.
Component success does not prove system success. Report remaining limits explicitly.

## Local milestone commits

Use selected checkpoints only in existing Git repositories with local-commit authorization.
After acceptance of a significant coherent step, slice, or related group, make one scoped commit.
First update its evidence receipt and status. For roadmaps, use step receipts and the index; otherwise use existing brief or status.
Do not make plan files for a commit. Do not commit every command or small edit, or make empty commits.
This procedure grants no repository-initialization permission. Do not probe Git for unrelated non-Git tasks.
Keep PLAN ONLY and REVIEW limits; planning alone grants no permission to commit user work.
A local commit grants no push, publication, broader source-change, or new-repository permission.

The director manages acceptance. An authorized existing executor or integration owner performs Git operations.
The designated status writer updates the existing plan or status. Do not start bookkeeping workers.
Assign one owner to the shared Git index; serialize access.
Include only the authorized accepted slice and its related tracked plan/status changes. Keep unrelated staged and dirty work.
Before commit, examine staged content. Do not use automatic `git add .`, destructive reset or stash, amend, or hook bypass.
Do not weaken acceptance criteria to obtain a commit.

Keep hooks active. After failure, timeout, or lost reply, examine actual status and HEAD before another attempt or success claim.
Do not make a completed commit again. Use valid accepted evidence while content and relevant inputs remain unchanged.
If hooks change files, validate affected content and inputs again before another attempt or checkpoint acceptance.

Return a compact receipt with full commit SHA, covered step/slice IDs, and check results.
On its next necessary update, the status writer adds the checkpoint reference to existing status authority.
Do not make a separate commit only to record its own SHA. A commit cannot contain its own final hash.
Keep roadmap receipts in step files and authoritative status in the index. Otherwise use existing brief or status.
The SHA identifies the checkpoint. It does not prove current content or acceptance when dirty work remains.

## Diagnose and recover

After failure, examine actual state before another attempt. A lost reply does not imply a lost result.
Find outputs and examine pending actions before overwriting work or causing external effects again.

Find whether the premise, dependency, approach, implementation, or integration caused failure. Replan only the affected portion.
Keep mandatory acceptance. Do not weaken criteria to pass a check.

Set a reachable exit criterion and justified retry bound from task risk, resources, and evidence. Do not use universal attempt counts.
Try again only after changed conditions or evidence of transient failure.
If blocked, state the impact and necessary action or input.

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

Save necessary native API and tool state through the environment's supported mechanism.
A prose checkpoint cannot restore a runtime, session, or pending call. On resume, examine their actual status before continuation.
If state is unavailable, state the recovery limit. Rebuild only safe state within the active mode.

On resume, read the index and steps necessary for the next authorized action.
Validate affected assignments, input revisions, and readiness. Do not load every step or full histories.
Keep stable IDs, valid artifacts, accepted evidence, and owner context.
Use current instruction/evidence bindings until a named change or gap. Reassess only affected dependencies, context bindings, or model decisions.
Before worker continuation, apply the manager's original-slice reuse rules. Planned labels and stale IDs do not prove live executors.
In PLAN ONLY, update authorized plan files. Describe future execution checks and starts without performing them.

## Evaluate the method

With available data, examine outcome quality, elapsed time, retries, tokens, and cost for all participants and tools.
Include coordination and integration. Mark unavailable measurements unknown, not zero. Do not claim measured savings without comparison data.
Use observed failures or costs to adjust the next relevant step. Do not add universal process.
