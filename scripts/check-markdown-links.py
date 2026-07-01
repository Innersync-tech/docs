#!/usr/bin/env python3
"""Check relative markdown links under src/content/docs resolve to files."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent / "src" / "content" / "docs"
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SKIP_SCHEMES = ("http://", "https://", "mailto:", "#")


def resolve_link(source: Path, target: str) -> Path | None:
    target = unquote(target.strip())
    if not target or target.startswith(SKIP_SCHEMES):
        return None
    if target.startswith("/"):
        path = ROOT / target.lstrip("/")
    else:
        path = (source.parent / target).resolve()
    path = path.split("#")[0] if isinstance(path, str) else path
    if "#" in target and not target.startswith("/"):
        path = (source.parent / target.split("#", 1)[0]).resolve()
    elif "#" in target and target.startswith("/"):
        path = (ROOT / target.lstrip("/").split("#", 1)[0]).resolve()
    return path


def candidate_paths(path: Path) -> list[Path]:
    if path.suffix == ".md":
        return [path]
    return [
        path,
        path.with_suffix(".md"),
        path / "index.md",
    ]


def main() -> int:
    broken: list[tuple[Path, str, Path]] = []
    for md in sorted(ROOT.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            raw = match.group(1)
            parsed = urlparse(raw)
            if parsed.scheme in ("http", "https", "mailto") or raw.startswith("#"):
                continue
            target_path = resolve_link(md, raw)
            if target_path is None:
                continue
            if not any(p.exists() for p in candidate_paths(target_path)):
                broken.append((md, raw, target_path))

    if broken:
        print(f"Broken relative links ({len(broken)}):")
        for src, raw, resolved in broken:
            rel = src.relative_to(ROOT)
            print(f"  {rel}: ({raw}) -> {resolved}")
        return 1

    print("All relative markdown links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
