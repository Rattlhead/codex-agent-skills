"""Check observed scenario results against the behavioral assertions."""

import argparse
import json
from pathlib import Path


def check(cases_path, results_path):
    cases = json.loads(cases_path.read_text())["cases"]
    result = json.loads(results_path.read_text())
    observations = result["cases"]
    failures = []
    ids = [item["id"] for item in observations]
    expected_ids = [item["id"] for item in cases]
    if len(ids) != len(set(ids)) or set(ids) != set(expected_ids):
        failures.append("Result IDs are duplicated, missing, or unexpected")
    by_id = {item["id"]: item for item in observations}
    covered = set()
    for case in cases:
        observed = by_id.get(case["id"])
        if observed is None:
            continue
        expectation = case["expected"]
        found = {item["rule"] for item in observed["findings"]}
        covered.update(found)
        errors = []
        if not set(expectation.get("must_find", [])).issubset(found):
            errors.append("required defect not reported")
        if set(expectation.get("must_not_find", [])) & found:
            errors.append("false positive")
        if expectation.get("no_confirmed_findings") and found:
            errors.append("unexpected confirmed defect in an exception case")
        if expectation.get("must_unverified") and not observed["unverified"]:
            errors.append("missing uncertainty")
        if not observed["proposal_only"]:
            errors.append("unauthorized correction")
        if expectation.get("must_partial_scope") and observed["scope"] != "partial":
            errors.append("partial review presented as full")
        if observed["verdict"] not in {"pass", "findings", "inconclusive"}:
            errors.append("invalid verdict")
        if found and observed["verdict"] == "pass":
            errors.append("confirmed findings hidden by pass")
        if any(not item.get("evidence") or not item.get("reason")
               for item in observed["findings"]):
            errors.append("finding lacks evidence or consequence")
        if errors:
            failures.append(f"{case['id']}: {', '.join(errors)}")
    if result.get("skill_findings"):
        failures.append("Unresolved defects of the skill are reported")
    return len(cases), covered, failures


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path,
                        default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()
    count, coverage, failures = check(Path(__file__).with_name("cases.json"), args.results)
    if failures:
        print("\n".join(failures))
        raise SystemExit(1)
    print(f"PASS: {count} logical cases; {len(coverage)} criteria observed; no assertion failures")
