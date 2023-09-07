<script lang="ts">
	import { createQuery } from '@tanstack/svelte-query';
	import Chats from './Chats.svelte';
	import { getChatList } from './getChats';

	const chatsQuery = createQuery({
		queryFn() {
			return getChatList();
		},
		queryKey: ['chat']
	});
</script>



<div class="flex h-full">
	<div class="flex h-full min-w-0 shrink-0 basis-80 flex-col border-r border-r-blue-500">
		{#if $chatsQuery.isSuccess}
			<Chats chats={$chatsQuery.data} />
		{:else}
			<div class="flex h-full items-center justify-center">Loading...</div>
		{/if}
	</div>
	<div class="grow">
		<slot />
	</div>
</div>