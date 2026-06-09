---
title: Innersync ID
description: Shared user profile, Core API surface, and Discord link flow.
---

**Innersync ID** is the shared user profile across App, Mind, Core API, and Alphapy. Authentication stays on **Supabase Auth**; Core exposes the canonical profile over HTTP.

## Concepts

- One platform user id (same as the Supabase Auth user id).
- **Global profile** — display name, avatar, cross-product preferences (via Core `GET|PATCH /users/me` or product-specific settings APIs).
- **Product settings** — App-only options (encryption, Grok, sharing) and Mind-only cockpit prefs live in separate settings layers, not in the global profile blob.
- **Discord link** — optional binding between Discord account and Innersync ID; started from Alphapy `/link`, completed in App.

## Core API (public surface)

Authenticated with the user’s Supabase JWT unless noted.

| Endpoint | Purpose |
|----------|---------|
| `GET /users/me` | Read profile (row created on first access) |
| `PATCH /users/me` | Update display name, avatar, preferences |

Discord link (service-to-service + user completion):

| Endpoint | Auth | Purpose |
|----------|------|---------|
| `POST /integrations/discord/link-session` | Service API key | Start link; returns App completion URL |
| `GET /integrations/discord/bot-profile` | Service API key | Resolve linked profile by Discord user id |
| `GET /integrations/discord/me` | User JWT | Discord link status for the signed-in user |
| `POST /integrations/discord/link-session/complete` | User JWT | Finish link after App OAuth |
| `DELETE /integrations/discord/link` | User JWT | Unlink Discord (App settings) |
| `POST /integrations/discord/unlink` | Service API key | Unlink by Discord snowflake (Alphapy `/unlink`) |

After link complete or unlink, Core writes Supabase `innersync_discord_links` and notifies Alphapy via HMAC webhook (`event`: `link` or `unlink`) so Railway `alphapy_discord_links` stays in sync.

App completion route: `/dashboard/settings/integrations/link?token=…` (proxies to Core).

## App integration

When `CORE_BASE_URL` is set, the dashboard may use Core for `/users/me`; otherwise it uses the shared Supabase profile layer with the user session.

## For maintainers

Database migrations and production env configuration are not published on the public docs site. Use private team onboarding materials.
