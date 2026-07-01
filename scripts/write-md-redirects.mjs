#!/usr/bin/env node
/** Write flat HTML redirect files for legacy *.md URLs (e.g. /alphapy/index.md). */
import { readdirSync, rmSync, statSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { buildMarkdownExtensionRedirects, fileToMdUrlPath, fileToUrlPath } from './starlight-urls.mjs';

const ROOT = join(fileURLToPath(new URL('.', import.meta.url)), '..');
const DIST = join(ROOT, 'dist');
const CONTENT = join(ROOT, 'src', 'content', 'docs');

function redirectHtml(from, to) {
  const absolute = to.startsWith('http') ? to : `https://docs.innersync.tech${to}`;
  return `<!doctype html><title>Redirecting to: ${to}</title><meta http-equiv="refresh" content="0;url=${to}"><meta name="robots" content="noindex"><link rel="canonical" href="${absolute}"><body><a href="${to}">Redirecting from <code>${from}</code> to <code>${to}</code></a></body>`;
}

function walkMdFiles(dir, files = []) {
  for (const name of readdirSync(dir)) {
    const full = join(dir, name);
    if (statSync(full).isDirectory()) {
      walkMdFiles(full, files);
    } else if (name.endsWith('.md')) {
      files.push(full);
    }
  }
  return files;
}

const redirects = buildMarkdownExtensionRedirects(CONTENT);
let written = 0;

for (const mdFile of walkMdFiles(CONTENT)) {
  const from = fileToMdUrlPath(mdFile);
  const to = fileToUrlPath(mdFile);
  if (from === to) {
    continue;
  }

  const outFile = join(DIST, from.slice(1));
  rmSync(outFile, { recursive: true, force: true });
  writeFileSync(outFile, redirectHtml(from, to), 'utf8');
  written += 1;

  const lowerFrom = from.toLowerCase();
  if (lowerFrom !== from) {
    const lowerOut = join(DIST, lowerFrom.slice(1));
    rmSync(lowerOut, { recursive: true, force: true });
    writeFileSync(lowerOut, redirectHtml(lowerFrom, to), 'utf8');
    written += 1;
  }
}

console.log(`Wrote ${written} legacy .md redirect file(s) to dist/`);
