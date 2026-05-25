#!/usr/bin/env bash
# Starlight docsSchema requires YAML frontmatter with title on every markdown page.
set -euo pipefail

ROOT="${1:-src/content/docs}"
missing=0

while IFS= read -r -d '' f; do
  if ! head -1 "$f" | grep -q '^---$'; then
    echo "::error::Missing Starlight frontmatter (---): ${f#"$ROOT"/}"
    missing=$((missing + 1))
  fi
done < <(find "$ROOT" -type f -name '*.md' -print0)

if [ "$missing" -gt 0 ]; then
  echo "Add --- title/description --- frontmatter (see PUBLICATION-POLICY.md)."
  exit 1
fi

echo "Starlight frontmatter check passed for $ROOT"
