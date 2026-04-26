# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is an MkDocs-based static documentation site for Innersync services, using **Material for MkDocs** and hosted at **docs.innersync.tech** via GitHub Pages.

## Local Development

To preview locally:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

The site runs at `http://127.0.0.1:8000`.

## Site Configuration

- `mkdocs.yml` — MkDocs + Material site configuration, navigation, and theme options
- `requirements.txt` — Python dependencies for local/dev and CI builds
- `CNAME` — custom domain (`docs.innersync.tech`)

## Content Structure

```
docs/alphapy/   — Discord bot documentation (synced from bryntje/alphapy)
docs/app/       — App docs (placeholder, coming soon)
docs/core/      — Core API docs (placeholder, coming soon)
docs/legal/     — Legal documents (terms, privacy, pricing) — NOT synced from Alphapy
```

## Automated Sync

`.github/workflows/sync-from-alphapy.yml` watches pushes to `bryntje/alphapy` and syncs `alphapy/docs/` into `docs/alphapy/` here, excluding legal files. It requires a `DOCS_SYNC_TOKEN` secret with repo write access.

`.github/workflows/deploy-mkdocs.yml` builds the site with MkDocs and deploys it to GitHub Pages.

Legal documents (`legal/`) are maintained directly in this repo and excluded from the sync.

## Adding Documentation

- New service sections follow the same pattern as `docs/alphapy/` — a directory with an `index.md` and individual topic files.
- Keep page titles as regular Markdown headings (`# ...`) and manage navigation in `mkdocs.yml`.
- `app/` and `core/` are placeholder directories awaiting synced content.
