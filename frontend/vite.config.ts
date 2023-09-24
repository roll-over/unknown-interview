import { sveltekit } from '@sveltejs/kit/vite';
import { FileSystemIconLoader } from 'unplugin-icons/loaders';
import Icons from 'unplugin-icons/vite';
import { defineConfig } from 'vite';
import genrateOpenApi from './scripts/openapi-gen';
import { generateRoutesWatcher } from './scripts/router-gen';

export default defineConfig({
	plugins: [
		sveltekit(),
		Icons({
			compiler: 'svelte',
			autoInstall: true,
			customCollections: { main: FileSystemIconLoader('./src/assets/img/main') },
			scale: 1
		}),
		{
			name: 'codegen',
			buildStart() {
				if (process.env.NODE_ENV !== 'development') return;

				generateRoutesWatcher();
				genrateOpenApi();
			}
		}
	],
	server: { watch: { usePolling: true } },
	test: { include: ['./src/**/*.{test,spec}.?(c|m)[jt]s?(x)'] }
});
