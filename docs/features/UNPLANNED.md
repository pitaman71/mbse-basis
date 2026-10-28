<!-- nav -->
[← Features](README.md) · [Home](../README.md)

# Features not yet planned

Features and capabilities without an ID, not in plan yet. A planned feature's own unplanned capabilities are in its detail file.

## no-code secure services

Out of scope for now.

- schema revisions : <migration>.<revision>
- secure server setup with credentials provided in service ENV
- Docker ubuntu image build

## search-sort-filter

User can apply search, sort, and filter in browser views.
Initially these will be in-browser executed and very
simple. Keyword, semantic, and hybrid searches will evolve
over time. Logical views are the lens through which
searches operate.

### search-sort-filter browser exact prop match

- executed in browser
- target object only
- props in detail view only
- text match for entire property value

## view paging

## hybrid search

## tenancy

### local (for demos)

Each application instance is entirely private.

### private (intermediate)

- system requires login for any access
- security configurations via patterns shared and enforced across services 
  and UI
- sessions uid is allocated on login and renewed with login tokens
- user/agent identity is recorded in session log
- session identity is recorded with every transaction
- transaction request/response signatures recorded in session log

### sequestered

A single application instance can permit multiple users to login to the
same instance but not see one another's data in any way.

### read-sharing

Users can share data views with one another on a read-only basis.

### groups and topics

### projections and forms

## agent chat integration

### in-app AI chats over modeled data

- user can create an in-app AI chat session authenticated to the AI service and model of their choice
- user can chat with the AI agent
- user can browse and manage in-app chat sessions

## constraint enforcement replaces bespoke workarounds

### shared property handling by constraints

---

<!-- nav -->
[← Features](README.md) · [Home](../README.md)
