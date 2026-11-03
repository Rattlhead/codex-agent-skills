# Applicable coverage and interactions

Use this reference to set the finite audit boundary.
Select dimensions from the deliverable, requirements, and risks.
For a dimension that does not apply, use `not applicable` with a reason.
Do not import a software checklist into other work.

| Dimension | Software evidence | Other deliverable evidence |
| --- | --- | --- |
| Functionality | Required outcomes, state transitions, valid and invalid inputs, error and recovery paths | Required content, calculations, transformations, constraints, and usable outputs |
| Integration | Actual contracts between callers, services, storage, configuration, and generated outputs | References, source data, linked assets, formulas, exports, and downstream consumers |
| Regression | Preserved behavior around the changed mechanism and prior failures | Unchanged required content, formulas, layout, citations, or production constraints around an edit |
| UI/UX | Ordinary user journey, readable states, reachable controls, feedback, keyboard access, recovery | Reading order, navigation, labels, legibility, accessibility, operator clarity, and rendered layout |
| Static quality | Types, lint, build, security-relevant data handling, source consistency | Structure, consistency, source validity, units, styles, naming, and internal references |
| Architecture | Responsibilities, dependency direction, contracts, lifecycle, shared state | Information hierarchy, document or asset composition, source-of-truth ownership, and maintainability |
| Flows | User, event, control, and data flow from entry to outcome | Input-to-output trace, provenance, reading or production sequence, and handoff |
| Boundaries | External input, persistence, permissions, environment, versions, failure and cancellation | Format, export, print, language, units, limits, recipient, and tool boundaries |
| Interactions | Features, states, roles, modules, or events that share resources or affect each other | Content, formulas, layout, assets, sources, or exports that constrain each other |

Use domain skills for concrete methods.
Examples include spreadsheet recalculation, document rendering, illustration preflight, source verification, and browser interaction.
A domain example is not a mandatory check for every artifact.

## Build the interaction matrix

Use the existing matrix or brief.
Add only entries necessary for the declared scope:

`entry or scenario -> interacting elements and shared boundary -> initial state/input -> action or change -> expected result/invariant -> evidence/check -> result and gap`

Before a statement of complete coverage, list reachable states, transitions, actors, inputs, outputs, and relevant dependencies.
Add normal, boundary, error, retry, cancellation, concurrency, and recovery cases only where they affect the scope.
Give priority to interactions that share data, callbacks, configuration, lifecycle, files, assets, or external contracts.
Include an independent control or counterexample where it can distinguish a suspected mechanism.

For each row, keep the exact artifact or runtime revision.
For delegated work, keep the owner for each row.
Use `pass`, `fail`, `not run`, `blocked`, or `not applicable` with a reason.
A finding's causal status can remain unresolved even when evidence confirms its observed failure.

Expand the boundary only for a requirement, supported dependency, or material observation.
Record the reason.
Report adjacent findings outside scope.
Do not silently make them an implementation assignment.
For sampling, pairwise cases, and a selected list of flows, keep an explicit coverage limit.
