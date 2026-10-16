<!-- nav -->
[← Features](FEATURES.md) · [Home](README.md) · [Capabilities →](CAPABILITIES.md)

# Principles

Design principles that can be reapplied locally across a class of related situations. P-001 and P-002 are the original
draft; P-003 onward are proposed, promoted from decisions each repository made separately. *Applied in* names where
each already holds, so that those local texts can be replaced by citations.

## Index

- **P-001** · adopted · Declaration order over sorted order. *Serves* F-002.
  *Applied in*: a schema's properties, adjacencies, branches, parts and parameters in declared order, in builders and
  in the plain schemas of schemas; a store's `names()` in registration order; a keyed list's items in insertion order;
  reachability and symbols in first-reference order (mbse-schemas `Reachable`, `Plain`); a transform session's
  candidates in the order it first saw them (mbse-patterns).
  *Exceptions*: a relation's entries are written sorted by the key it declares, where the key's values are ordered
  (mbse-schemas, PLN-16): an order by value, not by name.
- **P-002** · adopted · Open world means preserving unstructured data: don't lose, preserve, validate and cleanse on
  request. What is read is kept, undeclared or not, and written back as read; validation reports what does not fit,
  as unknown where the model is silent; cleansing removes or repairs it only when the caller asks. Only where a step
  cannot preserve, such as a third-party parser that drops what it cannot read, or a translation with no form in the
  target, is the input refused, by name and position; nothing is dropped silently. *Serves* F-005, F-006.
  *Relates to* P-007.
  *Applied in*: parsers that read semantically incorrect code (C-003); names a language cannot spell kept in the tree and flagged by validation, never renamed; `TranspileError`
  (mbse-programs); drops recorded as steps (mbse-codegen-python).
  *Not yet applied* in mbse-schemas: decoding refuses undeclared keys. Its `docs/OPEN_WORLD.md` proposes preserving
  them as a reading policy (Undeclared properties, policy 3).
- **P-003** · proposed · Everything is schema data: each kind of schema is a plain schema of schemas held by the store
  (`Schemas.OfObject`; mbse-schemas' store overhaul, Levels), and expressions, predicates, syntax trees, modules and
  traces serialize, reflect and compare like any other data. *Serves* F-001, F-002, F-003.
  *Applied in*: the plain schemas of schemas (mbse-schemas); kinds (mbse-programs); traces (mbse-patterns).
  *Not yet applied*: mbse-expressions (P-018).
- **P-004** · adopted · For kind X: `Visitors.OfX` is the one protocol through which code reads and writes a value of
  X, whether or not it knows the schema; `Proxies.OfX` defines `Spec`, `Builder` and `Data`, and both data instances
  and builders implement `Visitors.OfX`. Algorithms receive a visitor and pull through it; a value never writes itself
  into a visitor. Whether a write takes effect is the visitor's mode: data instances visit read-only, a write in
  read-only mode raises, and a read-only static view of the protocol types the code that must not write. Visitors pass
  child visitors to callbacks rather than return them, and an object's or an entry's visitor names its methods `as_*`,
  a prefix no schema-defined name may take. Builders are fluent, one setter per property taking a `Spec`; `create`, `clone` and `update` finalize
  and never validate. Anything that has a builder has a `Spec`: either a callable that takes that builder and returns
  it, or an instance of what the builder builds. *Serves* F-003. *Relates to* P-005.
  *Applied in*: mbse-schemas' `docs/VISITOR_PATTERN.md`, which supersedes the reverse protocol (`accept(visitor)`, a
  value writing itself into serializers and recorders that implemented `Visitors`); built in mbse-schemas 0.11, where
  each schema builder is a `Visitors.OfObject` over its store's plain schema of schemas (`Schemas.OfX`, since 0.14),
  through which an extension's members reach it: the same policy one level up.
- **P-005** · proposed · One entry point per kind, named `OfX`: visitors, comparison, evaluation and validation dispatch
  on a value's kind. *Serves* F-003.
  *Applied in*: `Visitors.OfX`, `Comparison.OfX` (mbse-schemas); `Evaluators.OfAny` (mbse-expressions).
- **P-006** · proposed · Text is one more dialect: tools map trees to trees, never rewrite text; only parsers read text
  and only printers write it, through `Text.ToText` and `Text.FromText`. *Serves* F-008.
  *Applied in*: `Text` modules (mbse-expressions); transpilers and the ban on text pre-passes (mbse-programs);
  `Bridges` (mbse-programs).
- **P-007** · proposed · Checking is three-valued and on request: unknown is not false, an unset property reads as
  absent, validation runs only when asked, and partial evaluation gives a residual, not a value. *Serves* F-005, F-006.
  *Applied in*: `Validators` (mbse-schemas, mbse-patterns); Kleene evaluation and residuals (mbse-expressions).
- **P-008** · superseded by P-002 · Refuse, never silently lose. Refusal as a default conflicts with the open world;
  it remains only as P-002's fallback where a step cannot preserve.
- **P-009** · proposed · One error shape: one `ValueError` subclass per layer, a one-line reason and a location (path,
  or position in code points), byte-identical across implementations. *Serves* F-001, F-002.
  *Applied in*: `DecodeError` (mbse-schemas); `ParseError`, `TranspileError` (mbse-programs).
- **P-010** · proposed · Dynamic proxies and generated code read alike, so code using one runs on the other unchanged.
  *Serves* F-008.
  *Applied in*: adjacencies as members, unset as `None`, flat unions (mbse-schemas); bridges (mbse-codegen-python).
- **P-011** · proposed · A capability lives in the lowest repository that can own it without gaining a dependency; a
  bridge between two lives in the repository that depends on both. *Serves* F-003, F-004.
  *Applied in*: constraints kept in mbse-patterns, not mbse-schemas; parsers and dialect bridges in mbse-programs, not
  mbse-expressions.
- **P-012** · proposed · Model published standards rather than invent: datatypes, value domains, language versions and
  formats are the standards' own (`Ieee754`, `Ieee1164`, C++ and ECMAScript editions), with only the parameters a
  standard defines. *Serves* F-004.
  *Applied in*: value domains (mbse-expressions); standards (mbse-programs).
- **P-013** · proposed · Nondeterminism is passed in, never held: a random source is given to each draw, with its seed,
  and streams depend on the seed and key alone. *Serves* F-005.
  *Applied in*: PCG32 and `Generators` (mbse-schemas, mbse-patterns).
- **P-014** · proposed · Every ambiguity is a decision: a parameter of one step, taken by a person, an agent or a policy
  chosen up front, and kept in a trace. *Serves* F-001, F-002.
  *Applied in*: `Transforms` (mbse-patterns); code generation (mbse-codegen-python).
- **P-015** · adopted · A *concrete reference* to a model object in code 
  is always by programmatic reference, not by string name. This is distinct
  from a *symbolic reference* which stands in place for a yet-to-be-bound
  model object. A *symbol* at the point of declaration (schema parameter 
  or function formal) or at the point of reference (expression term) 
  is a natural string or by an object declared with `stores.Symbols`. 
  Meant in full: any model used in code has typed bindings, generated or written, since dynamic proxies are invisible to type
  checkers. Names remain how the wire format and modules write references. "A declaration is not a reference," as
  the user decided: declaring a name (`.name('crm.Contact')`, a link's name) is not covered. *Relates to* P-010, C-004.
  *Exceptions*: in mbse-schemas' schema builders, an adjacency's `me` and a relation's `uniques` name links and
  properties by string, as the user decided (its `docs/FRAMEWORK.md`, Resolved, "Schema builders align with their
  meta-schemas"). A store path's `as_instance` (`store.Instances.crm.Contacts.as_instance('Anna Baker')`, mbse-schemas'
  `docs/OBJECT_IDENTITY.md`) "is the one and only one api location where the identity of an object can be used to
  reference the object", as the user decided, "and it is necessary because we can no longer retain instances in global
  files like Expressions.Framework.*.py": no schema object or other instance is shared across stores (mbse-schemas'
  `docs/SCHEMA_EXTENSION.md`, Decided, 23).
  *Not yet applied*, in the API the design documents show: `E.variable("c")` beside `pred.c`, `s.get("properties")`
  (mbse-patterns, mbse-codegen-python); `Transform("Label", ...)` and `Clause("Label", ...)` (mbse-patterns).
- **P-016** · proposed · Guidance is written once, in its reader's language: no copies and no symlinks. Each
  implementation's skill shows usage in its own language, covering the same topics in the same order as the other's;
  concepts live once, in the design document, which each skill links to rather than restates. *Serves* F-001, F-002.
  *Relates to* C-001.
- **P-017** · adopted · Transforms use Steps to mutate Models which are built on Dialects which are built on Schemas.
  *Relates to* P-014, P-018.
- **P-018** · adopted · "No model should need code to read or write. Ever." All model data is governed by a schema,
  and all builder/visitor/reader/write functionality comes from either proxies in mbse-schemas or generated
  dataclasses. No bespoke class implementations are allowed for models. *Relates to* P-003, P-004, P-010, P-017.
  *Not yet applied* in mbse-expressions (its `docs/EXPRESSIONS.md`, Open questions).
- **P-019** · adopted · "The preferred form of models as data is fluent builder syntax. Not wire format, pseudocode,
  or imagined shorthand." "Do not invent another DSL by wrapping builder syntax": helper functions that build a model
  through the builders are such a DSL; models are written in the builders' fluent syntax itself. *Relates to* P-004,
  P-018.

## Open items

- **P-015: what it serves.** Which features it serves is still to state.

- **P-001's exception and a proposal against it.** Decide whether entries sorted by their relation's key are a
  deliberate exception (an order by value, for byte-identity) or a debt against P-001. mbse-schemas'
  `docs/OPEN_WORLD.md` also proposes writing preserved properties sorted by name, against P-001.
- **P-004 beyond mbse-schemas.** mbse-expressions' writers, mbse-programs' `LANGUAGE.Builders.<Kind>()` and
  mbse-patterns' predicate and transform builders do not follow it yet; each comes to, building its models through
  mbse-schemas' builders (P-018, P-019), as it migrates to mbse-schemas 0.11.
- **P-016 is not applied.** Every repository copies one skill, byte-identical, from `skills/<repo>/` into both
  packages (`skills/sync.sh`, checked by SKL-01), so each package carries both languages' guides, and the "neutral"
  references (dialects, translating, languages, transpiling, serialization) teach TypeScript users with Python
  fragments. To apply it: write `python3/<package>/skill/` all in Python and `typescript5/skill/` all in TypeScript,
  with deliberate differences in `docs/EQUIVALENCE.md`; move concepts into the design document; remove `skills/`,
  `skills/sync.sh` and the `.claude/skills/<repo>` symlink, with AGENTS.md routing an agent to the skill for its
  language; make SKL-01 check that both skills cover the same topics, SKL-02 still running each skill's complete
  programs. Pilot on mbse-patterns (SKILL.md, python.md, typescript.md only), then the other four.

---

<!-- nav -->
[← Features](FEATURES.md) · [Home](README.md) · [Capabilities →](CAPABILITIES.md)
