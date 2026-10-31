<!-- nav -->
[← Qualities](../QUALITIES.md) · [Home](../README.md) · [Capabilities →](../capabilities/README.md)

# Features

The second tier of the design spec: a cohesive, focused category of utility a persona values, what problems the
product solves for that persona, not how. Each feature is **external**, serving a user persona, or **internal**,
serving an engineering persona; it confers qualities, and its capabilities say how far it is met. A feature may be
adopted before it is met. Features may overlap on purpose.

## Index

### Modeling

- <a id="FEA-008"></a>**[FEA-008: expressive program models](FEA-008.md)** · adopted · external · Program models have sufficient expressive power to concisely
  and precisely represent source code in its native and idiomatic form. *Confers* [QUA-004: models as an alternative representation of source code](../QUALITIES.md#QUA-004).
- <a id="FEA-009"></a>**[FEA-009: layered interaction models](FEA-009.md)** · adopted · external · Interaction models can model layered abstractions of
  functional behavior. *Confers* [QUA-004: models as an alternative representation of source code](../QUALITIES.md#QUA-004).
- <a id="FEA-010"></a>**FEA-010: system behavior** · adopted · external · Interaction models are a suitable representation of
  system-level behavior. *Confers* [QUA-007: one paradigm at every level of a system](../QUALITIES.md#QUA-007).
- <a id="FEA-011"></a>**FEA-011: hardware and firmware behavior** · adopted · external · Interaction models are a suitable representation of hardware
  behavior, firmware behavior, as well as interfaces and interactions between them. *Confers* [QUA-007: one paradigm at every level of a system](../QUALITIES.md#QUA-007).
- <a id="FEA-012"></a>**FEA-012: firmware, software and device behavior** · adopted · external · Interaction models are a suitable representation of firmware
  behavior, software behavior, device behavior, as well as interfaces and interactions between them. *Confers*
  [QUA-007: one paradigm at every level of a system](../QUALITIES.md#QUA-007).
- <a id="FEA-013"></a>**FEA-013: device, user, cloud and agent behavior** · adopted · external · Interaction models are a suitable representation of device
  behavior, user behavior, cloud resource behavior, agent behavior, as well as interfaces and interactions between
  them. *Confers* [QUA-007: one paradigm at every level of a system](../QUALITIES.md#QUA-007).
- <a id="FEA-014"></a>**FEA-014: device behavior** · adopted · external · Interaction models are a suitable representation of device
  behavior. *Confers* [QUA-007: one paradigm at every level of a system](../QUALITIES.md#QUA-007).
- <a id="FEA-015"></a>**FEA-015: user behavior** · adopted · external · Interaction models are a suitable representation of user
  behavior. *Confers* [QUA-007: one paradigm at every level of a system](../QUALITIES.md#QUA-007).
- <a id="FEA-016"></a>**FEA-016: community behavior** · adopted · external · Interaction models are a suitable representation of community
  behavior. *Confers* [QUA-007: one paradigm at every level of a system](../QUALITIES.md#QUA-007).
- <a id="FEA-017"></a>**FEA-017: AI in the loop via the model trace** · adopted · external · AI stays in the loop (with humans) via the model trace.
  *Confers* [QUA-001: AI and humans in the loop](../QUALITIES.md#QUA-001).
- <a id="FEA-018"></a>**FEA-018: humans in the loop via the model trace** · adopted · external · Humans stay in the loop (with AI) via the model trace.
  *Confers* [QUA-001: AI and humans in the loop](../QUALITIES.md#QUA-001).
- <a id="FEA-019"></a>**FEA-019: equivalent implementations** · proposed · external · Every model and every operation on it means the same in every
  implementation language: Python and TypeScript give the same results, errors and wire format. *Confers* [QUA-006: the same in every language](../QUALITIES.md#QUA-006).
  Principles reinforce it rather than capabilities: [PRI-028: both implementations change together](../PRINCIPLES.md#PRI-028) and [PRI-037: the same conformance corpora](../PRINCIPLES.md#PRI-037) to [PRI-040: deliberate differences listed](../PRINCIPLES.md#PRI-040),
  which superseded its capabilities [CAP-024: the same conformance corpora](../capabilities/README.md#CAP-024) and [CAP-030: the same cases in both languages](../capabilities/README.md#CAP-030) to [CAP-032: deliberate differences listed](../capabilities/README.md#CAP-032).
- <a id="FEA-020"></a>**[FEA-020: refinable models](FEA-020.md)** · adopted · external · All models allow refinements to be added, closing details in
  a targeted and agile manner. *Confers* [QUA-002: open-world models](../QUALITIES.md#QUA-002).

### Schema-driven visualization and editing

An index site for any mbse app, driven by its schemas. Each feature's detail file holds its capabilities'
specifications.

- <a id="FEA-021"></a>**[FEA-021: every generation ambiguity a parameter](FEA-021.md)** · proposed · external · Every
  ambiguity in generation is a parameter of the step that resolves it, decided by a human, an agent or a policy chosen
  up front, and kept in the trace. *Confers* [QUA-001: AI and humans in the loop](../QUALITIES.md#QUA-001). *Relates to*
  [PRI-014: every ambiguity a decision](../PRINCIPLES.md#PRI-014). Formerly CAP-040.
- <a id="FEA-001"></a>**FEA-001: schema-driven UI** · adopted · external · Services and UI present an app driven by its
  schemas, extended by schema-aware code only where wanted. *Confers* [QUA-008: usable without code](../QUALITIES.md#QUA-008). [Detail](FEA-001.md)
- <a id="FEA-003"></a>**FEA-003: no-code logical views** · adopted · external · Query formats the backend serves as
  mutation expressions, requested alone or nested in one response. *Confers* [QUA-008: usable without code](../QUALITIES.md#QUA-008). [Detail](FEA-003.md)
- <a id="FEA-004"></a>**FEA-004: index site browser views** · adopted · external · Browsing schemas, objects and
  relation entries as lists of chips. *Confers* [QUA-008: usable without code](../QUALITIES.md#QUA-008). [Detail](FEA-004.md)
- <a id="FEA-005"></a>**FEA-005: inspector views** · adopted · external · Inspecting, navigating among and editing
  objects, adjacencies and relations from any view. *Confers* [QUA-008: usable without code](../QUALITIES.md#QUA-008). [Detail](FEA-005.md)
- <a id="FEA-006"></a>**FEA-006: persistence** · adopted · external · An app's store outlives its service. *Confers*
  [QUA-008: usable without code](../QUALITIES.md#QUA-008). [Detail](FEA-006.md)
- <a id="FEA-007"></a>**FEA-007: property kinds** · adopted · external · Each property is shown and edited as its kind
  calls for, with who wrote it and when. *Confers* [QUA-008: usable without code](../QUALITIES.md#QUA-008). [Detail](FEA-007.md)
- <a id="FEA-022"></a>**FEA-022: code generation** · proposed · external · Models generate source code in each language
  family's own form, and are read back from it: a model is the source's alternative representation, not a description
  of it. *Confers* [QUA-004: models as an alternative representation of source code](../QUALITIES.md#QUA-004). Its capabilities: [CAP-027: Python3 source generated from schemas](../capabilities/CAP-027.md),
  [CAP-039: schemas round-trip through Python3](../capabilities/CAP-039.md), [CAP-045: TypeScript5 source generated from schemas](../capabilities/README.md#CAP-045) and [CAP-046: generated Python3 bound to its schemas](../capabilities/README.md#CAP-046) to [CAP-049: type parameters in Python3](../capabilities/README.md#CAP-049), [CAP-051: Python3 source from expression models](../capabilities/README.md#CAP-051) to [CAP-061: TypeScript5 source from pattern models](../capabilities/README.md#CAP-061), [CAP-088: TypeScript transpiled to Python](../capabilities/CAP-088.md) to [CAP-091: Ccpp expressions bridged to C and C++ source](../capabilities/CAP-091.md), and [CAP-162: Python dataclasses translated to and from schemas](../capabilities/CAP-162.md).
- <a id="FEA-023"></a>**[FEA-023: patterns over data](FEA-023.md)** · proposed · external · A pattern, one predicate over a store's
  data, is validated, queried, sampled from and generated from alike. *Confers* [QUA-002: open-world models](../QUALITIES.md#QUA-002).
- <a id="FEA-024"></a>**[FEA-024: expressions as data](FEA-024.md)** · proposed · external · Constraints are written once, as terms of
  expression dialects, and are stored, evaluated, validated and translated among the languages they come from.
  *Confers* [QUA-002: open-world models](../QUALITIES.md#QUA-002), [QUA-004: models as an alternative representation of source code](../QUALITIES.md#QUA-004).

- <a id="FEA-038"></a>**[FEA-038: no-code secure services](FEA-038.md)** · proposed · external · An mbse app is served securely without code written for it: its schemas revised by numbered migrations, its server set up with credentials from its environment, and its image built. *Confers* [QUA-008: usable without code](../QUALITIES.md#QUA-008).
- <a id="FEA-039"></a>**[FEA-039: search, sort and filter in browser views](FEA-039.md)** · proposed · external · Users search, sort and filter browser views, through logical views as the lens of every search. *Confers* [QUA-008: usable without code](../QUALITIES.md#QUA-008).
- <a id="FEA-040"></a>**[FEA-040: tenancy](FEA-040.md)** · proposed · external · An app's instances keep each tenant's data as private as its tenancy says, from one private instance for a demo to many users who share only what they choose. *Confers* [QUA-008: usable without code](../QUALITIES.md#QUA-008).
- <a id="FEA-041"></a>**[FEA-041: agent chat integration](FEA-041.md)** · proposed · external · Users chat in the app, with an AI agent and model of their choice, over its modeled data. *Confers* [QUA-001: AI and humans in the loop](../QUALITIES.md#QUA-001).
- <a id="FEA-042"></a>**[FEA-042: constraint enforcement in place of bespoke workarounds](FEA-042.md)** · proposed · external · What bespoke workarounds handle today, such as properties shared among objects, is enforced by constraints. *Confers* [QUA-008: usable without code](../QUALITIES.md#QUA-008).

### Schema-driven data

mbse-schemas' generic machinery: data of any schema, its identity, its transactions and its queries.

- <a id="FEA-025"></a>**[FEA-025: serialization behavior conventions in schema](FEA-025.md)** · proposed · external · Data of any schema is read and written, as values and containers, by conventions its schema declares, through
  one visitor protocol, so that no model needs code of its own to be serialized. *Confers*
  [QUA-008: usable without code](../QUALITIES.md#QUA-008).
- <a id="FEA-034"></a>**[FEA-034: analytic behavior conventions in schema](FEA-034.md)** · proposed · external · Data of any schema is compared, ordered, hashed and validated by conventions its schema declares, never by
  the host language's own. *Confers*
  [QUA-008: usable without code](../QUALITIES.md#QUA-008).
- <a id="FEA-035"></a>**[FEA-035: clean modeling separation between value objects and reference objects](FEA-035.md)** · proposed · external · A
  model separates what it holds as values, owned and nested in containers, from what it links as reference objects,
  identified and related, so that each application of a construct is clean. *Confers*
  [QUA-009: modeling provides clean separation of applications across constructs](../QUALITIES.md#QUA-009).
- <a id="FEA-036"></a>**[FEA-036: serialization behavior is consistent across bindings and generated source code](FEA-036.md)** · proposed · external · Data
  is read and written alike, with the same results and errors, by every binding and by generated source code.
  *Confers* [QUA-006: the same in every language](../QUALITIES.md#QUA-006). *Applies*
  [PRI-027: developers can assume completely consistent behavior across bindings and generated source code](../PRINCIPLES.md#PRI-027).
- <a id="FEA-031"></a>**[FEA-031: schemas as extensible data](FEA-031.md)** · proposed · external · Schemas are data, reference objects of their meta-schemas in modules, that any store holding them extends. *Confers*
  [QUA-008: usable without code](../QUALITIES.md#QUA-008).
- <a id="FEA-032"></a>**[FEA-032: schema loading and wire alignment](FEA-032.md)** · proposed · external · Schemas are loaded into a store by idempotent installs and read by name, so that every implementation holds and
  writes them alike. *Confers*
  [QUA-006: the same in every language](../QUALITIES.md#QUA-006).
- <a id="FEA-033"></a>**[FEA-033: model parameters](FEA-033.md)** · proposed · external · Models take parameters: a definition declares them, binds them, and has its bindings substituted and checked. *Confers*
  [QUA-008: usable without code](../QUALITIES.md#QUA-008).
- <a id="FEA-026"></a>**[FEA-026: deterministic object identity](FEA-026.md)** · proposed · external · Objects are
  identified from the model, never at random, so that the same model built twice, or in another language, gives the
  same identities. *Confers* [QUA-001: AI and humans in the loop](../QUALITIES.md#QUA-001).
- <a id="FEA-030"></a>**[FEA-030: transactions](FEA-030.md)** · proposed · external · A store changes only by transactions
  that commit all or nothing, journaled, snapshotted and replayed, each recorded with who made it and when, so that a
  store's history is the trace of what changed. *Confers* [QUA-001: AI and humans in the loop](../QUALITIES.md#QUA-001).
- <a id="FEA-027"></a>**[FEA-027: mutations as queries](FEA-027.md)** · proposed · external · A store is queried and
  changed in one language: patterns over its data, whose frames stream through terms that match, update and upsert, in
  one transaction. *Confers* [QUA-008: usable without code](../QUALITIES.md#QUA-008).
- <a id="FEA-028"></a>**[FEA-028: one API surface for all data access](FEA-028.md)** · proposed · external · Every
  access to data goes through one clean surface, the store's protocol `Visitors.OfStore`, so that any store serves any
  code alike. *Confers* [QUA-008: usable without code](../QUALITIES.md#QUA-008).
- <a id="FEA-029"></a>**[FEA-029: excluding imperative visitor expressions](FEA-029.md)** · proposed · external · A
  build is declared, not sequenced: whether it creates, updates or clones, and what it builds is identified by, follow
  from its schema, and a spec cannot read in order to write. *Confers* [QUA-008: usable without code](../QUALITIES.md#QUA-008).

- <a id="FEA-043"></a>**[FEA-043: interoperation with imported datatypes](FEA-043.md)** · proposed · external · Models interoperate, efficiently and incrementally, with datatypes imported from cross-language frameworks. *Confers* [QUA-003: no second-order inventions](../QUALITIES.md#QUA-003).

### Internal

Features that serve an engineering persona: the framework's maintainers.

- <a id="FEA-037"></a>**[FEA-037: the framework built on its own protocols](FEA-037.md)** · proposed · internal · The
  framework's own code reads and writes its schemas and specs through the protocols and builders it offers every
  model, so that its maintainers keep one paradigm, not a special case beside it. *Confers*
  [QUA-007: one paradigm at every level of a system](../QUALITIES.md#QUA-007).

## Earlier IDs

| Earlier | Now |
|---|---|
| F-001 | [FEA-017: AI in the loop via the model trace](#FEA-017), and [QUA-001: AI and humans in the loop](../QUALITIES.md#QUA-001) |
| F-002 | [FEA-018: humans in the loop via the model trace](#FEA-018), and [QUA-001: AI and humans in the loop](../QUALITIES.md#QUA-001) |
| F-003 | [QUA-005: an opinionated paradigm](../QUALITIES.md#QUA-005) |
| F-004 | [QUA-003: no second-order inventions](../QUALITIES.md#QUA-003) |
| F-005 | [QUA-002: open-world models](../QUALITIES.md#QUA-002), [PRI-020: no constraint, any configuration](../PRINCIPLES.md#PRI-020) |
| F-006 | [FEA-020: refinable models](#FEA-020) |
| F-007 | [QUA-002: open-world models](../QUALITIES.md#QUA-002), [PRI-021: refinement by constraint](../PRINCIPLES.md#PRI-021) |
| F-008 to F-016 | [FEA-008: expressive program models](#FEA-008) to [FEA-016: community behavior](#FEA-016) |

[FEA-001: schema-driven UI](FEA-001.md) and [FEA-003: no-code logical views](FEA-003.md) to [FEA-007: property kinds](FEA-007.md) kept the IDs they had in the workspace's former `VISUALIZATION.md`. FEA-002 is unassigned:
the work tracker's seed data uses it as an example ID.

## Open items

- **[FEA-021: every generation ambiguity a parameter](FEA-021.md) counts parameters, not coverage of ambiguities.** It
  needs a measure, such as the decisions fixed for every schema that should be parameters ([CAP-027: Python3 source
  generated from schemas](../capabilities/CAP-027.md#bridges) lists them).
- **[QUA-002: open-world models](../QUALITIES.md#QUA-002) is not met in shape.** mbse-schemas' decoding refuses an undeclared key, where [PRI-002: preserve, don't lose](../PRINCIPLES.md#PRI-002) preserves it; [CAP-033: undeclared properties preserved](../capabilities/CAP-033.md#design)
  proposes preserving (Undeclared properties, policy 3) but keeps closed as the default, which
  [QUA-002: open-world models](../QUALITIES.md#QUA-002)'s "by default" contradicts. Name resolution staying closed ([FEA-020: refinable models](FEA-020.md#decided-by-an-agent-for-review)) is consistent with
  [QUA-002: open-world models](../QUALITIES.md#QUA-002): names resolve or are refused, while data is kept.

---

<!-- nav -->
[← Qualities](../QUALITIES.md) · [Home](../README.md) · [Capabilities →](../capabilities/README.md)
