<!-- nav -->
[← The mbse basis](README.md) · [Home](README.md) · [Principles →](PRINCIPLES.md)

# Features

Qualitative objectives that hold across the project and stay relatively stable throughout its lifecycle. A feature
may be adopted before it is met; its capabilities say how far it is met. The features are a specification: each is a
constraint, and the objective is their conjunction, so features may overlap on purpose.

## Index

- **F-001** · adopted · AI is always in the loop.
- **F-002** · adopted · Humans are always in the loop.
- **F-003** · adopted · The MBSE project invents a modeling paradigm, constructs and a framework, and does so in an
  opinionated manner.
- **F-004** · adopted · The MBSE project avoids second-order inventions, things that can be modeled and invented
  elsewhere, such as a neutral expression language or datatypes. *Relates to* P-012.
  *Applied in*: mbse-expressions' Basic dialect, a neutral expression language, is being removed for this reason, and
  datatypes are to be ISO/IEC 11404's (V-020, C-002 L5).
- **F-005** · adopted · All models are open-world by default, assuming entropy and/or nondeterminism for any aspect not
  otherwise specified. *Relates to* P-002, P-007.
- **F-006** · adopted · All models allow refinements to be added, closing details in a targeted and agile manner.
- **F-007** · adopted · Individual model refinements are descriptive in nature; it takes a collection of applied
  refinements to represent a prescription.
- **F-008** · adopted · Program models have sufficient expressive power to concisely and precisely represent source
  code in its native and idiomatic form.
- **F-009** · adopted · Interaction models can model layered abstractions of functional behavior.
- **F-010** · adopted · Interaction models are a suitable representation of system-level behavior.
- **F-011** · adopted · Interaction models are a suitable representation of hardware behavior, firmware behavior, as
  well as interfaces and interactions between them.
- **F-012** · adopted · Interaction models are a suitable representation of firmware behavior, software behavior,
  device behavior, as well as interfaces and interactions between them.
- **F-013** · adopted · Interaction models are a suitable representation of device behavior, user behavior, cloud
  resource behavior, agent behavior, as well as interfaces and interactions between them.
- **F-014** · adopted · Interaction models are a suitable representation of device behavior.
- **F-015** · adopted · Interaction models are a suitable representation of user behavior.
- **F-016** · adopted · Interaction models are a suitable representation of community behavior.

## Open items

- **F-005 is not met in shape on main.** mbse-schemas' decoding there refuses an undeclared key, where P-002 preserves
  it; the `scalars` branch preserves it (C-002 L2), not yet landed. Name resolution staying closed is consistent with
  F-005: names resolve or are refused, while data is kept.
- **No feature covers equivalence across languages.** C-001, equivalent Python and TypeScript implementations, is the
  most enforced capability in the project and implements no feature above. Proposed: a feature that every model and
  every operation on it means the same in every implementation language.

---

<!-- nav -->
[← The mbse basis](README.md) · [Home](README.md) · [Principles →](PRINCIPLES.md)
