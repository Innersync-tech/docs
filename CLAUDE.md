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

<!-- gitnexus:start -->
# GitNexus — Code Intelligence

This project is indexed by GitNexus as **docs** (635 symbols, 674 relationships, 6 execution flows). Use the GitNexus MCP tools to understand code, assess impact, and navigate safely.

> Index stale? Run `node .gitnexus/run.cjs analyze` from the project root — it auto-selects an available runner. No `.gitnexus/run.cjs` yet? `npx gitnexus analyze` (npm 11 crash → `npm i -g gitnexus`; #1939).

## Always Do

- **MUST run impact analysis before editing any symbol.** Before modifying a function, class, or method, run `impact({target: "symbolName", direction: "upstream"})` and report the blast radius (direct callers, affected processes, risk level) to the user.
- **MUST run `detect_changes()` before committing** to verify your changes only affect expected symbols and execution flows. For regression review, compare against the default branch: `detect_changes({scope: "compare", base_ref: "main"})`.
- **MUST warn the user** if impact analysis returns HIGH or CRITICAL risk before proceeding with edits.
- When exploring unfamiliar code, use `query({search_query: "concept"})` to find execution flows instead of grepping. It returns process-grouped results ranked by relevance.
- When you need full context on a specific symbol — callers, callees, which execution flows it participates in — use `context({name: "symbolName"})`.
- For security review, `explain({target: "fileOrSymbol"})` lists taint findings (source→sink flows; needs `analyze --pdg`).

## Never Do

- NEVER edit a function, class, or method without first running `impact` on it.
- NEVER ignore HIGH or CRITICAL risk warnings from impact analysis.
- NEVER rename symbols with find-and-replace — use `rename` which understands the call graph.
- NEVER commit changes without running `detect_changes()` to check affected scope.

## Resources

| Resource | Use for |
|----------|---------|
| `gitnexus://repo/docs/context` | Codebase overview, check index freshness |
| `gitnexus://repo/docs/clusters` | All functional areas |
| `gitnexus://repo/docs/processes` | All execution flows |
| `gitnexus://repo/docs/process/{name}` | Step-by-step execution trace |

## CLI

| Task | Read this skill file |
|------|---------------------|
| Understand architecture / "How does X work?" | `.claude/skills/gitnexus/gitnexus-exploring/SKILL.md` |
| Blast radius / "What breaks if I change X?" | `.claude/skills/gitnexus/gitnexus-impact-analysis/SKILL.md` |
| Trace bugs / "Why is X failing?" | `.claude/skills/gitnexus/gitnexus-debugging/SKILL.md` |
| Rename / extract / split / refactor | `.claude/skills/gitnexus/gitnexus-refactoring/SKILL.md` |
| Tools, resources, schema reference | `.claude/skills/gitnexus/gitnexus-guide/SKILL.md` |
| Index, status, clean, wiki CLI commands | `.claude/skills/gitnexus/gitnexus-cli/SKILL.md` |

<!-- gitnexus:end -->
