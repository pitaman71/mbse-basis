# Journals

Initiative: [INI-013: journals framework](PRIORITIES.md#ini-013--journals-framework).

A journal is a store's history as a sequence of transactions, each written in a journal language that states exactly
what it changes. It is how a model is stored, communicated and analyzed: never as a snapshot. A new repository,
`mbse-journals`, depending on mbse-schemas alone, builds it in Python and TypeScript; its outline is
[CAP-199: journals as queryable stores (mbse-journals)](../docs/capabilities/CAP-199.md).

A transaction expression, as mbse-schemas executes it, reads like a query: an upsert finds or creates, a map ranges
over what matches, and a spec writes only where it does not hold, so what it changes depends on the state it meets.
A journal entry is that transaction's effect, resolved: it says what changed, and nothing is matched or searched for.

## Decided

The user's decisions (2026-11-11):

- **mbse-journals is its own initiative**, INI-013.
- **The journal language has three parts**: "A. object exists (basically just a symbol binding) B. relation entry add
  / remove C. property mutate (using mutation verbs already in mbse-schemas)".
- **An object is referred to by `References.OfObject`** ([CAP-130: references to objects, entries and frames](../docs/capabilities/CAP-130.md)).
- **Symbols do not cross transactions**: "journals remain fundamentally partitioned into transactions and symbols do
  not reuse across transaction boundaries."
- **Applying an entry is idempotent.**
- **Values are written by their property's schema**: "C's values should be serialized and deserialized according to
  the property's schema as always".
- **Surgical mutations of a property's value**: "journals [will] support not just set and get on whole property
  values, but also surgical mutations on subtrees of the property state using schema-appropriate mutation verbs. A
  container for example has clear, set, and get but also has insert (after/before/first/last) etc.", and "clear"
  applies to any property value.

## The journal language

A journal is a sequence of entries, one per transaction. An entry is its symbols, then its mutations, in order:

- **A. An object exists.** Each symbol is bound, before anything uses it, either to an object that exists, by its
  reference, or to a new object of a schema. Nothing is matched: an entry says which. A new owned object takes its
  identity from its ownership entry, added by the same entry's mutations.
- **B. A relation entry is added or removed.** An entry of a relation, its links each a symbol, and its properties, such
  as an ownership entry's `name`. Removing an object's ownership entry deletes the object, as mbse-schemas does.
- **C. A property is mutated.** On a symbol, a property and its mutation verbs, mbse-schemas' own: `set` and `clear`
  on any value, and, nested, the verbs of the value's schema kind on a part of it, a container's items or a union's
  branch.

Applying an entry makes what it states hold, and applying it again changes nothing: an object bound as new that exists
is bound to it, an entry added that is held is left, an entry removed that is absent is left, a value set that holds is
left. A symbol is the entry's own.

The changes a transaction makes are observed at its commit, and written as an entry in this language: its effect. A
reader sections an effect into the model's mutations exactly, as the diagrams framework's layout engine does
([CAP-261: layout driven by any journal entry](../docs/capabilities/README.md#CAP-261)).
