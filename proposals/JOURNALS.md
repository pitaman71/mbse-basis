# Journals

Initiative: [INI-013: journals framework](PRIORITIES.md#ini-013--journals-framework).

A journal is a store's history as a sequence of transactions, each written in a journal language that states exactly
what it changes. It is how a model is stored, communicated and analyzed: never as a snapshot. The journal language is
mbse-schemas' own, written in its schemas; the journal itself, its positions, files and streams, is a new repository's,
`mbse-journals`, depending on mbse-schemas alone, in Python and TypeScript; its outline is
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
- **The language is mbse-schemas' own** ("(b) agreed"): an entry is a transaction expression of mbse-schemas' own
  schemas, with no schema of its own, so that it is schema data, as
  [PRI-003: everything is schema data](../docs/PRINCIPLES.md#PRI-003) and [PRI-018: no model needs code to read or write](../docs/PRINCIPLES.md#PRI-018) require, and lives in the lowest repository that can own
  it, as [PRI-011: the lowest repository that can own it](../docs/PRINCIPLES.md#PRI-011) has it.
- **A journal's order is relations, never an order of entries** (2026-11-12): relation entries have no order,
  permanently, and ordering them would be a second-order invention; a sequenced container is relations that cooperate,
  as [FEA-058: parametric schema templates](../docs/features/FEA-058.md#decided) records.
- **An append that collides is refused by a unique clause** (2026-11-12): "a correct client will send - Last(container,a)
  + Last(container,b) in the same transaction", and where another appended first, "if - Last(container,a) is ignored
  because it has no effect then applying +Last(container,b) violates the unique clause"; "constraints are still under
  construction so it would be preferable not to rely on them for urgent functionality"
  ([CAP-293: an entry inserted against a unique clause refuses its transaction](../docs/capabilities/README.md#CAP-293)).
- **`Precedes` and `Follows` are held, as alternatives or complements** (2026-11-12): "They are stored as expressive
  alternatives or complements to After/Before. it is not necessary to infer the complete relation for any reason."
- **A database transaction around each journal transaction** (2026-11-12): "Backend bindings should use a database
  transaction around the journal transaction. This makes the db more or less responsible for serialization order."
- **A journal is downstream of a store's interpreter** (2026-11-12): "Mutation-transaction streams and change journals
  are not the same language - yet." "`Store` and `mbse-rest` currently communicate via Mutation-transaction streams.
  Ergo, all backends must interpret Mutation-transaction streams. A change journal on the other hand is an observer
  downstream of the mutation-transaction interpreter behind `Store`. Registering with `follow` any Store should cause
  the store to interpret whatever Mutation-transaction streams it is following and then report just the changes to any
  followers." So "journals store journal transactions which store changes": the changes a store reports, in the form
  of a transaction expression for now ([CAP-271: the journal language](../docs/capabilities/README.md#CAP-271)), are recorded as the journal's own data, (a) of
  the two ways the user was offered: "(a) is fine for now".
- **A journal is kept in any store, through the store interface** (2026-11-12): the journal storage interface is the
  store interface, "exactly" ([the journal storage proposal](JOURNAL-STORAGE.md#the-interface-and-how-a-backend-is-held-to-it)).
- **A counted object is immutable**: "Any change to a counted object, which is immutable, results in copy-on-write". It
  is written by value where it is linked, so that nothing is refused or dropped
  ([PRI-002: preserve, don't lose](../docs/PRINCIPLES.md#PRI-002)).

## The journal, a sequenced container

A journal is a container of its entries, in mbse-journals' own schemas, its order the relations that cooperate to make
a sequenced container ([FEA-058: parametric schema templates](../docs/features/FEA-058.md#decided)), declared there until a template declares them in one
([CAP-292: a sequenced container declared by one template](../docs/capabilities/README.md#CAP-292)): each entry `Contains`, the `First` and the `Last`, each entry's
immediate neighbours, `Before` and `After`, and, held where they say what is known, `Precedes` and `Follows`, never
inferred from the others. A position is an entry, never a number: a reader reads, or subscribes,
from an entry, following `After`. An entry appended after the last removes `Last(journal, a)` and inserts
`Last(journal, b)` and `After(journal, a, b)` in one transaction, which a unique clause refuses where another appended
first; an entry inserted at a view's position, between `a` and `b`, removes `After(journal, a, b)` and inserts
`After(journal, a, x)` and `After(journal, x, b)`. A backend applies each journal transaction within a database
transaction, so that the database orders them.

## The journal language

A journal is a sequence of entries, one per transaction. An entry is its symbols, then its mutations, in order:

- **A. An object exists.** Each symbol is bound, before anything uses it, either to an object that exists, by its
  reference, or to a new object of a schema. Nothing is matched: an entry says which. A new owned object takes its
  identity from its ownership entry, added by the same entry's mutations. A counted object, immutable, is not bound: it
  is defined by value where it is linked, and a change to one is a new one, copied on write.
- **B. A relation entry is added or removed.** An entry of a relation, its links each a symbol, and its properties, such
  as an ownership entry's `name`. Removing an object's ownership entry deletes the object, as mbse-schemas does, and
  in cascade every entry linking it and what it owns. An entry never names an object it deletes: it removes the
  ownership entry by its owner's key for it, and what goes with it follows, in every store that applies it.
- **C. A property is mutated.** On a symbol, a property and its mutation verbs, mbse-schemas' own: `set` and `clear`
  on any value, and, nested, the verbs of the value's schema kind on a part of it, a container's items or a union's
  branch.

Applying an entry makes what it states hold, and applying it again changes nothing: an object bound as new that exists
is bound to it, an entry added that is held is left, an entry removed that is absent is left, a value set that holds is
left. A symbol is the entry's own.

An entry is a transaction expression: an upsert whose symbols are bound to references, or to schemas for the objects it
makes, each found by its ownership entry, and whose spec inserts and removes relation entries and sets and clears
properties, in mbse-schemas' verbs. The changes a transaction makes are observed at its commit, and written as an entry
in this language: its effect. A reader sections an effect into the model's mutations exactly, as the diagrams
framework's layout engine does
([CAP-261: layout driven by any journal entry](../docs/capabilities/README.md#CAP-261)).

## Decided by an agent, for review

Where the user's decisions were silent, the simplest default consistent with them, each *proposed* until reviewed,
labeled with the repository and number it was decided under.

- **(mbse-journals 1)** **Names.** `Framework.Journals`: `install`, `journal(store, name)`, `append`, `insert`,
  `transactions`, `changes`, `follow`, `record` and `replay`. The singleton `Journals.Directory` owns each journal by
  its name; a journal owns its journal transactions (`Journals.Contains`); `Journals.Before(journal, earlier, later)`
  is read from the earlier as `next` and from the later as `previous`.
- **(mbse-journals 1)** **A journal transaction's changes as the journal's own data.** Each object the changes name is
  a binding, the `reference` of one the store held or the `schema` of one it made; each change an entry inserted or
  removed, on its holder's adjacency, with its other links' bindings and its properties' values, or a property set or
  cleared, with its value. Bindings and changes are each an indexed container, its index an entry property, as the
  user allows ("Indexed containers can have their index encoded as entry props"), so that the order the reported
  changes were written in is kept.
- **(mbse-journals 1)** **Plain forms carried as written.** A reference, a schema's path and a value are each held as
  their plain form, as text ([PRI-024: the plain form, carried as written](../docs/PRINCIPLES.md#PRI-024)), so that a journal store holds the journal's schemas
  alone, and not those of the store it records.
- **(mbse-journals 1)** **A journal transaction's name is given by its writer** where others append too: two writers
  counting alike would name two different transactions alike, and a store applying the other's changes would take one
  for the other. A single writer's are named `t` and their count.
- **(mbse-journals 1)** **Following a journal** gives a follower each journal transaction in order, from the first or
  after one, then each appended, by the journal store's own change observation; a transaction inserted before where a
  follower has reached is not given to it.

