# Audit records

Use only the sections that help the current task. Small audits can use a few paragraphs. Keep one canonical record. Link evidence instead of copying large logs or secrets.

## Boundary and evidence identity

- Requested area and expected behavior:
- Included entry points, states, transitions, and sequence bounds:
- Adjacent dependencies included and why:
- Excluded paths, unknowns, and access or permission limits:
- Source revision, relevant dirty changes, runtime artifact/build:
- Environment, configuration/data identity, observation time:
- Existing canonical record and evidence locations:

## Branch matrix

| ID | Entry/state | Event or input and guard | Expected result/next state | Related dependency/symptom | Check and evidence | Coverage status |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | | | | | | |

Use precise coverage status: `observed`, `statically inspected`, `blocked`, `not run`, or `excluded`. For `observed`, state whether the result matched the expected behavior. Add a reason for blocked and excluded rows. Keep evidence level separate from pass/fail. List known inventory gaps outside the matrix; they are not covered rows.

## Causal claims

| Claim ID | Symptom and trigger | Mechanism and conditions | Upstream source/shared symptoms | Prediction and alternative | Evidence/control and result | Status and limits |
| --- | --- | --- | --- | --- | --- | --- |
| C1 | | | | | | |

Use `confirmed`, `supported`, `unresolved`, or `rejected`. Evidence references should identify the command or observation, relevant input, version/environment, result, and location. Note changed assumptions that invalidate earlier evidence.

## Final report

Lead with what the evidence establishes and its practical effect. Then provide:

- Findings in impact order, with the causal chain and evidence status.
- Shared-cause links that were established, plus alternatives still open.
- The assessed boundary, covered branches, failures, and material gaps.
- Mitigations and proposed root fixes, clearly separated from work performed.
- The next useful checks, their access needs, and prevention proposals.
- The canonical location for durable verified findings, if an update is authorized.

State overall completion as completion of the agreed audit scope, with evidence limits. Do not imply that unresolved causes, untested branches, or proposed repairs are complete.
