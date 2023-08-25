<script lang="ts">
	import { QueryClientProvider } from '@tanstack/svelte-query';
	import '../app.pcss';

	export let data;
</script>

<QueryClientProvider client={data.queryClient}>
	<main>
		<slot />
	</main>
</QueryClientProvider>

<style>
	:global(html) {
		background-color: theme('colors.slate.700');
		color: theme('colors.white');
	}
</style>
