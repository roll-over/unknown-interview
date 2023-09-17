import { sveltekit } from '@sveltejs/kit/vite';
import { FileSystemIconLoader } from 'unplugin-icons/loaders';
import Icons from 'unplugin-icons/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [
		sveltekit(),
		Icons({
			compiler: 'svelte',
			autoInstall: true,
			customCollections: { main: FileSystemIconLoader('./src/assets/img/main') },
			scale: 1
		})
	],
	server: { watch: { usePolling: true } },
	test: { include: ['./src/**/*.{test,spec}.?(c|m)[jt]s?(x)'] }
});
