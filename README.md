# mbse-basis

The mbse repositories kept deciding the same things separately, each restating what another had already decided, until
their design documents no longer fit in anyone's head or an agent's context. mbse-basis states those shared ideas
once, as a small ontology of features, principles, capabilities and vocabulary with permanent IDs, so that every other
repository cites them and records only its local differences. The markdown, notebooks and skills across the
repositories had grown past what any person or agent can absorb; keeping them consolidated, and not special-casing the
project into an unmanageable mess, is an ongoing priority.

It holds no library code, only the tools every repository runs from here: `scripts/polyrepo.py`, which manages the
sibling checkouts (`python3 ../mbse-basis/scripts/polyrepo.py help`), and `scripts/update_doc_links.py`, which writes
each document's navigation links; their tests are `python3 -m unittest discover -s scripts`. Start with
[the basis](docs/README.md).

Why the mbse repositories exist, and each one's part: [MBSE.md](MBSE.md).
