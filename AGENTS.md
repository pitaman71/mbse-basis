# Guide for AI agents

mbse-basis states, once, what every mbse repository shares: qualities (QUA-), features (FEA-), capabilities (CAP-),
principles (PRI-) and vocabulary (VOC-), each with a permanent ID. It holds no library code, only the tools every repository runs from here
(`scripts/polyrepo.py`, `scripts/update_doc_links.py`, `scripts/update_item_titles.py`; tests: `python3 -m unittest discover -s scripts`), standard
library only and kept small. Other repositories are its siblings, checked out beside it (`../mbse-schemas`, ...),
and cite its items by ID.

## Start here

Read [docs/README.md](docs/README.md): the kinds of item, their relations, statuses and the rules for writing them.
Then read the index of whichever kind your task touches; each is short enough to read whole.

## Invariants

- **Follow [docs/README.md](docs/README.md)**: the kinds of item and their relations, statuses, detail files and the
  rules for writing items are stated there once. This file restates none of them; a rule found here belongs there.
- Never write to `~/.claude/projects/*/memory/` or any hidden memory: what is worth keeping goes in the repository.
