<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { route } from '$lib/utils/route';
	import { createQuery, keepPreviousData } from '@tanstack/svelte-query';
	import { derived } from 'svelte/store';
	import { YourID, getChat } from '../getChats';
	import { createGetQuery } from '$lib/api';

	let text = '';

	async function sendMessage() {
		try {
			const response = await fetch('/api/v1/chats/add_message', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ text })
			});

			if (response.ok) {
				alert('sent successfully');
			} else {
				alert('sent fail');
			}
		} catch (error) {
			console.error('sent error', error);
		}
	}

	$: messagesGet = createGetQuery('/api/v1/chats/{chat_id}', {
		params: { path: { chat_id: '84b2ddc3-2f21-4752-80e3-a6e19ca05ea4' } }
	});
	$: queryMessages = createQuery({
		queryKey: messagesGet.key,
		async queryFn() {
			const res = await messagesGet.runQuery();
			return res;
		}
	});

	const dateFormatter = new Intl.DateTimeFormat('en', { month: 'short', day: '2-digit' });
	const timeFormatter = new Intl.DateTimeFormat('en', {
		hour: '2-digit',
		minute: '2-digit',
		hour12: false
	});
	const relativeTimeFormatter = new Intl.RelativeTimeFormat('en');
	const msInMinute = 1000 * 60;
	const msInHour = msInMinute * 60;
	function formatTimestamp(timestamp: number) {
		const msDiff = Date.now() - timestamp;
		if (msDiff < 1 * msInHour)
			return relativeTimeFormatter.format(-Math.floor(msDiff / msInMinute), 'minute');
		if (msDiff < 6 * msInHour) {
			return relativeTimeFormatter.format(-Math.floor(msDiff / msInHour), 'hour');
		}
		return timeFormatter.format(timestamp);
	}

	function groupBy<T, V>(array: T[], getGroupValue: (value: T) => V) {
		const groupByMap = new Map<V, T[]>();
		for (const value of array) {
			const groupBy = getGroupValue(value);
			const grouppedvalues = groupByMap.get(groupBy);
			if (grouppedvalues) {
				grouppedvalues.push(value);
			} else {
				groupByMap.set(groupBy, [value]);
			}
		}
		return [...groupByMap];
	}

	$: chatQuery = createQuery(
		derived(page, (page) => {
			return {
				queryKey: ['chat', page.params.chatId],
				async queryFn() {
					const id = page.params.chatId;
					if (!id) {
						goto(route('/profile/chat'));
						return null;
					}
					const chat = await getChat(id);
					if (!chat || chat.id !== id) {
						goto(route('/profile/chat'));
						return null;
					}
					return chat;
				},
				placeholderData: keepPreviousData
			};
		})
	);

	let chatBottom: HTMLElement;
	$: if (chatBottom && $chatQuery.data) {
		chatBottom.scrollIntoView();
	}
</script>

{#if $queryMessages.status === 'pending'}
	<p>Loading...</p>
{/if}

{#if $queryMessages.status === 'error'}
	<p>Error :(</p>
{/if}

<div class="grid h-full grid-rows-5 border-2 border-l-0 border-sky-900">
	{#if $chatQuery.isSuccess && $chatQuery.data}
		{@const messageGroups = groupBy($chatQuery.data.messages, (message) =>
			dateFormatter.format(message.timestamp)
		)}
		<div
			class="row-span-4 flex flex-col transition-opacity"
			class:opacity-70={$chatQuery.isPlaceholderData}
		>
			<p class="bg-app-blue-50 py-4 text-center text-xl outline outline-2 outline-sky-900">
				{$chatQuery.data.label}
			</p>
			<div class="overflow-y-hidden p-5">
				<div class="h-full overflow-y-auto px-10 text-xl">
					{#each messageGroups as [date, messages] (date)}
						<p class="p-3 text-center">{date}</p>
						<div class="flex flex-col gap-2">
							{#each messages as message}
								{@const isYourMessage = message.author.id === YourID}
								<div
									class="max-w-lg"
									class:max-2xl:self-end={isYourMessage}
								>
									<div
										class="rounded-lg px-4 py-2 {isYourMessage
											? 'bg-app-blue-50'
											: 'bg-app-blue-100'}"
									>
										{message.content}
									</div>
									<p
										class="text-neutral-700/50"
										class:max-2xl:text-right={isYourMessage}
									>
										{formatTimestamp(message.timestamp)}
									</p>
								</div>
							{/each}
						</div>
					{/each}
					<div
						class="sr-only static"
						bind:this={chatBottom}
					/>
				</div>
			</div>
		</div>
		<div class="flex gap-2 px-16 py-6 font-title outline outline-2 outline-sky-900">
			<div
				class="grow rounded-3xl p-4 outline outline-1 outline-app-blue-600 focus-within:outline-2"
			>
				<textarea
					bind:value={text}
					class="h-full w-full resize-none outline-none placeholder:text-neutral-800"
					placeholder="Leave a message..."
				/>
			</div>
			<button
				on:click={sendMessage}
				class="flex items-center justify-center rounded-3xl bg-app-blue-600 px-12 text-2xl text-white"
			>
				SEND
			</button>
		</div>
	{:else}
		<div class="row-span-full m-auto">Loading...</div>
	{/if}
</div>
