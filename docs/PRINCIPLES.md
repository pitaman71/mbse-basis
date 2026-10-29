<!-- nav -->
[← Capabilities](capabilities/README.md) · [Home](README.md) · [Vocabulary →](VOCABULARY.md)

# Principles

A principle is a durable design or engineering decision that reinforces qualities when consistently applied across
repositories, components, source code and the rest. Principles sit outside the design spec's tiers: a capability says
what a release solves, a principle how every solution is shaped.

Most principles shape the product: a user could notice one broken, in how the product behaves or how its API reads
([PRI-004: one visitor protocol per kind](#PRI-004); [PRI-007: three-valued checking on request](#PRI-007)). Some shape the work instead, and only a
contributor could notice them broken ([PRI-016: guidance written once](#PRI-016)); these are conventions, which serve qualities an
engineering persona values (README, Conventions).

A principle is cited where it applies, with bridge language giving its gist, not its full statement. *Applied in*
names where each already holds, so that those local texts can be replaced by bridged citations. [PRI-001: declaration order](#PRI-001) and [PRI-002: preserve, don't lose](#PRI-002) are the original draft; [PRI-003: everything is schema data](#PRI-003) to [PRI-019: fluent builder syntax](#PRI-019) were
promoted from decisions each repository made separately.

## Index

- <a id="PRI-001"></a>**PRI-001: declaration order** · adopted · Declaration order over sorted order. *Serves* [QUA-001: AI and humans in the loop](QUALITIES.md#QUA-001).
  *Applied in*: a schema's properties, adjacencies, branches, parts and parameters in declared order, in builders and
  in the plain schemas of schemas; a store's `names()` in registration order; a keyed list's items in insertion order;
  reachability and symbols in first-reference order (mbse-schemas `Reachable`, `Plain`); a transform session's
  candidates in the order it first saw them (mbse-patterns).
  *Exceptions*: a relation's entries are written sorted by the key it declares, where the key's values are ordered
  (mbse-schemas, PLN-16): an order by value, not by name.
- <a id="PRI-002"></a>**PRI-002: preserve, don't lose** · adopted · Open world means preserving unstructured data: don't lose, preserve, validate and cleanse on
  request. What is read is kept, undeclared or not, and written back as read; validation reports what does not fit,
  as unknown where the model is silent; cleansing removes or repairs it only when the caller asks. Only where a step
  cannot preserve, such as a third-party parser that drops what it cannot read, or a translation with no form in the
  target, is the input refused, by name and position; nothing is dropped silently. *Serves* [QUA-002: open-world models](QUALITIES.md#QUA-002).
  *Relates to* [PRI-007: three-valued checking on request](#PRI-007).
  *Applied in*: parsers that read semantically incorrect code ([CAP-026: Python, TypeScript and C and C++ read as written](capabilities/README.md#CAP-026)); names a language cannot spell kept in the tree and flagged by validation, never renamed; `TranspileError`
  (mbse-programs); drops recorded as steps (mbse-codegen-python).
  *Not yet applied* in mbse-schemas: decoding refuses undeclared keys. Its [`docs/OPEN_WORLD.md`](../../mbse-schemas/docs/OPEN_WORLD.md) proposes preserving
  them as a reading policy (Undeclared properties, policy 3).
- <a id="PRI-003"></a>**PRI-003: everything is schema data** · proposed · Each kind of schema is a plain schema of schemas held by the store
  (`Schemas.OfObject`; mbse-schemas' store overhaul, Levels), and expressions, predicates, syntax trees, modules and
  traces serialize, reflect and compare like any other data. *Serves* [QUA-001: AI and humans in the loop](QUALITIES.md#QUA-001), [QUA-005: an opinionated paradigm](QUALITIES.md#QUA-005).
  *Applied in*: the plain schemas of schemas (mbse-schemas); kinds (mbse-programs); traces (mbse-patterns).
  *Not yet applied*: mbse-expressions ([PRI-018: no model needs code to read or write](#PRI-018)).
- <a id="PRI-004"></a>**PRI-004: one visitor protocol per kind** · adopted · For kind X: `Visitors.OfX` is the one protocol through which code reads and writes a value of
  X, whether or not it knows the schema; `Proxies.OfX` defines `Spec`, `Builder` and `Data`, and both data instances
  and builders implement `Visitors.OfX`. Algorithms receive a visitor and pull through it; a value never writes itself
  into a visitor. Whether a write takes effect is the visitor's mode: data instances visit read-only, a write in
  read-only mode raises, and a read-only static view of the protocol types the code that must not write. Visitors pass
  child visitors to callbacks rather than return them, and an object's or an entry's visitor names its methods `as_*`,
  a prefix no schema-defined name may take. Builders are fluent, one setter per property taking a `Spec`; `create`, `clone` and `update` finalize
  and never validate. Anything that has a builder has a `Spec`: either a callable that takes that builder and returns
  it, or an instance of what the builder builds. *Serves* [QUA-005: an opinionated paradigm](QUALITIES.md#QUA-005). *Relates to* [PRI-005: one entry point per kind](#PRI-005).
  *Applied in*: mbse-schemas' [`docs/VISITOR_PATTERN.md`](../../mbse-schemas/docs/VISITOR_PATTERN.md), which supersedes the reverse protocol (`accept(visitor)`, a
  value writing itself into serializers and recorders that implemented `Visitors`); built in mbse-schemas 0.11, where
  each schema builder is a `Visitors.OfObject` over its store's plain schema of schemas (`Schemas.OfX`, since 0.14),
  through which an extension's members reach it: the same policy one level up.
- <a id="PRI-005"></a>**PRI-005: one entry point per kind** · proposed · One entry point per kind, named `OfX`: visitors, comparison, evaluation and validation dispatch
  on a value's kind. *Serves* [QUA-005: an opinionated paradigm](QUALITIES.md#QUA-005).
  *Applied in*: `Visitors.OfX`, `Comparison.OfX` (mbse-schemas); `Evaluators.OfAny` (mbse-expressions).
- <a id="PRI-006"></a>**PRI-006: text is one more dialect** · proposed · Tools map trees to trees, never rewrite text; only parsers read text
  and only printers write it, through `Text.ToText` and `Text.FromText`. *Serves* [QUA-004: models as an alternative representation of source code](QUALITIES.md#QUA-004).
  *Applied in*: `Text` modules (mbse-expressions); transpilers and the ban on text pre-passes (mbse-programs);
  `Bridges` (mbse-programs).
- <a id="PRI-007"></a>**PRI-007: three-valued checking on request** · proposed · Checking is three-valued and on request: unknown is not false, an unset property reads as
  absent, validation runs only when asked, and partial evaluation gives a residual, not a value. *Serves* [QUA-002: open-world models](QUALITIES.md#QUA-002).
  *Applied in*: `Validators` (mbse-schemas, mbse-patterns); Kleene evaluation and residuals (mbse-expressions).
- <a id="PRI-008"></a>**PRI-008: refuse, never silently lose** · superseded by [PRI-002: preserve, don't lose](#PRI-002) · Refuse, never silently lose. Refusal as a default conflicts with the open world;
  it remains only as [PRI-002: preserve, don't lose](#PRI-002)'s fallback where a step cannot preserve.
- <a id="PRI-009"></a>**PRI-009: one error shape** · proposed · One `ValueError` subclass per layer, a one-line reason and a location (path,
  or position in code points), byte-identical across implementations. *Serves* [QUA-001: AI and humans in the loop](QUALITIES.md#QUA-001).
  *Applied in*: `DecodeError` (mbse-schemas); `ParseError`, `TranspileError` (mbse-programs).
- <a id="PRI-010"></a>**PRI-010: proxies and generated code read alike** · proposed · Dynamic proxies and generated code read alike, so code using one runs on the other unchanged.
  *Serves* [QUA-004: models as an alternative representation of source code](QUALITIES.md#QUA-004).
  *Applied in*: adjacencies as members, unset as `None`, flat unions (mbse-schemas); bridges (mbse-codegen-python).
- <a id="PRI-011"></a>**PRI-011: the lowest repository that can own it** · proposed · A capability lives in the lowest repository that can own it without gaining a dependency; a
  bridge between two lives in the repository that depends on both. *Serves* [QUA-005: an opinionated paradigm](QUALITIES.md#QUA-005), [QUA-003: no second-order inventions](QUALITIES.md#QUA-003).
  *Applied in*: constraints kept in mbse-patterns, not mbse-schemas; parsers and dialect bridges in mbse-programs, not
  mbse-expressions.
- <a id="PRI-012"></a>**PRI-012: model published standards** · proposed · Model published standards rather than invent: datatypes, value domains, language versions and
  formats are the standards' own (`Ieee754`, `Ieee1164`, C++ and ECMAScript editions), with only the parameters a
  standard defines. *Serves* [QUA-003: no second-order inventions](QUALITIES.md#QUA-003).
  *Applied in*: value domains (mbse-expressions); standards (mbse-programs).
- <a id="PRI-013"></a>**PRI-013: nondeterminism passed in** · proposed · Nondeterminism is passed in, never held: a random source is given to each draw, with its seed,
  and streams depend on the seed and key alone. *Serves* [QUA-002: open-world models](QUALITIES.md#QUA-002).
  *Applied in*: PCG32 and `Generators` (mbse-schemas, mbse-patterns).
- <a id="PRI-014"></a>**PRI-014: every ambiguity a decision** · proposed · Every ambiguity is a decision: a parameter of one step, taken by a person, an agent or a policy
  chosen up front, and kept in a trace. *Serves* [QUA-001: AI and humans in the loop](QUALITIES.md#QUA-001).
  *Applied in*: `Transforms` (mbse-patterns); code generation (mbse-codegen-python).
- <a id="PRI-015"></a>**PRI-015: concrete references are programmatic** · adopted · A *concrete reference* to a model object in code 
  is always by programmatic reference, not by string name. This is distinct
  from a *symbolic reference* which stands in place for a yet-to-be-bound
  model object. A *symbol* at the point of declaration (schema parameter 
  or function formal) or at the point of reference (expression term) 
  is a natural string or by an object declared with `stores.Symbols`. 
  Meant in full: any model used in code has typed bindings, generated or written, since dynamic proxies are invisible to type
  checkers. Names remain how the wire format and modules write references. "A declaration is not a reference," as
  the user decided: declaring a name (`.name('crm.Contact')`, a link's name) is not covered. *Relates to* [PRI-010: proxies and generated code read alike](#PRI-010), [CAP-027: Python3 source generated from schemas](capabilities/CAP-027.md).
  *Exceptions*: in mbse-schemas' schema builders, an adjacency's `me` and a relation's `uniques` name links and
  properties by string, as the user decided (its [`docs/FRAMEWORK.md`, Resolved](../../mbse-schemas/docs/FRAMEWORK.md#resolved), "Schema builders align with their
  meta-schemas"). There is no other: "Code expressions that name a reference object use Paths, not string lookup," as
  the user decided, a path from a singleton through ownership entries, each step its adjacency called with the entry's
  keys (`store.Instances.wts.Features.dir({ name: 'DEF-693' })`, mbse-schemas' [`docs/OBJECT_IDENTITY.md`, Decided](../../mbse-schemas/docs/OBJECT_IDENTITY.md#decided), 26
  and 27); the earlier `as_instance` exception is withdrawn.
  *Not yet applied*, in the API the design documents show: `E.variable("c")` beside `pred.c`, `s.get("properties")`
  (mbse-patterns, mbse-codegen-python); `Transform("Label", ...)` and `Clause("Label", ...)` (mbse-patterns).
- <a id="PRI-016"></a>**PRI-016: guidance written once** · proposed · Guidance is written once, in its reader's language: no copies and no symlinks. Each
  implementation's skill shows usage in its own language, covering the same topics in the same order as the other's;
  concepts live once, in the design document, which each skill links to rather than restates. *Serves* [QUA-001: AI and humans in the loop](QUALITIES.md#QUA-001).
  *Relates to* [CAP-024: the same conformance corpora](capabilities/README.md#CAP-024).
- <a id="PRI-017"></a>**PRI-017: transforms, models, dialects, schemas** · adopted · Transforms use Steps to mutate Models which are built on Dialects which are built on Schemas.
  *Relates to* [PRI-014: every ambiguity a decision](#PRI-014), [PRI-018: no model needs code to read or write](#PRI-018).
- <a id="PRI-018"></a>**PRI-018: no model needs code to read or write** · adopted · "No model should need code to read or write. Ever." All model data is governed by a schema,
  and all builder/visitor/reader/write functionality comes from either proxies in mbse-schemas or generated
  dataclasses. No bespoke class implementations are allowed for models. *Relates to* [PRI-003: everything is schema data](#PRI-003), [PRI-004: one visitor protocol per kind](#PRI-004), [PRI-010: proxies and generated code read alike](#PRI-010), [PRI-017: transforms, models, dialects, schemas](#PRI-017).
  *Not yet applied* in mbse-expressions (its [`docs/EXPRESSIONS.md`, Open questions](../../mbse-expressions/docs/EXPRESSIONS.md#open-questions)).
- <a id="PRI-019"></a>**PRI-019: fluent builder syntax** · adopted · "The preferred form of models as data is fluent builder syntax. Not wire format, pseudocode,
  or imagined shorthand." "Do not invent another DSL by wrapping builder syntax": helper functions that build a model
  through the builders are such a DSL; models are written in the builders' fluent syntax itself. *Relates to* [PRI-004: one visitor protocol per kind](#PRI-004),
  [PRI-018: no model needs code to read or write](#PRI-018).
- <a id="PRI-020"></a>**PRI-020: no constraint, any configuration** · adopted · An absence of constraints is interpreted as acceptance of any
  configuration of the model. Model interpretation assumes entropy and/or nondeterminism for any aspect not
  constrained. *Serves* [QUA-002: open-world models](QUALITIES.md#QUA-002).
- <a id="PRI-021"></a>**PRI-021: refinement by constraint** · adopted · Models can be refined incrementally and iteratively by adding a
  constraint that conservatively and precisely reduces the configuration space of a model. *Serves* [QUA-002: open-world models](QUALITIES.md#QUA-002).
  *Relates to* [VOC-003: refinement](VOCABULARY.md#VOC-003).
- <a id="PRI-022"></a>**PRI-022: second-order inventions by approval** · adopted · Second-order inventions ([VOC-027: second-order invention](VOCABULARY.md#VOC-027)) may be permitted with explicit developer
  approval, and are logged as a capability of an internal feature. *Serves* [QUA-003: no second-order inventions](QUALITIES.md#QUA-003).
- <a id="PRI-023"></a>**PRI-023: domain representations** · proposed · A domain representation carries three things at once: unvalidated data,
  usually in string form; a validation indicator for each possible validation error; and encoded properties (such as
  epoch, zone, year, month, day, hour and minute). *Serves* [QUA-002: open-world models](QUALITIES.md#QUA-002). *Relates to* [PRI-002: preserve, don't lose](#PRI-002).
  *Applied in*: planned for text and date properties ([FEA-007: property kinds](features/FEA-007.md), not yet planned).
- <a id="PRI-024"></a>**PRI-024: the plain form, carried as written** · proposed · A service or a store carries
  mbse-schemas' plain form as mbse-schemas wrote it, and defines no format of its own: a request's body, a frame, a
  journal entry or a table's item holds the value as written, never reinterpreted or re-encoded into the medium's own
  types. *Serves* [QUA-003: no second-order inventions](QUALITIES.md#QUA-003). *Relates to* [PRI-012: model published standards](#PRI-012).
  *Applied in*: mbse-rest's wire format ([CAP-012: logical view endpoints](capabilities/CAP-012.md)); mbse-dynamodb's
  table, which keeps JSON rather than DynamoDB maps, whose numbers would lose `1` against `1.0`
  ([CAP-013: an in-memory store journaled to DynamoDB](capabilities/CAP-013.md)).
- <a id="PRI-025"></a>**PRI-025: never guess the schema** · adopted · "Never guess the schema": what a value is, is never inferred from
  the shape of its data. A reader tracks the expected schema as context while traversing wire data, and the wire
  names a value's schema wherever that context leaves it open. *Relates to* [PRI-026: serialization through the
  visitor protocol](#PRI-026), [PRI-004: one visitor protocol per kind](#PRI-004).
  *Not yet applied* in mbse-schemas: a value of an `OfAny` restricted to several schemas is written bare and read by
  the one schema whose plain form fits it, refused where several fit (Str, Bytes and a non-finite Float all write text).
- <a id="PRI-026"></a>**PRI-026: serialization through the visitor protocol** · adopted · "serialization is handled via visitor protocol", and
  a reader tracks the expected schema as context while traversing wire data. "The wire format *usually* tracks each
  recursion by the writer while traversing in-memory data which has the effect of wrapping unions explicitly.
  Shorthands permit these wrappers to be skipped in cases where the correct behavior can be unambiguously and
  trivially inferred from context by a reader that already knows the expected schema. This makes the format more
  concise and resilient to errors from humans and agents in the loop." *Relates to* [PRI-025: never guess the schema](#PRI-025),
  [PRI-004: one visitor protocol per kind](#PRI-004); its shorthands are [CAP-055: wire format shorthand
  (scalars)](capabilities/README.md#CAP-055) and [CAP-056: wire format shorthand (containers)](capabilities/README.md#CAP-056).

## Open items

- **[PRI-015: concrete references are programmatic](#PRI-015) and [PRI-017: transforms, models, dialects, schemas](#PRI-017) to [PRI-019: fluent builder syntax](#PRI-019): what they serve.** Which qualities each serves is still to state.
- **Conventions among the principles.** [PRI-011: the lowest repository that can own it](#PRI-011) and [PRI-016: guidance written once](#PRI-016) govern
  the work rather than the product (README, Conventions). Each is to serve a quality an engineering persona values,
  and none exists yet (Qualities, open items). The conventions in each repository's `AGENTS.md` join them in a later
  batch.
- **[PRI-001: declaration order](#PRI-001)'s exception and a proposal against it.** Decide whether entries sorted by their relation's key are a
  deliberate exception (an order by value, for byte-identity) or a debt against [PRI-001: declaration order](#PRI-001). mbse-schemas'
  [`docs/OPEN_WORLD.md`](../../mbse-schemas/docs/OPEN_WORLD.md) also proposes writing preserved properties sorted by name, against [PRI-001: declaration order](#PRI-001).
- **[PRI-004: one visitor protocol per kind](#PRI-004) beyond mbse-schemas.** mbse-expressions' writers, mbse-programs' `LANGUAGE.Builders.<Kind>()` and
  mbse-patterns' predicate and transform builders do not follow it yet; each comes to, building its models through
  mbse-schemas' builders ([PRI-018: no model needs code to read or write](#PRI-018), [PRI-019: fluent builder syntax](#PRI-019)), as it migrates to mbse-schemas 0.11.
- **[PRI-016: guidance written once](#PRI-016) is not applied.** Every repository copies one skill, byte-identical, from `skills/<repo>/` into both
  packages (`skills/sync.sh`, checked by SKL-01), so each package carries both languages' guides, and the "neutral"
  references (dialects, translating, languages, transpiling, serialization) teach TypeScript users with Python
  fragments. To apply it: write `python3/<package>/skill/` all in Python and `typescript5/skill/` all in TypeScript,
  with deliberate differences in `docs/EQUIVALENCE.md`; move concepts into the design document; remove `skills/`,
  `skills/sync.sh` and the `.claude/skills/<repo>` symlink, with AGENTS.md routing an agent to the skill for its
  language; make SKL-01 check that both skills cover the same topics, SKL-02 still running each skill's complete
  programs. Pilot on mbse-patterns (SKILL.md, python.md, typescript.md only), then the other four.

## Earlier IDs

P-001 to P-019 are [PRI-001: declaration order](#PRI-001) to [PRI-019: fluent builder syntax](#PRI-019), the same numbers. Their *Serves* moved from features to the qualities those
features became (Features, Earlier IDs).

---

<!-- nav -->
[← Capabilities](capabilities/README.md) · [Home](README.md) · [Vocabulary →](VOCABULARY.md)
