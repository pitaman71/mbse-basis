<!-- nav -->
[← Qualities](../QUALITIES.md) · [Home](../README.md) · [Capabilities →](../capabilities/README.md)

# Features

The second tier of the design spec: a cohesive, focused category of utility a persona values, what problems the
product solves for that persona, not how. Each feature is **external**, serving a user persona, or **internal**,
serving an engineering persona; it confers qualities, and its capabilities say how far it is met. A feature may be
adopted before it is met. Features may overlap on purpose.

## Index

### Modeling

- <a id="FEA-008"></a>**FEA-008** · adopted · external · Program models have sufficient expressive power to concisely
  and precisely represent source code in its native and idiomatic form. *Confers* QUA-004.
- <a id="FEA-009"></a>**FEA-009** · adopted · external · Interaction models can model layered abstractions of
  functional behavior. *Confers* QUA-004.
- <a id="FEA-010"></a>**FEA-010** · adopted · external · Interaction models are a suitable representation of
  system-level behavior. *Confers* QUA-007.
- <a id="FEA-011"></a>**FEA-011** · adopted · external · Interaction models are a suitable representation of hardware
  behavior, firmware behavior, as well as interfaces and interactions between them. *Confers* QUA-007.
- <a id="FEA-012"></a>**FEA-012** · adopted · external · Interaction models are a suitable representation of firmware
  behavior, software behavior, device behavior, as well as interfaces and interactions between them. *Confers*
  QUA-007.
- <a id="FEA-013"></a>**FEA-013** · adopted · external · Interaction models are a suitable representation of device
  behavior, user behavior, cloud resource behavior, agent behavior, as well as interfaces and interactions between
  them. *Confers* QUA-007.
- <a id="FEA-014"></a>**FEA-014** · adopted · external · Interaction models are a suitable representation of device
  behavior. *Confers* QUA-007.
- <a id="FEA-015"></a>**FEA-015** · adopted · external · Interaction models are a suitable representation of user
  behavior. *Confers* QUA-007.
- <a id="FEA-016"></a>**FEA-016** · adopted · external · Interaction models are a suitable representation of community
  behavior. *Confers* QUA-007.
- <a id="FEA-017"></a>**FEA-017** · adopted · external · AI stays in the loop (with humans) via the model trace.
  *Confers* QUA-001.
- <a id="FEA-018"></a>**FEA-018** · adopted · external · Humans stay in the loop (with AI) via the model trace.
  *Confers* QUA-001.
- <a id="FEA-019"></a>**FEA-019** · proposed · external · Every model and every operation on it means the same in every
  implementation language: Python and TypeScript give the same results, errors and wire format. *Confers* QUA-006.
- <a id="FEA-020"></a>**FEA-020** · adopted · external · All models allow refinements to be added, closing details in
  a targeted and agile manner. *Confers* QUA-002.

### Schema-driven visualization and editing

An index site for any mbse app, driven by its schemas. Each feature's detail file holds its capabilities'
specifications.

- <a id="FEA-001"></a>**FEA-001** · adopted · external · Schema-driven UI: services and UI present an app driven by its
  schemas, extended by schema-aware code only where wanted. *Confers* QUA-008. [Detail](FEA-001.md)
- <a id="FEA-003"></a>**FEA-003** · adopted · external · No-code logical views: query formats the backend serves as
  mutation expressions, requested alone or nested in one response. *Confers* QUA-008. [Detail](FEA-003.md)
- <a id="FEA-004"></a>**FEA-004** · adopted · external · Index site browser views: browsing schemas, objects and
  relation entries as lists of chips. *Confers* QUA-008. [Detail](FEA-004.md)
- <a id="FEA-005"></a>**FEA-005** · adopted · external · Inspector views: inspecting, navigating among and editing
  objects, adjacencies and relations from any view. *Confers* QUA-008. [Detail](FEA-005.md)
- <a id="FEA-006"></a>**FEA-006** · adopted · external · Persistence: an app's store outlives its service. *Confers*
  QUA-008. [Detail](FEA-006.md)
- <a id="FEA-007"></a>**FEA-007** · adopted · external · Property kinds: each property is shown and edited as its kind
  calls for, with who wrote it and when. *Confers* QUA-008. [Detail](FEA-007.md)

## Not yet planned

Features without an ID are not in plan yet. Their notes are in [features/UNPLANNED.md](UNPLANNED.md): no-code
secure services, search-sort-filter, view paging, hybrid search, tenancy, agent chat integration, and constraint
enforcement replacing bespoke workarounds.

## Earlier IDs

| Earlier | Now |
|---|---|
| F-001 | FEA-017, and QUA-001 |
| F-002 | FEA-018, and QUA-001 |
| F-003 | QUA-005 |
| F-004 | QUA-003 |
| F-005 | QUA-002, PRI-020 |
| F-006 | FEA-020 |
| F-007 | QUA-002, PRI-021 |
| F-008 to F-016 | FEA-008 to FEA-016 |

FEA-001 and FEA-003 to FEA-007 kept the IDs they had in the workspace's `VISUALIZATION.md`. FEA-002 is unassigned:
the work tracker's seed data uses it as an example ID.

## Open items

- **QUA-002 is not met in shape.** mbse-schemas' decoding refuses an undeclared key, where PRI-002 preserves it; its
  `docs/OPEN_WORLD.md` proposes preserving (Undeclared properties, policy 3) but keeps closed as the default, which
  QUA-002's "by default" contradicts. Name resolution staying closed (OPEN_WORLD.md, Decided) is consistent with
  QUA-002: names resolve or are refused, while data is kept.
- **No internal feature exists yet.** Pure tech debt is to become capabilities of internal features; the logs it sits
  in today are drained in a later batch.

---

<!-- nav -->
[← Qualities](../QUALITIES.md) · [Home](../README.md) · [Capabilities →](../capabilities/README.md)
