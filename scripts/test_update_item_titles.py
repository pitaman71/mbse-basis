"""Tests of update_item_titles.py: python3 -m unittest discover -s scripts"""

import tempfile
import unittest
from pathlib import Path

import update_item_titles


class Titles(unittest.TestCase):
    def setUp(self) -> None:
        self.ws = Path(tempfile.mkdtemp())
        self.basis = self.ws / "mbse-basis"
        files = {
            "mbse-basis/docs/QUALITIES.md": '- <a id="QUA-001"></a>**QUA-001: AI and humans in the loop** · adopted · Text.\n',
            "mbse-basis/docs/capabilities/README.md":
                '- <a id="CAP-001"></a>**[CAP-001: no-code index view](CAP-001.md)** · adopted · Text.\n'
                '- <a id="CAP-024"></a>**CAP-024: the same conformance corpora** · proposed · Text. *Implements*\n'
                '  [QUA-001](../QUALITIES.md#QUA-001) (an old title).\n',
            "mbse-basis/docs/capabilities/CAP-001.md": "# CAP-001 · an old title\n\nSee [CAP-024: old](README.md#CAP-024).\n",
            "repo/README.md": "Builds [CAP-001](../mbse-basis/docs/capabilities/CAP-001.md) and "
                              "[CAP-024: stale](../mbse-basis/docs/capabilities/README.md#CAP-024).\n"
                              "Not an item: [CAP-001](docs/CAP-001.md); mismatched: [CAP-024](../mbse-basis/docs/capabilities/CAP-001.md); "
                              "unknown: [CAP-999](../mbse-basis/docs/capabilities/README.md#CAP-999).\n",
            "repo/src/a.py": '"""Serves [QUA-001](../../mbse-basis/docs/QUALITIES.md#QUA-001)."""\n',
            "repo/data.bin": "[CAP-001](../mbse-basis/docs/capabilities/CAP-001.md)\n",
        }
        for name, text in files.items():
            (self.ws / name).parent.mkdir(parents=True, exist_ok=True)
            (self.ws / name).write_text(text)

    def test_titles_from_index_heads(self) -> None:
        self.assertEqual(update_item_titles.titles(self.basis / "docs"), {
            "QUA-001": "AI and humans in the loop", "CAP-001": "no-code index view",
            "CAP-024": "the same conformance corpora"})

    def test_relabels_links_and_headings(self) -> None:
        roots = [self.basis, self.ws / "repo"]
        changed = update_item_titles.update(roots, basis=self.basis)
        self.assertEqual(sorted(p.relative_to(self.ws).as_posix() for p in changed), [
            "mbse-basis/docs/capabilities/CAP-001.md", "mbse-basis/docs/capabilities/README.md",
            "repo/README.md", "repo/src/a.py"])
        readme = (self.ws / "repo/README.md").read_text()
        self.assertIn("[CAP-001: no-code index view](../mbse-basis/docs/capabilities/CAP-001.md)", readme)
        self.assertIn("[CAP-024: the same conformance corpora](../mbse-basis/docs/capabilities/README.md#CAP-024)", readme)
        self.assertIn("Not an item: [CAP-001](docs/CAP-001.md)", readme)
        self.assertIn("mismatched: [CAP-024](../mbse-basis/docs/capabilities/CAP-001.md)", readme)
        self.assertIn("unknown: [CAP-999](", readme)
        self.assertEqual((self.ws / "repo/src/a.py").read_text(),
                         '"""Serves [QUA-001: AI and humans in the loop](../../mbse-basis/docs/QUALITIES.md#QUA-001)."""\n')
        detail = (self.basis / "docs/capabilities/CAP-001.md").read_text()
        self.assertTrue(detail.startswith("# CAP-001: no-code index view\n"))
        self.assertIn("[CAP-024: the same conformance corpora](README.md#CAP-024)", detail)
        self.assertEqual((self.ws / "repo/data.bin").read_text(), "[CAP-001](../mbse-basis/docs/capabilities/CAP-001.md)\n")
        self.assertEqual(update_item_titles.update(roots, basis=self.basis), [])

    def test_check_writes_nothing(self) -> None:
        before = (self.ws / "repo/README.md").read_text()
        changed = update_item_titles.update([self.ws / "repo"], basis=self.basis, check=True)
        self.assertEqual(len(changed), 2)
        self.assertEqual((self.ws / "repo/README.md").read_text(), before)


if __name__ == "__main__":
    unittest.main()
