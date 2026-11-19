# Grammar alternatives by version

Initiative: [INI-012: domain + expression dialect framework](PRIORITIES.md#ini-012--domain--expression-dialect-framework).

Each language's standards are data ([CAP-268: standards as tagged data](../docs/capabilities/CAP-268.md)): a standard,
one version of a language, links the kinds it has. But much of what changes from one version to the next is not a
kind. It is an alternative within a production of the grammar, a language feature (qualified here, as the vocabulary's
seam rule asks, from the design spec's features, `FEA-`): Python 3.15's `lazy import`, C23's digit separators,
TypeScript 5.2's `using`. Today those stay code, a table in each language's `Check` (`FEATURES`, `STATEMENT_FEATURES`
in mbse-programs' Python3, TypeScript5, C and Cpp), each entry a test on a syntax node or a term and the minor version
it arrived in, and the kinds themselves are seeded from a table of minimum versions (`SINCE`). This proposes recording
those alternatives as data, linked by the standards that have them, as the kinds are.

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

## The design (proposed)

**A grammar alternative** (`Expressions.Framework.Alternative`, a value object a dialect owns by name *(agent: the
name, for review)*): a kind, one of its properties, and what that property may hold there:

- **present** or **absent**: the alternative is the property set, or unset (Python's `Import.is_lazy`; C23's
  `static_assert` without a message, its `message` absent; TypeScript 5.3's import `attributes`);
- **one of these values**: scalars (Python 3.5's `AugAssign.op` `@`; C23's keyword spellings, `thread_local`,
  `alignas`, its integer suffix `wb`; TypeScript's `declarationKind` `using`, `phase` `defer`);
- **a term of one of these kinds**, each optionally with alternatives of its own, nested, for what the held term's own
  subterms may be: Python 3.11's subscript whose index is a starred term; Python 3.15's comprehension of starred
  elements; and PEP 614: Python 3.0 to 3.8 have "a decorator holds a dotted name, optionally called" (a `name`, an
  `attribute` whose value is one, or a `call` whose function is one), Python 3.9 on "a decorator holds any term".

**Membership, as for kinds**: `Expressions.Framework.Standard` gains a link to the alternatives it has, beside
`HasStandard`'s kinds. A dialect's `define` writes each version's kinds and alternatives by listing them, not by a
minimum version: `SINCE` tables go, in mbse-expressions' dialects and in mbse-programs' languages alike.

**Reading**: `Framework.Standards` gains `alternatives(standard)` beside `kinds(standard)`. A language's `Check`
asks, for each syntax node and term, which alternatives it takes (by its kind, its properties' values and its subterms'
kinds), and whether the target version has each: `body[2].decorator_list[0]: a decorator holding any term needs Python
3.9`. The code tables (`FEATURES`, `STATEMENT_FEATURES`) go.

**Where**: the model and the reading in mbse-expressions' framework (both implementations); each of its dialects
records its terms' alternatives (Python3, Python Types and Patterns, TypeScript5 and its family, C, C++, C Types,
C Preprocessor, SystemVerilog's); each of mbse-programs' languages records its statements' (Python3, TypeScript5, C,
Cpp).

## Open questions

1. **The name**: `Alternative`, as a grammar names one, beside a kind. Not "clause", which
   [VOC-032: clause](../docs/VOCABULARY.md#VOC-032) takes for a part of a statement that holds statements, nor
   "feature", the design spec's; a vocabulary entry for it either way.
2. **What an alternative an edition does not list means**: absent from every edition (a kind's property no version
   lists at all, the default) is taken as in every edition, so that only what changes between versions is recorded;
   or every alternative is listed, as every kind is. *Proposed: only what changes between versions*, as the tables do.
3. **The nested form's reach**: one level of nesting covers PEP 614 and every case found; deeper is allowed by the
   same shape. Whether a case needing more than a kind, a property and its values, nested, exists is to watch: those
   would be patterns ([FEA-023: patterns over data](../docs/features/FEA-023.md)), once mbse-patterns' port is done.

## Stages (proposed)

1. mbse-expressions: the model, the reading, and each dialect's alternatives in its `define`; `SINCE` gone; both
   implementations; a release.
2. mbse-programs: each language's statements' alternatives in its `Standards.define`; `Check` reading them; the code
   tables and `SINCE` gone; the suites asserting each former entry by data.
3. Drained into CAP-268 (its As built) and a capability of its own for alternatives, if the user wants one.
