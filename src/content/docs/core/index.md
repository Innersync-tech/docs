---
title: Core Documentation
description: Innersync Core control plane — web surface, Core API, identity, and telemetry ingress.
---

# Core

Innersync Core is the platform control plane: marketing site, Core API, identity broker, and telemetry ingress. App, Alphapy, and Mind are separate products that connect through Core for shared identity, webhooks, billing hooks, and telemetry.

**System status:** [mind.innersync.tech/status](https://mind.innersync.tech/status) (hosted on Mind).

Source code: [Innersync_Core on GitHub](https://github.com/Innersync-tech/Innersync_Core).

## Topics

| Topic | Description |
|-------|-------------|
| [Innersync ID](innersync-id/) | Shared user profile and Discord link API |
| [Telemetry data flow](telemetry/data_flow/) | How operational metrics reach Mind |

## What this site covers

Public docs focus on product behaviour and integration surfaces. They do not include SQL migrations, connection strings, service keys, or internal runbooks. Bot database schema is documented in the [Alphapy](../alphapy/database-schema/) section.
