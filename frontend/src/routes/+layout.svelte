<script lang="ts">
	import Analytics from '$lib/components/Analytics.svelte';
	import Header from '$lib/components/Header.svelte';
	import { arrow, autoUpdate, computePosition, flip, offset, shift } from '@floating-ui/dom';
	import '@fontsource-variable/inter';
	import '@fontsource-variable/montserrat';
	import { AppShell, Modal, initializeStores, storePopup } from '@skeletonlabs/skeleton';
	import { QueryClientProvider } from '@tanstack/svelte-query';
	import '../app.pcss';

	initializeStores();
	storePopup.set({ computePosition, autoUpdate, offset, shift, flip, arrow });
	export let data;
</script>

<svelte:head>
	<title>Hide-Hire</title>
</svelte:head>
<Modal />
<QueryClientProvider client={data.queryClient}>
	<Analytics />
	<AppShell
		regionPage="h-full w-full"
		slotPageContent="h-full w-full"
		class="flex flex-col-reverse text-neutral-800 sm:flex-col"
	>
		<svelte:fragment slot="header">
			<Header />
		</svelte:fragment>
		<slot />
	</AppShell>
</QueryClientProvider>
