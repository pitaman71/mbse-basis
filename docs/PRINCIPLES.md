<!-- nav -->
[← Why the mbse repositories exist](../MBSE.md) · [Home](../README.md) · [Qualities →](QUALITIES.md)

# Principles

A principle is a durable design or engineering decision that reinforces qualities when consistently applied across
repositories, components, source code and the rest. Principles sit outside the design spec's tiers: a capability says
what a release solves, a principle how every solution is shaped.

Most principles shape the product: a user could notice one broken, in how the product behaves or how its API reads
([PRI-004: one visitor protocol per kind](#PRI-004); [PRI-007: three-valued checking on request](#PRI-007)). Some shape the work instead, and only a
contributor could notice them broken ([PRI-016: guidance written once](#PRI-016)); these are conventions, which serve qualities an
engineering persona values, such as [QUA-010: every repository works alike](QUALITIES.md#QUA-010) ([the basis](README.md#the-design-spec), Conventions). Each of [PRI-028: both implementations change together](#PRI-028) onward says which
it governs.

A principle is cited where it applies, with bridge language giving its gist, not its full statement. *Applied in*
names where each already holds, so that those local texts can be replaced by bridged citations. [PRI-001: declaration order](#PRI-001) and [PRI-002: preserve, don't lose](#PRI-002) are the original draft; [PRI-003: everything is schema data](#PRI-003) to [PRI-019: fluent builder syntax](#PRI-019) were
promoted from decisions each repository made separately; [PRI-028: both implementations change together](#PRI-028) to [PRI-040: deliberate differences listed](#PRI-040) were
promoted from the conventions each repository's `AGENTS.md` copied, and from capabilities of [FEA-019: equivalent implementations](features/README.md#FEA-019).

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
  *Applied in*: parsers that read semantically incorrect code ([CAP-026: Python, TypeScript and C and C++ read as written](capabilities/CAP-026.md)); names a language cannot spell kept in the tree and flagged by validation, never renamed; `TranspileError`
  (mbse-programs); drops recorded as steps (mbse-codegen-python).
  *Not yet applied* in mbse-schemas: decoding refuses undeclared keys. [CAP-033: undeclared properties preserved](capabilities/CAP-033.md#design) proposes preserving
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
  *Applied in*: mbse-schemas, as [CAP-107: one visitor protocol reads and writes data](capabilities/CAP-107.md) records it, which supersedes the reverse protocol (`accept(visitor)`, a
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
  bridge between two lives in the repository that depends on both. *Serves* [QUA-005: an opinionated paradigm](QUALITIES.md#QUA-005), [QUA-003: no second-order inventions](QUALITIES.md#QUA-003), [QUA-010: every repository works alike](QUALITIES.md#QUA-010).
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
  properties by string, as the user decided ([CAP-109: schemas as linked objects in modules](capabilities/CAP-109.md#decided), "Schema builders align with their
  meta-schemas"). There is no other: "Code expressions that name a reference object use Paths, not string lookup," as
  the user decided, a path from a singleton through ownership entries, each step its adjacency called with the entry's
  keys (`store.Instances.wts.Features.dir({ name: 'DEF-693' })`, object identity 26
  and 27 in [CAP-119: owned objects found by path](capabilities/CAP-119.md#decided)); the earlier `as_instance` exception is withdrawn.
  *Not yet applied*, in the API the design documents show: `E.variable("c")` beside `pred.c`, `s.get("properties")`
  (mbse-patterns, mbse-codegen-python); `Transform("Label", ...)` and `Clause("Label", ...)` (mbse-patterns).
- <a id="PRI-016"></a>**PRI-016: guidance written once** · proposed · Guidance is written once, in its reader's language: no copies and no symlinks. Each
  implementation's skill shows usage in its own language, covering the same topics in the same order as the other's;
  concepts live once, in the design document, which each skill links to rather than restates. *Serves* [QUA-001: AI and humans in the loop](QUALITIES.md#QUA-001),
  [QUA-010: every repository works alike](QUALITIES.md#QUA-010). *Relates to* [PRI-037: the same conformance corpora](#PRI-037), [PRI-036: every program in a skill is complete and run; fragments are tagged as fragments](#PRI-036).
- <a id="PRI-017"></a>**PRI-017: transforms, models, dialects, schemas** · adopted · Transforms use Steps to mutate Models which are built on Dialects which are built on Schemas.
  *Relates to* [PRI-014: every ambiguity a decision](#PRI-014), [PRI-018: no model needs code to read or write](#PRI-018).
- <a id="PRI-018"></a>**PRI-018: no model needs code to read or write** · adopted · "No model should need code to read or write. Ever." All model data is governed by a schema,
  and all builder/visitor/reader/write functionality comes from either proxies in mbse-schemas or generated
  dataclasses. No bespoke class implementations are allowed for models. *Relates to* [PRI-003: everything is schema data](#PRI-003), [PRI-004: one visitor protocol per kind](#PRI-004), [PRI-010: proxies and generated code read alike](#PRI-010), [PRI-017: transforms, models, dialects, schemas](#PRI-017).
  *Not yet applied* in mbse-expressions ([CAP-098: dialects over one framework](capabilities/CAP-098.md#open-questions), Open questions).
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
  *Applied in*: mbse-schemas 0.26.3, a value of an `OfAny` restricted to several schemas wrapped by its kind and
  schema, bare only where one of its schemas takes its plain form ([CAP-069: wire format shorthand (scalars)](capabilities/CAP-069.md)).
- <a id="PRI-026"></a>**PRI-026: serialization through the visitor protocol** · adopted · "serialization is handled via visitor protocol", and
  a reader tracks the expected schema as context while traversing wire data. "The wire format *usually* tracks each
  recursion by the writer while traversing in-memory data which has the effect of wrapping unions explicitly.
  Shorthands permit these wrappers to be skipped in cases where the correct behavior can be unambiguously and
  trivially inferred from context by a reader that already knows the expected schema. This makes the format more
  concise and resilient to errors from humans and agents in the loop." *Relates to* [PRI-025: never guess the schema](#PRI-025),
  [PRI-004: one visitor protocol per kind](#PRI-004); its shorthands are [CAP-069: wire format shorthand
  (scalars)](capabilities/CAP-069.md) and [CAP-070: wire format shorthand (containers)](capabilities/CAP-070.md).
- <a id="PRI-027"></a>**PRI-027: developers can assume completely consistent behavior across bindings and generated source code** · proposed · Code
  written against one binding, or against generated source code, behaves the same against any other: the same
  results, errors and wire format, so that a developer need not test each binding apart. *Serves*
  [QUA-006: the same in every language](QUALITIES.md#QUA-006). *Applied in*: [FEA-036: serialization behavior is consistent across bindings and generated source code](features/FEA-036.md).
- <a id="PRI-028"></a>**PRI-028: both implementations change together** · proposed · Where a repository has a Python and a
  TypeScript implementation, they are one library in two languages: the same API (the same modules, classes, methods
  and argument order, with the same names, snake_case included), the same behavior (the same results, the same error
  classes and byte-identical error and validation messages, [PRI-009: one error shape](#PRI-009)), and the same data on the wire
  ([PRI-037: the same conformance corpora](#PRI-037)). A change to one is made to both in the same commit: the same names and messages, the test
  case added or changed in both suites under the same ID and position ([PRI-038: the same cases in both languages](#PRI-038)), the corpora regenerated in
  both, and both suites run under their coverage gates ([PRI-039: 100% coverage of both](#PRI-039)). Only a language's unavoidable mechanics
  differ, and a difference not listed is a bug ([PRI-040: deliberate differences listed](#PRI-040)). *Governs* the product. *Serves* [QUA-006: the same in every language](QUALITIES.md#QUA-006).
  *Relates to* [PRI-027: developers can assume completely consistent behavior across bindings and generated source code](#PRI-027), [FEA-019: equivalent implementations](features/README.md#FEA-019).
  *Applied in*: each repository's `docs/EQUIVALENCE.md`, which keeps its own checks, commands and exceptions (mbse-schemas'
  adapters, each translating its own language's type declarations).
- <a id="PRI-029"></a>**PRI-029: parallel work in polyrepo workspaces** · proposed · Agents and people working at the same
  time each work in a workspace, `python3 ../mbse-basis/scripts/polyrepo.py workspace <dir> --branch <name>`: git
  worktrees of the repository and of its siblings side by side, so that the relative paths to the siblings hold, the
  repository on the branch, and each sibling the change spans named by `--edit <sibling>` and on the same branch.
  They install there, and `land` the workspace when done, siblings before their dependents. A sibling is changed only
  so, never by editing its checkout from another repository's work; a worktree of one repository alone, such as an
  agent's built-in worktree isolation, breaks the relative paths. *Governs* the work. *Serves* [QUA-010: every repository works alike](QUALITIES.md#QUA-010).
  *Relates to* [PRI-032: a sibling's gap is reported, not worked around](#PRI-032), [PRI-033: work lands by branch and pull request](#PRI-033).
- <a id="PRI-030"></a>**PRI-030: one package layout** · proposed · Every repository lays out its packages alike: Python's under
  `python3/mbse/<Area>/` as `mbse.<Area>` or `mbse.<Area>.<Name>`, TypeScript's under `typescript5/` as
  `@mbse/<name>`, the repository's name without `mbse-`; the area and name capitalized as mbse-schemas has them
  (`mbse.Schemas`, `mbse.Services.Rest`, `mbse.Persistence.DynamoDB`, `mbse.Demos.Apps`). *Governs* the product: a user
  sees it in every import. *Serves* [QUA-005: an opinionated paradigm](QUALITIES.md#QUA-005).
- <a id="PRI-031"></a>**PRI-031: the version is the contract** · proposed · A repository's Python and TypeScript packages share one
  version, and a release is the tag `v<version>`. A sibling is compatible when it has the same major version (the same
  minor below 1.0) and is no older, so below 1.0 a change that dependents must adapt to bumps the minor version.
  Dependents develop against the sibling's checkout as it is, and pin the version and commit they were tested with in
  `siblings.json`, with `polyrepo.py pin`; a sibling without packages, such as mbse-basis, is pinned by commit alone.
  `scripts/polyrepo.py` carries it out (`polyrepo.py help`). *Governs* the work. *Serves* [QUA-010: every repository works alike](QUALITIES.md#QUA-010).
- <a id="PRI-032"></a>**PRI-032: a sibling's gap is reported, not worked around** · proposed · A repository uses its siblings as
  they stand. A gap or bug found in a sibling is reported to the user, and recorded under Blocked in the item it keeps
  from being met ([the basis](README.md#detail-files), Detail files); it is fixed in the sibling, through a workspace ([PRI-029: parallel work in polyrepo workspaces](#PRI-029)), never worked
  around locally. *Governs* the work. *Serves* [QUA-010: every repository works alike](QUALITIES.md#QUA-010). *Relates to* [PRI-011: the lowest repository that can own it](#PRI-011).
- <a id="PRI-033"></a>**PRI-033: work lands by branch and pull request** · proposed · Work is never committed to a repository's
  default branch: it is done on a branch, the same name in each repository it changes, pushed after every commit with
  `polyrepo.py push` (which pushes the siblings first, and refuses a branch behind its remote or a pin of a commit the
  sibling lacks), and proposed in one pull request per repository, listing the decisions taken for review
  ([the basis](README.md#detail-files), Decided by an agent, for review). *Governs* the work. *Serves* [QUA-010: every repository works alike](QUALITIES.md#QUA-010).
- <a id="PRI-034"></a>**PRI-034: tutorials run as tests, committed with their outputs** · proposed · Each tutorial
  ([the basis](README.md#the-doc-spec), Tutorials) is run by the repository's test suite, `tutorials/` beside `tests/`; the languages tell the same case
  studies with the same outputs; and a tutorial is committed with its outputs, re-executed after any change that
  alters them. *Governs* the product: a reader sees stale outputs. *Serves* [QUA-001: AI and humans in the loop](QUALITIES.md#QUA-001). *Relates to* [PRI-038: the same cases in both languages](#PRI-038).
- <a id="PRI-035"></a>**PRI-035: tests are notebooks: one suite each, the same case IDs in the same order in both languages** · proposed · A
  repository's tests ([the basis](README.md#the-doc-spec), Tests) are Jupyter notebooks, one suite per notebook, with the same case IDs in the same
  order in both languages. Each case is a markdown cell `## ID · title` followed by one code cell. Notebooks are JSON
  written with `indent=1`, `sort_keys=True` and `ensure_ascii=False`. Each language's `tests/TestPlan.md` lists the
  cases; the second language's lists only its differences. *Governs* the work. *Serves* [QUA-010: every repository works alike](QUALITIES.md#QUA-010),
  [QUA-006: the same in every language](QUALITIES.md#QUA-006). *Relates to* [PRI-038: the same cases in both languages](#PRI-038).
  *Applied in*: mbse-schemas, mbse-expressions, mbse-patterns, mbse-programs, mbse-codegen-python.
  *Not yet applied*: mbse-rest, mbse-dynamodb and mbse-demo-apps (pytest modules) and mbse-react (Vitest).
- <a id="PRI-036"></a>**PRI-036: every program in a skill is complete and run; fragments are tagged as fragments** · proposed · Every
  fenced block tagged `python` or `typescript` in a skill ([the basis](README.md#the-doc-spec), Skills) is a complete program that the repository's
  test suite runs (each repository's SKL-02); a fragment is tagged `python fragment` or `typescript fragment`.
  *Governs* the product: an agent copies what a skill shows. *Serves* [QUA-001: AI and humans in the loop](QUALITIES.md#QUA-001). *Relates to* [PRI-016: guidance written once](#PRI-016).
- <a id="PRI-037"></a>**PRI-037: the same conformance corpora** · proposed · Every repository's Python and TypeScript implementations
  pass the same conformance corpora (CONF suites): the same names, errors and messages, and byte-identical JSON (the
  same keys, key order, float formatting, escapes and whitespace); each implementation reads the other's output back
  into the same values. *Governs* the product. *Serves* [QUA-006: the same in every language](QUALITIES.md#QUA-006). *Relates to* [FEA-019: equivalent implementations](features/README.md#FEA-019).
  Formerly [CAP-024: the same conformance corpora](capabilities/README.md#CAP-024).
  - **Current**: met in mbse-schemas, mbse-expressions, mbse-patterns and mbse-programs; to assess in
    mbse-codegen-python.
- <a id="PRI-038"></a>**PRI-038: the same cases in both languages** · proposed · Every repository's tests and tutorials hold the
  same cases in both languages: the same suites and case IDs, in the same order, with the same assertions. *Governs*
  the work. *Serves* [QUA-006: the same in every language](QUALITIES.md#QUA-006). *Relates to* [FEA-019: equivalent implementations](features/README.md#FEA-019). Formerly [CAP-030: the same cases in both languages](capabilities/README.md#CAP-030).
  - **Current**: as [PRI-037: the same conformance corpora](#PRI-037)'s.
- <a id="PRI-039"></a>**PRI-039: 100% coverage of both** · proposed · Every repository's tests cover 100% of both implementations'
  code, gated by each language's coverage tool: statements and branches in Python; statements, branches, functions
  and lines in TypeScript. A gap is closed by an assertion in the shared case, in both suites under the same ID, or by
  removing the code no input reaches from both; never by excluding it. *Governs* the work. *Serves* [QUA-006: the same in every language](QUALITIES.md#QUA-006).
  *Relates to* [FEA-019: equivalent implementations](features/README.md#FEA-019). Formerly [CAP-031: 100% coverage of both](capabilities/README.md#CAP-031).
  - **Current**: as [PRI-037: the same conformance corpora](#PRI-037)'s.
- <a id="PRI-040"></a>**PRI-040: deliberate differences listed** · proposed · Each deliberate difference between a repository's
  implementations, one its languages force, is listed in its `docs/EQUIVALENCE.md` and in both test plans, with the
  cases that assert it; a difference not listed is a bug. *Governs* the product. *Serves* [QUA-006: the same in every language](QUALITIES.md#QUA-006).
  *Relates to* [FEA-019: equivalent implementations](features/README.md#FEA-019). Formerly [CAP-032: deliberate differences listed](capabilities/README.md#CAP-032).
  - **Current**: as [PRI-037: the same conformance corpora](#PRI-037)'s.

## Open items

- **[PRI-015: concrete references are programmatic](#PRI-015) and [PRI-017: transforms, models, dialects, schemas](#PRI-017) to [PRI-019: fluent builder syntax](#PRI-019): what they serve.** Which qualities each serves is still to state.
- **[PRI-001: declaration order](#PRI-001)'s exception and a proposal against it.** Decide whether entries sorted by their relation's key are a
  deliberate exception (an order by value, for byte-identity) or a debt against [PRI-001: declaration order](#PRI-001). [CAP-033: undeclared properties preserved](capabilities/CAP-033.md#open-questions)
  also proposes writing preserved properties sorted by name, against [PRI-001: declaration order](#PRI-001).
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
[← Why the mbse repositories exist](../MBSE.md) · [Home](../README.md) · [Qualities →](QUALITIES.md)
