"""Shared helpers for Starlight doc link paths (URL slugs, not repo dirs)."""
from __future__ import annotations

from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent / "src" / "content" / "docs"
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")


def file_to_url_parts(md_file: Path) -> list[str]:
    rel = md_file.relative_to(ROOT)
    parts = list(rel.parent.parts)
    stem = rel.stem
    if stem.lower() != "index":
        parts.append(stem.lower())
    return [part.lower() for part in parts]


def file_from_url_parts(parts: list[str]) -> Path | None:
    if not parts:
        index = ROOT / "index.md"
        return index if index.exists() else None

    parent = ROOT
    for part in parts[:-1]:
        parent = parent / part

    slug = parts[-1]
    direct = parent / f"{slug}.md"
    if direct.exists():
        return direct

    nested_index = parent / slug / "index.md"
    if nested_index.exists():
        return nested_index

    if parent.exists():
        for child in parent.iterdir():
            if child.is_file() and child.suffix == ".md" and child.stem.lower() == slug:
                return child

    return None


def resolve_url_parts(source: Path, raw: str) -> list[str] | None:
    path_part = unquote(raw.split("#", 1)[0].strip())
    if not path_part:
        return None

    if path_part.startswith("/"):
        segments = [part.lower() for part in path_part.strip("/").split("/") if part]
        return segments

    base = file_to_url_parts(source)
    resolved = list(base)
    for segment in path_part.split("/"):
        if segment in ("", "."):
            continue
        if segment == "..":
            if not resolved:
                return None
            resolved.pop()
            continue
        resolved.append(segment.lower())
    return resolved


def to_relative_link(source: Path, target_file: Path, anchor: str = "") -> str:
    source_parts = file_to_url_parts(source)
    target_parts = file_to_url_parts(target_file)

    common = 0
    for left, right in zip(source_parts, target_parts):
        if left == right:
            common += 1
        else:
            break

    rel_parts = [".."] * (len(source_parts) - common) + target_parts[common:]
    link = "./" if not rel_parts else "/".join(rel_parts) + "/"
    if anchor:
        link += f"#{anchor}"
    return link


def resolve_target_file(source: Path, raw: str) -> Path | None:
    target = unquote(raw.strip())
    if not target or target.startswith(SKIP_PREFIXES):
        return None

    parts = resolve_url_parts(source, target)
    if parts is not None:
        found = file_from_url_parts(parts)
        if found:
            return found

    # Bare slugs like `configuration/` are siblings under the current URL parent.
    path_part = target.split("#", 1)[0].strip()
    if (
        path_part
        and not path_part.startswith("/")
        and not path_part.startswith(".")
        and ".." not in path_part
    ):
        slug = path_part.strip("/").lower()
        parent_parts = file_to_url_parts(source)[:-1]
        return file_from_url_parts(parent_parts + [slug])

    return None
