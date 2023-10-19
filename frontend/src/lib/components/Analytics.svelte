<script
	lang="ts"
	context="module"
>
	import { browser } from '$app/environment';
	import type { Gtag } from 'gtag.js';

	declare global {
		interface Window {
			dataLayer: unknown[];
		}
	}
	if (browser) {
		window.dataLayer ||= [];
	}

	const googleTag = 'G-441JSZK837';

	export const gtag: Gtag.Gtag = (command, ...args) => {
		if (!browser) return;

		window.dataLayer.push(command, ...args);
	};

	gtag('js', new Date());
	gtag('config', googleTag);
</script>

<script lang="ts"></script>

<svelte:head>
	<script
		async
		src="https://www.googletagmanager.com/gtag/js?id={googleTag}"
	></script>
</svelte:head>
