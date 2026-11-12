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

## What a backend must do

A journal is never snapshotted ([FEA-056: fungible diagramming keeps agents and humans in the loop](../docs/features/FEA-056.md#decided)), and whether an entry is
accepted is decided by mbse-schemas alike in every recipient, by the constraints its schemas declare. So a backend
judges nothing: it never reads an entry's meaning, and needs a transaction only to order entries. It must give, for
each journal:

1. **Each journal transaction within a database transaction.** A journal's order is its relations
   ([the journals proposal](JOURNALS.md#the-journal-a-sequenced-container)), and a backend applies each journal transaction, an append or an insertion, within a
   database transaction, so that the database is responsible for the order they are serialized in, as the user decided:
   "Backend bindings should use a database transaction around the journal transaction. This makes the db more or less
   responsible for serialization order." Two writers appending after one last are told apart by a unique clause
   ([CAP-293: an entry inserted against a unique clause refuses its transaction](../docs/capabilities/README.md#CAP-293)).
2. **Reads and subscriptions from any entry.** A position is an entry. A subscriber catches up from any entry, the
   first included, since there is no snapshot to start from, and then follows live, with no entry missed or given
   twice.
3. **Entries as schema-free documents.** An entry is the plain form mbse-schemas writes, JSON, stored as it is.

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

## Open questions

- **Subscribers in browsers.** A browser holds no database's credentials, so it subscribes through mbse-journals'
  sender and receiver ([CAP-274: journals sent and received](../docs/capabilities/README.md#CAP-274)) rather than to a backend directly; Firestore's own
  subscriptions to browsers would then be a choice an app makes, not the framework's.
- **Both languages for every backend.** Each backend in Python and TypeScript, as
  [PRI-028: both implementations change together](../docs/PRINCIPLES.md#PRI-028) has it, or a backend in the language its database's
  best client is in, listed as a deliberate difference ([PRI-040: deliberate differences listed](../docs/PRINCIPLES.md#PRI-040)).
