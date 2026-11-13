# Stacked stores

Initiative: [INI-013: journals framework](PRIORITIES.md#ini-013--journals-framework).

There is one store interface, lazy by default ([FEA-028: one Store interface, lazy by default](../docs/features/FEA-028.md)): every layer between an
app and where its data is kept implements it, and each is stacked on another, so that an app composes what it needs,
and none of them moves a model as a snapshot. mbse-schemas' `Builders.Store` becomes lazy itself: given a store below
it, it loads from it on demand, and how much it keeps, lazy or eager, is decided when it runs
([QUA-018: lazy or eager, decided at runtime](../docs/QUALITIES.md#QUA-018)). This proposes the stack, the change to `Builders.Store`, and what replaces each use of
snapshots today.

## Decided

The user's decisions (2026-11-12):

- **No snapshots in the framework, but for checkpoints**: "I'm really trying to avoid snapshotting at all in the
  framework - except for a rolling checkpoint/restore for reliability, possibly some for hot-scaling." A model is
  stored, communicated and analyzed in journal form ([FEA-056: fungible diagramming keeps agents and humans in the loop](../docs/features/FEA-056.md#decided)).
- **A cache is a store, stacked on a store**: "caching is fine and a good thing to implement, but it be fully
  self-contained and it should implement `mbse-schemas.Store` so it can be cleanly stacked on top of another `Store`
  implementation that persists locally in memory, to file, or remotely via mbse-rest."
- **mbse-rest serves a store**: "the whole purpose of `mbse-rest` is to expose a `Store` instance via an encapsulated
  REST interface with both endpoints provided, verified, and battle-tested for any possible deployment."
- **Loaded on demand**: "I'd rather use caching that loads on demand than a toy in-memory store that pulls everything
  up-front."
- **An object is present or it is not**: "A path either is or is not present in the builder, and the builder should
  not create the object silently." An object is present in a store, made in it or loaded into it, or it is not; and
  where it is not, the store asks the store below.
- **An extent is found through ownership**: "A store client can compute this by introspecting schemas. Then closing
  ownership relations. The latter may be exposed as a store method if it is useful."

## The stack

Each layer implements the store interface, and each but the lowest is given the store below it:

- **A store kept in a database**, the lowest: its journal, the only record, kept as
  [the journal storage proposal](JOURNAL-STORAGE.md) states, and an index of each object's values and entries, kept
  current from the journal, from which it answers a read of one object. The index is the database's way of answering
  reads, never written apart from its journal, sent or moved between stores, so that it is no snapshot.
- **A store served over REST**, mbse-rest's: its service exposes any store, and its client implements the interface,
  so that a store in another process, or on another machine, stacks like any other. It may refuse a mode the interface
  offers, as [FEA-028: one Store interface, lazy by default](../docs/features/FEA-028.md#decided) allows, but implements every method.
- **`Builders.Store`**, the one store a program holds, lazy: given a store below, it loads an object when it is first
  read, writes a transaction through as its effect ([CAP-270: a transaction's changes observed at its commit](../docs/capabilities/README.md#CAP-270)), and applies the
  effects of others' transactions, to which it subscribes, to what it has loaded. What it is, a cache, is a matter of
  what lies below it, not a kind of store of its own; its rolling checkpoint, a reliability measure, is its own, never
  leaving it, and it rebuilt without one loses nothing. Given no store below, it holds only what is written to it, in
  memory, as it does today: the test double that lets a front end and a back end each be unit-tested alone.

A browser's app, for one, holds a `Builders.Store` over mbse-rest's client; mbse-rest's service, a `Builders.Store` over
a database's store.

## A lazy `Builders.Store`

`Builders.Store` reads an object's data only through the store protocol, `values(holder)` and `entries(holder)`
([CAP-149: data accessed through the store protocol](../docs/capabilities/CAP-149.md)), and a transaction's proposals are already a layer over the store's committed
data, `_Committed`. What makes it eager is where that committed data is: on each proxy object, so that an object is in
the store only once its proxy is, and `extent` walks everything reachable from the singletons. The change, in Python
and TypeScript:

1. **A store below.** `Builders.Store` is given the store below it, or none; its committed layer, `_Committed`, reads
   through it. With none, it behaves as it does today. Small, and no change of behaviour.
2. **Loading on demand.** On the first read of an object's values or entries, the committed layer reads them from the
   store below, and keeps them. An entry loaded links objects not yet loaded, so that the store gives each a proxy, its
   identity kept by its reference ([CAP-130: references to objects, entries and frames](../docs/capabilities/CAP-130.md)) in an identity map, its
   singletons and ownership keys resolved on demand. This is the largest part, in the proxies' core, and the one to
   prototype first.
3. **Writes through, and others' writes in.** A commit sends its effect to the store below, as a journal entry; the
   store applies each effect the store below observes to what it has loaded.
4. **Extent, through ownership.** `extent(name)`, the objects of a schema or of a schema refining it, is found as the
   user decided: the schemas give the ownership paths from the singletons that can reach `name`, and the extent is
   those paths' ownership relations closed, following only them. A lazy store fetches nothing eagerly to do so: the
   closure gives the extent's objects by reference, each a proxy that loads only when it is read, and no owner along
   the way is loaded. The closure of ownership may be a store method, which the store below answers in one call. A
   counted object, owned by nothing, is on no path: the counted mode of identity is being deprecated.
5. **Lazy or eager, tuned when it runs.** What the store loads ahead, a whole extent or what an object reaches, and
   what it keeps or lets go, are settings given when it runs, not code that uses it: lazy by default, as eager as an
   app asks.

Steps 1, 2, 4 and 5 are mbse-schemas'; 3 joins what [CAP-270: a transaction's changes observed at its commit](../docs/capabilities/README.md#CAP-270) and mbse-journals'
subscriptions already give. Together, about three or four capabilities, each at least CAP-270's size; step 2's
identity map is where the estimate may grow.

## Writing through, and others' writes in: what CAP-285 must decide

[CAP-285: writes through, others' writes in](../docs/capabilities/README.md#CAP-285) joins a store above to the store below in both directions. Building it raises
three questions, each with the agent's recommendation, for the user to decide:

1. **Which commits first.** The store below may refuse a transaction, alike in every store that considers it (a
   colliding append, [CAP-293: an entry inserted against a unique clause refuses its transaction](../docs/capabilities/README.md#CAP-293)), so that the store above must not have committed it
   where it does. *Recommended:* the store above sends a transaction's changes down before its own commit, within it,
   and commits only where the store below accepts them; a refusal there refuses the transaction above. This needs the
   changes written as plain data before the commit, which mbse-schemas writes now only after it, since writing them as
   a transaction expression writes to the store.
2. **What another writer's changes do above.** The store below reports each transaction it commits, its own and
   others' alike. *Recommended:* the store above applies each to the objects it holds and to no other, an object not
   present staying so, as a link to one not present is held by its path; its own come back changing nothing, since
   applying changes again changes nothing; and its followers are told of what changed above, as of any transaction of
   its own.
3. **When.** *Recommended:* synchronously, as a store in memory below gives them; a store over a database or over REST
   gives them as its change feed delivers them, and the store above applies them in the order given, each as it
   arrives, so that the order the store below committed them in is the order above.

## Capabilities

In [INI-013: journals framework](PRIORITIES.md#ini-013--journals-framework): the five steps above are
[CAP-283: a store given a store below](../docs/capabilities/README.md#CAP-283), [CAP-284: objects loaded on demand](../docs/capabilities/README.md#CAP-284), [CAP-285: writes through, others' writes in](../docs/capabilities/README.md#CAP-285),
[CAP-286: an extent through ownership](../docs/capabilities/README.md#CAP-286) and [CAP-287: lazy or eager, tuned when it runs](../docs/capabilities/README.md#CAP-287), in mbse-schemas; mbse-rest's part is
[CAP-290: a service's store stacked, with no snapshot](../docs/capabilities/README.md#CAP-290).

## Snapshots today, and what replaces each

`Plain.ToPlain(store).Snapshot()` writes a store as two transactions, its schemas and then its data
([CAP-127: snapshots made of transactions](../docs/capabilities/CAP-127.md)): a store's state, made into a document. It is used:

| Where | For | Replaced by |
|---|---|---|
| mbse-rest's service, with mbse-dynamodb's plugin | Persistence: a snapshot every 100 transactions (`snapshot_every`), and startup from the latest one and the journal after it | The journal alone, below a lazy `Builders.Store`; that store's own rolling checkpoint, for a restart or a new instance |
| mbse-rest's `GET /schemas`, and its client | A store's schemas sent to a client, the first of a snapshot's two transactions | The install transactions that made the schemas, the head of the journal |
| The conformance corpora of mbse-schemas, mbse-expressions and mbse-patterns | Each case's store written as a snapshot, compared across the two languages | Open: see below |
| mbse-schemas' examples | A store copied into another | A journal replayed into the other |

## Decided by an agent, for review

Where the user's decisions were silent, the simplest default consistent with them, each *proposed* until reviewed,
labeled with the repository and number it was decided under.

- **(mbse-schemas 30)** **What a store below answers: an object's document.** `document(path)` gives the object at a
  path as a one-transaction document ([CAP-128: graphs sent as one-transaction documents](../docs/capabilities/CAP-128.md)), its properties and its entries, each
  object they link by its path; None where it holds none. It is a mutation-transaction stream, the language stores
  already speak, so that a database's store and mbse-rest's client answer it alike, with no new form.
- **(mbse-schemas 30)** **Identity by path.** An object loaded from the store below is one proxy, kept by its path, the
  same each time it is named. A path resolves to an object present, through its owner's entries where it was made
  above, else to the store below's, loaded, else to none: one read, of the object named, and no owner loaded.
- **(mbse-schemas 30)** **A link to an object not present holds its path.** An entry the store below gives that links
  an object not present holds that object's path, and is held by the objects present it links; reading the link loads
  the object, which every entry waiting on its path then links, re-keyed. Nothing is made that is not present. Whether
  a link owns what it links is known from the relation, without the object: a relation that owns through a link owns
  whatever it links.
- **(mbse-schemas 30)** **Changes reported name what the store holds.** Removing the owning entry of an object not
  present deletes it, and is reported by its owner's key, as any deletion is; anything else the reported changes name
  is loaded first.
- **(mbse-schemas 30)** **Loading is no transaction of the store's.** An object's document is applied as the store's
  committed data, outside any transaction open, observed by no follower, recorded by no provenance and checked by
  nothing.

## Open questions

- **The conformance corpora.** Each implementation writes each case's store as a snapshot, and the two are compared:
  a store analyzed as a snapshot. Writing each case as the journal that makes it would compare how the two languages
  write as well as what they hold; it touches the corpora of three repositories.
- **Changes reported for entries kept by identity.** A builder's update of an object rewrites its entries of a relation
  with no unique clause, kept by identity, and the store reports each as removed and inserted, though nothing changed:
  found building [CAP-284: objects loaded on demand](../docs/capabilities/README.md#CAP-284), and as true of a store with no store below. A gap in
  [CAP-270: a transaction's changes observed at its commit](../docs/capabilities/README.md#CAP-270), to log where [INI-104: gaps plan category](PRIORITIES.md#ini-104--gaps-plan-category) logs gaps.
- **Reads over REST, one object at a time**, are many requests: whether mbse-rest's service answers a read of several
  objects, or of what one reaches, at once.
- **Where this is built in order**: after the journal and its storage interface in mbse-journals, or beside them, since
  steps 1 and 2 are mbse-schemas' alone.
