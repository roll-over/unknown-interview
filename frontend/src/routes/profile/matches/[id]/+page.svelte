<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { createQuery } from '@tanstack/svelte-query';
	import { tick } from 'svelte';
	import { scale } from 'svelte/transition';
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
	let chatContainer: HTMLDivElement;
	let prevData: Awaited<ReturnType<typeof getChat>>;
	$: chatQuery = createQuery({
		async queryFn() {
			const id = $page.params.id;
			if (!id) return goto('/profile/matches'), null;
			const chat = await getChat(id);
			if (!chat || chat.id !== id) return goto('/profile/matches'), null;
			prevData = chat;
			return chat;
		},
		queryKey: ['chat', $page.params.id],
		placeholderData: prevData
	});

	$: isPlaceholder = $chatQuery.isPlaceholderData;
	async function ScrollToBottom(isPlaceHolder: boolean, id: string | undefined) {
		id;
		if (!chatContainer || isPlaceHolder) return;

		await tick();
		chatContainer.scrollTo({ top: chatContainer.scrollHeight });
	}
	$: ScrollToBottom(isPlaceholder, $page.params.id);

	let initialLoad = true;
	
	let notes = [
		{ text: "Modi laboriosam quidem accusantium fugiat repellendus 1", id: "1" },
		{ text: "Modi laboriosam quidem accusantium fugiat repellendus 2", id: "2" },
		{ text: "Modi laboriosam quidem accusantium fugiat repellendus 3", id: "3" },
		{ text: "Modi laboriosam quidem accusantium fugiat repellendus 4, Modi laboriosam quidem accusantium fugiat repellendus 4", id: "4" },
		{ text: "Modi laboriosam quidem accusantium fugiat repellendus 5", id: "5" },
		{ text: "Modi laboriosam quidem accusantium fugiat repellendus 6", id: "6" }
	]
</script>

<div class="flex h-full flex-col">
	<div
		class="h-full overflow-y-scroll"
		bind:this={chatContainer}
	>
		<div class="relative min-h-full">
			{#if $chatQuery.isSuccess && $chatQuery.data}
				<ul
					class="flex origin-[center_calc(100%-50vh)] flex-col items-start gap-2 p-1 transition-opacity"
					class:opacity-40={$chatQuery.isPlaceholderData && !initialLoad}
					in:scale={{ start: 0.7 }}
					on:introstart={() => (initialLoad = false)}
				>
					{#each $chatQuery.data.messages as message (message.id)}
						<li
							class="max-w-lg rounded-lg p-3
							{message.author.id === YourID ? 'bg-slate-500 max-xl:self-end' : 'bg-neutral-500'}"
						>
							<div class="text-sm text-white/80">
								by {message.author.name} - {formatDate(message.timestamp)}
							</div>
							<div>{message.content}</div>
						</li>
					{/each}
				</ul>
			{:else}
				<div
					class="absolute bottom-[50vh] flex w-full origin-[center_calc(100%-50vh)] justify-center"
				>
					<span out:scale={{ start: 3 }}> Loading... </span>
				</div>
			{/if}
		</div>
	</div>
	<div class="flex p-1">
		<textarea
			class="grow resize-none rounded-l-lg bg-slate-500 p-1 text-black shadow-inner shadow-black/50"
		/>
		<button class="rounded-r-lg bg-slate-600 px-4">SEND</button>
	</div>
	
	<div class="flex flex-col h-1/3 justify-between border-t border-t-blue-500">
		<div class="overflow-y-scroll h-full">
		{#if notes.length}
			<ul class="flex flex-col h-full items-start gap-2 p-1">
				{#each notes as { text, id }, i (id)}
					<li class="max-w-lg rounded-lg p-3 bg-slate-500 max-xl">
						<p class="p-1">{ id }. { text }</p>
					</li>
				{/each}
			</ul>
		{:else}
			<div class="flex justify-center items-center w-full h-full">
				<span> Loading... </span>
			</div>
		{/if}
		</div>
	
		<div class="flex p-1">
			<textarea
				class="grow resize-none rounded-l-lg bg-slate-500 p-1 text-black shadow-inner shadow-black/50" />
			<button class="rounded-r-lg bg-slate-600 px-4">SEND</button>
		</div>
		
	</div>
</div>
