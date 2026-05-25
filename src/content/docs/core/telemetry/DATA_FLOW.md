---
title: Telemetry data flow
description: How subsystem metrics reach Mind and the public status page.
---

How subsystem health reaches the **Mind** dashboard and the [public status page](https://mind.innersync.tech/status).

## Overview

```text
Core web / Core API / Alphapy / App  →  ingest  →  shared telemetry store  →  Mind
```

Mind reads the latest subsystem snapshots from the shared store. If data is missing or stale, Mind falls back to live metrics endpoints (Core API, then Alphapy), then a safe skeleton response.

## Who writes data

| Source | When |
|--------|------|
| Core API | On `GET /api/metrics` (persists snapshot) |
| Core web | Optional background ingest in production |
| Alphapy | Periodic push + Core ingress API |
| App | Telemetry API where configured |

Without regular writes, the public status page may show stale or empty history until the next successful ingest.

## Who reads data

| Consumer | Use |
|----------|-----|
| Mind `/dashboard` | Full metrics (authenticated) |
| Mind `/status` | Public component health + vendors |
| Core `/api/metrics` proxy | Sanitized JSON for monitors (not the status UI) |

## Keeping data fresh

1. Ensure each product's ingest path is enabled in production.
2. Optionally schedule HTTP calls to each service's metrics endpoint (e.g. every 30–60s).
3. Confirm Mind can read from the shared telemetry store (configured in each product's deploy environment).

## For maintainers

SQL schemas and connection strings are not published on the public docs site. Implementation and migrations stay in private contributor materials.
