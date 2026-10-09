<!-- nav -->
[← Features](FEATURES.md) · [Home](README.md) · [Capabilities →](CAPABILITIES.md)

# Principles

Design principles that can be reapplied locally across a class of related situations. P-001 and P-002 are the original
draft; P-003 onward are proposed, promoted from decisions each repository made separately. *Applied in* names where
each already holds, so that those local texts can be replaced by citations.

## Index

- **P-001** · adopted · Declaration order over sorted order. *Serves* F-002.
  *Applied in*: a schema's member lists as open relations in declaration order, so that a schema read back equals the
  one built (mbse-schemas, `scalars` branch; sorting by name proved inconsistent); undeclared properties written in the
  order read (V-022); reachability in first-reference order (mbse-schemas `Reachable`); a transform session's
  candidates in the order it first saw them (mbse-patterns).
  *Exceptions*: a module's schemas are keyed and sorted by name; a relation's entries with a `unique` key are written
  sorted by that key.
- **P-002** · adopted · Open world means preserving unstructured data: don't lose, preserve, validate and cleanse on
  request. What is read is kept, undeclared or not, and written back as read; validation reports what does not fit,
  as unknown where the model is silent; cleansing removes or repairs it only when the caller asks. Only where a step
  cannot preserve, such as a third-party parser that drops what it cannot read, or a translation with no form in the
  target, is the input refused, by name and position; nothing is dropped silently. *Serves* F-005, F-006.
  *Relates to* P-007.
  *Applied in*: parsers that read semantically incorrect code (C-003); names a language cannot spell kept in the tree and flagged by validation, never renamed; `TranspileError`
  (mbse-programs); drops recorded as steps (mbse-codegen-python).
  *Applied on the `scalars` branch, not landed*: undeclared properties and plain values preserved by default, reported
  as unknown by checking, closed reading an option of each call (mbse-schemas; V-022, C-002 L2). On main, decoding
  still refuses undeclared keys.
- **P-003** · proposed · Everything is schema data: kinds are registered meta-schemas tagged `kind`, and expressions,
  predicates, syntax trees, modules and traces serialize, reflect and compare like any other data. *Serves* F-001,
  F-002, F-003.
  *Applied in*: meta-schemas and `Reflection` (mbse-schemas); expressions bound with `Bindings` (mbse-expressions);
  kinds (mbse-programs); traces (mbse-patterns).
- **P-004** · proposed · One shape for every kind: `Data`, `Builder`, `Spec` and `Schema`; fluent builders with one
  setter per property taking a `Spec`; `create`, `clone` and `update` finalize and never validate. *Serves* F-003.
  *Applied in*: mbse-schemas' builders; mbse-expressions' writers; mbse-programs' `LANGUAGE.Builders.<Kind>()`;
  mbse-patterns' predicates and transforms.
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
  formats are the standards' own (ISO/IEC 11404, `Ieee754`, `Ieee1164`, C++ and ECMAScript editions), with only the
  parameters a standard defines. *Serves* F-004.
  *Applied in*: datatypes of the 11404 dialect, decided (V-020); value domains (mbse-expressions); standards
  (mbse-programs).
- **P-013** · proposed · Nondeterminism is passed in, never held: a random source is given to each draw, with its seed,
  and streams depend on the seed and key alone. *Serves* F-005.
  *Applied in*: PCG32 and `Generators` (mbse-schemas, mbse-patterns).
- **P-014** · proposed · Every ambiguity is a decision: a parameter of one step, taken by a person, an agent or a policy
  chosen up front, and kept in a trace. *Serves* F-001, F-002.
  *Applied in*: `Transforms` (mbse-patterns); code generation (mbse-codegen-python).

## Open items

- **P-001's exceptions.** A module's schemas sorted by name, and keyed entries sorted by key, are sorted orders.
  Decide whether they are deliberate exceptions, say for lookup and byte-identity, or debts against P-001.
- **P-004 and P-005 may be one principle**, the uniform shape of a kind, or P-005 a part of P-003.

---

<!-- nav -->
[← Features](FEATURES.md) · [Home](README.md) · [Capabilities →](CAPABILITIES.md)
