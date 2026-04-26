# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Jekyll-based static documentation site for Innersync services, hosted at **docs.innersync.tech** via GitHub Pages. It is a pure documentation repository — no application code, no build tooling, no package manager.

## Local Development

Jekyll is the only dependency. To preview locally:

```bash
gem install jekyll bundler   # if not already installed
jekyll serve
```

The site runs at `http://localhost:4000`.

## Site Configuration

- `_config.yml` — Jekyll config (title, theme: minima, markdown: kramdown)
- `CNAME` — custom domain (`docs.innersync.tech`)

## Content Structure

```
alphapy/   — Discord bot documentation (synced from bryntje/alphapy)
core/      — Core API docs (placeholder, coming soon)
mind/      — Dashboard docs (placeholder, coming soon)
legal/     — Legal documents (terms, privacy, pricing) — NOT synced from Alphapy
```

## Automated Sync

`.github/workflows/sync-from-alphapy.yml` watches pushes to `bryntje/alphapy` and syncs `alphapy/docs/` into `alphapy/` here, excluding legal files. It requires a `DOCS_SYNC_TOKEN` secret with repo write access.

Legal documents (`legal/`) are maintained directly in this repo and excluded from the sync.

## Adding Documentation

- New service sections follow the same pattern as `alphapy/` — a directory with an `index.md` and individual topic files.
- All pages use standard Jekyll Markdown with optional YAML frontmatter.
- `core/` and `mind/` are placeholder directories awaiting content.
