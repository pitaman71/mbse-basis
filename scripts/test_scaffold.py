"""Tests of polyrepo.py's new, the scaffold, in a scratch directory beside a copy of mbse-basis:

    python3 -m unittest discover -s scripts

Standard library only, as polyrepo.py is: the Python notebooks' cases are run here without installing anything, and
the TypeScript ones only by the new repository's own `npm test`.
"""

from __future__ import annotations

import contextlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import unittest.mock
from pathlib import Path

import polyrepo

BASIS = Path(__file__).resolve().parent.parent
FILES = [
    ".gitignore", ".nvmrc", "AGENTS.md", "CLAUDE.md", "MBSE.md", "README.md", "siblings.json", "docs/EQUIVALENCE.md",
    "skills/mbse-example/SKILL.md", "skills/sync.sh",
    "python3/README.md", "python3/pyproject.toml", "python3/conftest.py", "python3/mbse/Example/__init__.py",
    "python3/mbse/Example/skill/SKILL.md", "python3/tests/01_Package.ipynb", "python3/tests/02_Skill.ipynb",
    "python3/tests/TestPlan.md", "python3/tutorials/README.md",
    "typescript5/README.md", "typescript5/package.json", "typescript5/tsconfig.json", "typescript5/.c8rc.json",
    "typescript5/deno.json", "typescript5/src/index.ts", "typescript5/skill/SKILL.md",
    "typescript5/tests/01_Package.ipynb", "typescript5/tests/02_Skill.ipynb", "typescript5/tests/support.ts",
    "typescript5/tests/run-notebooks.ts", "typescript5/tests/TestPlan.md", "typescript5/tutorials/README.md",
]


class Scaffold(unittest.TestCase):
    def setUp(self) -> None:
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name).resolve()
        environment = {"GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1", "GIT_AUTHOR_NAME": "t",
                       "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}
        patcher = unittest.mock.patch.dict(os.environ, environment)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.basis = self.root / "mbse-basis"
        shutil.copytree(BASIS, self.basis, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        subprocess.run(["git", "init", "--quiet", "--initial-branch=main", str(self.basis)], check=True)
        subprocess.run(["git", "-C", str(self.basis), "add", "--all"], check=True)
        subprocess.run(["git", "-C", str(self.basis), "commit", "--quiet", "-m", "basis"], check=True)
        self.commit = polyrepo.git(self.basis, "rev-parse", "HEAD")

    def new(self, name: str = "mbse-example", package: str = "Example", npm: str | None = None) -> str:
        printed = io.StringIO()
        with contextlib.redirect_stdout(printed):
            self.assertEqual(polyrepo.new(self.root / name, package, npm, self.basis), 0)
        return printed.getvalue()

    def test_the_starting_set(self) -> None:
        printed = self.new()
        repo = self.root / "mbse-example"
        for name in FILES:
            self.assertTrue((repo / name).is_file(), name)
        tracked = set(polyrepo.git(repo, "ls-files").split("\n"))
        self.assertEqual(tracked, set(FILES))  # every file, and no other, staged in a new git repository
        self.assertEqual(json.loads((repo / "siblings.json").read_text()),
                         {"mbse-basis": {"repository": "git@github.com:pitaman71/mbse-basis.git",
                                         "commit": self.commit}})
        self.assertEqual((repo / "CLAUDE.md").read_text(), "@AGENTS.md\n")
        self.assertEqual(json.loads((repo / "typescript5" / "package.json").read_text())["name"], "@mbse/example")
        for packaged in ("python3/mbse/Example/skill/SKILL.md", "typescript5/skill/SKILL.md"):
            self.assertEqual((repo / packaged).read_bytes(), (repo / "skills/mbse-example/SKILL.md").read_bytes())
        self.assertTrue((repo / "README.md").read_text().startswith("<!-- nav -->\n[Why the mbse repositories exist"))
        self.assertIn("Next, in it:", printed)

    def test_every_placeholder_filled(self) -> None:
        self.new()
        repo = self.root / "mbse-example"
        for path in repo.rglob("*"):
            if ".git" not in path.parts and path.is_file():
                self.assertNotIn("{{", path.read_text(), path)
                self.assertNotIn("{{", path.relative_to(repo).as_posix())

    def test_the_link_checks_are_clean(self) -> None:
        self.new()
        repo = self.root / "mbse-example"
        for tool in ("update_link_forms.py", "update_item_titles.py", "update_doc_titles.py"):
            run = subprocess.run([sys.executable, str(self.basis / "scripts" / tool), "--check"], cwd=repo,
                                 capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, f"{tool}: {run.stdout}{run.stderr}")

    def test_the_python_cases_pass(self) -> None:
        """PKG-01 and the SKL cases, from the Python notebooks, run here as nbmake would run them."""
        self.new()
        repo = self.root / "mbse-example"
        here, path, modules = Path.cwd(), list(sys.path), dict(sys.modules)
        try:
            os.chdir(repo / "python3" / "tests")
            sys.path.insert(0, str(repo / "python3"))
            for name in [m for m in sys.modules if m == "mbse" or m.startswith("mbse.")]:
                del sys.modules[name]
            for notebook in ("01_Package.ipynb", "02_Skill.ipynb"):
                scope: dict = {}
                for cell in json.loads(Path(notebook).read_text())["cells"]:
                    if cell["cell_type"] == "code":
                        exec("".join(cell["source"]), scope)  # noqa: S102
                self.assertIn("package", scope)
        finally:
            os.chdir(here)
            sys.path[:] = path
            for name in set(sys.modules) - set(modules):
                del sys.modules[name]
            sys.modules.update(modules)

    def test_an_area_and_name(self) -> None:
        self.new("mbse-example-services", "Example.Services", "@mbse/services")
        repo = self.root / "mbse-example-services"
        self.assertTrue((repo / "python3/mbse/Example/Services/__init__.py").is_file())
        self.assertTrue((repo / "python3/mbse/Example/Services/skill/SKILL.md").is_file())
        self.assertFalse((repo / "python3/mbse/Example/__init__.py").exists())  # a namespace, as PRI-030 has it
        self.assertIn('"mbse.Example.Services" = ["skill/*.md"]', (repo / "python3/pyproject.toml").read_text())
        self.assertEqual(json.loads((repo / "typescript5/package.json").read_text())["name"], "@mbse/services")

    def test_refusals(self) -> None:
        (self.root / "mbse-taken").mkdir()
        (self.root / "elsewhere").mkdir()
        for args, message in [(("mbse-taken", "Taken"), "already exists"),
                              (("Example", "Example"), "a repository's name"),
                              (("mbse-example", "example"), "--package example"),
                              (("mbse-example", "Example", "example"), "--npm example")]:
            with self.assertRaises(SystemExit) as refused:
                self.new(*args)
            self.assertIn(message, str(refused.exception))
        with self.assertRaises(SystemExit) as refused:
            polyrepo.new(self.root / "elsewhere" / "mbse-example", "Example", None, self.basis)
        self.assertIn("must be beside mbse-basis", str(refused.exception))
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), ["elsewhere", "mbse-basis", "mbse-taken"])
        self.assertEqual(list((self.root / "mbse-taken").iterdir()), [])

    def test_the_command_line(self) -> None:
        printed = io.StringIO()
        with contextlib.redirect_stdout(printed), unittest.mock.patch.object(polyrepo, "new", return_value=0) as new:
            polyrepo.main(self.basis, ["new", str(self.root / "mbse-example"), "--package", "Example"])
            polyrepo.main(self.basis, ["new", str(self.root / "mbse-x"), "--package", "X", "--npm", "@mbse/y"])
        self.assertEqual(new.call_args_list, [unittest.mock.call(self.root / "mbse-example", "Example", None),
                                              unittest.mock.call(self.root / "mbse-x", "X", "@mbse/y")])
        with self.assertRaises(SystemExit) as refused:
            polyrepo.main(self.basis, ["new", str(self.root / "mbse-example")])
        self.assertIn("new DIR --package", str(refused.exception))


if __name__ == "__main__":
    unittest.main()
