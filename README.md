# Innersync Documentation Hub

Central documentation for all Innersync services.

This repository is powered by **Astro** with **Starlight**.
Documentation source files live in `src/content/docs/`.

## Publication policy

**docs.innersync.tech** publishes product-level documentation only. It intentionally **does not** include:

- Database schemas, migration SQL, or table/column catalogs (except **Alphapy**, synced from the public [alphapy](https://github.com/Innersync-tech/alphapy) repo)
- Connection strings, service keys, or full internal env matrices
- Cross-repo data-store diagrams with internal table names

Contributors: clone the relevant product repository for SQL (`docs/sql/`, `supabase/`) and `.env.example`.

## Local development

```bash
npm install
npm run dev
```

The site runs at `http://localhost:4321`.

## Services

- [Alphapy](src/content/docs/alphapy/) — Discord bot for the Innersync • Alphapips community
- [App](src/content/docs/app/) — Dashboard and web interface *(coming soon)*
- [Core](src/content/docs/core/) — Core API and backend services *(coming soon)*

## Legal

- [Legal Information](src/content/docs/legal/legal.md) — Company details, enterprise number, registered office
- [Pricing](src/content/docs/legal/pricing.md)
- [Terms of Service](src/content/docs/legal/terms-of-service.md)
- [Privacy Policy](src/content/docs/legal/privacy-policy.md)

---

Questions? Reach out via `support@innersync.tech` or open an issue on GitHub.
