# Priorities

The order in which the schema-driven visualization ([FEA-001: schema-driven UI](../docs/features/FEA-001.md) and the features beside it)
was to be built. This proposal is drained ([the basis](../docs/README.md#other-documents), proposals): everything else
it listed now lives in the items that hold it, the qualities, features and capabilities of the design spec. Only the
two below are left, deferred until they are designed; as the user said, "keep until designe[d]".

*Initiatives* enumerate what were once called proposals and priorities.
Each initiative represents an investment of effort towards a particular
external demo or product goal in terms of a set of CAP that must be 
(or have been) completed.

## INI-0XX : infrastructure

## INI-001 : define and apply agentic engineering strategy for MBSE frameworks

**PRIORITY**: 4

## INI-002 : establish repository + dependency organization for MBSE repos

**PRIORITY**: 4

## INI-003 : plans + docs + source organized and optimized for selective consumption

**PRIORITY**: 3

Why?

- keeping agents and humans in the loop
- managing drift and proliferation
- optimization for consumption and fungibility
- self-renewing attention to quality, value

How?

- stabilizion of concepts and terminology
- enumeration of source IP asset kinds (e.g. programs, tests, docs, skills)
- enumeration of semantic categories that create organization within and across asset kinds
- establishing + maintaining semantic orthogonality ("source of truth")
- creating intentional, managed overlap with bridging
- circumscription at the boundary of each category

Documentation ([FEA-057: documentation organized by semantic role](../docs/features/FEA-057.md)):

- [CAP-248: skill gaps found automatically](../docs/capabilities/README.md#CAP-248): met
- [CAP-249: links labeled by title, not by path](../docs/capabilities/README.md#CAP-249): met
- [CAP-252: script generates a standard scaffold for new MBSE-adjacent repositories](../docs/capabilities/README.md#CAP-252): met
- [CAP-244: mbse-programs' cross-repository links in the agreed forms](../docs/capabilities/README.md#CAP-244), and
  [CAP-245: mbse-programs' skill linking its notebook cases](../docs/capabilities/README.md#CAP-245): after mbse-programs' overhaul
- [CAP-246: mbse-codegen-python's tutorials](../docs/capabilities/README.md#CAP-246), then
  [CAP-247: mbse-codegen-python's skill linking its notebook cases](../docs/capabilities/README.md#CAP-247): after mbse-codegen-python's port
- [CAP-250: decision tags made readable](../docs/capabilities/README.md#CAP-250): not yet scheduled

## INI-010 : build-out and stabilize schemas framework

**PRIORITY**: 3

Design: [parametrics](PARAMETRICS.md), in its order of work. Related: [INI-014: context + references +
changes cleanup](#ini-014--context--references--changes-cleanup), the contexts that validation and simplification take.

- [CAP-311: references stabilized](../docs/capabilities/README.md#CAP-311): met
- [CAP-312: a parameter reference in place of anything with a schema](../docs/capabilities/README.md#CAP-312): met
- [CAP-314: parameters assigned or bound by the data objects their schema governs](../docs/capabilities/README.md#CAP-314): superseded by CAP-313
- [CAP-313: parameter references valid where their parameters are assigned or bound](../docs/capabilities/README.md#CAP-313): met
- [CAP-114: parameter bindings are substituted and checked](../docs/capabilities/CAP-114.md): not met
- [CAP-296: simplification over literals, variables and parameters](../docs/capabilities/README.md#CAP-296): not met
- [CAP-298: simplification over type parameters](../docs/capabilities/README.md#CAP-298): not met
- [CAP-163: parameters assigned, bound, applied and generated beyond mbse-schemas](../docs/capabilities/CAP-163.md): not met

## INI-011 : build-out object + relation + pattern framework

**PRIORITY**: 3

Charter: [mbse-patterns afresh](https://github.com/pitaman71/mbse-patterns/blob/main/docs/proposals/rescope/README.md). Patterns over data ([FEA-023: patterns over data](../docs/features/FEA-023.md)), in mbse-patterns 0.10.0:

- [CAP-072: distributions linked to patterns](../docs/capabilities/CAP-072.md): not met there yet
- [CAP-042: data generated from constraints](../docs/capabilities/CAP-042.md): not met there yet; rejecting a draw by its `requires` is
  blocked on [CAP-142: expressions evaluated in queries](../docs/capabilities/CAP-142.md#blocked)
- [CAP-073: distributions fit from data](../docs/capabilities/CAP-073.md): not met

## INI-012 : domain + expression dialect framework

**PRIORITY**: 3

Design: [grammar alternatives by version](GRAMMAR-ALTERNATIVES.md): language features recorded as standards data.

## INI-013 : define and build journaled persistence framework

**PRIORITY**: 3

Proposals: [Journals](JOURNALS.md), [Journal storage](JOURNAL-STORAGE.md) for where a journal is kept, and
[Stacked stores](STACKED-STORES.md) for the stores stacked over it, each lazy by default. Journals, their language in mbse-schemas and the journal in a new repository
mbse-journals, in build order:

- [CAP-270: a transaction's changes observed at its commit](../docs/capabilities/README.md#CAP-270), in mbse-schemas
- [CAP-271: the journal language](../docs/capabilities/README.md#CAP-271), in mbse-schemas
- [CAP-269: transactions resolved into their effects](../docs/capabilities/README.md#CAP-269), in mbse-schemas
- [CAP-293: an entry inserted against a unique clause refuses its transaction](../docs/capabilities/README.md#CAP-293), in mbse-schemas
- [CAP-199: journals as queryable stores (mbse-journals)](../docs/capabilities/CAP-199.md)
- [CAP-288: the journal storage interface](../docs/capabilities/README.md#CAP-288), with the journal kept in memory, from
  [CAP-273: journals in memory and in local files](../docs/capabilities/README.md#CAP-273)
- [CAP-289: journals kept in DynamoDB](../docs/capabilities/README.md#CAP-289), by an agent of its own once CAP-288 is
  released, beside the five below
- [CAP-283: a store given a store below](../docs/capabilities/README.md#CAP-283), in mbse-schemas
- [CAP-284: objects loaded on demand](../docs/capabilities/README.md#CAP-284), in mbse-schemas
- [CAP-285: writes through, others' writes in](../docs/capabilities/README.md#CAP-285), in mbse-schemas
- [CAP-286: an extent through ownership](../docs/capabilities/README.md#CAP-286), in mbse-schemas
- [CAP-287: lazy or eager, tuned when it runs](../docs/capabilities/README.md#CAP-287), in mbse-schemas
- [CAP-308: stacking by mutation transactions, in one round trip](../docs/capabilities/README.md#CAP-308), in mbse-schemas, mbse-rest and mbse-dynamodb
- [CAP-309: errors annotated on frames](../docs/capabilities/README.md#CAP-309), in mbse-schemas
- [CAP-310: a cache layer's partial-aware interpretation](../docs/capabilities/README.md#CAP-310), in mbse-schemas
- [CAP-290: a service's store stacked, with no snapshot](../docs/capabilities/CAP-290.md), in mbse-rest
- [CAP-291: journals kept in MongoDB](../docs/capabilities/README.md#CAP-291)
- [CAP-272: surgical mutations of a property's value](../docs/capabilities/README.md#CAP-272)
- [CAP-274: journals sent and received](../docs/capabilities/README.md#CAP-274)
- [CAP-275: two stores' difference as a journal transaction](../docs/capabilities/README.md#CAP-275)

## INI-014 : context + references + changes cleanup

Design: [Context + References + Changes cleanup](CONTEXT-REFERENCES-CHANGES.md): contexts, references and changes made
proper MBSE data structures, contexts the standardized argument of procedures. Related:
[INI-010: schemas framework](#ini-010--schemas-framework), whose validation and simplification take contexts.

- [CAP-320: schema and value references](../docs/capabilities/README.md#CAP-320): not met
- [CAP-319: contexts as schema data](../docs/capabilities/README.md#CAP-319): not met
- [CAP-321: changes gathered as schema data](../docs/capabilities/README.md#CAP-321): not met

## INI-020 : build-out code mutation framework

**PRIORITY**: 3

Charter: [mbse-transforms](https://github.com/pitaman71/mbse-transforms/blob/main/docs/proposals/charter/README.md). Transforms ([FEA-059: transforms of models, applied step by step and certified](../docs/features/README.md#FEA-059), serving [FEA-021: every generation ambiguity a parameter](../docs/features/FEA-021.md)), in mbse-transforms:

- [CAP-074: transforms applied step by step](../docs/capabilities/CAP-074.md),
  [CAP-075: steps linked to what they matched and wrote](../docs/capabilities/CAP-075.md) and
  [CAP-076: reruns reuse decisions](../docs/capabilities/CAP-076.md): in its first release; not met there yet
- [CAP-077: changes explained across runs](../docs/capabilities/CAP-077.md): blocked on mbse-journals
- [CAP-078: incremental rebuild](../docs/capabilities/CAP-078.md): not met
- [CAP-079: steps undone](../docs/capabilities/CAP-079.md): not met
- [CAP-080: invertible transforms](../docs/capabilities/CAP-080.md): not met
- [CAP-081: transforms composed into pipelines](../docs/capabilities/CAP-081.md): not met
- [CAP-082: completeness reported](../docs/capabilities/CAP-082.md): not met
- [CAP-083: policies with guards and distributions](../docs/capabilities/CAP-083.md): not met
- [CAP-317: transforms targeting value objects](../docs/capabilities/README.md#CAP-317): not met; until then, transforms
  to and from program trees match whole files

## INI-030 : no/low-code and apps framework

**PRIORITY**: 3

## INI-040 : diagrams framework

**PRIORITY**: 3

Proposals: [Diagrams](DIAGRAMS.md), and [Interaction](INTERACTION.md) for how a diagram is edited. Diagrams ([FEA-056: fungible diagramming keeps agents and humans in the loop](../docs/features/FEA-056.md)), in build order:

- [CAP-237: logical layout schemas](../docs/capabilities/CAP-237.md)
- [CAP-238: container schemas and grid insertion](../docs/capabilities/CAP-238.md)
- [CAP-239: grid adjacency](../docs/capabilities/CAP-239.md)
- [CAP-240: conflicting layout rules ignored and requeued](../docs/capabilities/CAP-240.md)
- [CAP-241: physical layout schemas](../docs/capabilities/CAP-241.md)
- [CAP-242: incremental physical placement](../docs/capabilities/README.md#CAP-242)
- [CAP-264: containment separate from ownership](../docs/capabilities/README.md#CAP-264)
- [CAP-280: the grid in the logical layout](../docs/capabilities/CAP-280.md)
- [CAP-269: transactions resolved into their effects](../docs/capabilities/README.md#CAP-269), from [INI-013: journals framework](#ini-013--journals-framework), with what it builds on
- [CAP-261: layout driven by any journal transaction](../docs/capabilities/README.md#CAP-261)
- [CAP-243: a diagram displayed from its mutation stream](../docs/capabilities/README.md#CAP-243)
- [CAP-262: a candidate mutation's layout previewed, never journalled](../docs/capabilities/README.md#CAP-262)
- [CAP-263: touch-first gestures, each one mutation](../docs/capabilities/README.md#CAP-263)
- [CAP-266: shapes deleted](../docs/capabilities/README.md#CAP-266)

## INI-041 : Agentic AI integration

**PRIORITY**: 3

## INI-042 : Content Management Systems integration

**PRIORITY**: 5

Build the ability to quickly an MBSE system to shadow a (legacy) content 
management system where MBSE can serve as secondary, primary, or hybrid
source of truth / system of record. 

- survey content management systems
- devise a vocbulary of universal domains
- provide streaming data conduits for common file formats
- provide streaming data conduits for common service APIs
- prove that (via MCP) agents can conduct selective syncs with legacy
  systems on a recurring basis
- prove that (via MCP) agents can conduct surgical edits that durably
  round-trip with a legacy system

## INI-043 : Finance Management Systems integration

**PRIORITY**: 5

Build the ability to quickly an MBSE system to shadow a (legacy) finance 
management system where MBSE can serve as secondary, primary, or hybrid
source of truth / system of record. 

- survey finance management systems
- devise a vocbulary of universal domains
- provide streaming data conduits for common file formats
- provide streaming data conduits for common service APIs
- prove that (via MCP) agents can conduct selective syncs with legacy
  systems on a recurring basis
- prove that (via MCP) agents can conduct surgical edits that durably
  round-trip with a legacy system

## INI-044 : Engineering Systems Integration

**PRIORITY**: 5

Build the ability to quickly an MBSE system to shadow a (legacy) 
engineering system where MBSE can serve as secondary, primary, or hybrid
source of truth / system of record. 

- survey engineering systems
- devise a vocbulary of universal domains
- provide streaming data conduits for common file formats
- provide streaming data conduits for common service APIs
- prove that (via MCP) agents can conduct selective syncs with legacy
  systems on a recurring basis
- prove that (via MCP) agents can conduct surgical edits that durably
  round-trip with a legacy system

## INI-045 : Scientific Systems Integration

**PRIORITY**: 5

Build the ability to quickly an MBSE system to shadow a (legacy)
scientific system where MBSE can serve as secondary, primary, or hybrid
source of truth / system of record. 

- survey scientific systems
- devise a vocbulary of universal domains
- provide streaming data conduits for common file formats
- provide streaming data conduits for common service APIs
- prove that (via MCP) agents can conduct selective syncs with legacy
  systems on a recurring basis
- prove that (via MCP) agents can conduct surgical edits that durably
  round-trip with a legacy system

## INI-046 : Embedded Systems Integration

**PRIORITY**: 4

Build the ability to quickly an MBSE system to shadow a (legacy) 
embedded system where MBSE can serve as secondary, primary, or hybrid
source of truth / system of record. 

- survey embedded systems
- devise a vocbulary of universal domains
- provide streaming data conduits for common file formats
- provide streaming data conduits for common service APIs
- prove that (via MCP) agents can conduct selective syncs with legacy
  systems on a recurring basis
- prove that (via MCP) agents can conduct surgical edits that durably
  round-trip with a legacy system

## INI-047 : Robotic Systems Integration

**PRIORITY**: 5

Build the ability to quickly an MBSE system to shadow a (legacy)
robotic system where MBSE can serve as secondary, primary, or hybrid
source of truth / system of record. 

- survey robotic systems
- devise a vocbulary of universal domains
- provide streaming data conduits for common file formats
- provide streaming data conduits for common service APIs
- prove that (via MCP) agents can conduct selective syncs with legacy
  systems on a recurring basis
- prove that (via MCP) agents can conduct surgical edits that durably
  round-trip with a legacy system

## INI-048 : Autonomic Systems Integration

**PRIORITY**: 5

Build the ability to quickly an MBSE system to shadow a (legacy)
autonomic system where MBSE can serve as secondary, primary, or hybrid
source of truth / system of record. 

- survey autonomic management systems
- devise a vocbulary of universal domains
- provide streaming data conduits for common file formats
- provide streaming data conduits for common service APIs
- prove that (via MCP) agents can conduct selective syncs with legacy
  systems on a recurring basis
- prove that (via MCP) agents can conduct surgical edits that durably
  round-trip with a legacy system

## INI-080 : stabilize mbse-schemas and mbse-expressions

**PRIORITY**: 2

## INI-081 : stabilize Python codegen

**PRIORITY**: 2

## INI-082 : eliminate counted objects

**PRIORITY**: 3

Counted objects are deprecated, as the user decided (2026-11-10), "counted objects are now deprecated": a reference object is to be a singleton or owned,
never counted ([CAP-118: singletons, owned and counted objects](../docs/capabilities/CAP-118.md)). Its capabilities are not yet designed. What
counted objects reach today:

- [CAP-118: singletons, owned and counted objects](../docs/capabilities/CAP-118.md): the counted mode of identity, and its decisions
- [CAP-133: no durable references to counted objects](../docs/capabilities/CAP-133.md): not met
- [CAP-138: mutation expressions over frame streams](../docs/capabilities/CAP-138.md): a transaction's terms are counted objects (object identity 93 and 94)
- [CAP-010: object browser](../docs/capabilities/CAP-010.md), [CAP-011: relation browser](../docs/capabilities/CAP-011.md) and
  [FEA-003: no-code logical views](../docs/features/FEA-003.md): counted objects, having no reference, are left out of what they
  show and transmit

## INI-2XX : automated audits

## INI-201 : tutorials that double as tests

**PRIORITY**: 4

## INI-202 : equivalence requirements

**PRIORITY**: 4

## INI-208 : gaps plan category

**PRIORITY**: 4

- log bugs + tech debt in a "gaps" plan category
- consolidate and enuerate tech debt (from Later, below)

## INI-105 : nope plan category

**PRIORITY**: 4

- log boundaries around things we will not build in a "nope" plan category
- first entries: snapshots ([CAP-127: snapshots made of transactions](../docs/capabilities/CAP-127.md)), and
  [CAP-282: no model needs bespoke schema-aware code to read or write](../docs/capabilities/README.md#CAP-282), absorbed as a capability until then

## INI-3XX : demos

## INI-301 : formalize, parameterize, and visualize HW and LLM architectures

**PRIORITY**: 2

Builds on [INI-040: diagrams framework](#ini-040--diagrams-framework).

## INI-302 : explore, optimize LLM accelerator architectures (demo version)

**PRIORITY**: 1

## INI-303 : demo "the Attention Chip"

**PRIORITY**: 1

## INI-304 : demo "Tensor Parallelism with distributed K-V cache"

**PRIORITY**: 1

## INI-4XX : proofs

## INI-401 : fully agent and human visible and fungible

Prove that a combined system that integrates legacy system(s) with 
MBSE is fully agent and human visible and fungible

## INI-402 : fully secure, accountably authorized

Prove that a combined system that integrates legacy system(s) with 
MBSE is fully secure

## INI-403 : surgically and accountably correctable

Prove that surgical corrections can be retroactively applied to any 
data stored in MBSE. Prove that history prior to the correction remains
preserved. Prove that provenance and authorization of the correction
is just as auditable as the original history.

## INI-404 : continuously available

Prove that a combined system that integrates legacy system(s) with 
MBSE is continuously available

## INI-405 : absolutely trustworthy

Prove that a combined system that integrates legacy system(s) with 
MBSE is fully trustworthy with even the most sensitive information

## INI-406 : performant

Prove that the performance gap between pure MBSE code, hybrid code
using codegen with bespoke code, and pure bespoke code - can be
easily quantified and is well justified

## Later

- establishing reviews for leakage across document boundaries
- conceptual terminology drift is still a problem
- move integration workarounds into open source contribs
- drain historical notes from the documents written before the rule "State what is true now" ([the basis](../docs/README.md#rules-for-writing-items)) into git history
- consolidate and enumerate "decided" clauses 
- re-partition mutations and queries
