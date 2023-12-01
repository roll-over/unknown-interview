import { sveltekit } from '@sveltejs/kit/vite';
import { FileSystemIconLoader } from 'unplugin-icons/loaders';
import Icons from 'unplugin-icons/vite';
import { defineConfig } from 'vite';
import genrateOpenApi from './scripts/openapi-gen';
import { generateRoutesWatcher } from './scripts/router-gen';

let cleanup = () => void 0;
export default defineConfig({
	plugins: [
		sveltekit(),
		Icons({
			compiler: 'svelte',
			autoInstall: true,
			customCollections: {
				main: FileSystemIconLoader('./src/assets/img/main'),
				about: FileSystemIconLoader('./src/assets/img/about')
			},
			scale: 1
		}),
		{
			name: 'codegen',
			buildStart() {
				if (process.env.NODE_ENV !== 'development') return;
				const routegenCleanup = generateRoutesWatcher();
				genrateOpenApi();

				cleanup = () => {
					routegenCleanup();
				};
			},
			buildEnd() {
				cleanup();
			}
		}
	],
	server: { watch: { usePolling: true } },
	test: { include: ['./**/*.{test,spec}.?(c|m)[jt]s?(x)'] }
});
