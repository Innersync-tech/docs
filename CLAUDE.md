# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is an Astro-based static documentation site for Innersync services, using **Starlight** and hosted at **docs.innersync.tech** via GitHub Pages.

## Local Development

To preview locally:

```bash
npm install
npm run dev
```

The site runs at `http://localhost:4321`.

## Site Configuration

- `astro.config.mjs` — Astro + Starlight site configuration
- `package.json` — Node dependencies and scripts for local/dev and CI builds
- `CNAME` — custom domain (`docs.innersync.tech`)

Navigation is content-driven from `src/content/docs/` (Starlight auto sidebar), not a hand-maintained sidebar map in `astro.config.mjs`.

## Content Structure

```
src/content/docs/alphapy/   — Discord bot documentation (synced from bryntje/alphapy)
src/content/docs/app/       — App docs (placeholder, coming soon)
src/content/docs/core/      — Core API docs (placeholder, coming soon)
src/content/docs/legal/     — Legal documents (terms, privacy, pricing) — NOT synced from Alphapy
```

## Automated Sync

Primary sync is triggered from the Alphapy repository workflow (`alphapy/.github/workflows/sync-docs-to-docs-repo.yml`), which syncs `alphapy/docs/` into `docs/src/content/docs/alphapy/`, excluding legal files (`terms-of-service.md`, `privacy-policy.md`, `pricing.md`, `legal.md`).

`.github/workflows/sync-from-alphapy.yml` in this repo is a manual fallback workflow (workflow_dispatch) for one-off resync jobs.

`.github/workflows/deploy-starlight.yml` builds the site with Astro/Starlight and deploys it to GitHub Pages.

Legal documents in `src/content/docs/legal/` are canonical and maintained directly in this repo.

## Adding Documentation

- New service sections follow the same pattern as `src/content/docs/alphapy/` — a directory with an `index.md` and individual topic files.
- Keep page titles as regular Markdown headings (`# ...`) and organize navigation by placing files/folders under `src/content/docs/` (Starlight autogenerates sidebar structure).
- `src/content/docs/app/` and `src/content/docs/core/` are placeholder directories awaiting synced content.
