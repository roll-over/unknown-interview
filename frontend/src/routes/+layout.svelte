<script lang="ts">
	import { QueryClientProvider } from '@tanstack/svelte-query';
	import '../app.pcss';

	export let data;
</script>

<QueryClientProvider client={data.queryClient}>
	<div class="flex h-screen flex-col">
		<header class="bg-slate-400">
			<nav class="flex gap-3">
				<a href="/">Home</a>
				<a href="/auth/login">Log-in</a>
				<a href="/profile/matches">Matches</a>
			</nav>
		</header>
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
