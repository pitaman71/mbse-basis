"""Tests of update_link_forms.py: python3 -m unittest discover -s scripts"""

import contextlib
import io
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

import update_link_forms

GH = "https://github.com/pitaman71"


def notebook(cells: list[tuple[str, str]], **dump) -> str:
    cells = [{"cell_type": kind, "id": str(i), "metadata": {}, "source": text.splitlines(keepends=True),
              **({"execution_count": 1, "outputs": [{"output_type": "stream", "name": "stdout",
                                                    "text": ["[out](../../mbse-basis/docs/README.md)\n"]}]}
                 if kind == "code" else {})} for i, (kind, text) in enumerate(cells)]
    nb = {"cells": cells, "metadata": {"kernelspec": {"language": "python", "name": "python3"}}, "nbformat": 4,
          "nbformat_minor": 5}
    return json.dumps(nb, **(dump or {"indent": 1, "sort_keys": True, "ensure_ascii": False}))


class Forms(unittest.TestCase):
    def setUp(self) -> None:
        self.ws = Path(tempfile.mkdtemp())
        self.root = self.ws / "mbse-rest"
        self.files = {
            "mbse-basis/docs/README.md": '# The mbse basis\n\n## A link is a link\n\n- <a id="QUA-001"></a>Text.\n',
            "mbse-schemas/docs/EQUIVALENCE.md": "# Equivalence\n\n## Checks\n",
            "mbse-rest/README.md":
                "See [the basis](../mbse-basis/docs/README.md#a-link-is-a-link), [ours](docs/DESIGN.md),\n"
                "[a site](https://example.com/a.md), [our own](https://github.com/pitaman71/mbse-rest/blob/main/AGENTS.md),\n"
                "[a repository](https://github.com/pitaman71/mbse-schemas) and "
                "[shorthand](mbse:mbse-schemas/docs/EQUIVALENCE.md#checks \"Checks\").\n\n"
                "```md\n[fenced](../mbse-basis/docs/README.md)\n```\n\nA span: `[span](../mbse-basis/docs/README.md)`.\n",
            "mbse-rest/docs/DESIGN.md": "# Design\n\n[Equivalence](../../mbse-schemas/docs/EQUIVALENCE.md).\n",
            "mbse-rest/skills/mbse-rest/SKILL.md":
                "[Equivalence](../../../mbse-schemas/docs/EQUIVALENCE.md), "
                f"[the basis]({GH}/mbse-basis/blob/main/docs/README.md#QUA-001), [ours](../../README.md).\n",
            "mbse-rest/python3/mbse/Rest/skill/SKILL.md": "[Basis](../../../../../mbse-basis/docs/README.md).\n",
            "mbse-rest/python3/mbse/Rest/a.py":
                '"""Applies [the basis](../../../../mbse-basis/docs/README.md)."""\n\n'
                "# and [checks](../../../../mbse-schemas/docs/EQUIVALENCE.md#checks)\n"
                'FIXTURE = "[not a comment](../../../../mbse-basis/docs/README.md)"\n',
            "mbse-rest/typescript5/src/a.ts":
                "/** [The basis](../../../mbse-basis/docs/README.md) */\n"
                f"// [Checks]({GH}/mbse-schemas/blob/main/docs/EQUIVALENCE.md#checks)\n"
                "const s = '[a string](../../../mbse-basis/docs/README.md)';\n",
            "mbse-rest/run.sh": "# [The basis](../mbse-basis/docs/README.md)\necho '[x](../mbse-basis/docs/README.md)'\n",
            "mbse-rest/data.json": '{"a": "[x](../mbse-basis/docs/README.md)"}\n',
            "mbse-rest/python3/tests/01_A.ipynb": notebook([
                ("markdown", "# A\n\n[Basis](../../../mbse-basis/docs/README.md) · ünïcode\n"),
                ("code", "# [Checks](../../../mbse-schemas/docs/EQUIVALENCE.md#checks)\nx = 1\n")]) + "\n",
            "mbse-rest/python3/tests/02_B.ipynb": notebook([("markdown", "# B\n\n[Ours](../../README.md)\n")], indent=2),
        }
        for name, text in self.files.items():
            (self.ws / name).parent.mkdir(parents=True, exist_ok=True)
            (self.ws / name).write_text(text)

    def read(self, name: str) -> str:
        return (self.ws / name).read_text()

    def test_rewrites_each_file_in_its_form(self) -> None:
        wrong, missing, changed = update_link_forms.update([self.root])
        self.assertEqual(missing, [])
        self.assertEqual(sorted(p.relative_to(self.root).as_posix() for p in changed), [
            "README.md", "docs/DESIGN.md", "python3/mbse/Rest/a.py", "python3/mbse/Rest/skill/SKILL.md",
            "python3/tests/01_A.ipynb", "run.sh", "skills/mbse-rest/SKILL.md", "typescript5/src/a.ts"])
        self.assertEqual(len(wrong), 13)
        readme = self.read("mbse-rest/README.md")
        self.assertIn(f"[the basis]({GH}/mbse-basis/blob/main/docs/README.md#a-link-is-a-link)", readme)
        self.assertIn(f'[shorthand]({GH}/mbse-schemas/blob/main/docs/EQUIVALENCE.md#checks "Checks")', readme)
        for kept in ("[ours](docs/DESIGN.md)", "[a site](https://example.com/a.md)", "[a repository](https://github.com/pitaman71/mbse-schemas)",
                     "[our own](https://github.com/pitaman71/mbse-rest/blob/main/AGENTS.md)",
                     "[fenced](../mbse-basis/docs/README.md)", "`[span](../mbse-basis/docs/README.md)`"):
            self.assertIn(kept, readme)
        self.assertEqual(self.read("mbse-rest/docs/DESIGN.md"),
                         f"# Design\n\n[Equivalence]({GH}/mbse-schemas/blob/main/docs/EQUIVALENCE.md).\n")
        self.assertEqual(self.read("mbse-rest/skills/mbse-rest/SKILL.md"),
                         "[Equivalence](mbse:mbse-schemas/docs/EQUIVALENCE.md), "
                         "[the basis](mbse:mbse-basis/docs/README.md#QUA-001), [ours](../../README.md).\n")
        self.assertEqual(self.read("mbse-rest/python3/mbse/Rest/skill/SKILL.md"), "[Basis](mbse:mbse-basis/docs/README.md).\n")
        self.assertEqual(self.read("mbse-rest/python3/mbse/Rest/a.py"),
                         '"""Applies [the basis](mbse:mbse-basis/docs/README.md)."""\n\n'
                         "# and [checks](mbse:mbse-schemas/docs/EQUIVALENCE.md#checks)\n"
                         'FIXTURE = "[not a comment](../../../../mbse-basis/docs/README.md)"\n')
        self.assertEqual(self.read("mbse-rest/typescript5/src/a.ts"),
                         "/** [The basis](mbse:mbse-basis/docs/README.md) */\n"
                         "// [Checks](mbse:mbse-schemas/docs/EQUIVALENCE.md#checks)\n"
                         "const s = '[a string](../../../mbse-basis/docs/README.md)';\n")
        self.assertEqual(self.read("mbse-rest/run.sh"),
                         "# [The basis](mbse:mbse-basis/docs/README.md)\necho '[x](../mbse-basis/docs/README.md)'\n")
        self.assertEqual(self.read("mbse-rest/data.json"), self.files["mbse-rest/data.json"])

    def test_notebooks_edit_only_cell_sources(self) -> None:
        name = "mbse-rest/python3/tests/01_A.ipynb"
        expected = json.loads(self.files[name])
        expected["cells"][0]["source"] = ["# A\n", "\n", f"[Basis]({GH}/mbse-basis/blob/main/docs/README.md) · ünïcode\n"]
        expected["cells"][1]["source"] = ["# [Checks](mbse:mbse-schemas/docs/EQUIVALENCE.md#checks)\n", "x = 1\n"]
        update_link_forms.update([self.root])
        self.assertEqual(self.read(name), json.dumps(expected, indent=1, sort_keys=True, ensure_ascii=False) + "\n")
        self.assertIn("[out](../../mbse-basis/docs/README.md)", self.read(name))  # outputs untouched
        self.assertEqual(self.read("mbse-rest/python3/tests/02_B.ipynb"), self.files["mbse-rest/python3/tests/02_B.ipynb"])

    def test_check_writes_nothing_and_finds_unresolved(self) -> None:
        (self.root / "docs/MISSING.md").write_text(
            "[gone](../../mbse-schemas/docs/GONE.md), [bad anchor](../../mbse-schemas/docs/EQUIVALENCE.md#nowhere), "
            f"[case](../../mbse-schemas/docs/EQUIVALENCE.md#Checks), [bad URL]({GH}/mbse-basis/blob/main/docs/README.md#QUA-002), "
            "[no checkout](../../mbse-react/README.md), [beyond](../../../elsewhere/a.md).\n")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            status = update_link_forms.main(["--check", str(self.root)])
        self.assertEqual(status, 1)
        for name, text in self.files.items():
            if name.startswith("mbse-rest/"):
                self.assertEqual(self.read(name), text)
        unresolved = [line for line in out.getvalue().splitlines() if line.startswith("unresolved:")]
        self.assertEqual(len(unresolved), 5, unresolved)
        joined = "\n".join(unresolved)
        for fragment in ("no file mbse-schemas/docs/GONE.md", "no anchor #nowhere", "no anchor #QUA-002",
                         "no file mbse-react/README.md", "leaves the folder"):
            self.assertIn(fragment, joined)
        self.assertNotIn("#Checks", joined)
        self.assertIn("docs/MISSING.md:1:", joined)

    def test_rewritten_repository_checks_clean(self) -> None:
        update_link_forms.update([self.root])
        wrong, missing, changed = update_link_forms.update([self.root], check=True)
        self.assertEqual((wrong, missing, changed), ([], [], []))
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(update_link_forms.main(["--check", str(self.root)]), 0)

    def test_reads_only_tracked_files(self) -> None:
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "add", "README.md"], check=True)
        _, _, changed = update_link_forms.update([self.root])
        self.assertEqual(changed, [self.root / "README.md"])
        self.assertEqual(self.read("mbse-rest/docs/DESIGN.md"), self.files["mbse-rest/docs/DESIGN.md"])

    def test_heading_slugs(self) -> None:
        self.assertEqual(update_link_forms.slug("As built: `mbse-schemas`, [CAP-1](x.md)"), "as-built-mbse-schemas-cap-1")
        path = self.ws / "dup.md"
        path.write_text("# A\n## Decided\n```\n# Not a heading\n```\n## Decided\n")
        self.assertEqual(update_link_forms.anchors(path, {}), {"a", "decided", "decided-1"})


if __name__ == "__main__":
    unittest.main()
