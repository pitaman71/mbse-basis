# Priorities

The order in which the schema-driven visualization ([FEA-001: schema-driven UI](../docs/features/FEA-001.md) and the features beside it)
was to be built. This proposal is drained ([the basis](../docs/README.md#other-documents), proposals): everything else
it listed now lives in the items that hold it, the qualities, features and capabilities of the design spec. Only the
two below are left, deferred until they are designed; as the user said, "keep until designe[d]".

*Initiatives* enumerate what were once called proposals and priorities.
Each initiative represents an investment of effort towards a particular
external demo or product goal in terms of a set of CAP that must be 
(or have been) completed.

## INI-001 : agentic engineering strategy

## INI-002 : repository + dependency organization

## INI-003 : asset organization

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
- [CAP-244: mbse-programs' cross-repository links in the agreed forms](../docs/capabilities/README.md#CAP-244), and
  [CAP-245: mbse-programs' skill linking its notebook cases](../docs/capabilities/README.md#CAP-245): after mbse-programs' overhaul
- [CAP-246: mbse-codegen-python's tutorials](../docs/capabilities/README.md#CAP-246), then
  [CAP-247: mbse-codegen-python's skill linking its notebook cases](../docs/capabilities/README.md#CAP-247): after mbse-codegen-python's port
- [CAP-250: decision tags made readable](../docs/capabilities/README.md#CAP-250): not yet scheduled

## INI-010 : schemas framework

## INI-011 : object + relation + pattern framework

Charter: [mbse-patterns afresh](https://github.com/pitaman71/mbse-patterns/blob/main/docs/proposals/rescope/README.md). Patterns over data ([FEA-023: patterns over data](../docs/features/FEA-023.md)), in mbse-patterns 0.10.0:

- [CAP-072: distributions linked to patterns](../docs/capabilities/CAP-072.md): not met there yet
- [CAP-042: data generated from constraints](../docs/capabilities/CAP-042.md): not met there yet; rejecting a draw by its `requires` is
  blocked on [CAP-142: expressions evaluated in queries](../docs/capabilities/CAP-142.md#blocked)
- [CAP-073: distributions fit from data](../docs/capabilities/CAP-073.md): not met

## INI-012 : domain + expression dialect framework

## INI-020 : code mutation framework

Charter: [mbse-transforms](https://github.com/pitaman71/mbse-transforms/blob/main/docs/proposals/charter/README.md). Transforms ([FEA-021: every generation ambiguity a parameter](../docs/features/FEA-021.md)), in mbse-transforms:

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

## INI-030 : no/low-code and apps framework

## INI-040 : diagrams framework

Proposal: [Diagrams](DIAGRAMS.md). Diagrams ([FEA-056: fungible diagramming keeps agents and humans in the loop](../docs/features/FEA-056.md)), in build order:

- [CAP-237: logical layout schemas](../docs/capabilities/CAP-237.md)
- [CAP-238: container schemas and grid insertion](../docs/capabilities/CAP-238.md)
- [CAP-239: grid adjacency](../docs/capabilities/CAP-239.md)
- [CAP-240: conflicting layout rules ignored and requeued](../docs/capabilities/CAP-240.md)
- [CAP-241: physical layout schemas](../docs/capabilities/README.md#CAP-241)
- [CAP-242: incremental physical placement](../docs/capabilities/README.md#CAP-242)
- [CAP-243: a diagram displayed from its mutation stream](../docs/capabilities/README.md#CAP-243)

## INI-080 : stabilize mbse-schemas and mbse-expressions

## INI-081 : stabilize Python codegen


## INI-100 : formalize, parameterize, and visualize HW and LLM architectures

Builds on [INI-040: diagrams framework](#ini-040--diagrams-framework).

## INI-101 : explore, optimize LLM accelerator architectures (demo version)

## INI-102 : Attention Chip

## INI-103 : Tensor Parallelism with distributed K-V cache

## Later

- object properties as financial/scientific/engineering ([FEA-007: property kinds](../docs/features/FEA-007.md))
