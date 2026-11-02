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

## Persist one plan package

When a persisted roadmap is requested, use a compact main index and one file per defined step. For example:

```text
roadmap/index.md
roadmap/steps/S1-inspect.md
roadmap/steps/S2-change.md
roadmap/steps/S3-accept.md
```

These names are examples. Use the project's authorized location and preserve stable step IDs and paths. The index and step files form one canonical plan package, not separate trackers. Each defined future step gets a file; distant work remains a short outcome/dependency stub until its inputs are known. Do not invent detailed tasks for undefined work.

The index provides navigation, authoritative operational task status, planned owners, dependencies, essential global constraints and authorization, and the next authorized action. Link to step bodies, accepted receipts, and existing contracts instead of copying them into the index. Keep long logs and intermediate research in linked artifacts. Store an owner assessment or shared contract once, in an existing source or one maintained location when needed; do not require extra shared files or repeated boilerplate.

Step files hold their contract, bound inputs, minimal context, owner reference, model/effort recommendation, outputs, acceptance, and evidence receipt. They do not repeat mutable operational status. Use the index as status authority by default; if a project already designates another single status source, link it and make index status a derived view. Separate planned owners from actual agent bindings. A planned label is never proof of a worker start.

The director reads the index and only the step files needed for the current decision. A worker reads its own step and specifically named accepted dependency outputs or contracts. Carry essential global constraints and exact source path, path base, and revision/content bindings into the assignment. Do not glob-read all steps or full histories. Reuse current instructions, assessments, and accepted evidence until a named change or gap requires refresh. Refresh the affected dependency frontier, not the whole plan. Batch safe independent reads or file writes; keep dependency-sensitive updates ordered. Use compact receipts and changed decisions rather than repeated narratives. Do not impose fixed word/token quotas or claim unmeasured savings.

## Review an existing plan

Read the index and select the step files relevant to the review. Compare them with the contract and inspected artifacts. Report each material mismatch with the requirement, observed evidence, and proposed correction. Check for missing acceptance, unsupported assumptions, uncovered requirements, impossible dependencies, ownership conflicts, and execution beyond authorization. Validate the executor map, essential context bindings, readiness, and model recommendations against the actual manager/router rules. Preserve stable IDs, valid assignments, accepted artifacts, and evidence. Reassess only affected owners, context, dependencies, and configurations when an input or requirement changes. Do not add process simply to fill the template.

Migrate an existing monolithic roadmap only within explicit authorization to change that plan. Preserve its IDs, source bindings, and accepted evidence; replace its authoritative queue with the package index or a clear pointer to the existing authority. Do not silently restructure existing projects or leave two authoritative queues. A read-only REVIEW reports the proposed migration without performing it.

## Roadmap template

Adapt the authorized project location. Keep the index compact; put each step body in its linked file. This is one package, not a second manual queue.

```text
Mode and authorization:
Outcome and completion evidence:
Scope / exclusions / constraints:
Material decisions / assumptions / open questions, with source links:
Requirements: ID -> step IDs -> acceptance reference
Execution mode and basis; overall model/effort recommendation and assessment reference:
Steps: ID | linked step file | authoritative status | owner | dependencies
Executor/context map: compact ownership/assessment links; actual bindings only after start
Integration and final flow acceptance: linked step
Accepted outputs: receipt links / blockers / next authorized action
Resume: artifact locations and any required native runtime state
```

For a future plan-only roadmap, tasks are waiting and checks are not run. Do not describe the planned output as completed. Preserve existing project state labels where they have equivalent meaning. Task state and check outcome are separate fields.

## Single-task template

Use one file for each defined step. Keep ready steps actionable; abbreviate distant stubs to outcome, dependencies, owner/assessment reference, and future acceptance. Operational status stays in the index.

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
Evidence receipt: artifact/content identity + criterion/check outcome + limits; not run if future work
Status authority: index link (no duplicate mutable status)
```

Logical states do not replace the project's labels. A cancelled task needs a reason and a coverage decision if it carried a requirement. Include an integration task when separate branches of work must function together. Define its user flow and checks before claiming the whole outcome.
