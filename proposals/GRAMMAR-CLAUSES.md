# Grammar clauses by version

Initiative: [INI-012: domain + expression dialect framework](PRIORITIES.md#ini-012--domain--expression-dialect-framework).

Each language's standards are data ([CAP-268: standards as tagged data](../docs/capabilities/CAP-268.md)): a standard,
one version of a language, links the kinds it has. But much of what changes from one version to the next is not a
kind. It is an alternative within a production of the grammar, a language feature (qualified here, as the vocabulary's
seam rule asks, from the design spec's features, `FEA-`): Python 3.15's `lazy import`, C23's digit separators,
TypeScript 5.2's `using`. Today those stay code, a table in each language's `Check` (`FEATURES`, `STATEMENT_FEATURES`
in mbse-programs' Python3, TypeScript5, C and Cpp), each entry a test on a syntax node or a term and the minor version
it arrived in, and the kinds themselves are seeded from a table of minimum versions (`SINCE`). This proposes recording
those alternatives as data, grammar clauses that standards allow or forbid.

## Decided

The user decided, on this proposal's question:

- **What it is**: "OK now I understand, this is about connecting language construct patterns to language versions. And
  I can see how patterns might be useful. I am uncertain T="the paint is dry" on patterns. So we either need to shore
  up patterns for use here, or if this is a matter of conditional clauses within the language grammar, we might have a
  simple workaround." Shown that nearly every entry of today's tables is such an alternative, the grammar's, not a
  pattern: this proposal.
- **No minimum versions**: "PEP 614 removing a restriction is still a conditional clause just with an opposite sense of
  version progression. That excludes having a "minimum version" annotation which is hacky anyway." A standard lists the
  alternatives it has, as it lists the kinds it has; one that a version removes is absent from the versions after it,
  as one a version adds is absent from those before.
- **A proposal first**: "yes go", to writing this up for review before building it.
- **Editions linked by relations** (on open question 1): asked whether standard editions are singletons, "If so, add
  relations for `Allows` and `Forbids`". An edition is a reference object, `Expressions.Framework.Standard`, owned by
  its dialect through `Covers` and keyed by its designation, so it is linked directly; a grammar clause is then a
  reference object too, which a relation can link, owned by its dialect by name. The name is the user's: a "grammar
  clause" (`Expressions.Framework.GrammarClause`), qualified apart from
  [VOC-032: clause](../docs/VOCABULARY.md#VOC-032).
- **`before` and `after`, and the default** (on open question 2): "Add two optional properties on `Allows` and
  `Forbids` : 'before' and 'after' which are only used by the system to guess support in the case that an edition has
  no representation. And a grammar clause that has no `Allows` or `Forbids` should default to allows." Asked whether
  they are flags extending an entry to the editions before or after its own that the data does not represent (an
  `Allows` of Python 3.9 with `after`: an unrepresented Python 3.16 guessed to allow it), or editions' designations:
  "correct", flags.
- **Beyond the nested form** (on open question 3): "right": patterns, once mbse-patterns' port is done, where a case
  needs more.

## The design (proposed)

**A grammar clause** (`Expressions.Framework.GrammarClause`, a reference object a dialect owns by name): a kind, one
of its properties, and what that property may hold there:

- **present** or **absent**: the grammar clause is the property set, or unset (Python's `Import.is_lazy`; C23's
  `static_assert` without a message, its `message` absent; TypeScript 5.3's import `attributes`);
- **one of these values**: scalars (Python 3.5's `AugAssign.op` `@`; C23's keyword spellings, `thread_local`,
  `alignas`, its integer suffix `wb`; TypeScript's `declarationKind` `using`, `phase` `defer`);
- **a term of one of these kinds**, each optionally with grammar clauses of its own, nested, for what the held term's own
  subterms may be: Python 3.11's subscript whose index is a starred term; Python 3.15's comprehension of starred
  elements; and PEP 614: Python 3.0 to 3.8 have "a decorator holds a dotted name, optionally called" (a `name`, an
  `attribute` whose value is one, or a `call` whose function is one), Python 3.9 on "a decorator holds any term".

**Editions allow or forbid it**: relations `Expressions.Framework.Allows(standard, clause)` and
`Expressions.Framework.Forbids(standard, clause)`, each with optional flags `before` and `after`, which extend the entry
to the editions before or after its own that the data does not represent, only to guess support for one. A grammar
clause no `Allows` or `Forbids` names is allowed. Removal and addition are symmetric: no minimum version anywhere, and
the `SINCE` tables go, in mbse-expressions' dialects and in mbse-programs' languages alike.

**Reading**: `Framework.Standards` gains `allows(standard, clause)` (an edition's `Allows` and `Forbids`, else its
flagged neighbours', else allowed). A language's `Check` asks, for each syntax node and term, which grammar clauses it
takes (by its kind, its properties' values and its subterms'
kinds), and whether the target version has each: `body[2].decorator_list[0]: a decorator holding any term needs Python
3.9`. The code tables (`FEATURES`, `STATEMENT_FEATURES`) go.

**Where**: the model and the reading in mbse-expressions' framework (both implementations); each of its dialects
records its terms' grammar clauses (Python3, Python Types and Patterns, TypeScript5 and its family, C, C++, C Types,
C Preprocessor, SystemVerilog's); each of mbse-programs' languages records its statements' (Python3, TypeScript5, C,
Cpp).

## Open questions

None: each was answered (Decided, above).

## Stages (proposed)

1. mbse-expressions: the model, the reading, and each dialect's grammar clauses, allowed and forbidden by its editions
   in its `define`; `SINCE` gone; both implementations; a release.
2. mbse-programs: each language's statements' grammar clauses in its `Standards.define`; `Check` reading them; the code
   tables and `SINCE` gone; the suites asserting each former entry by data.
3. Drained into CAP-268 (its As built) and a capability of its own for grammar clauses, if the user wants one.
