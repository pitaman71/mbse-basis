# Journals

Initiative: [INI-013: journals framework](PRIORITIES.md#ini-013--journals-framework).

A journal is a store's history as a sequence of transactions, each written in a journal language that states exactly
what it changes. It is how a model is stored, communicated and analyzed: never as a snapshot. The journal language is
mbse-schemas' own, written in its schemas; the journal itself, its positions, files and streams, is a new repository's,
`mbse-journals`, depending on mbse-schemas alone, in Python and TypeScript.

A transaction expression, as mbse-schemas executes it, reads like a query: an upsert finds or creates, a map ranges over
what matches, and a spec writes only where it does not hold, so what it changes depends on the state it meets. A journal
transaction is that transaction's effect, resolved: it says what changed, and nothing is matched or searched for.

## Decided

The user's decisions:

- **mbse-journals is its own initiative**, INI-013.
- **The journal language has three parts**: "A. object exists (basically just a symbol binding) B. relation entry add
  / remove C. property mutate (using mutation verbs already in mbse-schemas)".
- **An object is referred to by `References.OfObject`** ([CAP-130: references to objects, entries and frames](../docs/capabilities/CAP-130.md)).
- **Symbols do not cross transactions**: "journals remain fundamentally partitioned into transactions and symbols do
  not reuse across transaction boundaries."
- **Applying a journal transaction is idempotent.**
- **Values are written by their property's schema**: "C's values should be serialized and deserialized according to
  the property's schema as always".
- **Surgical mutations of a property's value**: "journals [will] support not just set and get on whole property
  values, but also surgical mutations on subtrees of the property state using schema-appropriate mutation verbs. A
  container for example has clear, set, and get but also has insert (after/before/first/last) etc.", and "clear"
  applies to any property value.
- **The language is mbse-schemas' own** ("(b) agreed"; its form superseded by "`Changes` schemas", 2026-11-17, below;
  that the language is mbse-schemas' own stands): a journal transaction is a transaction expression of
  mbse-schemas' own schemas, with no schema of its own, so that it is schema data, as
  [PRI-003: everything is schema data](../docs/PRINCIPLES.md#PRI-003) and
  [PRI-018: no model needs code to read or write](../docs/PRINCIPLES.md#PRI-018) require, and lives in the lowest
  repository that can own it, as [PRI-011: the lowest repository that can own it](../docs/PRINCIPLES.md#PRI-011) has it.
- **A journal's order is relations, never an order of its transactions** (superseded: a journal is not kept in a
  store, and holds no relations; see "a store's data knows nothing about journals", below): relation entries have no order,
  permanently, and ordering them would be a second-order invention; a sequenced container is relations that cooperate,
  as [FEA-058: parametric schema templates](../docs/features/FEA-058.md#decided) records.
- **An append that collides is refused by a unique clause** (2026-11-12; superseded, as the order above is): "a correct client
  will send - Last(container,a) + Last(container,b) in the same transaction", and where another appended first, "if -
  Last(container,a) is ignored because it has no effect then applying +Last(container,b) violates the unique clause";
  "constraints are still under construction so it would be preferable not to rely on them for urgent functionality"
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
  (Superseded by "a journal is data", below: a journal is built without a store.)
- **A counted object is immutable**: "Any change to a counted object, which is immutable, results in copy-on-write". It
  is written by value where it is linked, so that nothing is refused or dropped
  ([PRI-002: preserve, don't lose](../docs/PRINCIPLES.md#PRI-002)).

The user's decisions (2026-11-17):

- **A journal is data**: "a journal is data. It's passive. We need to be able to construct it, build it, splice it,
  stream it, etc. without a store."
- **A subsection of a journal is a journal**: "Journals comprise transactions. A subsection of a journal (of whole
  transactions) is still a journal, which fundamentally supports streaming between peers synchronizing some data."
- **Schema-governed throughout**: "The transactions, changes, and journal object itself should be mbse schema governed
  data. mbse-schemas then provides built-in utilities for serialization, comparison, etc."
- **Iteration is its API**: "As data, the journal must provide at least an iteration api. That may be it."
- **A journal is not a follower**: "A journal is not a follower. A follower is a subscription object owned by a store
  that watches for transactions, forwards the effective changes from each transaction on a store as a
  single-transaction journal streamed to registered observers." This is the follower of "a journal is downstream of a
  store's interpreter", above, and the follow of [CAP-315: every read within a transaction or through a follow](../docs/capabilities/CAP-315.md).
- **`Changes` schemas, a temporary exception**: of the two forms offered for a transaction's changes, (a) a `Changes`
  schema module in mbse-schemas and (b) a transaction expression of the existing `Mutations` schemas, the user takes
  (a): "I don't see this as a second order invention but rather a temporary exception to the rule to allow us to
  envision what the future of changes, mutations, and queries should look like", as
  [PRI-022: second-order inventions by approval](../docs/PRINCIPLES.md#PRI-022) permits. Their names are of the form
  "`Changes.Journal`, `Changes.Transaction`, `Changes.Symbol`, `Changes.OfProperty`, `Changes.OfEntry` or somesuch".
- **mbse-journals' store-held form is the second-order invention**: "The 'third form for storage' actually seems more
  like a second order invention than (a)": the journal transactions, symbol bindings and changes mbse-journals keeps as
  reference objects of its own schemas, their values as text.
- **A counted object is held inline**: in a `Changes.Transaction`, a counted object is written by value, "inline", in
  the entry change or property change that links it, not bound to a symbol.
- **A transaction carries a unique id**: "yes a unique id".
- **A store's data knows nothing about journals**: "Stored objects, entries, etc. know nothing about journals. Why would
  they?" A journal is not kept in a store. "Journal is not an extension of Store, and never has been".

## The journal, a sequenced container

A journal is a container of its transactions, in mbse-journals' own schemas, its order the relations that cooperate to
make a sequenced container ([FEA-058: parametric schema templates](../docs/features/FEA-058.md#decided)), declared there
until a template declares them in one
([CAP-292: a sequenced container declared by one template](../docs/capabilities/README.md#CAP-292)): each transaction
`Contains`, the `First` and the `Last`, each transaction's immediate neighbours, `Before` and `After`, and, held where
they say what is known, `Precedes` and `Follows`, never inferred from the others. A position is a transaction, never a
number: a reader reads, or subscribes, from a transaction, following `After`. A transaction appended after the last
removes `Last(journal, a)` and inserts `Last(journal, b)` and `After(journal, a, b)` in one transaction, which a unique
clause refuses where another appended first; a transaction inserted at a view's position, between `a` and `b`, removes
`After(journal, a, b)` and inserts `After(journal, a, x)` and `After(journal, x, b)`. A backend applies each journal
transaction within a database transaction, so that the database orders them.

## The journal language

A journal is a sequence of journal transactions, one per transaction committed. A journal transaction is its symbols,
then its mutations, in order:

- **A. An object exists.** Each symbol is bound, before anything uses it, either to an object that exists, by its
  reference, or to a new object of a schema. Nothing is matched: a journal transaction says which. A new owned object
  takes its identity from its ownership entry, added by the same journal transaction's mutations. A counted object,
  immutable, is not bound: it is defined by value where it is linked, and a change to one is a new one, copied on write.
- **B. A relation entry is added or removed.** An entry of a relation, its links each a symbol, and its properties, such
  as an ownership entry's `name`. Removing an object's ownership entry deletes the object, as mbse-schemas does, and in
  cascade every relation entry linking it and what it owns. A journal transaction never names an object it deletes: it
  removes the ownership entry by its owner's key for it, and what goes with it follows, in every store that applies it.
- **C. A property is mutated.** On a symbol, a property and its mutation verbs, mbse-schemas' own: `set` and `clear`
  on any value, and, nested, the verbs of the value's schema kind on a part of it, a container's items or a union's
  branch.

Applying a journal transaction makes what it states hold, and applying it again changes nothing: an object bound as new
that exists is bound to it, a relation entry added that is held is left, a relation entry removed that is absent is
left, a value set that holds is left. A symbol is the journal transaction's own.

A journal transaction is a transaction expression: an upsert whose symbols are bound to references, or to schemas for
the objects it makes, each found by its ownership entry, and whose spec inserts and removes relation entries and sets
and clears properties, in mbse-schemas' verbs. The changes a transaction makes are observed at its commit, and written
as a journal transaction in this language: its effect. A reader sections an effect into the model's mutations exactly,
as the diagrams framework's layout engine does
([CAP-261: layout driven by any journal transaction](../docs/capabilities/README.md#CAP-261)).

## The `Changes` schemas (proposed)

A sketch, for the user's review, of the `Changes` schemas: the journal language's A, B and C as value object schemas
in mbse-schemas, so that a journal is built, spliced, streamed, written, read and compared as any value is, with no
store.

| Schema | What it holds |
|---|---|
| `Changes.Journal` | Its transactions, in order: an ordered container of `Changes.Transaction`. A subsection of whole transactions is a `Changes.Journal` too. |
| `Changes.Transaction` | Its symbols, each by its name, then its changes, in order: an ordered container whose elements are a `Changes.OfEntry` or a `Changes.OfProperty`. |
| `Changes.Symbol` | A: an object exists. Either an object the store held, by its `References.OfObject`, or a new object of a schema, by the schema's reference. |
| `Changes.OfEntry` | B: a relation entry `inserted` or `removed`, on its holder's adjacency: the holder's symbol, the adjacency's name, each other link's symbol by the link's name, and the entry's properties' values. |
| `Changes.OfProperty` | C: a property mutated: its holder's symbol, the property's name, and its mutations, mbse-schemas' verbs of the value's schema kind, `set` and `clear` on any value. |

A value is written by its property's schema, marked with its schema where the reader cannot tell it
([PRI-025: never guess the schema](../docs/PRINCIPLES.md#PRI-025)). A store's effect, as `Changes.observe` gives it, is
a `Changes.Journal` of one transaction, the form a follower streams. Applying a transaction stays idempotent, and a
symbol stays the transaction's own. A counted object is written inline, by value, in the change that links it, and a
`Changes.Transaction` carries a unique id (decided above).

## Decided by an agent, for review

Where the user's decisions were silent, the simplest default consistent with them, each *proposed* until reviewed,
labeled with the repository and number it was decided under.

- **(mbse-journals 1)** **Names.** (Superseded by "iteration is its API" and "a journal is not a follower", 2026-11-17.)
  `Framework.Journals`: `install`, `journal(store, name)`, `append`, `insert`, `transactions`, `changes`, `follow`,
  `record` and `replay`. The singleton `Journals.Directory` owns each journal by its name; a journal owns its journal
  transactions (`Journals.Contains`); `Journals.Before(journal, earlier, later)` is read from the earlier as `next` and
  from the later as `previous`.
- **(mbse-journals 1)** **A journal transaction's changes as the journal's own data.** (Superseded by "`Changes`
  schemas, a temporary exception", 2026-11-17.) Each object the changes name is a
  symbol binding, the `reference` of one the store held or the `schema` of one it made; each change an entry inserted or
  removed, on its holder's adjacency, with its other links' symbol bindings and its properties' values, or a property
  set or cleared, with its value. Symbol bindings and changes are each an indexed container, its index an entry
  property, as the user allows ("Indexed containers can have their index encoded as entry props"), so that the order the
  reported changes were written in is kept.
- **(mbse-journals 1)** **Plain forms carried as written.** (Superseded, as the form above is.) A reference, a schema's reference and a value are each held
  as their plain form, as text ([PRI-024: the plain form, carried as written](../docs/PRINCIPLES.md#PRI-024)), so that a
  journal store holds the journal's schemas alone, and not those of the store it records.
- **(mbse-journals 1)** **A journal transaction's name is given by its writer** (superseded by "a transaction carries a
  unique id", 2026-11-17) where others append too: two writers
  counting alike would name two different transactions alike, and a store applying the other's changes would take one
  for the other. A single writer's are named `t` and their count.
- **(mbse-journals 1)** **Following a journal** (superseded by "a journal is not a follower", 2026-11-17) gives a
  follower each journal transaction in order, from the first or after one, then each appended, by the journal store's
  own change observation; a transaction inserted before where a follower has reached is not given to it.

## Open questions

The 2026-11-17 decisions leave these open:

1. **Value or reference objects** (proposed below, in [the `Changes` schemas](#the-changes-schemas-proposed)). mbse-schemas holds reference objects only in a store, and links only reference
   objects by relations. A journal built without a store would be a value object, its transactions in order in an
   ordered container. Then its order is not relations, and the decisions on a journal's order and on an append refused
   by a unique clause, above, do not hold: a journal is not kept in a store.
2. **The change transaction's schema** (proposed below, in [the `Changes` schemas](#the-changes-schemas-proposed)). A journal transaction is written now as a transaction expression of
   mbse-schemas' own schemas, "for now" ("a journal is downstream of a store's interpreter", above); schema-governed
   transactions and changes may want a schema of their own, the journal language's A, B and C.
3. **Where `record` and `replay` go.** Recording a store's transactions is a follower's work, and applying a journal to
   a store is a store's; neither is the journal's.
4. **The capabilities that describe a journal kept in a store**:
   [CAP-273: journals in memory and in local files](../docs/capabilities/README.md#CAP-273),
   [CAP-274: journals sent and received](../docs/capabilities/README.md#CAP-274) and
   [CAP-288: the journal storage interface](../docs/capabilities/README.md#CAP-288), revised once the questions above are.
