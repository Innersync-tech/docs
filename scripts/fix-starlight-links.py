#!/usr/bin/env python3
"""Rewrite internal .md links to Starlight clean URLs (trailing slash, no .md)."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent / "src" / "content" / "docs"
LINK_RE = re.compile(r"(\[[^\]]*\]\()([^)#]+)(\)?)")
SKIP_SCHEMES = ("http://", "https://", "mailto:", "#")


def file_to_url_parts(md_file: Path) -> list[str]:
    rel = md_file.relative_to(ROOT)
    parts = list(rel.parent.parts)
    stem = rel.stem
    if stem.lower() != "index":
        parts.append(stem.lower())
    return [part.lower() for part in parts]


def to_relative_link(source: Path, target_file: Path, anchor: str = "") -> str:
    source_parts = list(source.parent.relative_to(ROOT).parts)
    target_parts = file_to_url_parts(target_file)

    common = 0
    for left, right in zip(source_parts, target_parts):
        if left.lower() == right.lower():
            common += 1
        else:
            break

    rel_parts = [".."] * (len(source_parts) - common) + target_parts[common:]
    if not rel_parts:
        link = "./"
    else:
        link = "/".join(rel_parts) + "/"
    if anchor:
        link += f"#{anchor}"
    return link


def resolve_target(source: Path, raw: str) -> Path | None:
    target = unquote(raw.strip())
    if not target or target.startswith(SKIP_SCHEMES):
        return None
    if target.startswith("/"):
        path = ROOT / target.lstrip("/")
    else:
        path = (source.parent / target.split("#", 1)[0]).resolve()
    if "#" in target:
        path = Path(str(path).split("#", 1)[0])
    return path


def fix_links(text: str, source: Path) -> tuple[str, int]:
    changes = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal changes
        prefix, target, suffix = match.group(1), match.group(2), match.group(3)
        parsed = urlparse(target)
        if parsed.scheme in ("http", "https", "mailto") or target.startswith("#"):
            return match.group(0)
        if not target.endswith(".md"):
            return match.group(0)

        anchor = ""
        if "#" in target:
            target_path, anchor = target.split("#", 1)
        else:
            target_path = target

        resolved = resolve_target(source, target_path)
        if resolved is None or not resolved.exists():
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
        return 0

    print("No .md internal links to fix.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
