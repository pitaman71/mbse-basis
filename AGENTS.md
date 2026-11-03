# Guide for AI agents

mbse-basis states, once, what every mbse repository shares: qualities (QUA-), features (FEA-), capabilities (CAP-),
principles (PRI-) and vocabulary (VOC-), each with a permanent ID. It holds no library code, only the tools every repository runs from here
(`scripts/polyrepo.py`, `scripts/update_doc_links.py`, `scripts/update_item_titles.py`, `scripts/update_link_forms.py`; tests: `python3 -m unittest discover -s scripts`), standard
library only and kept small. Other repositories are its siblings, checked out beside it (`../mbse-schemas`, ...),
and cite its items by ID.

## Start here

Agents must read these documents before doing any work:

- [The mbse basis](docs/README.md)
- [Principles](docs/PRINCIPLES.md)
- [Features](docs/features/README.md)
- [Capabilities](docs/capabilities/README.md)

These may be read selectively, on demand: [Vocabulary](docs/VOCABULARY.md) and [Qualities](docs/QUALITIES.md).

## Invariants

- **Follow [docs/README.md](docs/README.md)**: the kinds of item and their relations, statuses, detail files and the
  rules for writing items are stated there once. This file restates none of them; a rule found here belongs there.
- Never write to `~/.claude/projects/*/memory/` or any hidden memory: what is worth keeping goes in the repository.
- Resolve a link written `mbse:<repo>/<path>`, as skills and source comments write a link into another mbse
  repository, to the first of these that exists: in a polyrepo checkout, `<repo root>/../<repo>/<path>`, where `<repo
  root>` is this repository's root; for a link into the installed package's own repository, `<path>` without its
  language directory (`python3/` or `typescript5/`), under the installed package's root (Python: the `site-packages`
  directory that holds `mbse/`; npm: the package's directory), where the package ships that file; otherwise
  `https://github.com/pitaman71/<repo>/blob/main/<path>`.
