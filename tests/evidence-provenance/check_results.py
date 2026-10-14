"""Check saved behavioral observations and their source provenance."""

import hashlib
import json
from pathlib import Path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    directory = Path(__file__).parent
    repo = directory.parents[1]
    failures = []
    metadata = json.loads((directory / "metadata-results.json").read_text())
    quotations = json.loads((directory / "quotation-results.json").read_text())
    for result, skill, prefixes in [
        (metadata, "task-token-retrospective", ["undated", "dated", "conflicting"]),
        (quotations, "agent-instructions-audit", ["quotes"]),
    ]:
        if result["reviewed_skill_sha256"] != digest(repo / "skills" / skill / "SKILL.md"):
            failures.append(f"{skill}: stale skill observations")
        expected_files = {
            p.relative_to(directory / "fixtures").as_posix(): digest(p)
            for prefix in prefixes
            for p in (directory / "fixtures" / prefix).rglob("*") if p.is_file()
        }
        observed_files = {
            name.removeprefix("tests/evidence-provenance/fixtures/"): value
            for name, value in result["fixture_hashes"].items()
        }
        if len(observed_files) != len(result["fixture_hashes"]) or observed_files != expected_files:
            failures.append(f"{skill}: stale or incomplete fixture observations")
    criteria = repo / "skills/agent-instructions-audit/references/checks.md"
    if quotations["criteria_sha256"] != digest(criteria):
        failures.append("Stale audit criteria observations")
    dates = {
        "undated": ("unknown", "unknown", False),
        "dated": ("2024-03-02", "fixture-engine1.2", False),
        "conflicting": ("unknown", "unknown", True),
    }
    quote_decisions = {
        "exact": (True, False, False),
        "altered": (False, True, False),
        "paraphrase": (False, False, False),
        "wrong-location": (True, False, True),
    }
    skill_text = (repo / "skills/task-token-retrospective/SKILL.md").read_text()
    for result, expectations, fields in [
        (metadata, dates, ["successful_check_date", "environment_version", "date_conflict"]),
        (quotations, quote_decisions, ["wording_present", "wording_defect", "location_defect"]),
    ]:
        ids = [case["id"] for case in result["cases"]]
        if len(ids) != len(set(ids)) or set(ids) != set(expectations):
            failures.append("Missing, unexpected, or duplicate case IDs")
        for case in result["cases"]:
            if tuple(case[field] for field in fields) != expectations.get(case["id"]):
                failures.append(f"{case['id']}: unexpected behavior")
            if not case.get("reason") or not case.get("evidence"):
                failures.append(f"{case['id']}: missing acceptance evidence")
    for case in metadata["cases"]:
        if case["proposal_status"] != "proposed":
            failures.append(f"{case['id']}: unauthorized saved status")
        kind = case["approval_wording_kind"]
        if kind == "quotation" and case["approval_wording"] not in skill_text:
            failures.append(f"{case['id']}: quotation does not match its source")
        if kind not in {"quotation", "paraphrase"}:
            failures.append(f"{case['id']}: unclear quotation status")
    if failures:
        raise SystemExit("\n".join(failures))
    print("PASS: 7 saved behavioral cases; source hashes and quotation provenance match")


if __name__ == "__main__":
    main()
