"""Tests of update_doc_titles.py: python3 -m unittest discover -s scripts"""

import contextlib
import io
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

import update_doc_titles

GH = "https://github.com/pitaman71"


def notebook(cells: list[tuple[str, str]], **dump) -> str:
    cells = [{"cell_type": kind, "id": str(i), "metadata": {}, "source": text.splitlines(keepends=True),
              **({"execution_count": 1, "outputs": []} if kind == "code" else {})} for i, (kind, text) in enumerate(cells)]
    nb = {"cells": cells, "metadata": {"kernelspec": {"language": "python", "name": "python3"}}, "nbformat": 4,
          "nbformat_minor": 5}
    return json.dumps(nb, **(dump or {"indent": 1, "sort_keys": True, "ensure_ascii": False})) + "\n"


class Titles(unittest.TestCase):
    def setUp(self) -> None:
        self.ws = Path(tempfile.mkdtemp())
        self.root = self.ws / "mbse-basis"
        self.files = {
            "mbse-basis/MBSE.md": "<!-- nav -->\n[Home](README.md)\n\n# Why the mbse repositories exist.\n\n## Parts\n",
            "mbse-basis/docs/capabilities/README.md": "```md\n# Not the title\n```\n\n# Capabilities\n",
            "mbse-basis/docs/capabilities/CAP-001.md":
                "# CAP-001: no-code index view\n\nIndex entry:\n[capabilities/README.md](README.md#CAP-001).\n",
            "mbse-basis/docs/capabilities/CAP-002.md": "# CAP-002: two\n\nSee [CAP-001.md](CAP-001.md), "
                                                       "[CAP-001](CAP-001.md) and [the index](README.md).\n",
            "mbse-basis/docs/README.md":
                "# The mbse basis\n\nRead [`MBSE.md`](../MBSE.md#parts) and [MBSE.md](mbse:mbse-basis/MBSE.md).\n"
                "Never a path: `[docs/README.md](README.md)`, nor [docs/README.md](…).\n\n"
                "```md\n[capabilities/README.md](capabilities/README.md)\n```\n",
            "mbse-basis/skills/s/SKILL.md": "---\nname: s\n---\n\n# The skill\n\nSee [references/a.md](references/a.md).\n",
            "mbse-basis/skills/s/references/a.md": "# A [linked](../SKILL.md) reference: `code`!\n\n[SKILL.md](../SKILL.md)\n",
            "mbse-basis/docs/UNTITLED.md": "No title.\n",
            "mbse-basis/docs/LEFT.md":
                "# Left\n\n[tool.py](../tool.py), [gone.md](GONE.md), [UNTITLED.md](UNTITLED.md), "
                "[a.md](https://example.com/a.md), ![img.md](x.md).\n",
            "mbse-basis/tool.py": "# [MBSE.md](MBSE.md) in a comment is not a document's link\n",
            "mbse-basis/docs/SIBLINGS.md":
                f"# Siblings\n\n[mbse-schemas/docs/EQUIVALENCE.md]({GH}/mbse-schemas/blob/main/docs/EQUIVALENCE.md#checks), "
                "[EQUIVALENCE.md](../../mbse-schemas/docs/EQUIVALENCE.md), "
                "[01_A.ipynb](mbse:mbse-schemas/python3/tutorials/01_A.ipynb).\n",
            "mbse-schemas/docs/EQUIVALENCE.md": "# Equivalence of the implementations\n\n## Checks\n",
            "mbse-schemas/python3/tutorials/01_A.ipynb": notebook([("code", "# not a heading\n"),
                                                                   ("markdown", "Intro\n\n# 01 · A first case\n")]),
            "mbse-basis/python3/tutorials/02_B.ipynb": notebook([
                ("markdown", "# B\n\nSee [MBSE.md](../../MBSE.md) · ünïcode\n"),
                ("code", "# [MBSE.md](../../MBSE.md)\n")], indent=2),
            "mbse-basis/python3/tutorials/03_C.ipynb": notebook([("markdown", "# C\n\n[B](02_B.ipynb)\n")], indent=2),
        }
        for name, text in self.files.items():
            (self.ws / name).parent.mkdir(parents=True, exist_ok=True)
            (self.ws / name).write_text(text)

    def read(self, name: str) -> str:
        return (self.ws / name).read_text()

    def test_path_labels(self) -> None:
        for label in ("capabilities/README.md", "MBSE.md", "`docs/README.md`", "python3/tutorials/README.md",
                      "mbse-schemas/docs/X.md", "a.ipynb", "MBSE.md#parts", "Corpus.py", "siblings.json"):
            self.assertTrue(update_doc_titles.path_label(label), label)
        for label in ("Capabilities", "CAP-001: no-code index view", "CAP-001", "CAP-001.md", "Symbol.iterator",
                      "P.CONSTANT", "the basis", "a.b", "docs/"):
            self.assertFalse(update_doc_titles.path_label(label), label)

    def test_relabels_with_titles(self) -> None:
        findings, changed = update_doc_titles.update([self.root])
        self.assertEqual(sorted(p.relative_to(self.root).as_posix() for p in changed), [
            "docs/README.md", "docs/SIBLINGS.md", "docs/capabilities/CAP-001.md", "python3/tutorials/02_B.ipynb",
            "skills/s/SKILL.md", "skills/s/references/a.md"])
        self.assertEqual(self.read("mbse-basis/docs/capabilities/CAP-001.md"),
                         "# CAP-001: no-code index view\n\nIndex entry:\n[Capabilities](README.md#CAP-001).\n")
        readme = self.read("mbse-basis/docs/README.md")
        self.assertIn("Read [Why the mbse repositories exist](../MBSE.md#parts) and "
                      "[Why the mbse repositories exist](mbse:mbse-basis/MBSE.md).", readme)
        for kept in ("`[docs/README.md](README.md)`", "[docs/README.md](…)",
                     "```md\n[capabilities/README.md](capabilities/README.md)\n```"):
            self.assertIn(kept, readme)
        self.assertIn("See [A linked reference: `code`](references/a.md).", self.read("mbse-basis/skills/s/SKILL.md"))
        self.assertIn("[The skill](../SKILL.md)", self.read("mbse-basis/skills/s/references/a.md"))
        self.assertEqual(self.read("mbse-basis/docs/SIBLINGS.md"),
                         f"# Siblings\n\n[Equivalence of the implementations]({GH}/mbse-schemas/blob/main/docs/EQUIVALENCE.md#checks), "
                         "[Equivalence of the implementations](../../mbse-schemas/docs/EQUIVALENCE.md), "
                         "[01 · A first case](mbse:mbse-schemas/python3/tutorials/01_A.ipynb).\n")
        for name in ("mbse-basis/docs/capabilities/CAP-002.md", "mbse-basis/docs/LEFT.md", "mbse-basis/tool.py",
                     "mbse-schemas/docs/EQUIVALENCE.md"):
            self.assertEqual(self.read(name), self.files[name])
        self.assertEqual(sorted(f.kind for f in findings if f.kind != "rewritable"),
                         ["elsewhere", "missing", "not a document", "untitled"])

    def test_notebooks_edit_only_markdown_cells_keeping_their_format(self) -> None:
        name = "mbse-basis/python3/tutorials/02_B.ipynb"
        expected = json.loads(self.files[name])
        expected["cells"][0]["source"] = ["# B\n", "\n", "See [Why the mbse repositories exist](../../MBSE.md) · ünïcode\n"]
        update_doc_titles.update([self.root])
        self.assertEqual(self.read(name), json.dumps(expected, indent=2) + "\n")
        self.assertIn("# [MBSE.md](../../MBSE.md)", self.read(name))  # a code cell is left alone
        name = "mbse-basis/python3/tutorials/03_C.ipynb"
        self.assertEqual(self.read(name), self.files[name])

    def test_check_writes_nothing_and_lists_by_kind(self) -> None:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            status = update_doc_titles.main(["--check", str(self.root)])
        self.assertEqual(status, 1)
        for name, text in self.files.items():
            self.assertEqual(self.read(name), text)
        lines = out.getvalue().splitlines()
        self.assertTrue(any(line.startswith("path label: ") and "CAP-001.md:4: [capabilities/README.md]"
                            "(README.md#CAP-001) -> Capabilities" in line for line in lines), lines)
        for kind, fragment in (("not a document", "[tool.py](../tool.py)"), ("no such file", "[gone.md](GONE.md)"),
                               ("document without a title", "[UNTITLED.md](UNTITLED.md)"),
                               ("link to another site", "[a.md](https://example.com/a.md)")):
            self.assertTrue(any(line.startswith(f"path label, {kind}: ") and fragment in line for line in lines), kind)
        self.assertIn("9 path labels to relabel, in 6 files", lines[-1])

    def test_relabeled_repository_checks_clean_but_for_what_needs_a_human(self) -> None:
        update_doc_titles.update([self.root])
        findings, changed = update_doc_titles.update([self.root], check=True)
        self.assertEqual(changed, [])
        self.assertEqual(sorted(f.kind for f in findings), ["elsewhere", "missing", "not a document", "untitled"])
        (self.root / "docs/LEFT.md").write_text("# Left\n")
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(update_doc_titles.main(["--check", str(self.root)]), 0)

    def test_reads_only_tracked_files(self) -> None:
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "add", "docs/capabilities/CAP-001.md"], check=True)
        _, changed = update_doc_titles.update([self.root])
        self.assertEqual(changed, [self.root / "docs/capabilities/CAP-001.md"])


if __name__ == "__main__":
    unittest.main()
