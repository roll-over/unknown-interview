<script lang="ts">
	import { QueryClientProvider } from '@tanstack/svelte-query';
	import '../app.pcss';
	import Header from '$lib/components/header.svelte';

	export let data;
</script>

<QueryClientProvider client={data.queryClient}>
	<div class="flex h-screen flex-col">
		<Header />
		<!-- min-h-0 overwrites default behavior of min-h-auto on flex elements -->
		<main class="min-h-0 grow">
			<slot />
		</main>
	</div>
	<footer class="bg-slate-400">feet</footer>
</QueryClientProvider>

<style>
	:global(html) {
		background-color: theme('colors.slate.700');
		color: theme('colors.white');
	}
</style>
