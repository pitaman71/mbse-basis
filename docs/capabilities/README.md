<!-- nav -->
[← Features](../features/README.md) · [Home](../README.md) · [Principles →](../PRINCIPLES.md)

# Capabilities

The third tier of the design spec: an increment of utility within a feature, how in a coming release the product
solves a problem, circumscribing the part of the problem space it can solve. A feature's capabilities enumerate, in
full, how it is met; a capability has no capabilities below it. A capability is planned for one release, and
may have tasks; what remains after its release is another capability, not the same one again ([the
basis](../README.md#the-design-spec), scope is enumerated by capabilities and contained by features). **Current** says whether each is met and where that was checked, so that build status lives here rather
than in each repository's design document.

## Index

### Equivalent implementations

- <a id="CAP-024"></a>**CAP-024: the same conformance corpora** · proposed · Every repository's Python and TypeScript implementations pass the same
  conformance corpora (CONF suites): the same names, errors and messages, and byte-identical JSON. *Implements*
  [FEA-019: equivalent implementations](../features/README.md#FEA-019).
  - **Current**: met in mbse-schemas, mbse-expressions, mbse-patterns and mbse-programs; to assess in
    mbse-codegen-python.
- <a id="CAP-030"></a>**CAP-030: the same cases in both languages** · proposed · Every repository's tests and tutorials hold the same cases in both
  languages. *Implements* [FEA-019: equivalent implementations](../features/README.md#FEA-019).
  - **Current**: as [CAP-024: the same conformance corpora](#CAP-024)'s: met in mbse-schemas, mbse-expressions, mbse-patterns and mbse-programs; to assess in
    mbse-codegen-python.
- <a id="CAP-031"></a>**CAP-031: 100% coverage of both** · proposed · Every repository's tests cover 100% of both implementations. *Implements*
  [FEA-019: equivalent implementations](../features/README.md#FEA-019).
  - **Current**: as [CAP-024: the same conformance corpora](#CAP-024)'s: met in mbse-schemas, mbse-expressions, mbse-patterns and mbse-programs; to assess in
    mbse-codegen-python.
- <a id="CAP-032"></a>**CAP-032: deliberate differences listed** · proposed · Each deliberate difference between a repository's implementations is
  listed in its `docs/EQUIVALENCE.md`. *Implements* [FEA-019: equivalent implementations](../features/README.md#FEA-019).
  - **Current**: as [CAP-024: the same conformance corpora](#CAP-024)'s: met in mbse-schemas, mbse-expressions, mbse-patterns and mbse-programs; to assess in
    mbse-codegen-python.

### Open-world models

- <a id="CAP-025"></a>**[CAP-025: nothing mandatory but by constraint](CAP-025.md)** · proposed · Nothing in a schema's content is mandatory but by
  a constraint, the open-world default ([PRI-020: no constraint, any configuration](../PRINCIPLES.md#PRI-020)) applied to schemas (checked as [CAP-029: three-valued constraint checking](CAP-029.md) says). *Implements* [FEA-020: refinable models](../features/README.md#FEA-020).
  - **Current**: met in mbse-schemas 0.10.0; its dependents to assess.
- <a id="CAP-033"></a>**[CAP-033: undeclared properties preserved](CAP-033.md)** · proposed · Properties a schema does not declare are preserved when data is read,
  and written back as read. *Implements*: none (see Open items). *Applies* [PRI-002: preserve, don't lose](../PRINCIPLES.md#PRI-002).
  - **Current**: not met.
- <a id="CAP-034"></a>**[CAP-034: schemas specialized by classifier intersection and union](CAP-034.md)** · proposed · A module declares subtypes of a
  schema it does not own by intersecting and uniting classifiers, as KerML and SysML v2 do, with qualified extension
  properties. *Implements* [FEA-020: refinable models](../features/README.md#FEA-020).
  - **Current**: not met.
- <a id="CAP-035"></a>**[CAP-035: schema evolution](CAP-035.md)** · proposed · A schema evolves so that data written for it stays valid. *Implements*
  [FEA-020: refinable models](../features/README.md#FEA-020).
  - **Current**: not met.
- <a id="CAP-029"></a>**[CAP-029: three-valued constraint checking](CAP-029.md)** · proposed · Constraints are checked, three-valued. *Implements* [FEA-020: refinable models](../features/README.md#FEA-020), [FEA-023: patterns over data](../features/FEA-023.md).
  - **Current**: met: mbse-patterns' validators (0.1; the VAL suites).
- <a id="CAP-042"></a>**[CAP-042: data generated from constraints](CAP-042.md)** · proposed · Data is generated from constraints: sampled, and pseudorandom.
  *Implements* [FEA-020: refinable models](../features/README.md#FEA-020), [FEA-023: patterns over data](../features/FEA-023.md).
  - **Current**: met: mbse-patterns' sampling and generators (0.3, 0.4; the GEN suites).
- <a id="CAP-043"></a>**[CAP-043: constraints resolved in any direction](CAP-043.md)** · proposed · Constraints are resolved in any direction. *Implements* [FEA-020: refinable models](../features/README.md#FEA-020).
  - **Current**: to assess.

- <a id="CAP-167"></a>**[CAP-167: schemas refined by other schemas](CAP-167.md)** · proposed · An object or container schema refines another through `Schemas.Refines`, inheriting its members and narrowing them where validation confirms it. *Implements* [FEA-020: refinable models](../features/FEA-020.md). *Relates to* [CAP-034: schemas specialized by classifier intersection and union](CAP-034.md).
  - **Current**: met in mbse-schemas 0.26.4 (checked in the code at 0.26.4: `Schemas.Refines`).
### Patterns over data

- <a id="CAP-150"></a>**[CAP-150: predicates as data](CAP-150.md)** · proposed · A predicate, a named constraint over symbols and parameters, is built fluently, written and read as
  data, applied by reference, and checked when asked. *Implements* [FEA-023: patterns over data](../features/FEA-023.md). Numbered CAP-069 to CAP-071 in batch 2c by mistake; those IDs belong to the wire-format shorthands.
  - **Current**: met (mbse-patterns 0.1, 0.5, 0.6; the CON suites).
- <a id="CAP-151"></a>**[CAP-151: constraint evaluation within query interpretation](CAP-151.md)** · proposed · A predicate is a query: its matches among a store's data stream lazily, planned from the constraint's
  shape, and a store that answers queries natively answers them. *Implements* [FEA-023: patterns over data](../features/FEA-023.md). Numbered CAP-069 to CAP-071 in batch 2c by mistake; those IDs belong to the wire-format shorthands.
  - **Current**: met (mbse-patterns 0.1; the QRY suites).
- <a id="CAP-152"></a>**[CAP-152: relation constraint terms as mandatory, possible, or forbidden entry patterns](CAP-152.md)** · proposed · Whether a link is mandatory, possible or forbidden is a predicate: quantifiers over a
  store's extents, tests of an adjacency's entries, and weighted alternatives. *Implements* [FEA-023: patterns over data](../features/FEA-023.md). Numbered CAP-069 to CAP-071 in batch 2c by mistake; those IDs belong to the wire-format shorthands.
  - **Current**: met (mbse-patterns 0.2; the ALG suites).
- <a id="CAP-072"></a>**[CAP-072: distributions in predicates](CAP-072.md)** · proposed · A predicate's constraint says how its matches are distributed, by weighted alternatives and
  distributions of values, so that one predicate is validated, queried, sampled and generated from alike. *Implements* [FEA-023: patterns over data](../features/FEA-023.md).
  - **Current**: met (mbse-patterns 0.3, 0.4; the DST suites).
- <a id="CAP-073"></a>**[CAP-073: distributions fit from data](CAP-073.md)** · proposed · A characterizer reads a stream of objects and fits a distribution to them, in one pass and bounded
  memory, round-tripping with the generators. *Implements* [FEA-023: patterns over data](../features/FEA-023.md).
  - **Current**: not met.

### Transforms

- <a id="CAP-074"></a>**[CAP-074: transforms applied step by step](CAP-074.md)** · proposed · A transform, a rewrite with a before and an after, is applied by a session one decision per
  step, a policy ranking the candidates, and the steps kept as a trace. *Implements* [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md), [FEA-017: AI in the loop via the model trace](../features/README.md#FEA-017), [FEA-018: humans in the loop via the model trace](../features/README.md#FEA-018).
  - **Current**: met (mbse-patterns 0.7; the TRF suites).
- <a id="CAP-075"></a>**[CAP-075: steps linked to what they matched and wrote](CAP-075.md)** · proposed · Each step of a transform links the elements it matched and wrote, each in
  a role, as relations that predicates query. *Implements* [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md), [FEA-017: AI in the loop via the model trace](../features/README.md#FEA-017), [FEA-018: humans in the loop via the model trace](../features/README.md#FEA-018).
  - **Current**: met (mbse-patterns 0.9).
- <a id="CAP-076"></a>**[CAP-076: reruns reuse decisions](CAP-076.md)** · proposed · A rerun takes each earlier decision again where its key still occurs, reports the orphans, and diffs
  the traces. *Implements* [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md), [FEA-017: AI in the loop via the model trace](../features/README.md#FEA-017), [FEA-018: humans in the loop via the model trace](../features/README.md#FEA-018).
  - **Current**: met (mbse-patterns 0.8; TRF-08).
- <a id="CAP-077"></a>**[CAP-077: changes explained across runs](CAP-077.md)** · proposed · A source diff names what changed in the model, and a target diff traces each change in the
  output to the model change or the answer that caused it. *Implements* [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md), [FEA-017: AI in the loop via the model trace](../features/README.md#FEA-017), [FEA-018: humans in the loop via the model trace](../features/README.md#FEA-018).
  - **Current**: blocked: diffing stores in general is mbse-journals', which is planned.
- <a id="CAP-078"></a>**[CAP-078: incremental rebuild](CAP-078.md)** · proposed · A rerun after a model change reuses the work of every step whose reads did not change, by recorded reads,
  fingerprints and invalidation, with the same result as a run from scratch. *Implements* [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md), [FEA-017: AI in the loop via the model trace](../features/README.md#FEA-017), [FEA-018: humans in the loop via the model trace](../features/README.md#FEA-018).
  - **Current**: not met.
- <a id="CAP-079"></a>**[CAP-079: steps undone](CAP-079.md)** · proposed · A session takes back its last step exactly, every step's effect recorded as mutations with what they replaced. *Implements* [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md), [FEA-017: AI in the loop via the model trace](../features/README.md#FEA-017), [FEA-018: humans in the loop via the model trace](../features/README.md#FEA-018).
  - **Current**: not met.
- <a id="CAP-080"></a>**[CAP-080: invertible transforms](CAP-080.md)** · proposed · A transform declares its inverse, so that a target and its trace give back the source, and an edit of
  the output is carried back to the model or named as one no inverse can carry. *Implements* [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md), [FEA-017: AI in the loop via the model trace](../features/README.md#FEA-017), [FEA-018: humans in the loop via the model trace](../features/README.md#FEA-018).
  - **Current**: not met.
- <a id="CAP-081"></a>**[CAP-081: transforms composed into pipelines](CAP-081.md)** · proposed · Transforms compose as passes, one's after-symbols bound to the next one's before-symbols, a
  pipeline itself a transform. *Implements* [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md), [FEA-017: AI in the loop via the model trace](../features/README.md#FEA-017), [FEA-018: humans in the loop via the model trace](../features/README.md#FEA-018).
  - **Current**: not met.
- <a id="CAP-082"></a>**[CAP-082: completeness reported](CAP-082.md)** · proposed · A session reports every element no transform has rewritten that some transform could match. *Implements* [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md), [FEA-017: AI in the loop via the model trace](../features/README.md#FEA-017), [FEA-018: humans in the loop via the model trace](../features/README.md#FEA-018).
  - **Current**: not met.
- <a id="CAP-083"></a>**[CAP-083: policies with guards and distributions](CAP-083.md)** · proposed · A policy's clauses are guarded by predicates over the match, and weigh a parameter's values by
  a distribution over its domain, written as data. *Implements* [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md), [FEA-017: AI in the loop via the model trace](../features/README.md#FEA-017), [FEA-018: humans in the loop via the model trace](../features/README.md#FEA-018).
  - **Current**: not met.

### Expressions as data

- <a id="CAP-095"></a>**[CAP-095: Basic terms as data](CAP-095.md)** · proposed · Constraints are written as terms of Basic's core vocabulary, total and pure so that any is also a
  constraint, and are validated, stored, serialized and compared as any value of their schemas. *Implements* [FEA-024: expressions as data](../features/FEA-024.md).
  - **Current** (main, v0.5.4): met.
- <a id="CAP-106"></a>**[CAP-106: expressions evaluated three-valued](CAP-106.md)** · proposed · An expression is evaluated in three-valued
  logic (Kleene's): an absent property is unknown, nothing is coerced, and everything but a reference object compares
  deeply. *Implements* [FEA-024: expressions as data](../features/FEA-024.md).
  - **Current** (main, v0.5.4): met.
- <a id="CAP-096"></a>**[CAP-096: collections in expressions](CAP-096.md)** · proposed · Expressions read lists and an object's entries as collections, quantify over their items, and
  compare them deeply. *Implements* [FEA-024: expressions as data](../features/FEA-024.md).
  - **Current** (main, v0.5.4): met.
- <a id="CAP-097"></a>**[CAP-097: value domains of published standards](CAP-097.md)** · proposed · A value's domain names a published standard (IEEE 754, IEEE 1164, two's complement integers),
  with exact-then-rounded arithmetic, bitwise operations and explicit conversions. *Implements* [FEA-024: expressions as data](../features/FEA-024.md).
  - **Current** (main, v0.5.4): met.
- <a id="CAP-098"></a>**[CAP-098: dialects over one framework](CAP-098.md)** · proposed · Expression languages are dialects of one framework, which validates, infers, evaluates and
  translates any of them from its kinds' roles, a dialect extending another. *Implements* [FEA-024: expressions as data](../features/FEA-024.md).
  - **Current** (main, v0.5.4): met.
- <a id="CAP-099"></a>**[CAP-099: partial evaluation](CAP-099.md)** · proposed · An expression is reduced over the variables given, to a residual that agrees with it wherever it evaluates. *Implements* [FEA-024: expressions as data](../features/FEA-024.md).
  - **Current** (main, v0.5.4): met.
- <a id="CAP-100"></a>**[CAP-100: six languages' expression dialects](CAP-100.md)** · proposed · Python's, MATLAB's, Excel's, LaTeX's, C and C++'s and SystemVerilog's expressions are
  dialects, each with its own kinds, values, evaluation, source text and scope. *Implements* [FEA-024: expressions as data](../features/FEA-024.md).
  - **Current** (main, v0.5.4): met.
- <a id="CAP-101"></a>**[CAP-101: translation between dialects](CAP-101.md)** · proposed · Each pair of dialects translates both ways by declared rules, round-tripping what both can write, and
  agreeing with a translation through a third. *Implements* [FEA-024: expressions as data](../features/FEA-024.md).
  - **Current** (main, v0.5.4): met.
- <a id="CAP-102"></a>**[CAP-102: collections translated to LaTeX and C and C++](CAP-102.md)** · proposed · Collections translate to LaTeX and C and C++, and directly between
  SystemVerilog and the other dialects. *Implements* [FEA-024: expressions as data](../features/FEA-024.md).
  - **Current**: not met.
- <a id="CAP-103"></a>**[CAP-103: SystemVerilog's other operations translated](CAP-103.md)** · proposed · `has`, the logical `>>` and the 4-state comparisons translate between
  Basic and SystemVerilog. *Implements* [FEA-024: expressions as data](../features/FEA-024.md).
  - **Current**: not met.
- <a id="CAP-104"></a>**[CAP-104: typed values translated beyond C and SystemVerilog](CAP-104.md)** · proposed · Conversions and typed values translate to Python, MATLAB, Excel and LaTeX. *Implements* [FEA-024: expressions as data](../features/FEA-024.md).
  - **Current**: not met.
- <a id="CAP-105"></a>**[CAP-105: Excel ranges and structured references](CAP-105.md)** · proposed · Excel's ranges (`A1:B3`) and structured references (`Table1[@age]`) are
  modeled, as array values. *Implements* [FEA-024: expressions as data](../features/FEA-024.md).
  - **Current**: not met.

### Serialization behavior conventions in schema

- <a id="CAP-107"></a>**[CAP-107: one visitor protocol reads and writes data](CAP-107.md)** · proposed · Code reads and
  writes a value of any schema through one protocol per kind, `Visitors.OfX`, its read-only view `Readers.OfX` and their
  shorthands, the visitor's mode deciding whether a write takes effect. *Implements* [FEA-025: serialization behavior conventions in schema](../features/FEA-025.md).
  *Applies* [PRI-004: one visitor protocol per kind](../PRINCIPLES.md#PRI-004).
  - **Current**: met in mbse-schemas 0.26.3.
- <a id="CAP-153"></a>**[CAP-153: unions and intersections of named branches and parts](CAP-153.md)** · proposed · A union holds exactly one of its named branches and an intersection every one of its named parts, written unpacked, by name, and read flat where the schema says so. *Implements* [FEA-025: serialization behavior conventions in schema](../features/FEA-025.md).
  - **Current**: met in mbse-schemas 0.26.4 (checked in the code at 0.26.4: `HasBranch`, `HasPart`, flat unions and intersections, unique names).
- <a id="CAP-155"></a>**[CAP-155: `unique` clauses on relation schemas govern relation cardinality](CAP-155.md)** · proposed · A relation links two or more reference objects by named links, and its `unique` clauses decide whether its entries are a set or a list and what keys them from each end. *Implements* [FEA-025: serialization behavior conventions in schema](../features/FEA-025.md). *Relates to* [FEA-034: analytic behavior conventions in schema](../features/FEA-034.md).
  - **Current**: met in mbse-schemas 0.26.4 (checked in the code at 0.26.4: equal entries elided in a set, an adjacency's `at` and `project`).
- <a id="CAP-157"></a>**[CAP-157: values of any schema, restricted or not](CAP-157.md)** · proposed · An `OfAny` holds a value of any schema, or of the schemas its builder selects, refusing any other when written and read. *Implements* [FEA-025: serialization behavior conventions in schema](../features/FEA-025.md).
  - **Current**: met in mbse-schemas 0.26.4 (checked in the code at 0.26.4: `Schemas.OfAny.Value`, the refusal of another host type).
- <a id="CAP-168"></a>**[CAP-168: containers by an index neither ordered nor hashable read back](CAP-168.md)** · proposed · A container whose index is neither ordered nor hashable is read back from a snapshot. *Implements* [FEA-025: serialization behavior conventions in schema](../features/FEA-025.md).
  - **Current**: not met (checked in the code: reading one is refused, "not read from snapshots yet").
### Clean modeling separation between value objects and reference objects

- <a id="CAP-108"></a>**[CAP-108: relations as scalable containers](CAP-108.md)** · proposed · Values, value objects among
  them, are held in containers by an index of any schema, dense, sparse or by key, nesting, and belong to their one
  owner; reference objects are never held in containers, but linked by relations of two links or more, and identified.
  *Implements* [FEA-035: clean modeling separation between value objects and reference objects](../features/FEA-035.md).
  - **Current**: met in mbse-schemas 0.26.3; value and reference objects checked in the code at 0.26.4 (`.ref()`,
    `Proxies.owner_of`, validation's refusals).
- <a id="CAP-154"></a>**[CAP-154: value objects and reference objects](CAP-154.md)** · superseded by [CAP-108: relations as scalable containers](CAP-108.md) · An
  object schema describes reference objects, linked by relations and identified, or value objects, owned by one
  owner, nested and compared deeply. Merged into [CAP-108: relations as scalable containers](CAP-108.md), with its content.

### Serialization behavior consistent across bindings and generated source code

- <a id="CAP-159"></a>**[CAP-159: error handling during deserialization is consistent across Python3 and Typescript5 bindings](CAP-159.md)** · proposed · Every problem in decoded data raises one `DecodeError`, with a one-line reason and a location, identical in every binding but for a YAML parser's own syntax errors. *Implements* [FEA-036: serialization behavior is consistent across bindings and generated source code](../features/FEA-036.md). *Applies* [PRI-009: one error shape](../PRINCIPLES.md#PRI-009).
  - **Current**: met in mbse-schemas 0.26.4 (checked in the code at 0.26.4: `Errors.DecodeError` in both languages).

### Analytic behavior conventions in schema

- <a id="CAP-111"></a>**[CAP-111: equality and ordering defined by the schema](CAP-111.md)** · proposed · Values are
  compared, ordered and hashed by their schema, never by the host language's equality. *Implements*
  [FEA-034: analytic behavior conventions in schema](../features/FEA-034.md).
  - **Current**: met in mbse-schemas 0.26.3.
- <a id="CAP-147"></a>**[CAP-147: links validated against their schemas](CAP-147.md)** · proposed · Validation checks
  each linked object against the schema its link declares. *Implements* [FEA-034: analytic behavior conventions in schema](../features/FEA-034.md).
  - **Current**: not met.

- <a id="CAP-160"></a>**[CAP-160: data validated against its schema on request](CAP-160.md)** · proposed · Data is checked against its schema, with what is reachable from it, only when the caller asks, problems reported by path and what cannot be decided as unknown. *Implements* [FEA-034: analytic behavior conventions in schema](../features/FEA-034.md). *Applies* [PRI-007: three-valued checking on request](../PRINCIPLES.md#PRI-007).
  - **Current**: met in mbse-schemas 0.26.4 (checked in the code at 0.26.4: `Validators.Validate`, `Check`, `Reachable`).
- <a id="CAP-166"></a>**[CAP-166: constraints attached where they constrain](CAP-166.md)** · proposed · Constraints are attached to the parts of a model they constrain, and those attached to a model combine into one conjunction. *Implements* [FEA-034: analytic behavior conventions in schema](../features/FEA-034.md).
  - **Current**: not met: not designed (Open questions).
### Schemas as extensible data

- <a id="CAP-109"></a>**[CAP-109: schemas as linked objects in modules](CAP-109.md)** · proposed · Every schema object
  is a reference object of its kind's meta-schema, linked to the others by relations, built by builders that are
  visitors of it, and defined in nesting modules. *Implements* [FEA-031: schemas as extensible data](../features/FEA-031.md).
  - **Current**: met in mbse-schemas 0.26.3.
- <a id="CAP-116"></a>**[CAP-116: framework schemas extended, checked](CAP-116.md)** · proposed · Any transaction may
  add members to a schema the store was made holding, meta-schemas included, but not change or remove them, each store
  extending its own. *Implements* [FEA-031: schemas as extensible data](../features/FEA-031.md), [FEA-020: refinable models](../features/FEA-020.md).
  - **Current**: met in mbse-schemas 0.23.0.
- <a id="CAP-117"></a>**[CAP-117: extension adjacencies to any relation](CAP-117.md)** · proposed · An extension's
  adjacency may be to any relation, one with properties or more than two links included. *Implements*
  [FEA-031: schemas as extensible data](../features/FEA-031.md).
  - **Current**: not met.

- <a id="CAP-165"></a>**[CAP-165: snapshots read by a store lacking their extensions](CAP-165.md)** · proposed · A store reading a snapshot made with an extension it lacks ignores, and lists, each member whose meaning needs that extension. *Implements* [FEA-031: schemas as extensible data](../features/FEA-031.md).
  - **Current**: met in mbse-schemas 0.26.4 (checked in the code at 0.26.4: `ignored` in `Plain`, `JSON` and `YAML`).
- <a id="CAP-171"></a>**[CAP-171: parameters attached to every schema kind by extension](CAP-171.md)** · proposed · `Parametrics`, installed before
  use, extends every kind of schema with an adjacency to its set of parameters, which the core no longer declares, and
  a store lacking it reads their snapshots. *Implements* [FEA-031: schemas as extensible data](../features/FEA-031.md); *relates to*
  [FEA-033: model parameters](../features/FEA-033.md).
  - **Current**: met in mbse-schemas 0.24.0.
### Schema loading and wire alignment

- <a id="CAP-115"></a>**[CAP-115: schemas defined by idempotent installs](CAP-115.md)** · proposed · Every schema is
  defined in a module-scope `install(txn)`, a transaction that upserts it, so that installing again writes nothing, and
  the framework defines its own schemas the same way. *Implements* [FEA-032: schema loading and wire alignment](../features/FEA-032.md).
  - **Current**: met in mbse-schemas 0.23.0.
- <a id="CAP-110"></a>**[CAP-110: a store's schemas read as one module](CAP-110.md)** · proposed · A store's schemas are
  read as one hierarchical root module, each by its module-qualified name, which resolves or is refused. *Implements*
  [FEA-032: schema loading and wire alignment](../features/FEA-032.md).
  - **Current**: met in mbse-schemas 0.26.4, by schema objects' paths from the root module `"."` and `References`, not
    by a `root_module()` method.

- <a id="CAP-156"></a>**[CAP-156: the five basic scalars with boundless domains](CAP-156.md)** · proposed · Every store holds the five basic scalars, `Schemas.OfBool` to `Schemas.OfBytes`, each mapped to each language's host type, and builds no other scalar schema. *Implements* [FEA-032: schema loading and wire alignment](../features/FEA-032.md).
  - **Current**: met since mbse-schemas 0.18.0 (checked in the code at 0.26.4: "a store builds no scalar schema").
- <a id="CAP-158"></a>**[CAP-158: values written as plain data, JSON and YAML](CAP-158.md)** · proposed · Any value is written as plain data, strict JSON or YAML 1.2, through a store that names its schemas, and read back, byte-identical in every implementation. *Implements* [FEA-032: schema loading and wire alignment](../features/FEA-032.md).
  - **Current**: met in mbse-schemas 0.26.4 (checked in the code at 0.26.4: `Plain`, `JSON`, `YAML` in both languages).
### Model parameters

- <a id="CAP-112"></a>**[CAP-112: parameters modeled as schema data](CAP-112.md)** · proposed · A definition's
  parameters are declared through `Parametrics`, a module installed before use, which validates them. *Implements*
  [FEA-033: model parameters](../features/FEA-033.md).
  - **Current**: met in mbse-schemas 0.24.0.
- <a id="CAP-113"></a>**[CAP-113: parameters bound at their definitions](CAP-113.md)** · proposed · A definition binds
  each of its parameters to a value or an object, through `Parametrics`' bindings. *Implements*
  [FEA-033: model parameters](../features/FEA-033.md).
  - **Current**: not met.
- <a id="CAP-114"></a>**[CAP-114: parameter bindings are substituted and checked](CAP-114.md)** · proposed · A binding is substituted
  where its definition is used, and its value checked against the schema its parameter is for. *Implements*
  [FEA-033: model parameters](../features/FEA-033.md).
  - **Current**: not met.

- <a id="CAP-163"></a>**[CAP-163: parameters bound, applied and generated beyond mbse-schemas](CAP-163.md)** · proposed · Parameters are bound and applied in mbse-expressions, bound by predicates in mbse-patterns and by statements in mbse-programs, and generated as each language's own construct. *Implements* [FEA-033: model parameters](../features/FEA-033.md). *Relates to* [CAP-113: parameters bound at their definitions](CAP-113.md), [CAP-114: parameter bindings are substituted and checked](CAP-114.md).
  - **Current**: not met.
### Deterministic object identity

- <a id="CAP-118"></a>**[CAP-118: singletons, owned and counted objects](CAP-118.md)** · proposed · A reference object
  is a singleton, owned or counted, as its schema declares, and nothing about its identity is drawn at random.
  *Implements* [FEA-026: deterministic object identity](../features/FEA-026.md).
  - **Current**: met in mbse-schemas 0.20.0.
- <a id="CAP-119"></a>**[CAP-119: owned objects found by path](CAP-119.md)** · proposed · An owned object is found by
  its path, each step's adjacency called with the keys of the entry that leads to it, and its path is read off its
  ownership entries. *Implements* [FEA-026: deterministic object identity](../features/FEA-026.md).
  - **Current**: met in mbse-schemas 0.20.0.
- <a id="CAP-120"></a>**[CAP-120: owned objects named and placed when built](CAP-120.md)** · proposed · An owned
  object's keys are generated from its owning relation's key patterns, and an object built without an owner is given the
  one owner possible when its transaction ends. *Implements* [FEA-026: deterministic object identity](../features/FEA-026.md).
  - **Current**: met in mbse-schemas 0.20.0.
- <a id="CAP-121"></a>**[CAP-121: owned objects deleted in cascade](CAP-121.md)** · proposed · Removing an owned
  object's owning entry deletes it, and in cascade everything it owns, within the transaction. *Implements*
  [FEA-026: deterministic object identity](../features/FEA-026.md).
  - **Current**: met in mbse-schemas 0.20.0.
- <a id="CAP-123"></a>**[CAP-123: schema objects identified by path](CAP-123.md)** · proposed · A named schema object's
  identity is its path from the root module; an unnamed one has none, and is written nested in the one object that links
  it. *Implements* [FEA-026: deterministic object identity](../features/FEA-026.md).
  - **Current**: met in mbse-schemas 0.21.0.
- <a id="CAP-130"></a>**[CAP-130: references to objects, entries and frames](CAP-130.md)** · proposed · An object, a
  relation entry and a frame each have a reference, a value written and read as any, which resolves to what it
  designates in a store. *Implements* [FEA-026: deterministic object identity](../features/FEA-026.md).
  - **Current**: met in mbse-schemas 0.25.0.
- <a id="CAP-132"></a>**[CAP-132: paths retired for references](CAP-132.md)** · proposed · Paths are retired: references
  designate objects, entries and frames, and paths no longer overlap them. *Implements*
  [FEA-026: deterministic object identity](../features/FEA-026.md).
  - **Current**: not met.
- <a id="CAP-133"></a>**[CAP-133: no durable references to counted objects](CAP-133.md)** · proposed · Nothing holds a
  durable reference to a counted object: the executor finds what an upsert made without one. *Implements*
  [FEA-026: deterministic object identity](../features/FEA-026.md).
  - **Current**: not met.

### Transactions

- <a id="CAP-124"></a>**[CAP-124: writes all-or-nothing in transactions](CAP-124.md)** · proposed · Every write to a
  store is part of a transaction, under an id the program gives, which commits all of its writes or none, each store's
  apart from another's. *Implements* [FEA-030: transactions](../features/FEA-030.md).
  - **Current**: met in mbse-schemas 0.22.0.
- <a id="CAP-125"></a>**[CAP-125: imperative transaction scope](CAP-125.md)** · proposed · Code that calls builders
  writes within a transaction's imperative scope, all or nothing, as an expression's terms do. *Implements*
  [FEA-030: transactions](../features/FEA-030.md).
  - **Current**: met in mbse-schemas 0.22.0.
- <a id="CAP-127"></a>**[CAP-127: snapshots made of transactions](CAP-127.md)** · proposed · A store's snapshot is two
  transactions, its schemas then its data, and reading one replays them. *Implements* [FEA-030: transactions](../features/FEA-030.md).
  - **Current**: met in mbse-schemas 0.22.0.
- <a id="CAP-128"></a>**[CAP-128: graphs sent as one-transaction documents](CAP-128.md)** · proposed · A graph sent
  without its store is one transaction, its counted objects numbered within it, and the owned objects and singletons it
  links referred to by path. *Implements* [FEA-030: transactions](../features/FEA-030.md).
  - **Current**: met in mbse-schemas 0.22.0.
- <a id="CAP-129"></a>**[CAP-129: journals replayed by execution](CAP-129.md)** · proposed · A journal is the list of
  transactions as submitted, replayed by executing each again. *Implements* [FEA-030: transactions](../features/FEA-030.md).
  - **Current**: met in mbse-schemas 0.22.0.
- <a id="CAP-134"></a>**[CAP-134: transactions recorded with provenance](CAP-134.md)** · proposed · Each transaction
  that writes is recorded with when and where it ran, its session and its identity, and linked to the objects it created
  or last modified, for the schemas an app chooses. *Implements* [FEA-030: transactions](../features/FEA-030.md).
  - **Current**: met in mbse-schemas 0.26.3.
- <a id="CAP-135"></a>**[CAP-135: provenance records reproducible and attributable](CAP-135.md)** · proposed · Every
  transaction's provenance record is reproducible and attributable: none gets a random `uid`, the clock's time or the
  shared session `unknown`, whether it comes from an imperative scope or from an expression that names none.
  *Implements* [FEA-030: transactions](../features/FEA-030.md).
  - **Current**: not met.

- <a id="CAP-164"></a>**[CAP-164: subsequent snapshots sent as transactions](CAP-164.md)** · proposed · A stateful writer sends a store's later snapshots as the transactions since the last, without its modules and schemas again. *Implements* [FEA-030: transactions](../features/FEA-030.md).
  - **Current**: not met.
### Mutations as queries

- <a id="CAP-131"></a>**[CAP-131: frames witness values and entries](CAP-131.md)** · proposed · A frame witnesses the
  property values and relation entries it asserts, each by its objects' references. *Implements*
  [FEA-027: mutations as queries](../features/FEA-027.md).
  - **Current**: met in mbse-schemas 0.26.3.
- <a id="CAP-137"></a>**[CAP-137: patterns of symbols, variables and specs](CAP-137.md)** · proposed · A pattern
  declares symbols bound to reference objects and variables assigned values, and its spec says what must hold of a
  frame, all as schema data. *Implements* [FEA-027: mutations as queries](../features/FEA-027.md).
  - **Current**: met in mbse-schemas 0.22.0.
- <a id="CAP-138"></a>**[CAP-138: mutation expressions over frame streams](CAP-138.md)** · proposed · A transaction's
  expression is a chain of terms, map, reduce, partition, update and upsert, each consuming and producing a stream of
  frames. *Implements* [FEA-027: mutations as queries](../features/FEA-027.md).
  - **Current**: met in mbse-schemas 0.22.0.
- <a id="CAP-139"></a>**[CAP-139: upserts find before they create](CAP-139.md)** · proposed · An upsert finds the object
  its spec designates before it creates one: an owned object by its owning entry, a counted one by what made it, a
  schema object by its name. *Implements* [FEA-027: mutations as queries](../features/FEA-027.md).
  - **Current**: met in mbse-schemas 0.22.0.
- <a id="CAP-140"></a>**[CAP-140: entries removed through a spec](CAP-140.md)** · proposed · A spec removes entries as
  it inserts them, through an adjacency's `remove` and `clear`. *Implements* [FEA-027: mutations as queries](../features/FEA-027.md).
  - **Current**: met in mbse-schemas 0.23.0.
- <a id="CAP-141"></a>**[CAP-141: queries start from a referenced object](CAP-141.md)** · proposed · A pattern's symbol
  may be given a reference in place of a schema, binding the one object it designates, so that a query starts from it.
  *Implements* [FEA-027: mutations as queries](../features/FEA-027.md).
  - **Current**: met in mbse-schemas 0.26.3.
- <a id="CAP-142"></a>**[CAP-142: expressions evaluated in queries](CAP-142.md)** · proposed · The executor evaluates
  the expressions of a query: a pattern's `requires` and variables, a collector's fold, a branch's condition.
  *Implements* [FEA-027: mutations as queries](../features/FEA-027.md).
  - **Current**: blocked: its evaluation is mbse-expressions', in its port ([CAP-142: expressions evaluated in queries](CAP-142.md#blocked)).
- <a id="CAP-144"></a>**[CAP-144: transactions sharded and run in parallel](CAP-144.md)** · proposed · A transaction is
  divided into shards that run in parallel, as MapReduce runs, with the same effect as run in order. *Implements*
  [FEA-027: mutations as queries](../features/FEA-027.md).
  - **Current**: not met.
- <a id="CAP-145"></a>**[CAP-145: queries over a distributed persistent store](CAP-145.md)** · proposed · Queries run
  over a persistent store distributed beyond one process, through a transactional cache, with certificates that track
  their writes. *Implements* [FEA-027: mutations as queries](../features/FEA-027.md).
  - **Current**: not met.
- <a id="CAP-146"></a>**[CAP-146: queries planned from specs and constraints](CAP-146.md)** · proposed · The executor
  plans a query from its patterns' specs and constraints, rather than enumerating each cross product. *Implements*
  [FEA-027: mutations as queries](../features/FEA-027.md).
  - **Current**: not met.

### One API surface for all data access

- <a id="CAP-149"></a>**[CAP-149: data accessed through the store protocol](CAP-149.md)** · proposed · An object's
  property values, a value object's, and the entries linking an object are read and written through `Visitors.OfStore`,
  which a transaction's `Proposals` implements. *Implements* [FEA-028: one API surface for all data access](../features/FEA-028.md).
  - **Current**: met in mbse-schemas 0.22.0.
- <a id="CAP-126"></a>**[CAP-126: schema objects read through the store protocol](CAP-126.md)** · proposed · Schema
  objects are read and written through `Visitors.OfStore`, as data is, not field by field. *Implements*
  [FEA-028: one API surface for all data access](../features/FEA-028.md).
  - **Current**: not met.

- <a id="CAP-161"></a>**[CAP-161: isolated stores, with no global registry](CAP-161.md)** · proposed · Code reaches schemas, builders and objects only through a store; stores are isolated, and a store's data is what its singletons reach. *Implements* [FEA-028: one API surface for all data access](../features/FEA-028.md).
  - **Current**: met in mbse-schemas 0.26.4 (checked in the code at 0.26.4: "the object belongs to another store").
### Excluding imperative visitor expressions

- <a id="CAP-136"></a>**[CAP-136: one finisher for every build](CAP-136.md)** · proposed · A single `done()` replaces
  `create`, `update` and `clone`. *Implements* [FEA-029: excluding imperative visitor expressions](../features/FEA-029.md).
  - **Current**: not met.
- <a id="CAP-148"></a>**[CAP-148: sense inferred by the executor](CAP-148.md)** · proposed · Whether a build creates,
  updates or clones is inferred from the object's identity information and its schema's value or reference distinction,
  with callbacks from caller to callee. *Implements* [FEA-029: excluding imperative visitor expressions](../features/FEA-029.md).
  - **Current**: not met.
- <a id="CAP-143"></a>**[CAP-143: specs declarative, no read-modify-write](CAP-143.md)** · proposed · A spec cannot read
  in order to write: a builder in a spec context is a writer, so that a spec is declarative. *Implements*
  [FEA-029: excluding imperative visitor expressions](../features/FEA-029.md).
  - **Current**: not met.

### Program models

- <a id="CAP-036"></a>**[CAP-036: complete kinds for Python, TypeScript and C and C++](CAP-036.md)** · proposed · Python's, TypeScript's and C
  and C++'s program models have complete kinds, built and printed. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current** (main, v0.3.28): met.
- <a id="CAP-063"></a>**[CAP-063: complete kinds for Verilog and SystemVerilog](CAP-063.md)** · proposed · Verilog's and SystemVerilog's program models have complete kinds, built
  and printed. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current** (main, v0.3.28): met.
- <a id="CAP-026"></a>**[CAP-026: Python, TypeScript and C and C++ read as written](CAP-026.md)** · adopted · Source code transpilers read
  Python, TypeScript and C and C++ source as written, semantically incorrect code included, through a pinned parser
  (tree-sitter, a practical choice at the time) whose gaps are corrected on the tree. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  *Applies* [PRI-002: preserve, don't lose](../PRINCIPLES.md#PRI-002).
  - **Current** (main, v0.3.28): met.
- <a id="CAP-062"></a>**[CAP-062: Verilog and SystemVerilog read as written](CAP-062.md)** · proposed · Verilog and SystemVerilog source is read as written, semantically incorrect code included,
  through slang. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current** (main, v0.3.28): met.
- <a id="CAP-044"></a>**[CAP-044: Verilog and SystemVerilog read by slang](CAP-044.md)** · proposed · Verilog and SystemVerilog source is read
  by its reference front end, slang, rather than tree-sitter. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current** (main, v0.3.28): met.
- <a id="CAP-066"></a>**CAP-066: Python read by CPython's ast** · proposed · Python source is read by its reference front end, CPython's `ast`, rather than
  tree-sitter. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current**: not met: read through tree-sitter.
- <a id="CAP-067"></a>**CAP-067: TypeScript read by the TypeScript compiler API** · proposed · TypeScript and JavaScript source is read by their reference front end, the
  TypeScript compiler API, rather than tree-sitter. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current**: not met: read through tree-sitter.
- <a id="CAP-068"></a>**[CAP-068: C and C++ read by Clang](CAP-068.md)** · proposed · C and C++ source is read by its reference front end, Clang, rather than tree-sitter. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current**: not met: read through tree-sitter.
- <a id="CAP-037"></a>**[CAP-037: Python and TypeScript trees as faithful as the reference front end's](CAP-037.md)** · proposed · Python and
  TypeScript program models read source as faithfully as the language's reference front end reads correct code: their
  trees are checked against that front end's wherever it reads the code. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current** (main, v0.3.28): met on the conformance sources (PYPRS-01 against CPython's `ast`, TSPRS-01 against
    typescript-estree).
- <a id="CAP-064"></a>**CAP-064: C and C++ trees as faithful as the reference front end's** · proposed · C and C++ program models read source as faithfully as Clang reads correct
  code, their trees checked against its. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current**: not met: C and C++ have no oracle yet.
- <a id="CAP-065"></a>**CAP-065: Verilog and SystemVerilog trees as faithful as the reference front end's** · proposed · Verilog and SystemVerilog program models read source as faithfully as
  slang reads correct code, their trees checked against its. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current**: to assess.
- <a id="CAP-038"></a>**[CAP-038: every construct of Python's standards](CAP-038.md)** · proposed · Python's program model reads every
  construct of Python's standards, and locates an error where the text goes wrong. *Implements* [FEA-008: expressive program models](../features/FEA-008.md).
  - **Current**: not met: tree-sitter-python 0.25 lags Python 3.13 and later, and its errors are located where recovery
    starts.
- <a id="CAP-092"></a>**[CAP-092: every construct of TypeScript's standards](CAP-092.md)** · proposed · TypeScript's and JavaScript's
  program model reads every construct of their standards, and locates an error where the text goes wrong. *Implements*
  [FEA-008: expressive program models](../features/FEA-008.md).
  - **Current**: not met: tree-sitter-typescript 0.23 lags TypeScript 4.7 and later.
- <a id="CAP-093"></a>**[CAP-093: every construct of C's and C++'s standards](CAP-093.md)** · proposed · C's and C++'s program model
  reads every construct of their standards, and locates an error where the text goes wrong. *Implements* [FEA-008: expressive program models](../features/FEA-008.md).
  - **Current**: not met: tree-sitter-cpp 0.23 lags C++23 and C++26.
- <a id="CAP-094"></a>**[CAP-094: every construct of Verilog's and SystemVerilog's standards](CAP-094.md)** · proposed · Verilog's and
  SystemVerilog's program model reads every construct of IEEE 1364 and IEEE 1800, and locates an error where the text
  goes wrong. *Implements* [FEA-008: expressive program models](../features/FEA-008.md).
  - **Current** (main, v0.3.28): met.

- <a id="CAP-084"></a>**[CAP-084: program trees as data](CAP-084.md)** · proposed · Programs are complete abstract syntax trees, plain objects of kinds in categories, validated by
  path and written and read as data, with the traversals and fluent builders every language shares. *Implements* [FEA-008: expressive program models](../features/FEA-008.md).
  - **Current** (main, v0.3.28): met.
- <a id="CAP-085"></a>**[CAP-085: standards record availability](CAP-085.md)** · proposed · Every kind and feature records the standards that have it, so that a standard checks a tree
  against what it lacks, by path. *Implements* [FEA-008: expressive program models](../features/FEA-008.md).
  - **Current** (main, v0.3.28): met.
- <a id="CAP-086"></a>**[CAP-086: programs printed](CAP-086.md)** · proposed · Each language's trees print in one fixed layout, parenthesized by precedence, so that printing then
  parsing gives the same tree. *Implements* [FEA-008: expressive program models](../features/FEA-008.md).
  - **Current** (main, v0.3.28): met for Ccpp, Python, TypeScript and Verilog.
- <a id="CAP-087"></a>**[CAP-087: definitions resolve names](CAP-087.md)** · proposed · Each language's definitions read a tree into the entities and scopes it declares, and resolve a
  name from a syntax node, by the language's own scoping rules. *Implements* [FEA-008: expressive program models](../features/FEA-008.md).
  - **Current** (main, v0.3.28): met for Ccpp, Python, TypeScript and Verilog.

### Code generation and the model trace

- <a id="CAP-027"></a>**[CAP-027: Python3 source generated from schemas](CAP-027.md)** · proposed · MBSE can generate Python3
  source code from schema models: their types, as dataclasses and type aliases. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md),
  [FEA-017: AI in the loop via the model trace](../features/README.md#FEA-017), [FEA-018: humans in the loop via the model trace](../features/README.md#FEA-018).
  [PRI-015: concrete references are programmatic](../PRINCIPLES.md#PRI-015) depends on it: typed bindings are how code refers to model elements by reference.
  - **Current**: met (mbse-codegen-python's `Types`).
- <a id="CAP-045"></a>**CAP-045: TypeScript5 source generated from schemas** · proposed · MBSE can generate TypeScript5
  source code from schema models. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-046"></a>**CAP-046: generated Python3 bound to its schemas** · proposed · Classes generated in Python3 are bound to their schemas (mbse-schemas' `Bindings`), so that they serialize,
  validate and are queried as a store's objects. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-047"></a>**CAP-047: parametric schemas as Python3 generics** · proposed · A parametric schema generates a Python3 generic: its value parameters as PEP 695 type parameters bounded by
  their types (`class Matrix[rows: int, cols: int]`), an application with `Literal` arguments. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-048"></a>**CAP-048: terms in generated Python3** · proposed · A width, an extent or an argument that is a term is written in generated Python3. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: blocked: terms are written by [CAP-051: Python3 source from expression models](#CAP-051).
- <a id="CAP-049"></a>**CAP-049: type parameters in Python3** · proposed · A schema's type parameters generate a generic Python3 class (`class Box[T]`). *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: blocked: mbse-schemas has no type parameters.
- <a id="CAP-051"></a>**CAP-051: Python3 source from expression models** · proposed · MBSE can generate Python3 source code from expression models. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-052"></a>**CAP-052: Python3 source from pattern models** · proposed · MBSE can generate Python3 source code from pattern models. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-053"></a>**CAP-053: C and C++ source from schema models** · proposed · MBSE can generate C and C++ source code from schema models. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-054"></a>**CAP-054: Verilog and SystemVerilog source from schema models** · proposed · MBSE can generate Verilog and SystemVerilog source code from schema models. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-055"></a>**CAP-055: generated TypeScript5 bound to its schemas** · proposed · Classes generated in TypeScript5 are bound to their schemas, so that they
  serialize, validate and are queried as a store's objects. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-056"></a>**CAP-056: parametric schemas as TypeScript5 generics** · proposed · A parametric schema generates a TypeScript5 generic, its parameters as type
  parameters and an application with literal type arguments. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-057"></a>**CAP-057: terms in generated TypeScript5** · proposed · A width, an extent or an argument that is a term is written in generated TypeScript5. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: blocked: terms are written by [CAP-060: TypeScript5 source from expression models](#CAP-060).
- <a id="CAP-058"></a>**CAP-058: type parameters in TypeScript5** · proposed · A schema's type parameters generate a generic TypeScript5 class (`class Box<T>`). *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: blocked: mbse-schemas has no type parameters.
- <a id="CAP-059"></a>**CAP-059: schemas round-trip through TypeScript5** · proposed · MBSE can round-trip schema models through TypeScript5 source: schemas to
  source and back give the same schemas, and source to schemas and back the same source, given the same decisions. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-060"></a>**CAP-060: TypeScript5 source from expression models** · proposed · MBSE can generate TypeScript5 source code from expression models. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-061"></a>**CAP-061: TypeScript5 source from pattern models** · proposed · MBSE can generate TypeScript5 source code from pattern models. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-088"></a>**[CAP-088: TypeScript transpiled to Python](CAP-088.md)** · proposed · A TypeScript program's tree is translated into a Python module's, covering the subset ordinary code
  is written with, and refusing by path what it does not cover. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current** (main, v0.3.28): met.
- <a id="CAP-089"></a>**[CAP-089: Python expressions bridged to Python source](CAP-089.md)** · proposed · The Python dialect's terms and Python syntax nodes map into each other, so that a
  constraint stored as data becomes Python code and Python code a constraint. *Implements* [FEA-022: code generation](../features/README.md#FEA-022).
  - **Current** (main, v0.3.28): met.
- <a id="CAP-090"></a>**[CAP-090: SystemVerilog expressions bridged to Verilog source](CAP-090.md)** · proposed · The SystemVerilog dialect's terms and Verilog syntax nodes map into each other:
  a constraint becomes a function, a `constraint` block or an assertion, and back. *Implements* [FEA-022: code generation](../features/README.md#FEA-022).
  - **Current** (main, v0.3.28): met.
- <a id="CAP-091"></a>**[CAP-091: Ccpp expressions bridged to C and C++ source](CAP-091.md)** · proposed · The Ccpp dialect's terms and Ccpp syntax nodes map into each other, as Python's and
  SystemVerilog's bridges do. *Implements* [FEA-022: code generation](../features/README.md#FEA-022).
  - **Current**: not met.
- <a id="CAP-039"></a>**[CAP-039: schemas round-trip through Python3](CAP-039.md)** · proposed · MBSE can round-trip schema
  models through Python3 source: schemas to source and back give the same schemas, and source to schemas and back the
  same source, given the same decisions. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-017: AI in the loop via the model trace](../features/README.md#FEA-017), [FEA-018: humans in the loop via the model trace](../features/README.md#FEA-018).
  - **Current**: met for schemas' types (mbse-codegen-python's `Types`: the round trips are laws, tested both ways).
- <a id="CAP-040"></a>**CAP-040: every generation ambiguity a parameter** · superseded by [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md) · Every
  ambiguity in generation is a parameter of the step that resolves it. It is a feature, not an increment of one.

- <a id="CAP-162"></a>**[CAP-162: Python dataclasses translated to and from schemas](CAP-162.md)** · proposed · Python dataclasses are read as the schemas they describe, in an install, and schemas written back as dataclasses, through `ast` trees. *Implements* [FEA-022: code generation](../features/README.md#FEA-022).
  - **Current**: met in mbse-schemas 0.26.4, Python only (checked in the code at 0.26.4: `Adapters/Dataclasses.py`).
### Wire format

- <a id="CAP-069"></a>**[CAP-069: wire format shorthand (scalars)](CAP-069.md)** · proposed · "in the scalar case of a `Schemas.OfAny` that represents a specific
  scalar (such as `Schemas.OfScalar` -> `Schemas.OfInt`) the wire format may omit the implied union wrapper(s) e.g.
  `1` instead of `{ "scalar": { "int": 1 } }` provided the written form unambiguously aligns with the schema (e.g.
  `scalar` -> `int`) and the reader must tolerate this optionality of representation": from `OfAny` through `OfScalar`
  to `OfInt`, up to two wrapper levels ("Yes, if you start with `OfAny` then go through `OfScalar` then `OfInt` you
  get up to 2 wrapper levels"). The unrestricted case is [CAP-071: unrestricted OfAny serializes with 1-level tag](#CAP-071). *Implements* [FEA-006: persistence](../features/README.md#FEA-006), [FEA-032: schema loading and wire alignment](../features/FEA-032.md); applies
  [PRI-025: never guess the schema](../PRINCIPLES.md#PRI-025) and [PRI-026: serialization through the visitor protocol](../PRINCIPLES.md#PRI-026).
  - **Current**: met in mbse-schemas 0.26.3 (checked in the code of both languages, and by the ANY suite: wrapped by
    kind and schema, bare only where one of the restriction's schemas takes the plain form).
- <a id="CAP-070"></a>**[CAP-070: wire format shorthand (containers)](CAP-070.md)** · proposed · "in the container case of a `Schemas.OfAny` that represents a
  specific container (e.g. `Schemas.OfContainer`) the wire format may omit the implied union wrapper
  `[ "dog", "cat", "mouse" ]` instead of `{ "container": [ "dog", "cat", "mouse" ] }` and the reader must tolerate this
  optionality of representation". *Implements* [FEA-006: persistence](../features/README.md#FEA-006), [FEA-032: schema loading and wire alignment](../features/FEA-032.md); applies
  [PRI-025: never guess the schema](../PRINCIPLES.md#PRI-025) and [PRI-026: serialization through the visitor protocol](../PRINCIPLES.md#PRI-026).
  - **Current**: met in mbse-schemas 0.26.3 (checked in the code of both languages: `{"container": [...]}`, bare where
    the restriction's one container schema takes the plain form).
- <a id="CAP-071"></a>**[CAP-071: unrestricted OfAny serializes with 1-level tag](CAP-071.md)** · proposed · An unrestricted
  `OfAny`'s value is written tagged by one level, its basic scalar's tag or its schema's registered name (`{"int": 1}`,
  `{"crm.Phone": {...}}`), and read back only so tagged. Accepting untagged plain data is
  [CAP-170: unrestricted OfAny also accepts and roundtrips untagged plain data](#CAP-170).
  *Implements* [FEA-006: persistence](../features/README.md#FEA-006), [FEA-032: schema loading and wire alignment](../features/FEA-032.md).
  - **Current**: met since before mbse-schemas 0.20.0, the first tagged release holding it (built with "`OfAny`
    returns"); checked in the code at 0.26.4 (`Plain.py`'s `_any_value` and `_decode_any`, `Plain.ts`'s `anyValue` and
    `decodeAny`).
- <a id="CAP-170"></a>**[CAP-170: unrestricted OfAny also accepts and roundtrips untagged plain data](CAP-170.md)** · proposed · An
  unrestricted `OfAny` may also hold any plain data, untagged, and writes it back as read, the one-level tag of
  [CAP-071: unrestricted OfAny serializes with 1-level tag](#CAP-071) legal but no longer required. *Implements* [FEA-032: schema loading and wire alignment](../features/FEA-032.md); *relates to*
  [FEA-020: refinable models](../features/FEA-020.md), [QUA-002: open-world models](../QUALITIES.md#QUA-002).
  - **Current**: not met.
### Interaction models

- <a id="CAP-028"></a>**CAP-028: layered interaction models** · proposed · Interaction models layer functional behavior. *Implements* [FEA-009: layered interaction models](../features/README.md#FEA-009).
  - **Current**: not met.
- <a id="CAP-041"></a>**CAP-041: every kind of participant** · proposed · Interaction models cover each kind of participant (system, hardware,
  firmware, software, device, user, community, cloud resource, agent) and the interfaces between them. *Implements*
  [FEA-010: system behavior](../features/README.md#FEA-010) to [FEA-016: community behavior](../features/README.md#FEA-016).
  - **Current**: no kind covered.

### Schema-driven visualization and editing

Each capability's specification is in its own detail file, linked from the ID. **Current** for these is as recorded
before they moved here; each is to assess against mbse-rest, mbse-react, mbse-dynamodb and mbse-demo-apps.

- <a id="CAP-001"></a>**[CAP-001: no-code index view](CAP-001.md)** · adopted · Services and UI
  present a useful and usable index site driven exclusively by the schema. *Implements* [FEA-001: schema-driven UI](../features/FEA-001.md).
  - **Current**: to assess.
- <a id="CAP-002"></a>**[CAP-002: named schema list](CAP-002.md)** · adopted · An endpoint returns
  every named schema. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: met, by the store's schema snapshot, which holds every named schema ([As built](CAP-002.md#as-built)).
- <a id="CAP-003"></a>**[CAP-003: schema inspector](CAP-003.md)** · adopted · Given a schema's name,
  the UI obtains its full detail, unnamed schemas defined inline and named ones referenced. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: blocked: mbse-schemas cannot yet write one schema object as a document.
- <a id="CAP-004"></a>**[CAP-004: logical view templates](CAP-004.md)** · adopted · An endpoint
  returns, for every logical view kind, a mutation-query template whose symbols the UI gives each a schema or a
  reference. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: to assess.
- <a id="CAP-012"></a>**[CAP-012: logical view endpoints](CAP-012.md)** · adopted · One endpoint per
  logical view kind, taking a template with its symbols given and returning a stream of frames. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: to assess.
- <a id="CAP-005"></a>**[CAP-005: label and summary view](CAP-005.md)** · adopted · Logical view as label and summary: the
  minimum-sized view of an object or a relation entry. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: to assess.
- <a id="CAP-006"></a>**[CAP-006: chip view](CAP-006.md)** · adopted · Logical view as chip: a medium-sized,
  abbreviated view of an object or a relation entry. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: to assess.
- <a id="CAP-007"></a>**[CAP-007: detail view](CAP-007.md)** · adopted · Logical view of an object as detail: every
  schema-defined property and adjacency. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: to assess.
- <a id="CAP-008"></a>**[CAP-008: adjacency as a list of chips](CAP-008.md)** · adopted · Logical view of an adjacency as a list of
  chips: the immediate adjacencies of an object through one named adjacency. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: to assess.
- <a id="CAP-009"></a>**[CAP-009: schema browser](CAP-009.md)** · adopted · A section per named app
  schema, with a scrollable list of object chips. *Implements* [FEA-004: index site browser views](../features/FEA-004.md).
  - **Current**: to assess.
- <a id="CAP-010"></a>**[CAP-010: object browser](CAP-010.md)** · adopted · A section per directory,
  with the chips of the objects its singleton holds. *Implements* [FEA-004: index site browser views](../features/FEA-004.md).
  - **Current**: to assess.
- <a id="CAP-011"></a>**[CAP-011: relation browser](CAP-011.md)** · adopted · A section per relation
  entry, its properties' chip aside its linked objects' chips. *Implements* [FEA-004: index site browser views](../features/FEA-004.md).
  - **Current**: to assess.
- <a id="CAP-017"></a>**[CAP-017: object inspector](CAP-017.md)** · adopted · A shared panel showing
  the detail view of whatever object a gesture picks. *Implements* [FEA-005: inspector views](../features/FEA-005.md).
  - **Current**: complete (mbse-react, M3; editing added by [CAP-014: properties as markdown](CAP-014.md)).
- <a id="CAP-018"></a>**[CAP-018: adjacency inspector](CAP-018.md)** · adopted · Viewing and editing an
  entry and its outbound object, extant or proposed. *Implements* [FEA-005: inspector views](../features/FEA-005.md).
  - **Current**: to assess.
- <a id="CAP-019"></a>**[CAP-019: adjacencies at the end of a detail](CAP-019.md)** · adopted · Adjacencies at the end of a detail, each
  entry previewed as one chip. *Implements* [FEA-005: inspector views](../features/FEA-005.md).
  - **Current**: to assess.
- <a id="CAP-020"></a>**[CAP-020: provenance display](CAP-020.md)** · adopted · Who created an object,
  and when it was created and last modified. *Implements* [FEA-005: inspector views](../features/FEA-005.md).
  - **Current**: to assess.
- <a id="CAP-021"></a>**[CAP-021: lists ordered by creation](CAP-021.md)** · adopted · Adjacency lists ordered by creation where
  provenance is present. *Implements* [FEA-005: inspector views](../features/FEA-005.md).
  - **Current**: to assess.
- <a id="CAP-023"></a>**[CAP-023: relation inspector](CAP-023.md)** · adopted · The object inspector of
  one object among its siblings, stepping to the previous or next. *Implements* [FEA-005: inspector views](../features/FEA-005.md).
  - **Current**: to assess.
- <a id="CAP-013"></a>**[CAP-013: an in-memory store journaled to DynamoDB](CAP-013.md)** · adopted · An in-memory store journaled to DynamoDB,
  with occasional snapshots, replayed at startup. *Implements* [FEA-006: persistence](../features/FEA-006.md).
  - **Current**: to assess.
- <a id="CAP-014"></a>**[CAP-014: properties as markdown](CAP-014.md)** · adopted · Object properties as markdown, viewed and
  edited in the inspector. *Implements* [FEA-007: property kinds](../features/FEA-007.md).
  - **Current**: to assess.
- <a id="CAP-022"></a>**[CAP-022: booleans as checkboxes](CAP-022.md)** · adopted · Boolean properties as checkboxes.
  *Implements* [FEA-007: property kinds](../features/FEA-007.md).
  - **Current**: to assess.
- <a id="CAP-015"></a>**[CAP-015: transaction provenance](CAP-015.md)** · adopted · Services keep a
  record of each transaction that writes, as mbse-schemas' `Provenance` module defines it. *Implements* [FEA-007: property kinds](../features/FEA-007.md).
  - **Current**: to assess.
- <a id="CAP-016"></a>**[CAP-016: comments](CAP-016.md)** · adopted · Comments, as data in an app's schema,
  shown and posted through general, schema-driven capabilities. *Implements* [FEA-007: property kinds](../features/FEA-007.md).
  - **Current**: to assess.

## Not yet planned

Capabilities without an ID are not in plan yet. Each planned feature's are at the end of its detail file in `../features/`: low-code
custom views ([FEA-001: schema-driven UI](../features/FEA-001.md)); detail with closures, closure as a list of chips ([FEA-003: no-code logical views](../features/FEA-003.md)); store over DynamoDB ([FEA-006: persistence](../features/FEA-006.md));
object links in markdown, shared property handling by the UI, properties as text and dates, and as financial,
scientific and engineering values ([FEA-007: property kinds](../features/FEA-007.md)). Those of unplanned features are in
[features/UNPLANNED.md](../features/UNPLANNED.md).

## Earlier IDs

| Earlier | Now | Earlier | Now | Earlier | Now |
|---|---|---|---|---|---|
| C-001 | [CAP-024: the same conformance corpora](#CAP-024) | C-008 | [CAP-031: 100% coverage of both](#CAP-031) | C-015 | [CAP-038: every construct of Python's standards](CAP-038.md) |
| C-002 | [CAP-025: nothing mandatory but by constraint](#CAP-025) | C-009 | [CAP-032: deliberate differences listed](#CAP-032) | C-016 | [CAP-039: schemas round-trip through Python3](CAP-039.md) |
| C-003 | [CAP-026: Python, TypeScript and C and C++ read as written](CAP-026.md) | C-010 | [CAP-033: undeclared properties preserved](#CAP-033) | C-017 | [CAP-040: every generation ambiguity a parameter](#CAP-040) |
| C-004 | [CAP-027: Python3 source generated from schemas](CAP-027.md) | C-011 | [CAP-034: schemas specialized by classifier intersection and union](#CAP-034) | C-018 | [CAP-041: every kind of participant](#CAP-041) |
| C-005 | [CAP-028: layered interaction models](#CAP-028) | C-012 | [CAP-035: schema evolution](#CAP-035) | C-019 | [CAP-042: data generated from constraints](CAP-042.md) |
| C-006 | [CAP-029: three-valued constraint checking](CAP-029.md) | C-013 | [CAP-036: complete kinds for Python, TypeScript and C and C++](CAP-036.md) | C-020 | [CAP-043: constraints resolved in any direction](#CAP-043) |
| C-007 | [CAP-030: the same cases in both languages](#CAP-030) | C-014 | [CAP-037: Python and TypeScript trees as faithful as the reference front end's](CAP-037.md) | C-021 | [CAP-044: Verilog and SystemVerilog read by slang](CAP-044.md) |

[CAP-001: no-code index view](CAP-001.md) to [CAP-023: relation inspector](CAP-023.md) kept the IDs they had in the workspace's former `VISUALIZATION.md`.

## Open items


- **Which parser for each language** (low priority). Tolerance and spec-awareness differ by language, as the editors'
  language services show. TypeScript's compiler, which tsserver is, parses any text to a full tree, type errors never
  affecting it. Python's semantic errors never affect a parse; CPython's `ast` fails only on syntax errors, without
  recovery, while Pyright's parser (Pylance's; MIT, written in TypeScript) and Ruff's recover from them. slang parses
  tolerantly and elaborates separately. C++ is the exception: its grammar depends on whether a name is a type, so a
  parser must resolve names, and Clang drops what it cannot resolve; EDG (Microsoft's C/C++ IntelliSense) copes but
  is commercial, so for Ccpp [CAP-068: C and C++ read by Clang](CAP-068.md) conflicts with [CAP-026: Python, TypeScript and C and C++ read as written](CAP-026.md). [CAP-068: C and C++ read by Clang](CAP-068.md) keeps Ccpp's front end among its open questions until this is decided.
- The capabilities above are drafted from each repository's status sections; confirm them, then remove those sections
  and cite the capabilities instead. Schema capabilities land in mbse-schemas first, then in its dependents, each
  pinning the new release.
- **[CAP-033: undeclared properties preserved](#CAP-033) implements no feature.** It implemented F-005, now a quality ([QUA-002: open-world models](../QUALITIES.md#QUA-002)). Preserving undeclared data is not
  refinement ([FEA-020: refinable models](../features/README.md#FEA-020)); a feature for it is missing.
- **[CAP-015: transaction provenance](CAP-015.md) and [CAP-016: comments](CAP-016.md) sit under [FEA-007: property kinds](../features/FEA-007.md)** as they were first placed; provenance and comments
  may be features of their own.
- **Tech debt in the visualization capabilities.** Counted objects have no reference, so they are neither recorded nor
  transmitted ([FEA-003: no-code logical views](../features/FEA-003.md)), and browsers leave them out ([CAP-010: object browser](CAP-010.md), [CAP-011: relation browser](CAP-011.md)). It is to become a capability of a feature.

---

<!-- nav -->
[← Features](../features/README.md) · [Home](../README.md) · [Principles →](../PRINCIPLES.md)
