# Innersync Documentation Hub

**Live site:** [docs.innersync.tech](https://docs.innersync.tech) — built with **Astro + Starlight** (dark theme, search, sidebar).

This README is for **contributors on GitHub**. Source files live in `src/content/docs/`; public URLs omit that path (e.g. `/alphapy/`, not `/src/content/docs/alphapy/`).

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

- [Alphapy](https://docs.innersync.tech/alphapy/) — Discord bot for the Innersync • Alphapips community
- [App](https://docs.innersync.tech/app/) — Dashboard and web interface *(coming soon)*
- [Core](https://docs.innersync.tech/core/) — Core API and backend services *(coming soon)*

## Legal

- [Legal Information](https://docs.innersync.tech/legal/legal/) — Company details, enterprise number, registered office
- [Pricing](https://docs.innersync.tech/legal/pricing/)
- [Terms of Service](https://docs.innersync.tech/legal/terms-of-service/)
- [Privacy Policy](https://docs.innersync.tech/legal/privacy-policy/)

---

Questions? Reach out via `support@innersync.tech` or open an issue on GitHub.
