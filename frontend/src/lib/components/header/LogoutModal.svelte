<script
	lang="ts"
	context="module"
>
	import { getModalStore, type ModalStore } from '@skeletonlabs/skeleton';
	import type { ComponentProps } from 'svelte';
	import ProfileModal from './LogoutModal.svelte';

	export function showLogoutModal(
		modalStore: ModalStore,
		{ email, image }: ComponentProps<ProfileModal>
	) {
		modalStore.trigger({
			type: 'component',
			component: {
				ref: ProfileModal,
				props: { email, image }
			},
			backdropClasses: 'backdrop-blur-md'
		});
	}
</script>

<script lang="ts">
	export let email: string;
	export let image: string;

	const modalStore = getModalStore();
</script>

<div class="rounded-md bg-white p-10 shadow-md">
	<div class="flex flex-col items-start gap-4">
		<h1 class="text-xl">Are you sure you want to logout?</h1>
		{email}
		{#if image}
			<img
				src={image}
				alt=""
				class="h-20 w-20 rounded-full"
			/>
		{/if}
		<div class="flex w-full flex-row justify-between">
			<a href="/api/v1/auth/logout">Logout</a>
			<button on:click={() => modalStore.close()}>Close</button>
		</div>
	</div>
</div>
