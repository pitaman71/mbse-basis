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

1. **An ordered, atomic append.** An entry is appended at the next position, and the append fails where another took
   that position first, so that two writers never interleave: optimistic concurrency, the one transaction a backend
   needs.
2. **Reads and subscriptions from any position.** A subscriber catches up from any position, the first included,
   since there is no snapshot to start from, and then follows live, with no entry missed or given twice.
3. **Entries as schema-free documents.** An entry is the plain form mbse-schemas writes, JSON, stored as it is.

## The interface, and how a backend is held to it

The interface is mbse-journals': part of [CAP-199: journals as queryable stores (mbse-journals)](../docs/capabilities/CAP-199.md), in Python and TypeScript, the three
above as operations, with no type from any database in it. A conformance suite, in mbse-journals, states each
operation's behaviour as cases, among them two writers racing for one position and a subscriber that falls behind and
catches up; it runs against the journal kept in memory ([CAP-273: journals in memory and in local files](../docs/capabilities/README.md#CAP-273)), the
interface's test double, which also lets a front end and a back end each be unit-tested alone, and every backend passes
it unchanged, much as
[PRI-037: the same conformance corpora](../docs/PRINCIPLES.md#PRI-037) holds every repository's implementations to the same corpora.

Each backend is a repository of its own, depending on mbse-journals alone, as mbse-dynamodb already is and as
[CAP-200: journals persisted to AWS S3](../docs/capabilities/CAP-200.md) and [CAP-202: journals persisted to MySQL](../docs/capabilities/CAP-202.md) plan theirs, so that an app takes only the backends it uses.

## Which backends, in order

**First**, DynamoDB, so that the framework can be demonstrated full stack, then MongoDB: two that differ in every way
the interface could quietly come to depend on, their transactions, how they give changes, where they run and on which
side of the open-source and paid line they fall.

| Backend | Append | Subscriptions | Why |
|---|---|---|---|
| **DynamoDB** | A conditional put on journal and position | A stream, kept a day, ordered within a partition; older entries caught up by reading the table | Managed and proprietary; the backend the user has run before; mbse-dynamodb exists |
| **MongoDB** | A unique index on journal and position; multi-document transactions | Change streams, resumed by token as far back as the oplog; older entries caught up by reading the collection | Self-hosted, Community edition under the source-available SSPL, or managed on any of the three large clouds (Atlas) |

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

## Capabilities, proposed

Each to be given an ID when it is planned, in this order, in INI-013 after CAP-199:

- The journal storage interface and its conformance suite, in mbse-journals, run against the journal in memory.
- Journals kept in DynamoDB, in mbse-dynamodb, refining [CAP-013: an in-memory store journaled to DynamoDB](../docs/capabilities/CAP-013.md).
- Journals kept in MongoDB, in a new mbse-mongodb.
- Then one for each build-out backend, in the order above, refining
  [CAP-220: persistence in other NoSQL stores](../docs/capabilities/CAP-220.md), whose scope these name.

## Open questions

- **CAP-013's snapshots.** mbse-dynamodb journals each committed transaction "with occasional snapshots", and its
  startup reads the latest snapshot. A journal is never snapshotted; whether its startup replays the whole journal,
  or keeps a store in memory as a cache that is never stored or sent, is open.
- **Subscribers in browsers.** A browser holds no database's credentials, so it subscribes through mbse-journals'
  sender and receiver ([CAP-274: journals sent and received](../docs/capabilities/README.md#CAP-274)) rather than to a backend directly; Firestore's own
  subscriptions to browsers would then be a choice an app makes, not the framework's.
- **Both languages for every backend.** Each backend in Python and TypeScript, as
  [PRI-028: both implementations change together](../docs/PRINCIPLES.md#PRI-028) has it, or a backend in the language its database's
  best client is in, listed as a deliberate difference ([PRI-040: deliberate differences listed](../docs/PRINCIPLES.md#PRI-040)).
