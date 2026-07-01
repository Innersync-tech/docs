#!/usr/bin/env python3
"""Check internal markdown links resolve and use correct Starlight URL paths."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from starlight_links import ROOT, resolve_target_file, to_relative_link

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def main() -> int:
    broken: list[tuple[Path, str, str]] = []

    for md in sorted(ROOT.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            raw = match.group(1)
            parsed = urlparse(raw)
            if parsed.scheme in ("http", "https", "mailto") or raw.startswith("#"):
                continue

            path_part = raw.split("#", 1)[0]
            anchor = raw.split("#", 1)[1] if "#" in raw else ""

            if path_part.endswith(".md"):
                broken.append((md, raw, "use Starlight URL without .md"))
                continue

            resolved = resolve_target_file(md, path_part)
            if resolved is None:
                broken.append((md, raw, "target not found"))
                continue

            expected = to_relative_link(md, resolved, anchor)
            if expected != raw:
                broken.append((md, raw, f"expected {expected}"))

    if broken:
        print(f"Broken internal links ({len(broken)}):")
        for src, raw, reason in broken:
            print(f"  {src.relative_to(ROOT)}: ({raw}) — {reason}")
        return 1

    print("All internal markdown links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
