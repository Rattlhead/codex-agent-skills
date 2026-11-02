# Planning and plan review

## Establish the contract

Define an observable outcome, the permitted scope, exclusions, constraints, and completion evidence. State numerical targets only when they come from the user, an applicable contract, or measurements. Otherwise label a target as a proposal and explain its basis. Do not invent a tolerance to make a task testable.

Keep facts, decisions, assumptions, and open questions distinct. Resolve a question before dependent work when its answer can change acceptance, authorization, or an expensive choice. Continue independent work within the active mode.

Inspect applicable instructions, existing artifacts, interfaces, and checks before proposing changes. Verify paths, APIs, tools, and relevant baseline health. If not verified, label them unknown or proposed. Do not present a guessed path or assumed passing baseline as fact.

For research, set the question, source scope, needed evidence, and stop condition before searching. Stop when the evidence supports the required decision or when the declared limit requires a qualified result. An unresolved question is not a license for unbounded research. For analysis, identify inputs, method, uncertainty, and reproducible outputs. For document work, identify the intended reader, source material, output artifact, and content or layout checks.

## Build backward from the outcome

Start with final acceptance. Identify the outputs and preconditions that can establish it. Then derive tasks and their dependencies.

Keep requirement coverage in the canonical plan. Map each material requirement to at least one task and check. Every task must support a requirement, a dependency, or an observed risk. Remove tasks with no such basis. A requirement may need several tasks; a task may satisfy several requirements.

Make slices independently acceptable where feasible. Keep each behavior change with the configuration, documentation, and tests needed to accept that behavior. Avoid separate layer tasks that leave no usable outcome until all layers exist.

For substantial roadmaps, plan the executors and their context with [delegation.md](delegation.md). Group connected steps under a coherent slice owner instead of rediscovering assignments at every step. Keep the detailed investigation, changes, and checks with that owner where its original scope permits; retain required independent review. The director keeps the shared contract, decisions, dependency state, and acceptance evidence, rather than loading every worker's research.

Specify each slice's inputs, outputs, interfaces, and decisions. Identify consumers and providers of shared interfaces. Build the actual dependency graph, including shared state and hidden links. Check for cycles, missing preconditions, and dependencies that only appear independent because they touch different files. Resolve cycles through an explicit interface decision or a prerequisite task. Do not schedule a worker to wait for an absent input.

Detail the next ready tasks enough to execute them. Keep distant work at outcome and dependency level. Refine it when inputs and decisions become available. Do not write future implementation details as if unknown conditions were settled.

## Review an existing plan

Compare the plan with the contract and inspected artifacts. Report each material mismatch with the requirement, observed evidence, and proposed correction. Check for missing acceptance, unsupported assumptions, uncovered requirements, impossible dependencies, ownership conflicts, and execution beyond authorization. Validate the executor map, essential context bindings, readiness, and model recommendations against the actual manager/router rules. Preserve valid assignments, accepted artifacts, and evidence. Reassess only affected owners, context, dependencies, and configurations when an input or requirement changes. Do not add process simply to fill the template.

## Roadmap template

Adapt the existing project format. Keep this information together in the canonical plan rather than creating a second manual queue.

```text
Mode and authorization:
Outcome and completion evidence:
Scope / exclusions / constraints:
Facts [source] / decisions [reason] / assumptions / open questions:
Requirements: ID -> task IDs -> check and criterion
Dependency graph and unresolved preconditions:
Execution mode and basis; overall model/effort recommendation and assessment reference:
Executor/context map: use delegation.md; planned owners, not claimed agent starts
Tasks: use the task template below
Integration and final flow acceptance:
Current state / accepted outputs and proof / active work:
Decisions / blockers / next authorized action:
Resume: artifact locations and any required native runtime state
```

For a future plan-only roadmap, tasks are waiting and checks are not run. Do not describe the planned output as completed. Preserve existing project state labels where they have equivalent meaning. Task state and check outcome are separate fields.

## Single-task template

For significant tasks, use the following fields. Abbreviate small tasks to action, criterion, and status.

```text
ID:
Requirement or rationale:
Observable outcome:
Inputs and verified locations:
Dependencies and readiness conditions:
Planned slice owner and executor-map reference; actual agent ID only after start:
Model/effort recommendation: reuse owner assessment or state needed change
Change scope and shared resources:
Outputs, interfaces, and decisions:
Acceptance: criterion + method + required evidence
State: waiting | in progress | review | done | blocked | cancelled
Proof: artifact/content identity + check outcome; not run if future work
Next step:
```

Logical states do not replace the project's labels. A cancelled task needs a reason and a coverage decision if it carried a requirement. Include an integration task when separate branches of work must function together. Define its user flow and checks before claiming the whole outcome.
