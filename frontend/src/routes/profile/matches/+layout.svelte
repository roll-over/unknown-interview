<script lang="ts">
	import { createQuery } from '@tanstack/svelte-query';
	import Chats from './Chats.svelte';
	import { getChatList } from './getChats';
	import { AppRail } from '@skeletonlabs/skeleton';

	const chatsQuery = createQuery({
		queryFn() {
			return getChatList();
		},
		queryKey: ['chat']
	});
</script>

<div class="flex h-full">
	<AppRail
		width="w-80"
		regionDefault="h-full"
	>
		{#if $chatsQuery.isSuccess}
			<Chats chats={$chatsQuery.data} />
		{:else}
			<div class="flex h-full items-center justify-center overflow-y-scroll">Loading...</div>
		{/if}
	</AppRail>
	<div class="grow">
		<slot />
	</div>
</div>
