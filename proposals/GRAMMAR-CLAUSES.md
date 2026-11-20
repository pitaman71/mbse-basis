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
- **"The "open universe" design philosophy is interpreted by unions as "any"."**, as the user decided
  ([PRI-020: no constraint, any configuration](../docs/principles/PRI-020.md#decided)): a syntax node or a term is
  accepted at a place if the target edition allows any grammar clause it takes there.
  Read as "each", PEP 614's two overlapping grammar clauses would refuse a dotted decorator in every version.
- **Beyond the nested form** (on open question 3): "right": patterns, once mbse-patterns' port is done, where a case
  needs more.

## The design (proposed)

**A grammar clause** (`Expressions.Framework.GrammarClause`, a reference object a dialect owns by name): a kind, one
of its properties, and what that property may hold there:

- **present** or **absent**: the grammar clause is the property set, or unset (Python's `Import.is_lazy`; C23's
  `static_assert` without a message, its `message` absent; TypeScript 5.3's import `attributes`);
- **one of these values**: scalars (Python 3.5's `AugAssign.op` `@`; C23's keyword spellings, `thread_local`,
  `alignas`, its integer suffix `wb`; TypeScript's `declarationKind` `using`, `phase` `defer`);
- **a term of one of these kinds**, each optionally with grammar clauses of its own, nested, for what the held term's
  own subterms may be: Python 3.11's subscript whose index is a starred term; Python 3.15's comprehension of starred
  elements; and PEP 614: Python 3.0 to 3.8 have "a decorator holds a dotted name, optionally called" (a `name`, an
  `attribute` whose value is one, or a `call` whose function is one), Python 3.9 on "a decorator holds any term".

**Editions allow or forbid it**: relations `Expressions.Framework.Allows(standard, clause)` and
`Expressions.Framework.Forbids(standard, clause)`, each with optional flags `before` and `after`, which extend the entry
to the editions before or after its own that the data does not represent, only to guess support for one. A grammar
clause no `Allows` or `Forbids` names is allowed. Removal and addition are symmetric: no minimum version anywhere, and
the `SINCE` tables go, in mbse-expressions' dialects and in mbse-programs' languages alike.

**Reading**: `Framework.Standards` gains `allows(standard, clause)` (an edition's `Allows` and `Forbids`, else its
flagged neighbours', else allowed). A language's `Check` asks, for each syntax node and term, which grammar clauses it
takes at each place (by its kind, its properties' values and its subterms' kinds), and whether the target version
allows any of them there, alternatives as a union's branches are (Decided, above):
`body[2].decorator_list[0]: a decorator holding any term needs Python 3.9`. The code tables (`FEATURES`,
`STATEMENT_FEATURES`) go.

**Where**: the model and the reading in mbse-expressions' framework (both implementations); each of its dialects
records its terms' grammar clauses (Python3, Python Types and Patterns, TypeScript5 and its family, C, C++, C Types,
C Preprocessor, SystemVerilog's); each of mbse-programs' languages records its statements' (Python3, TypeScript5, C,
Cpp).

## Open questions

Stage 1 built the design above (mbse-expressions 0.15.0); stage 2 (mbse-programs #25 and #26) is in review. What
they found it cannot yet do, each to be addressed, as the user decided ("All of the shortcomings you list - they do
need to be addressed"):

1. **An edition the data does not represent.** `before` and `after` guess a grammar clause's support for an edition
   the data does not represent, but only for one stored: `allows` takes a stored `Standard`, so a Python 3.16 or a C2y
   cannot be checked unless it is written, and a kind's membership (`HasStandard`) has no guess at all. Proposed:
   (a) `allows` and a kind's membership answer for an edition given by its designation and revision, stored or not,
   from its neighbours' flagged entries; (b) `HasStandard` gains `before` and `after` too, written on each standard's
   oldest and newest editions, as `Allows` and `Forbids` have them.
2. **What one grammar clause cannot express.** Found by stage 2, each kept as code (`Check.UNRECORDED`) until decided:
   - *every* or *none* of a list's elements (C's unnamed parameter of a definition: no element of its declarator's
     specifiers is a lone `void`; C's inferred `auto`: none of the specifiers names a type);
   - two properties together (C's `u8` character literal: `prefix` and `quote`; C++'s bit-field with a default member
     initializer: `bitfield` and `initializer`; C++'s `static operator()`: a specifier and the declarator's name);
   - a count (C++23's subscript of several indices: two or more elements);
   - alternatives among the nested grammar clauses of one kind (each nested one must hold today).

   Options: (a) the grammar clause grows these forms: a quantifier on a list property (`any`, the default, `every`,
   `none`), a count (`at least`), and a conjunction of grammar clauses on one syntax node or term (`Requires(clause,
   clause)`), alternatives among nested ones read as "any", as [PRI-020](../docs/principles/PRI-020.md#decided)
   reads unions; (b) they wait for patterns ([FEA-023: patterns over data](../docs/features/FEA-023.md)), as decided
   for what needs more than the nested form, staying code meanwhile. *Proposed: (a)*, each small and of the grammar's
   own shape, and every case found so far fits them; patterns stay for what a grammar does not say.
3. **Removals.** No grammar clause records what an edition removed: C23's K&R function definitions, C++17's
   `register`. They are data only, a grammar clause `Forbids` from the edition that removed it, with no model change.
   Proposed: recorded in stage 3.
4. **Two small API gaps in mbse-expressions.** `takes` reads a list property as a whole, so a caller finds which element
   took a grammar clause itself (per-element answers proposed); and the writer `grammar_clauses_spec` binds a fixed
   frame symbol, `dialect` (the caller's symbol proposed).

## Stages (proposed)

1. mbse-expressions: the model, the reading, and each dialect's grammar clauses, allowed and forbidden by its editions
   in its `define`; `SINCE` gone; both implementations; a release.
2. mbse-programs: each language's statements' grammar clauses in its `Standards.define`; `Check` reading them; the code
   tables and `SINCE` gone; the suites asserting each former entry by data.
3. The open questions above, once decided: the guesses for unrepresented editions, the grammar clause's further forms,
   removals, and the API gaps; mbse-expressions first, then mbse-programs, `Check.UNRECORDED` emptied.
4. Drained into CAP-268 (its As built) and a capability of its own for grammar clauses, if the user wants one.
