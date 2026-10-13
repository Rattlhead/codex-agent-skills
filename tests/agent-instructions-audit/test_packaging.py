"""Run README installation and update snippets in disposable local directories."""

import re
import shlex
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
NAMES = ("task-model-router", "subagent-manager", "task-token-retrospective",
         "agent-instructions-audit")


class PackagingTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="codex-skill-packaging-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.clone = self.root / "clone"
        self.target = self.root / "installed"
        self.backup = self.root / "backup"
        self.clone.mkdir()
        self.target.mkdir()
        shutil.copytree(REPO / "skills", self.clone / "skills")
        blocks = re.findall(r"```sh\n(.*?)\n```", (REPO / "README.md").read_text(), re.S)
        self.install = next(block for block in blocks if "git clone" in block)
        self.update = next(block for block in blocks if "rsync" in block)

    def run_snippet(self, snippet):
        snippet = snippet[snippet.index("(\n"):]
        snippet = snippet.replace('skill_root="${CODEX_HOME:-$HOME/.codex}/skills"',
                                  "skill_root=" + shlex.quote(str(self.target)))
        snippet = snippet.replace(
            'backup_dir="${CODEX_HOME:-$HOME/.codex}/skill-backups/$(date +%Y%m%d-%H%M%S)-$$"',
            "backup_dir=" + shlex.quote(str(self.backup)))
        # Only Git fetching is mocked. File checks, copy, backup, and rsync run.
        prefix = 'git() { test "$*" = "pull --ff-only"; }\n'
        return subprocess.run(["sh"], input=prefix + snippet, text=True,
                              cwd=self.clone, capture_output=True)

    def assert_success(self, process):
        self.assertEqual(process.returncode, 0, process.stderr[-1500:])
        for name in NAMES:
            source = self.clone / "skills" / name
            installed = self.target / name
            expected = {p.relative_to(source): p.read_bytes()
                        for p in source.rglob("*") if p.is_file()}
            actual = {p.relative_to(installed): p.read_bytes()
                      for p in installed.rglob("*") if p.is_file()}
            self.assertEqual(actual, expected)

    def test_new_install(self):
        self.assert_success(self.run_snippet(self.install))

    def test_install_preserves_existing_directory(self):
        existing = self.target / NAMES[0]
        existing.mkdir()
        (existing / "local.txt").write_text("keep")
        self.assertNotEqual(self.run_snippet(self.install).returncode, 0)
        self.assertEqual((existing / "local.txt").read_text(), "keep")
        self.assertFalse((self.target / NAMES[-1]).exists())

    def test_install_rejects_dangling_link(self):
        link = self.target / NAMES[-1]
        link.symlink_to(self.root / "absent")
        self.assertNotEqual(self.run_snippet(self.install).returncode, 0)
        self.assertTrue(link.is_symlink())
        self.assertFalse((self.target / NAMES[0]).exists())

    def test_update_backs_up_before_replacing_local_content(self):
        existing = self.target / NAMES[0]
        existing.mkdir()
        (existing / "SKILL.md").write_text("local version")
        (existing / "stale.txt").write_text("old")
        self.assert_success(self.run_snippet(self.update))
        saved = self.backup / NAMES[0]
        self.assertEqual((saved / "SKILL.md").read_text(), "local version")
        self.assertEqual((saved / "stale.txt").read_text(), "old")
        self.assertFalse((existing / "stale.txt").exists())

    def test_update_rejects_symbolic_link_before_any_backup(self):
        link = self.target / NAMES[-1]
        link.symlink_to(self.root / "absent")
        self.assertNotEqual(self.run_snippet(self.update).returncode, 0)
        self.assertTrue(link.is_symlink())
        self.assertFalse(self.backup.exists())

    def test_update_missing_source_stops_before_writes(self):
        (self.clone / "skills" / NAMES[-1] / "SKILL.md").unlink()
        self.assertNotEqual(self.run_snippet(self.update).returncode, 0)
        self.assertFalse(self.backup.exists())
        self.assertEqual(list(self.target.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
