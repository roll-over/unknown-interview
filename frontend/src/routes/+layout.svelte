<script lang="ts">
	import { QueryClientProvider } from '@tanstack/svelte-query';
	import '../app.pcss';
	import Header from '$lib/components/header.svelte';
	import { AppShell } from '@skeletonlabs/skeleton';

	export let data;
</script>

<QueryClientProvider client={data.queryClient}>
	<AppShell
		slotHeader="bg-slate-400"
		slotFooter="bg-slate-400"
		regionPage="h-full w-full"
		slotPageContent="h-full w-full"
	>
		<svelte:fragment slot="header">
			<Header />
		</svelte:fragment>
		<slot />
		<svelte:fragment slot="footer">feet</svelte:fragment>
	</AppShell>
</QueryClientProvider>

<style lang="postcss">
	:global(::-webkit-scrollbar-thumb) {
		background-color: theme('colors.black/0.6');
		border-radius: theme('borderRadius.md');
	}
	:global(::-webkit-scrollbar) {
		background-color: theme('colors.white/0.1');
		width: theme('width.2');
	}
</style>
