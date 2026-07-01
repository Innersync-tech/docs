import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

const legacyRepoPathRedirects = Object.fromEntries(
  ['alphapy', 'app', 'core', 'legal'].flatMap((section) => {
    const target = section === 'legal' ? '/legal/legal/' : `/${section}/`;
    return [
      [`/src/content/docs/${section}`, target],
      [`/src/content/docs/${section}/`, target],
    ];
  })
);

export default defineConfig({
  site: 'https://docs.innersync.tech',
  redirects: legacyRepoPathRedirects,
  integrations: [
    starlight({
      title: 'Innersync Documentation',
      social: [
        { icon: 'github', label: 'GitHub', href: 'https://github.com/Innersync-tech/docs' }
      ]
    })
  ]
});
