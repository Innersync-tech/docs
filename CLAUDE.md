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

- `astro.config.mjs` — Astro + Starlight site configuration and sidebar structure
- `package.json` — Node dependencies and scripts for local/dev and CI builds
- `CNAME` — custom domain (`docs.innersync.tech`)

## Content Structure

```
src/content/docs/alphapy/   — Discord bot documentation (synced from bryntje/alphapy)
src/content/docs/app/       — App docs (placeholder, coming soon)
src/content/docs/core/      — Core API docs (placeholder, coming soon)
src/content/docs/legal/     — Legal documents (terms, privacy, pricing) — NOT synced from Alphapy
```

## Automated Sync

`.github/workflows/sync-from-alphapy.yml` watches pushes to `bryntje/alphapy` and syncs `alphapy/docs/` into `src/content/docs/alphapy/` here, excluding legal files. It requires a `DOCS_SYNC_TOKEN` secret with repo write access.

`.github/workflows/deploy-starlight.yml` builds the site with Astro/Starlight and deploys it to GitHub Pages.

Legal documents (`src/content/docs/legal/`) are maintained directly in this repo and excluded from the sync.

## Adding Documentation

- New service sections follow the same pattern as `src/content/docs/alphapy/` — a directory with an `index.md` and individual topic files.
- Keep page titles as regular Markdown headings (`# ...`) and manage navigation in `astro.config.mjs`.
- `src/content/docs/app/` and `src/content/docs/core/` are placeholder directories awaiting synced content.
