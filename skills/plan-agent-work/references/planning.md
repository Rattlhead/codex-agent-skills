# Planning and plan review

## Establish the contract

Define the observable outcome, permitted scope, exclusions, constraints, and completion evidence.
Use numerical targets from the user, applicable contracts, or measurements. Otherwise label targets proposed and give their basis.
Do not invent tolerances to make work testable.

Keep facts, decisions, assumptions, and open questions separate.
Before dependent work, answer questions that can change acceptance, authorization, or expensive choices. Continue independent work within the active mode.

Before proposed changes, examine applicable instructions, artifacts, interfaces, and checks.
Make sure paths, APIs, tools, and relevant baseline health are correct. Otherwise label them unknown or proposed.
Do not present guessed paths or assumed baseline success as facts.

Before research, specify the question, source scope, necessary evidence, and stop condition.
Stop when evidence is sufficient for the decision or the declared limit makes a qualified result necessary.
Do not research without bounds.
For analysis, specify inputs, method, uncertainty, and reproducible outputs.
For documents, specify the reader, sources, output artifact, and content or layout checks.

## Build backward from the outcome

Start with final acceptance. Find the outputs and preconditions that can prove it. Then derive tasks and dependencies.

Keep requirement coverage in the canonical plan. Map each material requirement to at least one task and check.
Each task must address a requirement, dependency, or observed risk. Remove tasks without that basis.
Requirements and tasks can have many-to-many relationships.

Where possible, make each slice independently acceptable. Include the configuration, documentation, and tests necessary to accept its behavior change.
Avoid layer tasks that produce no usable outcome until every layer exists.

For substantial roadmaps, use [delegation.md](delegation.md) to plan executors and context. Group connected steps under a coherent slice owner.
Keep investigation, changes, and checks with that owner where permitted by its original scope. Keep mandatory independent review.
The director keeps shared contracts, decisions, dependency state, and acceptance evidence. Do not load every worker's research.

Specify slice inputs, outputs, interfaces, and decisions. Identify shared-interface producers and consumers.
Build the dependency graph, including shared state and hidden links. Examine cycles, missing preconditions, and false independence between different files.
Remove cycles through an explicit interface decision or prerequisite task. Do not schedule workers to wait for absent inputs.

Use rolling-wave planning: detail ready tasks; describe distant work by outcomes and dependencies.
Add detail when inputs and decisions become available. Do not present unknown future conditions as settled.

## Persist one plan package

When a persisted roadmap is requested, use a compact main index and one file per defined step. For example:

```text
roadmap/index.md
roadmap/steps/S1-inspect.md
roadmap/steps/S2-change.md
roadmap/steps/S3-accept.md
```

Use the project's authorized location; these paths are examples. Keep stable step IDs and paths.
The index and step files form one canonical package. Give each defined future step a file.
Until inputs are known, keep distant steps as short outcome/dependency stubs. Do not invent detailed undefined tasks.

In the index, keep navigation, authoritative task status, planned owners, dependencies, global constraints, authorization, and the next authorized action.
Link step bodies, accepted receipts, contracts, long logs, and intermediate research. Do not copy them into the index.
Store each owner assessment or shared contract once. Use existing sources or one maintained location, without extra mandatory shared files.

In step files, keep contracts, bound inputs, essential context, owner references, model/effort recommendations, outputs, acceptance, and evidence receipts.
Do not duplicate mutable status. By default, the index is the status authority.
If the project has another single status authority, link it and derive index status from it.
Separate planned owners from actual agent bindings. Planned labels do not prove worker starts.

The director reads the index and step files necessary for its decision.
Workers read their steps and specifically named accepted dependencies or contracts.
Include essential global constraints, exact source paths, path bases, and revision/content bindings in assignments.
Do not read all steps or full histories by default.
Use current instructions, assessments, and evidence until a named change or gap.
Refresh only affected dependencies. Batch safe independent reads or writes; order dependent updates.
Use compact receipts and decision changes. Do not impose fixed word/token quotas or claim unmeasured savings.

## Review an existing plan

Read the index and relevant step files. Compare them with the contract and examined artifacts.
Report material mismatches with their requirement, evidence, and proposed correction.
Look for missing acceptance, unsupported assumptions, uncovered requirements, impossible dependencies, ownership conflicts, and unauthorized execution.
Validate the executor map, context bindings, readiness, and model recommendations against actual manager/router rules.
Keep stable IDs, valid assignments, accepted artifacts, and evidence. After input or requirement changes, examine only affected owners, context, dependencies, and configurations.
Do not add process only to complete a template.

Migrate a monolithic roadmap only with explicit authorization to change it. Keep IDs, source bindings, and accepted evidence.
Replace its authoritative queue with the package index or a clear pointer to existing authority.
Do not restructure projects silently or leave two authoritative queues. In read-only REVIEW, propose migration without execution.

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

For future plan-only roadmaps, tasks wait and checks are not run. Do not describe planned output as complete.
Keep equivalent project state labels. Task state and check outcome are separate fields.

## Single-task template

Use one file for each defined step. Keep ready steps actionable; abbreviate distant stubs to outcome, dependencies, owner/assessment reference, and future acceptance. Operational status stays in the index.

```text
ID:
Requirement or rationale:
Observable outcome:
Inputs and verified locations:
Dependencies and readiness conditions:
Planned slice owner and executor-map reference; actual agent ID only after start:
Model/effort recommendation: existing owner assessment or necessary change
Change scope and shared resources:
Outputs, interfaces, and decisions:
Acceptance: criterion + method + required evidence
Evidence receipt: artifact/content identity + criterion/check outcome + limits; not run if future work
Status authority: index link (no duplicate mutable status)
```

Logical states do not replace the project's labels. A cancelled task needs a reason and a coverage decision if it carried a requirement. Include an integration task when separate branches of work must function together. Define its user flow and checks before claiming the whole outcome.
