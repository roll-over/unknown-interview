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

<div class="flex h-full p-10">
	<div class="flex flex-col border-2 border-sky-800 bg-app-blue-50 pl-5 pr-5">
		<h2 class="pb-5 pt-5 text-center">Messages</h2>
		<AppRail
			width="w-80 overflow-x-hidden"
			regionDefault="h-full w-80"
		>
			{#if $chatsQuery.isSuccess}
				<Chats chats={$chatsQuery.data} />
			{:else}
				<div class="flex h-full items-center justify-center overflow-y-scroll">Loading...</div>
			{/if}
		</AppRail>
	</div>
	<div class="grow border-2 border-sky-800">
		<slot />
	</div>
</div>
