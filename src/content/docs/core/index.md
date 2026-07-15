---
title: Core Documentation
description: Innersync Core control plane — web surface, Core API, identity, and telemetry ingress.
---

Innersync Core is the platform control plane: marketing site, Core API, identity broker, and telemetry ingress.

## What Core is

See the [Innersync Core repository](https://github.com/Innersync-tech/Innersync_Core) for the codebase. App, Alphapy, and Mind are separate products; Core routes shared identity, webhooks, billing hooks, and telemetry.

**Public system status:** [mind.innersync.tech/status](https://mind.innersync.tech/status) (hosted on Mind, not Core web).

## Documentation

| Topic | Description |
|-------|-------------|
| [Innersync ID](./innersync-id.md) | Shared user profile and Discord link (API surface) |
| [Telemetry data flow](./telemetry/DATA_FLOW.md) | How metrics reach Mind (no SQL) |

## Publication policy

Docs on [docs.innersync.tech](https://docs.innersync.tech) intentionally **omit**:

- Database schemas, migration SQL, and table/column listings
- Connection strings, service keys, and full env matrices
- Internal architecture runbooks and dual-database layout details

SQL migrations and contributor runbooks are **not** on the public docs site. Bot database schema is documented in the [alphapy](https://github.com/Innersync-tech/alphapy) GitHub repository (separate from this site).
