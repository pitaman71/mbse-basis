# Stacked stores

Initiative: [INI-013: journals framework](PRIORITIES.md#ini-013--journals-framework).

Every layer between an app and where its data is kept is a store, mbse-schemas' `Store`: a cache that loads on demand,
a store served over REST, a store kept in a database. Each is stacked on another, so that an app composes what it
needs, and none of them moves a model as a snapshot. This proposes the stack, the change to mbse-schemas that makes a
store lazy, and what replaces each use of snapshots today.

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
- **An extent is found through ownership**: "A store client can compute this by introspecting schemas. Then closing
  ownership relations. The latter may be exposed as a store method if it is useful."

## The stack

Each layer is a `Store`, and each but the lowest is given the store below it:

- **A store kept in a database**, the lowest: its journal, the only record, kept as
  [the journal storage proposal](JOURNAL-STORAGE.md) states, and an index of each object's values and entries, kept
  current from the journal, from which it answers a read of one object. The index is the database's way of answering
  reads, never written apart from its journal, sent or moved between stores, so that it is no snapshot.
- **A store served over REST**, mbse-rest's: its service exposes any store, and its client is a store, so that a store
  in another process, or another machine, stacks like any other.
- **A cache**, a store over any store, which loads an object when it is first read, writes a transaction through as its
  effect ([CAP-270: a transaction's changes observed at its commit](../docs/capabilities/README.md#CAP-270)), and applies the effects of others' transactions, to which it subscribes, to
  what it has loaded. Its rolling checkpoint, a reliability measure, is its own: it never leaves the cache, and the
  cache rebuilt without it loses nothing.
- **The store kept in memory**, mbse-schemas' `Builders.Store` as it is today: every object held, nothing loaded; the
  test double that lets a front end and a back end each be unit-tested alone.

A browser's app, for one, stacks a cache on mbse-rest's client; mbse-rest's service, a cache on a database's store.

## A store that loads on demand

`Builders.Store` reads an object's data only through the store protocol, `values(holder)` and `entries(holder)`
([CAP-149: data accessed through the store protocol](../docs/capabilities/CAP-149.md)), and a transaction's proposals are already a layer over the store's committed
data, `_Committed`. What makes it eager is where that committed data is: on each proxy object, so that an object is in
the store only once its proxy is, and `extent` walks everything reachable from the singletons. The change, in Python
and TypeScript:

1. **The committed layer, pluggable.** `_Committed` becomes an interface, and today's behaviour its eager
   implementation, with no change of behaviour. Small.
2. **A committed layer that loads.** On the first read of an object's values or entries, it reads them from the store
   below, and keeps them. An entry loaded links objects not yet loaded, so that the store gives each a proxy, its
   identity kept by its reference ([CAP-130: references to objects, entries and frames](../docs/capabilities/CAP-130.md)) in an identity map, its
   singletons and ownership keys resolved on demand. This is the largest part, in the proxies' core, and the one to
   prototype first.
3. **Writes through, and others' writes in.** A commit sends its effect to the store below, as a journal entry; the
   cache applies each effect the store below observes to what it has loaded.
4. **Extent, through ownership.** `extent(name)`, the objects of a schema or of a schema refining it, is found as the
   user decided: the schemas give the ownership paths from the singletons that can reach `name`, and the extent is
   those paths' ownership relations closed, following only them. A lazy store fetches nothing eagerly to do so: the
   closure gives the extent's objects by reference, each a proxy that loads only when it is read, and no owner along
   the way is loaded. The closure of ownership may be a store method, which the store below answers in one call. A
   counted object, owned by nothing, is on no path: the counted mode of identity is being deprecated.

Steps 1 and 2 are mbse-schemas'; 3 joins what [CAP-270: a transaction's changes observed at its commit](../docs/capabilities/README.md#CAP-270) and mbse-journals'
subscriptions already give. Together, about three capabilities, each at least CAP-270's size; step 2's identity map is
where the estimate may grow.

## Snapshots today, and what replaces each

`Plain.ToPlain(store).Snapshot()` writes a store as two transactions, its schemas and then its data
([CAP-127: snapshots made of transactions](../docs/capabilities/CAP-127.md)): a store's state, made into a document. It is used:

| Where | For | Replaced by |
|---|---|---|
| mbse-rest's service, with mbse-dynamodb's plugin | Persistence: a snapshot every 100 transactions (`snapshot_every`), and startup from the latest one and the journal after it | The journal alone, below a cache that loads on demand; a cache's own rolling checkpoint, for a restart or a new instance |
| mbse-rest's `GET /schemas`, and its client | A store's schemas sent to a client, the first of a snapshot's two transactions | The install transactions that made the schemas, the head of the journal |
| The conformance corpora of mbse-schemas, mbse-expressions and mbse-patterns | Each case's store written as a snapshot, compared across the two languages | Open: see below |
| mbse-schemas' examples | A store copied into another | A journal replayed into the other |

## Open questions

- **The conformance corpora.** Each implementation writes each case's store as a snapshot, and the two are compared:
  a store analyzed as a snapshot. Writing each case as the journal that makes it would compare how the two languages
  write as well as what they hold; it touches the corpora of three repositories.
- **Reads over REST, one object at a time**, are many requests: whether mbse-rest's service answers a read of several
  objects, or of what one reaches, at once.
- **Where this is built in order**: after the journal and its storage interface in mbse-journals, or beside them, since
  steps 1 and 2 are mbse-schemas' alone.
