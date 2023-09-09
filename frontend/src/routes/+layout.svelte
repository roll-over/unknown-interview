<script lang="ts">
	import Header from '$lib/components/Header.svelte';
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
			<footer class="bg-app-blue-100">feet</footer>
		</svelte:fragment>
	</AppShell>
</QueryClientProvider>
