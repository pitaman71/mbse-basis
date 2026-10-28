# Guide for AI agents

mbse-basis states, once, what every mbse repository shares: qualities (QUA-), features (FEA-), capabilities (CAP-),
principles (PRI-) and vocabulary (VOC-), each with a permanent ID. It holds no library code, only the tools every repository runs from here
(`scripts/polyrepo.py`, `scripts/update_doc_links.py`; tests: `python3 -m unittest discover -s scripts`), standard
library only and kept small. Other repositories are its siblings, checked out beside it (`../mbse-schemas`, ...),
and cite its items by ID.

## Start here

Read [docs/README.md](docs/README.md): the kinds of item, their relations, statuses and the rules for writing them.
Then read the index of whichever kind your task touches; each is short enough to read whole.

## Invariants

- **Only what spans repositories belongs here.** A decision that holds in one repository stays in that repository's
  design documents, citing the items it applies. When a local decision turns out to be general, promote it here and
  replace the local text with a citation.
- **Follow the rules in [docs/README.md](docs/README.md#rules-for-writing-items)**: IDs are permanent, one entry per
  item, bridge don't duplicate (every link introduced by enough bridge language to read on without following it), edit
  never append, items may overlap, and each index stays short (about 10 KB, a guideline that yields to keeping the
  documents organized).
- **A modeling construct is named, not defined.** [VOCABULARY.md](docs/VOCABULARY.md) defines terms that are not
  constructs, and lists each construct with a link to the repository that defines it.
- **Record what the user decides as the user decides it.** Adopted items are the user's; an agent proposes, and records
  open items rather than resolving them silently.
- **Current status is checked, not guessed.** A capability's current status names where it was checked (a branch,
  a version, a test), or says it is to assess.
