# Director role and execution mode check

## Scope and evidence

This is a read-only routing assessment of five supplied situations. No underlying project task, project check, agent start, or budget action was performed. I reviewed the manager skill, router skill, and universal-project coordination instructions after the parent marked the source set FROZEN.

Source identities:

- `skills/subagent-manager/SKILL.md` — SHA-256 `077d4280148af002cf7ff3ca05937f1e1d70eb919224d9dd059a248f9e4d0f01`
- `skills/task-model-router/SKILL.md` — SHA-256 `2a31663a93289871074c3e951c0c3e90ebff5012514a9abd9e1c404cda6b51a7`
- `templates/universal-project/AGENTS.md` — SHA-256 `0ef03dbda0366e85336885df290b7bd874fe170733f8d32ecb6914f9857e3099`
- `templates/universal-project/agent-rules/coordination.md` — SHA-256 `9b2846070fa9209915a6cef41dcd774d05efe15e0210f65ce479b5609c58aa25`
- Manager metadata prompt — SHA-256 `48e58c657cbb3f3361f7474da0fccfa1c5d9519401a107b69d3bce72cd47801c`
- Router metadata prompt — SHA-256 `9e4ca98352205b11bf08a71f724aec180d49ab33ed4425626dc3351a8c8e9fb0`

The parent supplied the expected manager and router hashes. The computed hashes match. The prompt and template hashes identify the reviewed revisions; no runtime model selection, rate lookup, or performance measurement was performed.

## Scenario judgments

| Case | Execution mode and roles | Allowed next action | Boundary |
| --- | --- | --- | --- |
| A. One known plaintext typo; primary adequate; exact narrow diff and bounded check; no further stages or worker request | `primary_only`. The primary is both executor and acceptance owner. | Correct the typo and perform the specified bounded check. | Keep the edit and check within the known local correction. Do not add a worker just because multiple actions are involved. |
| B. One tiny final production edit remains in an active delegated feature; primary could do it faster | Remains `delegate`. Primary is director and acceptance owner; the assigned worker remains production owner. | Have the original worker finish the edit through the existing slice, with a follow-up if scope and contract still match. | Do not promote a small remaining substep into a new whole-goal short-task exception. Primary may coordinate and accept, but must not take over production. |
| C. User says only “fix the project”; scale, acceptance, and context are unknown; no evidence the whole goal is short | `delegate` unless bounded discovery affirmatively establishes the whole-goal exception. Primary is director; a worker owns subsequent execution. | Do only minimal bounded clarification or discovery needed to determine the whole goal and its acceptance. | Do not treat missing scope as proof of a short task, begin primary execution, or start an agent solely to classify. If uncertainty remains, keep `delegate`. |
| D. Worker reports completion; a named evidence gap prevents acceptance | Remains `delegate`. Primary directs and owns acceptance; original worker remains slice owner. | Assign the gap to the worker if reuse conditions hold, or perform the manager-authorized bounded inspection/check for that named gap with scope and owner identified. | Inspect only the gap on the identified revision. Do not repeat full research or the test suite without a changed input, contradiction, or further gap. The worker's completion statement alone does not establish acceptance. |
| E. Substantial goal within primary capability and cheaper to execute directly, but includes broad investigation, implementation, and integration | `delegate`. Primary is director and acceptance owner; worker(s) execute production and integration. Keep coupled stages with one worker when scope and permissions allow. | Route the whole goal before full research, then assign the adequate configuration and slice(s). | Cost optimization applies only among configurations that pass the mode gates. Direct-cost claims do not make a broad multi-stage goal eligible for `primary_only`; actual cost advantage remains unverified absent applicable counters and rates. |

## Instruction consistency and limits

The sources agree on the role boundary: the primary is director by default; `primary_only` is an affirmative exception for a confirmed short, self-contained whole goal. The router requires `delegate` for substantive stage chains or substantial anticipated context even if primary capability is adequate. The manager assigns production and integration to workers in `delegate` mode and retains coordination and final acceptance. The template coordination rule says to follow the current router decision.

The cost wording is conditional, not an exception to the mode gate: compare total cost only after the short-task exception is established, and select the lower-cost mode only when both modes meet the requirements. Thus it does not authorize direct primary execution in B or E. Unknown cost must remain unknown; it is not evidence that either mode is cheaper.

No contradictory default/exception instruction was observed in the reviewed passages. A wording risk remains: read in isolation, “choose the lower-cost mode” could appear to override the `delegate` default. The router's immediately preceding eligibility gates and its explicit short-task condition resolve that reading. This assessment did not evaluate every installed project instruction or runtime behavior.

Observed judgments are instruction-based scenario outcomes, not measured execution speed, latency, cost savings, model capability tests, or evidence that an actual worker is available. Case C intentionally lacks facts needed to confirm the exception; its default routing is therefore `delegate`, with only bounded discovery allowed before substantive execution.
