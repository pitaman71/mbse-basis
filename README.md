# mbse-basis

The mbse repositories kept deciding the same things separately, each restating what another had already decided, until
their design documents no longer fit in anyone's head or an agent's context. mbse-basis states those shared ideas
once, as a small ontology of features, principles, capabilities and vocabulary with permanent IDs, so that every other
repository cites them and records only its local differences.

It holds no code. Start with [the basis](docs/README.md).

| Repository | Its part |
|---|---|
| [mbse-schemas](https://github.com/pitaman71/mbse-schemas) | The structure: objects, relations and their properties |
| [mbse-expressions](https://github.com/pitaman71/mbse-expressions) | The constraints, as expressions in dialects |
| [mbse-patterns](https://github.com/pitaman71/mbse-patterns) | Constraints over populations of data: predicates, generators, transforms |
| [mbse-programs](https://github.com/pitaman71/mbse-programs) | The code: languages' syntax trees as data |
| [mbse-codegen-python](https://github.com/pitaman71/mbse-codegen-python) | Python generated from, and read back into, models |
