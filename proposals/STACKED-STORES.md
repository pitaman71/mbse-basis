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

The user's decisions (2026-11-14):

- **A transaction is recorded once, in the lowest store** ("yes, the lowest store"): a store above records none
  (`Provenance`), and sends the transaction's `uid`, `when`, `session` and `where` below with its changes; the record the
  lowest store makes reaches the stores above as the store below's writes do.
- **A store below that answers later is a capability of its own** ("agreed - make it a separate CAP"):
  [CAP-304: a store below that answers later](../docs/capabilities/README.md#CAP-304).

The user's decisions (2026-11-15):

- **What a store asks of the store below it is a public interface**, a capability of its own ("yes"):
  [CAP-306: a public store-below interface](../docs/capabilities/README.md#CAP-306), so that a store below depends on no
  private part of mbse-schemas ([PRI-043: framework interfaces authoritative and versatile](../docs/PRINCIPLES.md#PRI-043)).
- **An install reaches the store below by a member of its own**: of an `install(plain)` beside `commit` and `follow`,
  or installs sent through `commit` and reported by `follow`, the user chose the first ("1."). `commit` and `follow` carry
  data changes alone; a store runs each install the store below first, so that a store below given no schemas of its
  own holds those of the stores above it. Whether a journal is headed by its installs stays open.

The user's decision (2026-11-16), on conformance corpora:

- **A corpus is frames, in mbse-programs**: each case is the `References.OfFrame` of the transaction that builds it,
  written as any value is (`References.of(store, frame)`), its `binds` each object's reference and its `assigns` its
  properties: "transaction is one representation but may be difficult to compare. Frame I think already has equality
  and comparison". Recorded here at the user's word, for the conformance corpora below.

The user's decisions (2026-11-16), on the stack as CAP-283 to CAP-285 and CAP-306 built it, a store above interpreting
each transaction itself, loading each object it reads by a request of its own, and sending what it changed below:

- **One Store interface**: "we also invented a second store interface when a single interface was required by the
  design". `Stores.Below` is withdrawn with [CAP-306: a public store-below interface](../docs/capabilities/README.md#CAP-306).
- **Atomicity is the database's**: the interface as built "breaks persistence-enforced atomicity", a transaction's
  reads being made apart from its writes, and one transaction above being many requests below.
- **Streaming, not calls**: it was added "in a synchronous style that is inferior to its existing streaming
  counterpart", the mutation-transaction stream ([CAP-138: mutation expressions over frame streams](../docs/capabilities/README.md#CAP-138)).
- **The design**, in the user's words:

  > The Store interface supports stacking by passing mutation transactions down the stack and back up - all of it in a
  > single round trip.
  >
  > - minor adjustments to the vocabulary of mutations may be needed to facilitate inter-layer cooperation
  > - mutation transacations are always processed in streaming fashion
  > - client code sends a mutation transaction in which embedded queries mix reads, computations, and writes of paths,
  >   properties, adjacencies
  > - client code receives a stream of frames as the fundamental result
  > - any errors that occur duriung processing are annotated on frames
  > - in the case of an unresolvable error that occurs partway through interpreting the mutation expression, a
  >   partially bound frame is a preferred result
  >
  > The cache layer code interprets the mutation expression doing two things in parallel:
  > A. forwarding the mutation expression to layers below
  > B. interpreting the mutation expression recursively
  >
  > A "partial-aware" variant of mutation expression interpretation might use these arguments:
  >
  > - the original mutation expression (root)
  > - a residual/remainder handle to the subterm being evaluated
  > - a map from symbols that *should be bound* at that evaluation level to a stream of pre-qualified candidates for
  >   each symbol
  >
  > If the mutation expression interpreter reaches a leaf with all symbols fully bound, it may stream the resulting
  > frame back to the caller immediately.
  >
  > If the layer below streams back a frame (same symbol/variable bindings) that collides with a frame already
  > returned, the cache layer should check if there is any information present in that frame (such as property values)
  > that conflicts, and if so, the cache should be updated and the updated frame from below forwarded to the client.
  >
  > This also implies that clients must be capable of receiving a frame with identical bindings more than once,
  > treating each subsequent arrival as a re-evaluation or replacement for the previous arrival.
- **Frames are those already implemented**: a frame comes back up the stack as `References.OfFrame`, each symbol bound
  to an object by its reference and each variable to its value ([CAP-130: references to objects, entries and frames](../docs/capabilities/CAP-130.md)); the user asked, of what a
  frame carries, "frames are already implemented - where?".
- **No read of an object a store does not hold, outside a transaction**: a proxy's `.get()` of an object a cache layer
  does not hold "should not be possible"; nothing but the loading these capabilities replace uses it.
- **Others' writes reach a cache layer by a follow**: "continuous synchronization requires a `follow`", the store
  below reporting each transaction it commits, as `Changes.observe` and mbse-journals' `follow` do; they apply to the
  objects present alone, as [CAP-285: writes through, others' writes in](../docs/capabilities/README.md#CAP-285)'s second decision has it.
- **An install keeps a method of its own, where that is simpler**: "I do not object to the separate `Store.install`
  method, if preserving it avoids noticably increased net complexity."

Later, as the user decided:

- **Each layer has its own transaction interpreter**: "each layer of the stack gets its own transaction interpreter
  (not executor) instance. This instance is of a class that is internally coupled with the stack layer on which it
  operators. It does not need to use the `Store` interface to access its own stack layer. It is acceptable for there to
  be a base class, perhaps one that encapsulates consistent interpretation. But then it must provide hooks that the
  various kinds of stores can expose to the interpreter."
- **A follow is coupled with its layer**: "A follower reads what the follow delivers, and Follower subscriptions are
  layer-coupled as well." A follow is the one alternative to a transaction for reading a store
  ([CAP-315: every read within a transaction or through a follow](../docs/capabilities/CAP-315.md#decided)).

## Stacking by mutation transactions

As the user decided (2026-11-16), a stack of stores has one interface, the Store interface's own: a mutation
transaction goes in, and a stream of frames comes out ([CAP-308: stacking by mutation transactions, in one round trip](../docs/capabilities/README.md#CAP-308)). A client sends one transaction, whose embedded queries
mix reads, computations and writes of object references, properties and adjacencies, and receives the frames it binds,
as a stream; errors are annotated on frames, and an unresolvable error partway through gives a partially bound frame
([CAP-309: errors annotated on frames](../docs/capabilities/README.md#CAP-309)). Each layer takes the same transaction and streams frames back, so that a transaction goes down the stack and
its frames come back up in one round trip.

Each layer interprets a transaction with an interpreter of its own: an instance of a class coupled with the layer, which
reads and writes the layer directly, not through the Store interface. A base class holds what every layer interprets
alike, so that each refuses what every layer refuses: binding symbols, frames, unique clauses and errors annotated on
frames. Each kind of store gives the base class hooks for what only that kind knows: the object an object reference
designates among what it holds, the entries of a relation that link an object, the schema that an object reference
implies, and what it does where it holds no such object. A store in memory finds none there. A cache layer forwards the
transaction to the layer below. A follow that a layer gives is coupled with the layer too, and its follower reads only
what it delivers.

A cache layer, a store over another, does two things with a transaction at once: it forwards the transaction to the
layer below, and it interprets it itself, partially, over what it holds
([CAP-310: a cache layer's partial-aware interpretation](../docs/capabilities/README.md#CAP-310)). Where its own
interpretation binds a frame fully, it may stream the frame to the client at once. Where the layer below streams back a
frame with the same symbol bindings as one already given, it compares them: where they conflict, as in a property's
value, the layer below's holds, the cache takes it, and the client is given the frame again, as the layer below gave it.
So a client receives a frame with the same symbol bindings more than once, each later arrival a re-evaluation of the one
before, which it replaces. The lowest layer, a store kept in a database, executes the transaction within the database's
transaction, so that the database alone decides what commits and in what order
([the journal storage proposal](JOURNAL-STORAGE.md#what-a-backend-must-do)).

What it replaces in what is built: `Stores.Below` and its members (`document`, `commit`, `install`, `follow`,
`records`); a store above loading each object it reads by a request of its own; and a store above interpreting a
transaction before sending what it changed below. The sections that follow describe the stack as CAP-283 to CAP-285
built it, until these capabilities replace it.

## Interpreters and their hooks (proposed)

A design, for the user's review, of "each layer of the stack gets its own transaction interpreter", as
[CAP-308: stacking by mutation transactions, in one round trip](../docs/capabilities/README.md#CAP-308) and
[CAP-310: a cache layer's partial-aware interpretation](../docs/capabilities/README.md#CAP-310) would build it. Nothing
here is decided.

**As built (mbse-schemas 0.30.1).** One interpreter, the module `Transactions`, interprets every store's transactions.
It reaches into the store it is given for what it reads and writes: a schema's objects, a singleton, what an object
reference designates, the entries that link an object, the transaction's proposals, the owners it settles and the
counted objects it made. A store above a store below interprets the transaction itself, then sends what it changed
below (`Stores.Below.commit`), and loads each object it reads by a request of its own.

**The base class.** An interpreter is an instance of a class coupled with its layer, made for one transaction. The base
class holds what every layer interprets alike: the expression's terms, bound in order (`map`, `upsert`, `update`,
`reduce`, `then`); symbols and frames; the frames given back, by object reference ([CAP-315: every read within a transaction or through a follow](../docs/capabilities/CAP-315.md)); errors annotated on
frames ([CAP-309: errors annotated on frames](../docs/capabilities/README.md#CAP-309)); and unique clauses held at commit. It gives
its frames as a stream: a Python generator, a TypeScript observable.

**The hooks.** What only a kind of store knows, each a method the layer's class gives:

| Hook | What it gives |
|---|---|
| designated(reference) | the object an object reference designates among what the layer holds, or that it holds none |
| extent(schema) | the objects of a schema the layer holds, as candidates for a symbol |
| singleton(schema) | a singleton |
| linking(relation, link, object) | the entries of a relation that link an object through a link |
| create, set, clear, insert, remove | the writes of a spec, into the layer's transaction |
| absent(...) | what the layer does where it holds no such object: a store in memory finds none; a cache layer leaves the symbol to the layer below |
| commit, abort | the end of the layer's transaction: a store in memory commits its proposals; a store kept in a database commits within the database's transaction |

**The layers.**

- **A store in memory**: the hooks read and write what it holds; the base class alone does the rest.
- **A store kept in a database**, the lowest: it interprets the whole transaction within one database transaction,
  reads and writes alike, as the user decided ("the entirety of a transaction - reads and writes - are all conducted
  within a single transaction of the persistence layer"); the database decides what commits.
- **A cache layer**, any store over another: it sends the transaction below and interprets it over what it holds at
  once (CAP-310). A frame it binds fully it streams; a symbol it holds nothing for is the layer below's (`absent`).
  What comes back from below replaces what it gave, frame by frame by symbol bindings, a frame it gave whose object is
  gone retracted; what it wrote speculatively is undone where the layer below refuses.
- **mbse-rest's client and service**: the client is a cache layer whose layer below is the service; the service passes
  the transaction to its own store and streams the frames back.

**A follow** is the layer's too: it gives each transaction the layer commits as a one-transaction journal, and a cache
layer applies what its layer below's follow gives to what it holds.

**What it replaces**: `Stores.Below` and its members (`document`, `commit`, `install`, `follow`, `records`); a store
above loading each object it reads by a request; and a store above interpreting a transaction before sending what it
changed below.

**Stages**, each a release of mbse-schemas, then of mbse-rest and mbse-dynamodb:

1. The base class and the store in memory's hooks: the interpreter as built, moved behind the hooks, its behaviour
   unchanged.
2. Frames as a stream from `store.transaction`.
3. Forwarding (CAP-308): a store over another sends the transaction below, and the lowest interprets it whole;
   mbse-rest and mbse-dynamodb as layers; `Stores.Below` retired.
4. A cache layer's partial-aware interpretation (CAP-310), with the undo log, reconciliation and retraction kept on
   mbse-schemas' branch `CAP-310` (#44, closed for this rework).

**Questions for the user**:

1. **The hooks**: is the table the right division between the base class and a layer?
2. **The stream**: `store.transaction(callback)` gives back a stream of frames instead of a list (breaking); or a
   second method gives the stream, the first collecting it?
3. **A frame given again**: how a client tells a frame that replaces one given before from a new one, and knows that
   none will come again: by its symbol bindings, and the stream's end?
4. **The frame transducer**, a mutation kind of its own, "in most cases non-delegatable across `mbse-rest`" (the
   transaction-object proposal in mbse-schemas): is a term a layer does not send below interpreted by the highest
   layer that holds what it reads, or refused where none does?
5. **The order of the stages**, and whether stage 1 may land before the others are designed.

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
   store below, and keeps them. An entry loaded links objects not yet loaded, and the store holds each as a placeholder,
   `Proxies._Unresolved`, which holds the object's reference
   ([CAP-130: references to objects, entries and frames](../docs/capabilities/CAP-130.md)) until the link is read, when
   the store loads the object. [CAP-308: stacking by mutation transactions, in one round trip](../docs/capabilities/README.md#CAP-308)
   retires the placeholder for a `References.OfObject`. This is the largest part, in the proxies' core, and the one to
   prototype first.
3. **Writes through, and others' writes in.** A commit sends its effect to the store below, as a journal transaction; the
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

## Writing through, and others' writes in

[CAP-285: writes through, others' writes in](../docs/capabilities/README.md#CAP-285) joins a store above to the store below in both directions, as the user
decided (2026-11-13):

1. **The store below commits first** ("of course"). A store above sends a transaction's changes down before its own
   commit, within it, and commits only where the store below accepts them; a refusal there, such as a colliding append
   ([CAP-293: an entry inserted against a unique clause refuses its transaction](../docs/capabilities/README.md#CAP-293)), refuses the transaction above. The changes are written as plain data before
   the commit.
2. **Others' writes apply to present objects alone** ("agreed - broadcast updates apply only to present objects"). The
   store below reports each transaction it commits; the store above applies each to the objects present in it and to no
   other, an object not present staying so, linked by its object reference where an object present links it; and its
   followers are told of what changed above.
3. **In the order the store below committed them** ("right"): synchronously from a store in memory, and from a store
   over a database or over REST as its change feed delivers them, each applied as it arrives.

## Capabilities

In [INI-013: journals framework](PRIORITIES.md#ini-013--journals-framework): the five steps above are
[CAP-283: a store given a store below](../docs/capabilities/README.md#CAP-283), [CAP-284: objects loaded on demand](../docs/capabilities/README.md#CAP-284), [CAP-285: writes through, others' writes in](../docs/capabilities/README.md#CAP-285),
[CAP-286: an extent through ownership](../docs/capabilities/README.md#CAP-286) and [CAP-287: lazy or eager, tuned when it runs](../docs/capabilities/README.md#CAP-287), in mbse-schemas; mbse-rest's part is [CAP-290: a service's store stacked, with no snapshot](../docs/capabilities/README.md#CAP-290). Stacking by mutation transactions is
[CAP-308: stacking by mutation transactions, in one round trip](../docs/capabilities/README.md#CAP-308), with [CAP-309: errors annotated on frames](../docs/capabilities/README.md#CAP-309) and [CAP-310: a cache layer's partial-aware interpretation](../docs/capabilities/README.md#CAP-310).

## Snapshots today, and what replaces each

`Plain.ToPlain(store).Snapshot()` writes a store as two transactions, its schemas and then its data
([CAP-127: snapshots made of transactions](../docs/capabilities/CAP-127.md)): a store's state, made into a document. It is used:

| Where | For | Replaced by |
|---|---|---|
| mbse-rest's service, with mbse-dynamodb's plugin | Persistence: a snapshot every 100 transactions (`snapshot_every`), and startup from the latest one and the journal after it | The journal alone, below a lazy `Builders.Store`; that store's own rolling checkpoint, for a restart or a new instance |
| mbse-rest's `GET /schemas`, and its client | A store's schemas sent to a client, the first of a snapshot's two transactions | The install transactions that made the schemas, the head of the journal |
| The conformance corpora of mbse-schemas, mbse-expressions and mbse-patterns | Each case's store written as a snapshot, compared across the two languages | Each case as a frame, as mbse-programs' are; for these three, open: see below |
| mbse-schemas' examples | A store copied into another | A journal replayed into the other |

## Decided by an agent, for review

Where the user's decisions were silent, the simplest default consistent with them, each *proposed* until reviewed,
labeled with the repository and number it was decided under.

- **(mbse-schemas 30)** **What a store below answers: one object, as one transaction.** `Stores.Below.document(path)`
  gives the object an object reference designates as a one-transaction document
  ([CAP-128: graphs sent as one-transaction documents](../docs/capabilities/CAP-128.md)), its properties and its
  entries, each object they link by its object reference; None where it holds none. It is a mutation-transaction stream,
  the language stores already speak, so that a database's store and mbse-rest's client answer it alike, with no new
  form. This answer belongs to the design that
  [CAP-308: stacking by mutation transactions, in one round trip](../docs/capabilities/README.md#CAP-308) supersedes, in
  which a store below streams back the frames of the transaction it is sent.
- **(mbse-schemas 30)** **Identity by object reference.** An object loaded from the store below is one proxy, kept by
  its object reference, the same each time it is named. An object reference resolves to an object present, through its
  owner's entries where it was made above, else to the store below's, loaded, else to none: one read, of the object
  named, and no owner loaded.
- **(mbse-schemas 30)** **A link to an object not present holds its object reference.** An entry the store below gives
  that links an object not present holds that object's reference, and is held by the objects present it links; reading
  the link loads the object, which every entry waiting on its reference then links, re-keyed. Nothing is made that is
  not present. Whether a link owns what it links is known from the relation, without the object: a relation that owns
  through a link owns whatever it links.
- **(mbse-schemas 30, 35)** **Changes reported load nothing.** Removing the owning entry of an object not present
  deletes it, and is reported by its owner's key, as any deletion is; anything else not present the reported changes
  name, they name by its object reference, the schema it is written by the one its reference implies.
- **(mbse-schemas 35)** **Each store of a stack commits a write as one transaction, as the lowest did.** While a store
  sends a transaction below, what the store below reports it committed, what it added among it, as its record, is
  taken into the transaction before it commits, and is the effect the store's followers are given of it: one effect
  per write, the same in every store of the stack.
- **(mbse-schemas 31)** **A store's own transactions come back, and are applied again.** What the store below reports
  while a transaction above is open, the store above applies once it ends, in the order the store below committed it,
  its own transaction among them, rather than skipping its own: so that where another wrote below between what the
  store above read and its own commit, the two stores end alike. Applied again with nothing between, its own changes
  nothing, and its followers are told nothing more; this is also how a change feed delivers a store's own transactions.
- **(mbse-schemas 31)** **Applying is a transaction of the store above's that loads, checks and sends nothing.**
  Others' changes, already checked and committed below, are not checked again above, nor sent back down; its followers
  are told what changed, as of any transaction.
- **(mbse-schemas 31)** **An entry is applied from an object present it links.** An effect writes each entry on the
  adjacency of one object it links; where that object is not present above, the store above writes it from one that
  is, through that object's adjacency by name. One that links no object present is left out. One whose objects present
  have no adjacency to it by name is applied directly, as the (mbse-schemas 34) decision below states.
- **(mbse-schemas 31)** **Deleting an object not present deletes, among those present, what reached it.** Removing
  the owning entry of an object not present removes every entry that links it, or anything it owns, and so deletes
  each object present it owns; these follow from the removal, which alone is reported, as a deletion's cascade is.
- **(mbse-schemas 30)** **Loading is no transaction of the store's.** What `document` gives for an object is applied as
  the store's committed data, outside any transaction open, observed by no follower, recorded by no provenance and
  checked by nothing.
- **(mbse-dynamodb 15)** **A store below is given its schemas apart.** A transaction that writes only schemas reports
  no changes, so that a store above sends no install below and none is journaled: each process gives the store kept in
  a database its installs, as an app gives its own store its installs. Whether a journal also begins with them is open
  (below).
- **(mbse-dynamodb 15)** **A read is of one transaction of the journal.** What `document` gives for an object is read
  from its index items as they stood after one journal transaction; where another process commits while they are read,
  they are read again.
- **(mbse-dynamodb 15)** **A counted object is kept by its value.** It has no reference, so that an entry linking it is
  kept under the objects it links that have one, with the counted object's schema and values; `document` is refused for
  one of them, as a store in memory refuses it.
- **(mbse-dynamodb 15)** **mbse-dynamodb's persistence plugin is kept until CAP-290.** The plugin, which snapshots, is
  superseded by the store kept in DynamoDB, and kept unchanged while mbse-rest's service persists through it; it goes
  with [CAP-290: a service's store stacked, with no snapshot](../docs/capabilities/README.md#CAP-290).
- **(mbse-rest 19)** **The service makes its store over the store below it is given.** It is given a store below, a
  database's or one in memory, and makes its own store, a `Builders.Store` over it; each install runs in both, the store
  below given its schemas apart, and an app's seed runs in its own store where the store below is new: one that keeps a
  journal holding no transaction, or one in memory. A seed is not run again over what it wrote, which may have been
  edited since.
- **(mbse-rest 19)** **mbse-rest's client is a `Builders.Store` whose store below is the service**, as a store kept in
  a database is one whose store below is its index, in Python and TypeScript alike: a store above gives the store below
  plain data read with that store's own schemas, and observes it through mbse-schemas' `Changes.observe`, so that it
  needs no change to mbse-schemas. Made, it executes the install transactions the service gives.
- **(mbse-rest 19)** **The endpoints a store below needs.** What `document` gives for an object by its object reference
  (`POST /documents`), or none; a transaction's changes, committed or refused, the refusal named by the kind of error
  the store raised (`ValueError`, `TypeError`, `LookupError`), which the client raises; the change feed
  (`GET /changes`); the install transactions that made the schemas (`GET /schemas`), and an install given
  (`POST /schemas`).
- **(mbse-rest 19)** **The change feed is read by position, its reads long-polled.** Each transaction the service's
  store commits is numbered from 1 in commit order, and a client reads those after the last it was given, so that it is
  given each once, none missed, from any position the feed keeps; a read that finds none new is held open until one
  commits, or a time passes. A read by position, rather than a stream held open, is what a synchronous transport can
  make (below), passes any proxy, and is plain polling where it is not held open. The positions are the service's own,
  under a name of the feed's; it keeps the latest 10 000; a position before them, or another feed's, as after a
  restart, is refused (410), and the client's store is made again. A write is one transaction of the feed's, its
  record (`Provenance`) among it, as the store below committed it.
- **(mbse-rest 19)** **A client commits its own transaction as the service committed it, and applies the change feed
  as any store applies the store below's reports.** The service answers a transaction with what its store committed of
  it, its record among it; the client takes that into its own commit, and its followers are given it then, once. Each
  transaction it reads from the feed, its own among them, is applied to the objects present in it, its followers told
  what changed there; its own, applied again, changes nothing.
- **(mbse-rest 19)** **An install a client is given is sent to the service**, which runs it in its store and the store
  below, and serves it after the installs it holds, once: a client is given its schemas as any store is, and gives
  them to the store it stands for. The installs served are those the service was given, not read from a journal.
- **(mbse-schemas 34)** **The lowest store is the one whose store below records nothing.** A store records each
  transaction it commits where the store below it does not (`Store.records`): one with no store below, or one over a
  store below that does not record, such as a database store's own index, records; one over another store does not.
- **(mbse-schemas 34)** **An entry no object present has an adjacency to by name is applied directly.** Applying the
  store below's transaction, an entry that no object present it links has an adjacency to by name, as Provenance's
  `CreatedBy` and `ModifiedBy` on an object extended by an anonymous adjacency, is written to the tables of the objects
  present it links, the others linked by their object references, rather than refused; applied again, it changes
  nothing. Only such an entry linking a counted object, which has no reference, is refused.
- **(mbse-rest 19)** **The client's transport is synchronous**, as mbse-schemas' store interface is: in Node, a request
  waits on a worker thread that fetches; in a browser, it is a synchronous `XMLHttpRequest`, best made from a worker.
- **(mbse-rest 19)** **A view that writes is refused before it runs where its frames cannot bind the view's symbols**,
  since what the store below has committed is not undone.
- **(mbse-rest 19)** **The service polls a store below that is followed by polling**, as a store kept in a database is
  (`poll()`), before each request and while a read of the change feed is held open, so that what other processes
  committed reaches its clients.
- **(mbse-rest 19)** **The service over a store kept in DynamoDB is tested in mbse-dynamodb**, which has mbse-rest as a
  test dependency, so that neither repository depends on the other at run time, nor each on the other.
- **(mbse-rest 20)** **mbse-rest's client is a store over a remote that implements `Stores.Below`.** `Remote`
  implements the interface over the service's endpoints (`install` by `POST /schemas`), and a client store is a plain
  `Builders.Store` over it. It reads the change feed when polled and after each commit, a store over the interface
  having no hook where a transaction begins: its followers may hear its own write before another's committed earlier
  and not yet read, the data alike once both are applied. The service's own installs, which a client store is given
  when it is made, are not sent back to it.
- **(mbse-dynamodb 17)** **A store kept in DynamoDB implements `Stores.Below`, interpreting each transaction in a store
  of its own.** It holds a `Builders.Store` over an index that implements the interface itself and records nothing, so
  that its store records each transaction; the index's `commit`, within that store's transaction, writes the journal
  transaction and the index items in one DynamoDB transaction, a conflict or a failure there rolling the transaction
  back, which is interpreted again once caught up, up to a bound, as a transaction written in a block is too. Each
  object is kept as that store's `document(path)` gives it, with the objects linking it; reading one needs no install.

## Open questions

- **Stacking by mutation transactions: what is open.** Each to be decided as
  [CAP-308: stacking by mutation transactions, in one round trip](../docs/capabilities/README.md#CAP-308) to [CAP-310: a cache layer's partial-aware interpretation](../docs/capabilities/README.md#CAP-310) are planned:
  - the "minor adjustments to the vocabulary of mutations" the layers need to cooperate;
  - what of [CAP-283: a store given a store below](../docs/capabilities/README.md#CAP-283) to [CAP-285: writes through, others' writes in](../docs/capabilities/README.md#CAP-285), met as built, these capabilities supersede, and what
    of mbse-rest and mbse-dynamodb is rewritten.

- **The conformance corpora.** Each implementation writes each case's store as a snapshot, and the two are compared:
  a store analyzed as a snapshot. mbse-programs' corpora are frames, as the user decided (below); whether mbse-schemas',
  mbse-expressions' and mbse-patterns' follow is open. The mbse-programs Python port measured them on mbse-schemas 0.27,
  over its corpus of 153 objects:
  - a case's frame was 146 KB, against 180 KB as a transaction and 274 KB as a snapshot, the last even for a case of
    two objects;
  - it was byte-identical when built in two separate stores, and written, read back and written again;
  - two stores' frames, read back into one store, compared equal (`Comparison.OfObject`, 0); compared across stores
    directly, they were incomparable, each store holding its own schema objects;
  - a change of the source's layout alone left it equal and byte-identical; a change of a value made it incomparable.

  What it asks of a corpus: a frame witnesses the data and does not make it, so that a case is made again by running
  it; the values `assigns` holds are of a registered schema, so that an unnamed container is named; only the objects
  bound to symbols are witnessed, with the properties the spec names, and a counted object is refused; and a
  comparison says equal or incomparable, not where, which a diff of the written frames shows.
- **A transaction applied above, refused there.** A store above that cannot apply what the store below committed, an
  entry linking a counted object that no object present has an adjacency to by name, raises within the store below's
  report of its commit: the writer below, whose transaction has committed, is given the error, and the store below's
  later followers are not told. Whether a store above should instead hold such a transaction aside, and report it, is
  open.
- **Identity by object reference, where an ownership key changes.** A store keeps each object it loaded by its object
  reference; an object whose owning entry is rewritten with other keys has a new reference, and a store above that
  loaded it by its old one holds it under that one still.
- **Reads over REST, one object at a time**, are many requests: whether mbse-rest's service answers a read of several
  objects, or of what one reaches, at once.
- **A journal headed by its installs.** A store kept in a database is given its schemas by each process that opens it,
  and journals no install. Journaling the installs, at the journal's head, would let a process open a store knowing
  none of its schemas, and is what replaces mbse-rest's `GET /schemas` above; it asks a store to report an install as
  it reports a transaction's changes.
- **One change feed for many instances of a service.** Each instance numbers its own feed, so that a client keeps to
  one; reading the store below's journal by its own positions, where it keeps one, would let a client read from any.
- **Where this is built in order**: after the journal and its storage interface in mbse-journals, or beside them, since
  steps 1 and 2 are mbse-schemas' alone.
