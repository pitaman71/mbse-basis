<!-- nav -->
[← Principles](PRINCIPLES.md) · [Home](../README.md) · [The mbse basis →](README.md)

# Qualities

The first tier of the design spec: how a persona, human or agent, instinctively assesses the product's value, against
a rubric that seems natural to them. A quality says neither what the product does nor how. Features confer qualities;
principles serve them.

## Index

- <a id="QUA-001"></a>**QUA-001: AI and humans in the loop** · adopted · AI and humans are always in the loop at every step. *Conferred by*
  [FEA-017: AI in the loop via the model trace](features/README.md#FEA-017), [FEA-018: humans in the loop via the model trace](features/README.md#FEA-018),
  [FEA-021: every generation ambiguity a parameter](features/FEA-021.md), [FEA-026: deterministic object identity](features/FEA-026.md), [FEA-030: transactions](features/FEA-030.md).
- <a id="QUA-002"></a>**QUA-002: open-world models** · adopted · Models are open-world by default, allowing incremental addition of detail
  that transits from descriptive to prescriptive. *Conferred by* [FEA-020: refinable models](features/README.md#FEA-020),
  [FEA-023: patterns over data](features/FEA-023.md).
- <a id="QUA-003"></a>**QUA-003: no second-order inventions** · adopted · The project avoids second-order inventions ([VOC-027: second-order invention](VOCABULARY.md#VOC-027)).
- <a id="QUA-004"></a>**QUA-004: models as an alternative representation of source code** · adopted · Models are a concise, precise, comprehensive and neutral alternative
  representation for source code. *Conferred by* [FEA-008: expressive program models](features/README.md#FEA-008), [FEA-009: layered interaction models](features/README.md#FEA-009),
  [FEA-022: code generation](features/README.md#FEA-022).
- <a id="QUA-005"></a>**QUA-005: an opinionated paradigm** · adopted · The project invents a modeling paradigm, constructs and a framework, and
  does so in an opinionated manner.
- <a id="QUA-006"></a>**QUA-006: the same in every language** · proposed · A model means the same, and every operation on it gives the same result,
  in every implementation language. *Conferred by* [FEA-019: equivalent implementations](features/README.md#FEA-019), [FEA-032: schema loading and wire alignment](features/FEA-032.md), [FEA-036: serialization behavior is consistent across bindings and generated source code](features/FEA-036.md).
- <a id="QUA-007"></a>**QUA-007: one paradigm at every level of a system** · proposed · One modeling paradigm represents a system at every level, from hardware
  to community, and the interfaces between levels. *Conferred by* [FEA-010: system behavior](features/README.md#FEA-010) to [FEA-016: community behavior](features/README.md#FEA-016), and [FEA-037: the framework built on its own protocols](features/FEA-037.md).
- <a id="QUA-008"></a>**QUA-008: usable without code** · proposed · Any model is usable without code written for it: browsed, inspected,
  edited and persisted from its schemas alone. *Conferred by* [FEA-001: schema-driven UI](features/FEA-001.md), [FEA-003: no-code logical views](features/FEA-003.md) to [FEA-007: property kinds](features/FEA-007.md),
  [FEA-025: serialization behavior conventions in schema](features/FEA-025.md), [FEA-027: mutations as queries](features/FEA-027.md), [FEA-028: one API surface for all data access](features/FEA-028.md), [FEA-029: excluding imperative visitor expressions](features/FEA-029.md), [FEA-034: analytic behavior conventions in schema](features/FEA-034.md), [FEA-031: schemas as extensible data](features/FEA-031.md), [FEA-033: model parameters](features/FEA-033.md).
- <a id="QUA-009"></a>**QUA-009: modeling provides clean separation of applications across constructs** · proposed · Each
  modeling construct has one clean application, so that what a model means does not depend on how a construct is
  stretched to serve another's. *Conferred by* [FEA-035: clean modeling separation between value objects and reference objects](features/FEA-035.md).

## Earlier IDs

[QUA-001: AI and humans in the loop](#QUA-001) to [QUA-005: an opinionated paradigm](#QUA-005) restate features of the first draft, which moved here:

| Earlier | Now |
|---|---|
| F-001, F-002 | [QUA-001: AI and humans in the loop](#QUA-001), with [FEA-017: AI in the loop via the model trace](features/README.md#FEA-017) and [FEA-018: humans in the loop via the model trace](features/README.md#FEA-018) |
| F-003 | [QUA-005: an opinionated paradigm](#QUA-005) |
| F-004 | [QUA-003: no second-order inventions](#QUA-003) |
| F-005, F-007 | [QUA-002: open-world models](#QUA-002), with [PRI-020: no constraint, any configuration](PRINCIPLES.md#PRI-020) and [PRI-021: refinement by constraint](PRINCIPLES.md#PRI-021) |

## Open items

- **[QUA-005: an opinionated paradigm](#QUA-005)'s tier.** F-003 moved here by an agent's reading, not by the examples that set the tiers; confirm it is
  a quality rather than a principle.
- **No quality an engineering persona values** exists yet, so the conventions among the principles ([PRI-011: the lowest repository that can own it](PRINCIPLES.md#PRI-011), [PRI-016: guidance written once](PRINCIPLES.md#PRI-016))
  serve nothing in that tier; see Principles, open items.

---

<!-- nav -->
[← Principles](PRINCIPLES.md) · [Home](../README.md) · [The mbse basis →](README.md)
