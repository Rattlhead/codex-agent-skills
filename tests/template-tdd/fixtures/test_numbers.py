import hashlib
import json
from pathlib import Path
import unittest

from numbers import smallest


def observe(name, actual, expected):
    directory = Path(__file__).parent
    record = {
        "case": name,
        "source_sha256": hashlib.sha256((directory / "numbers.py").read_bytes()).hexdigest(),
        "test_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "actual": repr(actual),
        "expected": repr(expected),
        "passed": actual == expected,
    }
    with (directory / "test-runs.jsonl").open("a") as stream:
        stream.write(json.dumps(record) + "\n")


class SmallestTests(unittest.TestCase):
    def test_empty(self):
        actual = smallest([])
        observe("empty", actual, None)
        self.assertIsNone(actual)

    def test_negative(self):
        actual = smallest([3, -7, -1])
        observe("negative", actual, -7)
        self.assertEqual(actual, -7)

    def test_zero(self):
        actual = smallest([4, 0, 2])
        observe("zero", actual, 0)
        self.assertEqual(actual, 0)


if __name__ == "__main__":
    unittest.main()
