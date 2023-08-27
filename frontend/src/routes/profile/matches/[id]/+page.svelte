<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { createQuery } from '@tanstack/svelte-query';
	import { tick } from 'svelte';
	import { YourID, getChat } from '../getChats';

	const dateFormatter = new Intl.DateTimeFormat('ru');
	const relativeDateFormatter = new Intl.RelativeTimeFormat('en');
	const msInMinute = 1000 * 60;
	const msInHour = msInMinute * 60;
	const msInDay = msInHour * 24;
	function formatDate(timestamp: number) {
		const msDiff = Date.now() - timestamp;
		if (msDiff > 3 * msInDay) return dateFormatter.format(timestamp);
		if (msDiff > msInDay) return relativeDateFormatter.format(-Math.round(msDiff / msInDay), 'day');
		if (msDiff > msInHour)
			return relativeDateFormatter.format(-Math.round(msDiff / msInHour), 'hour');
		return relativeDateFormatter.format(-Math.round(msDiff / msInMinute), 'minute');
	}
	let chatContainer: HTMLUListElement;
	$: chatQuery = createQuery({
		async queryFn() {
			const id = $page.params.id;
			if (!id) return goto('/profile/matches'), null;
			const chat = await getChat(id);
			if (!chat || chat.id !== id) return goto('/profile/matches'), null;
			return chat;
		},
		queryKey: ['chat', $page.params.id]
	});
	$: isChatLoading = $chatQuery.isLoading;

	async function ScrollToBottom(isLoading: boolean, id: string | undefined) {
		id;
		if (!chatContainer || isLoading) return;

		await tick();
		chatContainer.scrollTo({ top: chatContainer.scrollHeight });
	}
	$: ScrollToBottom(isChatLoading, $page.params.id);
</script>

<div class="flex h-full flex-col">
	<ul
		bind:this={chatContainer}
		class="flex h-full flex-col items-start gap-2 overflow-y-scroll p-1"
	>
		{#if $chatQuery.isSuccess && $chatQuery.data}
			{#each $chatQuery.data.messages as message (message.id)}
				<li
					class="max-w-lg rounded-lg p-3
                    {message.author.id === YourID
						? 'bg-slate-500 max-xl:self-end'
						: 'bg-neutral-500'}"
				>
					<div class="text-sm text-white/80">
						by {message.author.name} - {formatDate(message.timestamp)}
					</div>
					<div>{message.content}</div>
				</li>
			{/each}
		{:else}
			<div class="flex h-full items-center justify-center self-stretch">Loading...</div>
		{/if}
	</ul>
	<div class="flex p-1">
		<textarea
			class="grow resize-none rounded-l-lg bg-slate-500 p-1 text-black shadow-inner shadow-black/50"
		/>
		<button class="rounded-r-lg bg-slate-600 px-4">SEND</button>
	</div>
</div>
