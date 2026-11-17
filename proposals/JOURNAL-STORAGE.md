# Journal storage

Initiative: [INI-013: journals framework](PRIORITIES.md#ini-013--journals-framework).

Where a journal is kept, so that many users, in the cloud or on their own servers, read and write one. mbse is a
framework, not a product: it is married to no one database, service or licence, and each storage backend is one of
several, chosen by the app that uses it. This proposes the interface every backend meets, how a backend is held to it,
and which backends to build first.

## Decided

The user's decisions (2026-11-12):

- **Versatility first**: "I am making a framework, not a product. Therefore versatility is a top goal. So I don't want
  to marry the framework to a particular service or to one side of the open-source/paid line."
- **NoSQL by preference**: "I like noSQL's adaptable schemas as they better align with the kind of 'stability via
  semantic normalization' mbse-schemas strives to create." DynamoDB has kept journals before: "It worked."
- **The journal in memory is for unit tests; a full-stack demo needs a real backend**: "I think the in-memory reference
  we have is good for unit testing front end and backend separately, and it's at least partially already built. It's
  just that we need DynamoDB or something better to demo full stack." A journal kept in memory, or by a store meant for
  one browser, is "primarily useful for demos and testing", not a cloud or multi-user backend.

The user's decisions (2026-11-15):

- **A store's layout in its database is a mapping, utterly parametric**: told that a table mbse-dynamodb 0.2.0 wrote
  has an index the store rewritten on `Stores.Below` cannot read, the user answered "okay for now. this is a very good
  reason for the mapping from mbse-schema to dynamodb-schema to be utterly parametric": how a backend lays a store's
  objects and journal out in its database is a mapping given as parameters, so that a layout changes, or two are read,
  without a backend rewritten.

## What a backend must do

A journal is never snapshotted
([FEA-056: fungible diagramming keeps agents and humans in the loop](../docs/features/FEA-056.md#decided)), and whether
a journal's transaction is accepted is decided by mbse-schemas alike in every recipient, by the constraints its schemas
declare. So a backend judges nothing: it never reads a journal transaction's meaning, and needs a database transaction
only to order journal transactions. It must give, for each journal:

1. **Each journal transaction within a database transaction.** A journal's order is its relations
   ([the journals proposal](JOURNALS.md#the-journal-a-sequenced-container)), and a backend applies each journal transaction, an append or an insertion, within a
   database transaction, so that the database is responsible for the order they are serialized in, as the user decided:
   "Backend bindings should use a database transaction around the journal transaction. This makes the db more or less
   responsible for serialization order." Two writers appending after one last are told apart by a unique clause
   ([CAP-293: an entry inserted against a unique clause refuses its transaction](../docs/capabilities/README.md#CAP-293)).
2. **Reads and subscriptions from any journal transaction.** A position is a journal transaction. A subscriber catches
   up from any journal transaction, the first included, since there is no snapshot to start from, and then follows
   live, with no journal transaction missed or given twice.
3. **Journal transactions as schema-free JSON.** A journal transaction is the plain form mbse-schemas writes, JSON,
   stored as it is.

## The interface, and how a backend is held to it

The interface is the store interface itself, as the user decided ("exactly"): a journal is data in a store
([FEA-028: one Store interface, lazy by default](../docs/features/FEA-028.md)), so that a backend is a store over its database, which interprets the mutation-transaction
streams it is given, each within a database transaction, and reports to each follower only the changes, its change
feed giving what `Changes.observe` gives for a store kept in memory ([the journals proposal](JOURNALS.md#decided)). Nothing
in it is a database's. A conformance suite, in mbse-journals, states what a journal kept in a store does as cases,
among them two writers appending after one last, each from what it last saw, and a follower that catches up; it runs
against the store kept in memory, the test double, which also lets a front end and a back end each be unit-tested
alone, and every backend passes it unchanged, much as [PRI-037: the same conformance corpora](../docs/PRINCIPLES.md#PRI-037) holds every repository's
implementations to the same corpora.

Each backend is a repository of its own, as mbse-dynamodb already is and as
[CAP-200: journals persisted to AWS S3](../docs/capabilities/CAP-200.md) and [CAP-202: journals persisted to MySQL](../docs/capabilities/CAP-202.md) plan theirs, so that an app takes only the backends it uses.

## Which backends, in order

**First**, DynamoDB, so that the framework can be demonstrated full stack, then MongoDB: two that differ in every way
the interface could quietly come to depend on, their transactions, how they give changes, where they run and on which
side of the open-source and paid line they fall.

| Backend | Transaction | Subscriptions | Why |
|---|---|---|---|
| **DynamoDB** | `TransactWriteItems` around each journal transaction | A stream, kept a day, ordered within a partition; older entries caught up by reading the table | Managed and proprietary; the backend the user has run before; mbse-dynamodb exists |
| **MongoDB** | A multi-document transaction around each journal transaction | Change streams, resumed by token as far back as the oplog; older entries caught up by reading the collection | Self-hosted, Community edition under the source-available SSPL, or managed on any of the three large clouds (Atlas) |

**Build-out**, each widening what the interface is proven against:

| Backend | What it adds |
|---|---|
| **Azure Cosmos DB** | A second managed cloud; a change feed kept as long as the data, ordered within a journal's partition |
| **FoundationDB** | Open source (Apache 2.0) and distributed at production scale, with the strongest transactions; subscriptions are a thin layer over its watches |
| **Firestore** | Changes pushed to browsers directly; a low sustained write rate per document |
| **EventStoreDB (Kurrent)** | A store made for journals: append at an expected version, and subscriptions from any position, built in |
| **CouchDB, or Cloudant managed** | A changes feed from any sequence number, and replication to clients that work offline |
| **PostgreSQL, with JSONB** | Not NoSQL, but everywhere |

Each backend's limits, prices and licence are checked when it is planned: those above are as they stood when this was
written.

## Capabilities

In [INI-013: journals framework](PRIORITIES.md#ini-013--journals-framework), after CAP-199:

- [CAP-288: the journal storage interface](../docs/capabilities/README.md#CAP-288), in mbse-journals, run against the journal in memory.
- [CAP-289: journals kept in DynamoDB](../docs/capabilities/README.md#CAP-289), in mbse-dynamodb, refining [CAP-013: an in-memory store journaled to DynamoDB](../docs/capabilities/CAP-013.md).
- [CAP-291: journals kept in MongoDB](../docs/capabilities/README.md#CAP-291), in a new mbse-mongodb.
- Then one for each build-out backend, in the order above, refining
  [CAP-220: persistence in other NoSQL stores](../docs/capabilities/CAP-220.md), whose scope these name: each given an ID when it is planned.

## Decided by an agent, for review

Where the user's decisions were silent, the simplest default consistent with them, each *proposed* until reviewed,
labeled with the repository and number it was decided under.

- **(mbse-dynamodb 15)** **DynamoDB orders a journal by an item holding its length.** Each journal transaction is
  committed in one `TransactWriteItems` with an item holding the number of the journal's last transaction, on condition
  that it holds the number the committing process last caught up to, so that of two processes committing at once one is
  refused. The refused one catches up and interprets its transaction again, which what the other committed may now
  refuse
  ([CAP-293: an entry inserted against a unique clause refuses its transaction](../docs/capabilities/README.md#CAP-293));
  a transaction written imperatively, which the store cannot run again, is refused, to be run again by its writer.
- **(mbse-dynamodb 15)** **The index in DynamoDB.** By a hash of each object's reference: an item of its schema and
  property values, and an item for each entry linking it, under every object the entry links, so that a deletion finds
  each entry linking what it deletes, loaded or not, and what that owns, in cascade. Equal entries of a relation that
  keeps them are one item, with their count. The index items a transaction changes are written in the same
  `TransactWriteItems` as its journal transaction where DynamoDB's limits on one allow (100 items, 4 MB); else the
  journal transaction is committed with them kept beside it, and they are written out before any process reads the
  store, by the writer or by whichever process reads next. A transaction is committed once its journal transaction is.
- **(mbse-dynamodb 15)** **Subscriptions read the table, in order.** A process catches up by reading the journal's
  transactions after the last it gave its followers, in order, before each of its transactions and when polled, rather
  than from DynamoDB Streams: a stream orders records per item and keeps them a day, while the journal's numbers are its
  commit order, kept as long as the table. A stream may later wake a process to poll, and no more.
- **(mbse-dynamodb 1)** **One table, keyed by store and record**: one thing to make and configure, which several
  stores (demos, tests) share, each under its own partition key.
- **(mbse-dynamodb 3)** **Parts of 350 000 bytes** of UTF-8 JSON, uncompressed, so that a journal transaction reads back
  as text in the console; compression (zlib) would cut cost and parts roughly tenfold.
- **(mbse-dynamodb 7)** **The table is made when absent by default** (`create=True`, on-demand capacity), for demos;
  production sets `MBSE_DYNAMODB_CREATE=0` and makes the table with its own tooling.
- **(mbse-dynamodb 10)** **Settings from `MBSE_DYNAMODB_*`**, read by `Store()` with no arguments, as mbse-rest's
  service makes the store below it by name, each overridden by an argument; the region falls back to boto3's own.

## Open questions

- **A write's cost, where an object holds many entries.** mbse-dynamodb keeps each object whole, as
  `Stores.Below.document` gives it, so that a write rewrites it, entries and all, its cost growing with the object. A
  write of part of a property's value is
  [CAP-272: surgical mutations of a property's value](../docs/capabilities/README.md#CAP-272); an object kept in parts
  by relation entry, as the layout above may give, would bound the cost of a write to an object's entries too.

- **Subscribers in browsers.** A browser holds no database's credentials, so it subscribes through mbse-journals'
  sender and receiver ([CAP-274: journals sent and received](../docs/capabilities/README.md#CAP-274)) rather than to a backend directly; Firestore's own
  subscriptions to browsers would then be a choice an app makes, not the framework's.
- **Both languages for every backend.** Each backend in Python and TypeScript, as
  [PRI-028: both implementations change together](../docs/PRINCIPLES.md#PRI-028) has it, or a backend in the language its database's
  best client is in, listed as a deliberate difference ([PRI-040: deliberate differences listed](../docs/PRINCIPLES.md#PRI-040)).
