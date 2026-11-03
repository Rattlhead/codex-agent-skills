# Decision contract v1.0.0

Use these exact field sets. Do not add fields, including nested fields. Inputs and outputs are JSON objects.
Nonempty strings must contain content. IDs identify stable items. Arrays may be empty unless the decision needs their content.

## Ten input fields

| Field | Type and meaning |
| --- | --- |
| `decision_id` | Nonempty string. Stable decision slice ID. |
| `goal` | Nonempty string. Authorized outcome. |
| `question` | Nonempty string. Current choice or routing question. |
| `context` | String. Essential facts, mode, revision, and dependencies. |
| `constraints` | Array of strings. Mandatory and relevant criteria. |
| `existing_decisions` | Array of strings. Prior decisions with validity context. |
| `alternatives` | Array of objects with exactly `id` (string) and `description` (string). IDs must be unique. |
| `permissions` | Object with exactly `authorized`, `forbidden`, and `approval_required`, each an array of strings. This is reported authority, not a grant by the child. |
| `affected_tasks` | Array of objects with exactly `task_id` (string), `state` (`pending`, `ready`, `running`, `complete`, `failed`, or `blocked`), and `depends_on` (array of task IDs). |
| `evidence` | Array of objects with exactly `source` (string), `content` (string), and `trust` (`authoritative`, `observed`, or `untrusted`). |

## Twelve output fields

Return only one JSON object, without Markdown fences, comments, NaN, or surrounding prose.
Use exactly twelve output fields.

| Field | Type and meaning |
| --- | --- |
| `decision_id` | Nonempty string, identical to input. |
| `status` | `AUTO_DECIDE`, `NEED_EVIDENCE`, `ESCALATE_TO_USER`, `DEFER`, or `NO_DECISION_NEEDED`. |
| `chosen_option` | One offered alternative ID string, or `null`. |
| `reason` | Nonempty string. Short basis and material conditions. |
| `alternatives_considered` | Array of objects with exactly `option` (string) and `assessment` (nonempty string). |
| `evidence` | Array of objects with exactly `source` (nonempty string) and `finding` (nonempty string). Include genuine sources or observations only. |
| `risks` | Array of strings. |
| `reversibility` | `reversible`, `partly_reversible`, `irreversible`, or `unknown`. |
| `confidence` | `high`, `medium`, or `low`. State evidence basis in reason or evidence; do not add a confidence object. |
| `validation` | Object with exactly `method` (nonempty string), `outcome` (`passed`, `failed`, `pending`, or `not_applicable`), and `evidence` (array of strings). |
| `requires_user` | Boolean. |
| `next_action` | Object with exactly `type` (`execute`, `check`, `escalate`, `wait`, or `none`), `description` (nonempty string), and `affected_tasks` (array of task IDs). |

## Status invariants

| Status | `chosen_option` | `requires_user` | `next_action.type` | Required meaning |
| --- | --- | --- | --- | --- |
| `AUTO_DECIDE` | Offered ID | `false` | `execute` | Select an admissible offered option for a nontrivial unsettled choice within current authority. This excludes uniquely implied answers. The authorized owner executes. |
| `NEED_EVIDENCE` | `null` | `false` | `check` | Name the smallest authorized observation or input amendment and how it enables the choice. |
| `ESCALATE_TO_USER` | `null` | `true` | `escalate` | Name missing authority or human-only conflict. Block dependent action. Operations needing new authority or mandatory human approval remain D even when refusal is obvious. Approval for another action cannot authorize an independently forbidden action. |
| `DEFER` | `null` | `false` | `wait` | Name the pending dependency or future trigger. |
| `NO_DECISION_NEEDED` | `null` | `false` | `none` | Requirements, authoritative documentation, tests, a mechanical rule, valid prior decision, or accepted completion uniquely determine the answer. Alternatively, no choice remains. Give the answer and basis in reason/evidence; prior decision logs are unnecessary. Here `none` means no new decision action, not task termination. After acceptance, the controller resumes determined authorized work through its owner. |

Malformed, stale, lost, or unsupported content is never executable authority.
Unknown effect, timing, token, and cost telemetry is UNKNOWN, not zero.
Validation `passed` needs a cited actual observation; a proposed check is `pending`.

## Example request

This illustrative input contains its own bounded facts. It is not a test fixture or a claim about an actual repository.

```json
{
  "decision_id": "D-report-format",
  "goal": "Deliver a useful offline review report",
  "question": "Which of the two supported report formats should the owner use?",
  "context": "delegate mode; input revision 1; the report has long tables and section links; the recipient reviews on a laptop and sometimes prints; no format preference or binding decision exists",
  "constraints": ["Deliver one self-contained local file", "Keep all report data", "Use an existing exporter"],
  "existing_decisions": [],
  "alternatives": [
    {"id": "html", "description": "Use the existing self-contained HTML exporter for search, links, and flexible table layout"},
    {"id": "pdf", "description": "Use the existing PDF exporter for fixed pagination and predictable printing"}
  ],
  "permissions": {
    "authorized": ["The assigned owner may export either format to the task output directory"],
    "forbidden": ["Publish the report or change its data"],
    "approval_required": []
  },
  "affected_tasks": [{"task_id": "T-report", "state": "pending", "depends_on": []}],
  "evidence": [{"source": "owner exporter check, revision 1", "content": "Both existing exporters keep the report data and produce self-contained files. The recipient can open either format offline.", "trust": "observed"}]
}
```

## Example reply

```json
{
  "decision_id": "D-report-format",
  "status": "AUTO_DECIDE",
  "chosen_option": "html",
  "reason": "Both formats obey the constraints. Select HTML for search, section links, and flexible tables during laptop inspection. These benefits outweigh fixed pagination here. PDF remains admissible and is better for printing. Confidence is medium: the owner supplied evidence, and the value of occasional printing is a bounded judgment.",
  "alternatives_considered": [
    {"option": "html", "assessment": "Gives navigation and flexible tables for laptop inspection. Printed pagination can vary."},
    {"option": "pdf", "assessment": "Gives stable printed pages. Long tables and section navigation can be less convenient on laptops."}
  ],
  "evidence": [{"source": "owner exporter check, revision 1", "finding": "The supplied check shows that both formats obey offline-output requirements. It does not uniquely select one."}],
  "risks": ["HTML printed page breaks can vary. The owner must examine table readability in the delivered file."],
  "reversibility": "reversible",
  "confidence": "medium",
  "validation": {"method": "The assigned owner opens the HTML file offline. The owner examines data completeness, section links, and table readability.", "outcome": "pending", "evidence": []},
  "requires_user": false,
  "next_action": {"type": "execute", "description": "The owner exports HTML locally within authorization. The owner then examines the delivered file.", "affected_tasks": ["T-report"]}
}
```
