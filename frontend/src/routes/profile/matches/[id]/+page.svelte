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
							{message.author.id === YourID ? 'bg-blue-200/30 max-xl:self-end' : 'bg-black/10'}"
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
			class="grow resize-none rounded-l-lg bg-blue-300/20 p-1 shadow-inner shadow-white/50"
		/>
		<button class="rounded-r-lg bg-black/30 px-4">SEND</button>
	</div>
</div>
