<script lang="ts">
	import Header from '$lib/components/header.svelte';
	import { arrow, autoUpdate, computePosition, flip, offset, shift } from '@floating-ui/dom';
	import { AppShell, storePopup } from '@skeletonlabs/skeleton';
	import { QueryClientProvider } from '@tanstack/svelte-query';
	import '../app.pcss';
	storePopup.set({ computePosition, autoUpdate, offset, shift, flip, arrow });

	export let data;
</script>

<QueryClientProvider client={data.queryClient}>
	<AppShell
		regionPage="h-full w-full"
		slotPageContent="h-full w-full"
	>
		<svelte:fragment slot="header">
			<Header />
		</svelte:fragment>
		<slot />
		<svelte:fragment slot="footer">
			<footer class="shadow-[white_0px_-1px_2px]">feet</footer>
		</svelte:fragment>
	</AppShell>
</QueryClientProvider>
