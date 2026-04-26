import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://docs.innersync.tech',
  integrations: [
    starlight({
      title: 'Innersync Documentation',
      social: [
        { icon: 'github', label: 'GitHub', href: 'https://github.com/Innersync-tech/docs' }
      ]
    })
  ]
});
