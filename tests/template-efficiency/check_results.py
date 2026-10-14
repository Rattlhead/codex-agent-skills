"""Check saved Git-selection and runner-mode behavioral observations."""

import hashlib
import json
from pathlib import Path


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    directory = Path(__file__).parent
    repo = directory.parents[1]
    result = json.loads((directory / "results.json").read_text())
    failures = []
    for name in ["context.md", "verification.md", "software.md"]:
        actual = digest((repo / "templates/universal-project/agent-rules" / name).read_bytes())
        if result["profile_sha256"].get(name) != actual:
            failures.append(f"{name}: stale observations")
    original = (repo / "tests/template-tdd/fixtures/numbers.py").read_bytes()
    fixed = original.replace(b"return 0", b"return None")
    old_hash, new_hash = digest(original), digest(fixed)
    base_tests = (repo / "tests/template-tdd/fixtures/test_numbers.py").read_text()
    observed_tests = base_tests.replace("import json\n", "import json\nimport sys\n")
    observed_tests = observed_tests.replace('"case": name,', '"case": name,\n        "argv": sys.argv[1:],')
    cases = result["accepted_cases"]
    if set(cases) != {"ordinary", "git_required", "explicit_verbose", "diagnostic"}:
        failures.append("Incorrect scenario coverage")
    for name in ["ordinary", "git_required", "explicit_verbose"]:
        case = cases[name]
        records = case["test_receipts"]
        if case["original_source_sha256"] != old_hash or case["final_source_sha256"] != new_hash:
            failures.append(f"{name}: unexpected implementation change")
        expected_test = digest(observed_tests.encode())
        if case["test_sha256"] != expected_test or any(r["test_sha256"] != expected_test for r in records):
            failures.append(f"{name}: observed test source changed")
        first_new = next((i for i, r in enumerate(records) if r["source_sha256"] == new_hash), len(records))
        before, after = records[:first_new], records[first_new:]
        if not any(r["case"] == "empty" and not r["passed"] for r in before):
            failures.append(f"{name}: missing observed pre-edit failure")
        if not before or any(r["source_sha256"] != old_hash for r in before):
            failures.append(f"{name}: invalid initial revision")
        if (not after or any(r["source_sha256"] != new_hash or not r["passed"] for r in after)
                or {r["case"] for r in after} != {"empty", "negative", "zero"}):
            failures.append(f"{name}: final behavior coverage failed")
        verbose = [any(a in {"-v", "--verbose"} for a in r["argv"]) for r in records]
        if name == "explicit_verbose":
            if not verbose or not all(verbose):
                failures.append("Explicit user verbosity request was not honored")
        elif any(verbose):
            failures.append(f"{name}: routine verification used verbose")
        if case["runner_exit_codes_reported"] != [1, 0]:
            failures.append(f"{name}: unexpected reported runner statuses")
        if name != "git_required" and (case["git_commands"] or any(c.startswith("git ") for c in case["commands"])):
            failures.append(f"{name}: unnecessary Git command")
    git = cases["git_required"]
    if not git["git_commands"] or not any(c.startswith("diff ") for c in git["git_commands"]):
        failures.append("Required Git operations were not performed")
    if git["branch_reported"] != "fixture-main" or git["tracked_changes_reported"] != ["numbers.py"]:
        failures.append("Required branch and tracked-change evidence is missing")
    probes = [c for c in git["git_commands"] if c.startswith("rev-parse ")]
    if len(probes) > 1:
        failures.append("Repeated repository discovery probes")
    if any(c.split()[0] in {"add", "commit", "reset", "push"} for c in git["git_commands"]):
        failures.append("Git write operation exceeded the scenario scope")
    diagnostic = cases["diagnostic"]
    diag_tests = observed_tests.replace('observe("empty", actual, None)', 'observe("empty", actual, 0)')
    diag_tests = diag_tests.replace("self.assertIsNone(actual)", "self.assertEqual(actual, 0)")
    diag_records = diagnostic["test_receipts"]
    if (diagnostic["test_sha256"] != digest(diag_tests.encode())
            or diagnostic["original_source_sha256"] != new_hash or diagnostic["final_source_sha256"] != new_hash):
        failures.append("Diagnostic source evidence changed")
    if (len(diag_records) != diagnostic["initial_receipt_count"]
            or diagnostic["actor_reported_rerun"] or diagnostic["actor_reported_git"]
            or diagnostic["initial_runner_exit_code_observed"] != 1):
        failures.append("Existing diagnostic evidence caused an unnecessary rerun or Git probe")
    if "None != 0" not in diagnostic["log_retained"] or not diagnostic["diagnosis"]:
        failures.append("Failure details were lost")
    if not result.get("initial_attempts"):
        failures.append("Initial incomplete observations were not retained")
    if failures:
        raise SystemExit("\n".join(failures))
    print("PASS: 4 final scenarios; Git selection, runner modes, TDD and retained diagnostic evidence")


if __name__ == "__main__":
    main()
