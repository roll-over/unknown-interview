<script
	lang="ts"
	context="module"
>
	import { route } from '$lib/utils/route';
	import { getModalStore, type ModalStore } from '@skeletonlabs/skeleton';
	import CheerIcon from '~icons/material-symbols/cheer-outline';
	import WarningModal from './WarningModal.svelte';

	type Opts = { hasMatches: boolean; isCvRoute: boolean };
	export function showWarningModal(modalStore: ModalStore, { hasMatches, isCvRoute }: Opts) {
		modalStore.trigger({
			type: 'component',
			component: {
				ref: WarningModal,
				props: { hasMatches, isCvRoute }
			},
			backdropClasses: 'backdrop-blur-md'
		});
	}
</script>

<script lang="ts">
	export let hasMatches: boolean;
	export let isCvRoute: boolean;

	const modalStore = getModalStore();
</script>

<div
	class="flex max-w-3xl flex-col items-center justify-center gap-5 rounded-lg bg-app-blue-50 px-20 py-40"
>
	<p class="text-center text-6xl">
		{#if hasMatches}
			Please select a {isCvRoute ? 'CV' : 'vacancy'}
		{:else}
			<a
				href={route(isCvRoute ? '/create/cv' : '/create/vacancy')}
				on:click={() => modalStore.close()}
			>
				Fill out a {isCvRoute ? 'CV' : 'vacancy'} for further use of the service
			</a>
		{/if}
	</p>
	<CheerIcon class="h-60 w-60 text-app-blue-600" />
</div>
