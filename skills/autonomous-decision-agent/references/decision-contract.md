# Decision contract v1.0.0

Use these exact field sets. No extra fields are permitted, including at nested object levels. Inputs and outputs are JSON objects. Strings described as nonempty must contain content. IDs identify stable items. Arrays may be empty unless a specific decision requires their content.

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

Return one JSON object only. No Markdown fences, comments, NaN, or surrounding prose. The supplied contract names twelve output fields; do not add a thirteenth.

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
| `AUTO_DECIDE` | Offered ID | `false` | `execute` | Resolve a genuinely unsettled nontrivial choice among admissible offered options inside current authority. Computing a uniquely implied answer is not this status. Execution belongs to the authorized owner. |
| `NEED_EVIDENCE` | `null` | `false` | `check` | Name the smallest authorized observation or input amendment and how it enables the choice. |
| `ESCALATE_TO_USER` | `null` | `true` | `escalate` | Name missing authority or the human-only conflict; block dependent action. A requested operation that still needs new authority or mandatory human approval remains D even when its immediate refusal is obvious. Approval for another action cannot permit an independently forbidden action. |
| `DEFER` | `null` | `false` | `wait` | Name the pending dependency or future trigger. |
| `NO_DECISION_NEEDED` | `null` | `false` | `none` | The answer is uniquely determined by current requirements, authoritative documentation, tests, a mechanical rule, a valid prior decision, or accepted completion; or no choice is open. State the answer and supporting basis in reason/evidence. No prior logged decision is required. Here `none` means no new decision action; it does not stop the task. After acceptance, the controller resumes any already determined authorized task through its owner. |

Malformed, stale, lost, or unsupported content is never executable authority. Unknown effect, timing, token, and cost telemetry is UNKNOWN, not zero. Validation `passed` requires a cited actual observation; a proposed check is `pending`.

## Example request

This illustrative input contains its own bounded facts. It is not a test fixture or a claim about an actual repository.

```json
{
  "decision_id": "D-report-format",
  "goal": "Deliver a useful offline review report",
  "question": "Which of the two supported report formats should the owner use?",
  "context": "delegate mode; input revision 1; the report has long tables and section links; the recipient reviews on a laptop and sometimes prints; no format preference or binding decision exists",
  "constraints": ["Deliver one self-contained local file", "Preserve all report data", "Use an existing exporter"],
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
  "evidence": [{"source": "owner exporter check, revision 1", "content": "Both existing exporters preserve the report data and produce a self-contained file; the recipient can open either format offline", "trust": "observed"}]
}
```

## Example reply

```json
{
  "decision_id": "D-report-format",
  "status": "AUTO_DECIDE",
  "chosen_option": "html",
  "reason": "Both formats meet the constraints. Choose HTML because search, section links, and flexible tables offer more benefit for laptop review than fixed pagination. PDF remains admissible and is stronger for printing. Confidence is medium because the owner check is supplied evidence and the relative value of occasional printing is a bounded judgment.",
  "alternatives_considered": [
    {"option": "html", "assessment": "Supports navigation and flexible tables during laptop review; printed pagination can vary."},
    {"option": "pdf", "assessment": "Provides stable printed pages; long tables and cross-section navigation can be less convenient on a laptop."}
  ],
  "evidence": [{"source": "owner exporter check, revision 1", "finding": "The supplied check supports both formats as compliant offline outputs; it does not uniquely select one."}],
  "risks": ["HTML printed page breaks can vary; the owner must check table readability in the delivered file."],
  "reversibility": "reversible",
  "confidence": "medium",
  "validation": {"method": "The assigned owner opens the HTML file offline and checks data completeness, section links, and table readability.", "outcome": "pending", "evidence": []},
  "requires_user": false,
  "next_action": {"type": "execute", "description": "The authorized owner exports HTML locally and checks the delivered file.", "affected_tasks": ["T-report"]}
}
```
