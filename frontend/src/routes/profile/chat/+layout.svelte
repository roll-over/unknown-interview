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

	const notes = [
		{ text: 'Modi laboriosam quidem accusantium fugiat repellendus 1', id: '1' },
		{ text: 'Modi laboriosam quidem accusantium fugiat repellendus 2', id: '2' },
		{ text: 'Modi laboriosam quidem accusantium fugiat repellendus 3', id: '3' },
		{
			text: 'Modi laboriosam quidem accusantium fugiat repellendus 4, Modi laboriosam quidem accusantium fugiat repellendus 4',
			id: '4'
		},
		{ text: 'Modi laboriosam quidem accusantium fugiat repellendus 5', id: '5' },
		{ text: 'Modi laboriosam quidem accusantium fugiat repellendus 6', id: '6' }
	];
</script>

<div class="grid h-full grid-rows-5">
	<div class="row-span-4 grid grid-cols-3">
		<div class="flex flex-col overflow-y-hidden border-2 border-sky-900 bg-app-blue-50 p-5">
			<h1 class="pb-5 text-center font-title text-xl">Messages</h1>
			{#if $chatsQuery.isSuccess}
				<Chats chats={$chatsQuery.data} />
			{:else}
				<div class="flex h-full items-center justify-center">Loading...</div>
			{/if}
		</div>
		<div class="col-span-2 overflow-y-hidden">
			<slot />
		</div>
	</div>
	<div class="flex flex-col">
		NOTES
		<div class="flex flex-col justify-between overflow-y-hidden border-t border-t-blue-500">
			<div class="overflow-y-scroll">
				{#if notes.length}
					<ul class="flex h-full flex-col items-start gap-2 p-1">
						{#each notes as { text, id } (id)}
							<li class="max-w-lg rounded-lg bg-slate-500 p-3">
								<p class="p-1">{id}. {text}</p>
							</li>
						{/each}
					</ul>
				{:else}
					<div class="flex h-full w-full items-center justify-center">
						<span> Loading... </span>
					</div>
				{/if}
			</div>
			<div class="flex p-1">
				<textarea
					class="grow resize-none rounded-l-lg bg-slate-500 p-1 text-black shadow-inner shadow-black/50"
				/>
				<button class="rounded-r-lg bg-slate-600 px-4">SEND</button>
			</div>
		</div>
	</div>
</div>
