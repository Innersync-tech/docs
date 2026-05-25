# Publication policy — docs.innersync.tech

This repository is **automatically built and published** on every push to `main`. Treat all files under `src/content/docs/` as public.

## Never publish here

- SQL migrations, table/column dumps, or connection strings (Core/App — use product repos + META privately)
- Contributor runbooks, tester plans, rollout runbooks, or “manual insert” SQL with real IDs
- Env matrices with secret values, Railway project tokens, webhook secrets, or service role keys
- Workspace META paths as operational instructions for end users

## Sync sources

| Source repo | Target folder | Mode |
|-------------|---------------|------|
| `Innersync_Core` | `core/` | **Allowlist** — only `index.md`, `innersync-id.md`, `telemetry/**` |
| `alphapy` | `alphapy/` | **Rsync + denylist** — excludes internal filenames (see workflows) |

Legal pages under `legal/` are **canonical in this repo** (not overwritten by Alphapy sync).

## CI guard

Workflows run `scripts/verify-publication-safe.sh` after sync and before push. It blocks Discord snowflakes, credential-like URLs, and forbidden filenames.

## Adding docs in product repos

- **Core:** edit allowlisted files under `Innersync_Core/docs/` only.
- **Alphapy:** put public docs in `alphapy/docs/`; mark internal files with a sibling `*.md` name listed in workflow excludes, or move them outside `docs/`.
