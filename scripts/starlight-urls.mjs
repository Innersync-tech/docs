import { readdirSync, statSync } from 'node:fs';
import { join, relative, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const CONTENT_ROOT = join(fileURLToPath(new URL('.', import.meta.url)), '..', 'src', 'content', 'docs');

/** Public Starlight URL for a content file (trailing slash). */
export function fileToUrlPath(mdFile) {
  const rel = relative(CONTENT_ROOT, mdFile).split(sep).join('/');
  const parts = rel.replace(/\.md$/i, '').split('/');
  if (parts[parts.length - 1].toLowerCase() === 'index') {
    parts.pop();
  } else {
    parts[parts.length - 1] = parts[parts.length - 1].toLowerCase();
  }
  if (parts.length === 0) {
    return '/';
  }
  return `/${parts.join('/')}/`;
}

/** Repo-style /path/to/file.md URL that Starlight wrongly emits for .md links. */
export function fileToMdUrlPath(mdFile) {
  return `/${relative(CONTENT_ROOT, mdFile).split(sep).join('/')}`;
}

/** Redirect /foo/bar.md → /foo/bar/ for every content page. */
export function buildMarkdownExtensionRedirects(root = CONTENT_ROOT) {
  const redirects = {};

  function walk(dir) {
    for (const name of readdirSync(dir)) {
      const full = join(dir, name);
      if (statSync(full).isDirectory()) {
        walk(full);
      } else if (name.endsWith('.md')) {
        const target = fileToUrlPath(full);
        const mdPath = fileToMdUrlPath(full);
        if (mdPath !== target) {
          redirects[mdPath] = target;
        }
        const lowerMdPath = mdPath.toLowerCase();
        if (lowerMdPath !== mdPath && lowerMdPath !== target) {
          redirects[lowerMdPath] = target;
        }
      }
    }
  }

  walk(root);
  return redirects;
}
