<script lang="ts">
	import { createQuery } from '@tanstack/svelte-query';
	import Chats from './Chats.svelte';
	import Notion from './Notion.svelte';
	import { getChatList } from './getChats';

	const chatsQuery = createQuery({
		queryFn() {
			return getChatList();
		},
		queryKey: ['chat']
	});
</script>

<div class="grid h-full grid-rows-4">
	<div class="row-span-4 grid grid-cols-4">
		<div class="flex flex-col overflow-y-hidden border-2 border-sky-900 bg-app-blue-50 p-5">
			<h1 class="pb-5 text-center font-title text-xl">Chats</h1>
			{#if $chatsQuery.isSuccess}
				<Chats chats={$chatsQuery.data} />
			{:else}
				<div class="flex h-full items-center justify-center">Loading...</div>
			{/if}
		</div>
		<div class="col-span-2 overflow-y-hidden">
			<slot />
		</div>
		<Notion></Notion>
	</div>
</div>
