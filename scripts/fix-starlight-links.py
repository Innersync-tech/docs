#!/usr/bin/env python3
"""Rewrite internal markdown links to correct Starlight relative URLs."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from starlight_links import ROOT, resolve_target_file, to_relative_link

LINK_RE = re.compile(r"(\[[^\]]*\]\()([^)#]+)(\)?)")


def fix_links(text: str, source: Path) -> tuple[str, int]:
    changes = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal changes
        prefix, target, suffix = match.group(1), match.group(2), match.group(3)
        parsed = urlparse(target)
        if parsed.scheme in ("http", "https", "mailto") or target.startswith("#"):
            return match.group(0)

        anchor = ""
        if "#" in target:
            target_path, anchor = target.split("#", 1)
        else:
            target_path = target

        resolved = resolve_target_file(source, target_path)
        if resolved is None:
            return match.group(0)

        new_target = to_relative_link(source, resolved, anchor)
        if new_target != target:
            changes += 1
            return f"{prefix}{new_target}{suffix}"
        return match.group(0)

    return LINK_RE.sub(repl, text), changes


def main() -> int:
    total = 0
    for md in sorted(ROOT.rglob("*.md")):
        original = md.read_text(encoding="utf-8")
        updated, count = fix_links(original, md)
        if count:
            md.write_text(updated, encoding="utf-8")
            print(f"{md.relative_to(ROOT)}: {count} link(s)")
            total += count

    if total:
        print(f"Updated {total} internal link(s).")
    else:
        print("All internal links already use Starlight URL paths.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
