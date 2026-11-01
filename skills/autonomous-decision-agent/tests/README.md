# Portable decision benchmark

Run commands from the skill directory. The declared design target is Python 3.10 or newer with its standard library. Tests here ran on Python 3.14.7 only; compatibility with other Python versions was not tested. No network, agent API, emulator or dependencies are used by these checks.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_*.py'
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_results.py validate-fixtures --inputs tests/fixtures/development-inputs.jsonl tests/fixtures/holdout-inputs.jsonl --oracles tests/fixtures/development-oracles.jsonl tests/fixtures/holdout-oracles.jsonl --index tests/fixtures/index.json
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_decision.py --request request.json --response reply.json
```

The runtime validator accepts one request object and one reply object, not JSONL. Exit 0 means the structure, status invariants and IDs/options pass. It does not grant permission, execute actions or prove evidence truth. Exit 1 indicates invalid structure or unreadable input.

To score a 44-case core result file mechanically:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_results.py check --inputs tests/fixtures/development-inputs.jsonl tests/fixtures/holdout-inputs.jsonl --oracles tests/fixtures/development-oracles.jsonl tests/fixtures/holdout-oracles.jsonl --results core-results.jsonl
```

For consistency, each result file represents one round or condition, with unique decision IDs within that round. It may concatenate outputs from several fresh batch contexts. The core round contains 44 cases from six fresh batches: four batches of eight and two batches of six. Each repeat round contains the ten predeclared IDs from two fresh batches of eight and two. Record the actual context IDs and the mapping from batches to records separately. A combined core file does not represent one 44-case context.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_results.py consistency --inputs tests/fixtures/development-inputs.jsonl tests/fixtures/holdout-inputs.jsonl --oracles tests/fixtures/development-oracles.jsonl tests/fixtures/holdout-oracles.jsonl --index tests/fixtures/index.json --results core-results.jsonl repeat-round1.jsonl repeat-round2.jsonl
```

Important consistency limit: this unchanged frozen checker rejects malformed consistency inputs. It does not generate the primary missing/invalid-as-nonmatch table itself. Keep the expected 30 same-case pairs, 4 paraphrases and 4 flips as the primary denominator; count each invalid participating pair as a nonmatch. Parsed-only agreement is secondary and needs its own denominator. The reference run had one malformed neutral reply outside all predefined comparisons, so no relevant comparison was excluded.

There are 28 unique software checks: 21 runtime/contract tests and 7 metric tests. Historical external checks exercised the same cases; they are not extra unique coverage. These tests validate software contracts and accounting, not model decision quality or native controller behavior.

The 44 case fixtures are now public regression cases. Reusers must create and freeze a fresh holdout before tuning or making a new held-out performance claim. Use protocol.md, reporting-addendum.md, rubric.json and contract.json. Semantic scores require an independent reviewer. Do not grade architecture by keyword matching.
