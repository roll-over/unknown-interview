<script lang="ts">
	import { createQuery } from '@tanstack/svelte-query';
	import { YourID, getChatList } from './getChats';
	import { page } from '$app/stores';

	const chatsQuery = createQuery({
		queryFn() {
			return getChatList();
		},
		queryKey: ['chat']
	});
</script>

<div class="flex h-full">
	<ul
		class="flex shrink-0 basis-80 flex-col gap-1 overflow-y-scroll border-r border-r-blue-500 p-1"
	>
		{#if $chatsQuery.isSuccess}
			{#each $chatsQuery.data as chat (chat.id)}
				<li class=" border-b border-b-blue-500 pb-1 last:border-b-0">
					<a
						href="/profile/matches/{chat.id}"
						class="flex flex-col gap-1 {$page.params.id === chat.id ? 'bg-slate-800' : ''}"
					>
						<span class="font-bold">{chat.label}</span>
						{#if chat.lastMessage}
							<span class=" overflow-hidden text-ellipsis whitespace-nowrap">
								{#if chat.lastMessage.author.id === YourID}
									<span class="opacity-80">You:</span>
								{/if}
								{chat.lastMessage.content}
							</span>
						{/if}
					</a>
				</li>
			{/each}
		{:else}
			<div class="flex h-full items-center justify-center">Loading...</div>
		{/if}
	</ul>
	<div class="grow">
		<slot />
	</div>
</div>
