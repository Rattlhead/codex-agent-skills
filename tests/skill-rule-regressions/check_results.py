"""Compare a saved independent instruction trace with behavioral expectations."""

import hashlib
import json
from pathlib import Path


def main():
    directory = Path(__file__).parent
    cases = json.loads((directory / "cases.json").read_text())["cases"]
    result = json.loads((directory / "results.json").read_text())
    observations = result["cases"]
    ids = [item["id"] for item in observations]
    expected = {item["id"]: item["expected"] for item in cases}
    failures = []
    sources = {
        "skills/task-model-router/SKILL.md",
        "skills/task-model-router/references/rates.md",
        "skills/subagent-manager/SKILL.md",
        "skills/agent-instructions-audit/references/checks.md",
    }
    reviewed = result.get("reviewed_files", {})
    if set(reviewed) != sources:
        failures.append("Incomplete reviewed source set")
    for name in sources:
        digest = hashlib.sha256((directory.parents[1] / name).read_bytes()).hexdigest()
        if reviewed.get(name) != digest:
            failures.append(f"{name}: observations are missing or stale")
    if len(ids) != len(set(ids)) or set(ids) != set(expected):
        failures.append("Missing, unexpected, or duplicate case IDs")
    for observation in observations:
        if observation["decision"] != expected.get(observation["id"]):
            failures.append(f"{observation['id']}: unexpected decision")
        if not observation.get("reason") or not observation.get("evidence"):
            failures.append(f"{observation['id']}: missing reason or evidence")
    if result.get("findings"):
        failures.append("The independent review reports unresolved findings")
    if failures:
        raise SystemExit("\n".join(failures))
    print(f"PASS: {len(cases)} saved independent traces; no assertion failures")


if __name__ == "__main__":
    main()
