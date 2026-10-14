"""Check observed test ordering and the preserved unavailable-runtime exception."""

import hashlib
import json
from pathlib import Path


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    directory = Path(__file__).parent
    repo = directory.parents[1]
    result = json.loads((directory / "results.json").read_text())
    profile = (repo / "templates/universal-project/agent-rules/software.md").read_bytes()
    original = (directory / "fixtures/numbers.py").read_bytes()
    fixed = original.replace(b"return 0", b"return None")
    tests = (directory / "fixtures/test_numbers.py").read_bytes()
    old_hash, new_hash, test_hash = digest(original), digest(fixed), digest(tests)
    failures = []
    for name, actual in [("profile_sha256", digest(profile)),
                         ("original_source_sha256", old_hash),
                         ("test_sha256", test_hash)]:
        if result[name] != actual:
            failures.append(f"{name}: stale observations")
    exception = "Если проверка до изменения невозможна или несоразмерна задаче, объясни причину и выбери проверку после изменения."
    if exception not in profile.decode():
        failures.append("The original exception is missing")
    records = result["normal"]["test_receipts"]
    first_new = next((i for i, r in enumerate(records)
                      if r["source_sha256"] == new_hash), len(records))
    before, after = records[:first_new], records[first_new:]
    if not any(r["case"] == "empty" and not r["passed"] for r in before):
        failures.append("No observed failing empty case before the implementation change")
    if not before or any(r["source_sha256"] != old_hash for r in before):
        failures.append("The original test phase has an unknown source revision")
    if not after or any(r["source_sha256"] != new_hash or not r["passed"] for r in after):
        failures.append("The final phase is missing or does not pass on the changed revision")
    if {r["case"] for r in after} != {"empty", "negative", "zero"}:
        failures.append("Final behavior coverage is incomplete")
    if any(r["test_sha256"] != test_hash for r in records):
        failures.append("The test source changed during the observation")
    if result["normal"]["exit_codes_reported"] != [1, 0]:
        failures.append("Unexpected reported runner exit codes")
    for case in [result["normal"], result["unavailable"]]:
        if case["source_sha256"] != new_hash:
            failures.append("The accepted source diff exceeds the requested correction")
    blocked = result["unavailable"]
    if (blocked["authorized_runtime_available"] or blocked["test_executed"]
            or blocked["runtime_result"] != "unverified" or blocked["test_receipts"]
            or not blocked["explanation_reported"]):
        failures.append("The blocked case does not preserve execution limits and uncertainty")
    if failures:
        raise SystemExit("\n".join(failures))
    print("PASS: observed pre-edit failure, post-edit success, and explicit unavailable-runtime exception")


if __name__ == "__main__":
    main()
