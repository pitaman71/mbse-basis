<!-- nav -->
[← Features](README.md) · [Home](../README.md)

# Features not yet planned

Features and capabilities without an ID, not in plan yet. A planned feature's own unplanned capabilities are in its detail file.

## no-code secure services

Out of scope for now.

- schema revisions : <migration>.<revision>
- secure server setup with credentials provided in service ENV
- Docker ubuntu image build

## search-sort-filter

User can apply search, sort, and filter in browser views.
Initially these will be in-browser executed and very
simple. Keyword, semantic, and hybrid searches will evolve
over time. Logical views are the lens through which
searches operate.

### search-sort-filter browser exact prop match

- executed in browser
- target object only
- props in detail view only
- text match for entire property value

## view paging

## hybrid search

## tenancy

### local (for demos)

Each application instance is entirely private.

### private (intermediate)

- system requires login for any access
- security configurations via patterns shared and enforced across services 
  and UI
- sessions uid is allocated on login and renewed with login tokens
- user/agent identity is recorded in session log
- session identity is recorded with every transaction
- transaction request/response signatures recorded in session log

### sequestered

A single application instance can permit multiple users to login to the
same instance but not see one another's data in any way.

### read-sharing

Users can share data views with one another on a read-only basis.

### groups and topics

### projections and forms

## agent chat integration

### in-app AI chats over modeled data

- user can create an in-app AI chat session authenticated to the AI service and model of their choice
- user can chat with the AI agent
- user can browse and manage in-app chat sessions

## constraint enforcement replaces bespoke workarounds

### shared property handling by constraints

## journals

A new repository, mbse-journals: "Journal is an extension of Store and may be queried. Any Journal may optionally
predicates that describe portion contained." A transaction's expression as data, and journals replayed by executing
it, are built in mbse-schemas ([CAP-129: journals replayed by execution](../capabilities/CAP-129.md)); diffing stores is what [CAP-077: changes explained across runs](../capabilities/CAP-077.md) waits on.

- schema-kind-specific serializable mutation protocols (`mbse/Journals/Framework/Mutations`, one per schema kind and
  `OfStore`), and their dataclasses (`mbse/Journals/Proxies/Mutations`), serialized by the builder, visitor and
  meta-schema pattern
- "All Builders - whether proxy or generated - must implement the appropriate mutation protocol. Can this be
  accomplished without littering the syntax with lots of extra '.get' and '.set' calls?"
- protocols: `Journals.OfStore`, of streaming atomic transactions; `OfSender`, a transmitter endpoint; `OfReceiver`, a
  receiver endpoint; and stores: `Cache`, in memory, and `File`, a local filesystem copy
- `Journal.from_batch(transaction)`, `Journal.to_batch()`, `Journal.diff(a, b)` of two stores,
  `Sender.send(source)`, `Sender.subscribe(observable)`, `Receiver.observe()`
- new repositories: mbse-s3, to persist in AWS S3; mbse-mcp, which "implements MCP via Journal protocol and schema
  introspection"; mbse-mysql, to persist in MySQL. mbse-dynamodb is [CAP-013: an in-memory store journaled to DynamoDB](../capabilities/CAP-013.md)'s.

### reference evaluators

"Should Evaluators delegate to a per-language library? Perhaps optionally. This could be in sub-repos."

## imported datatypes

"MBSE must have an efficient, incrementally updateable model-centric process that supports interoperation with
imported datatypes, particularly datatypes from cross-language frameworks like Numpy, Safetensors, Pandas Dataframes.
Also first-class synergy with Protobufs."

Open: "How does this interoperate with Expression Dialects and Program Dialects?"

## imported functionality

## cost models

---

<!-- nav -->
[← Features](README.md) · [Home](../README.md)
