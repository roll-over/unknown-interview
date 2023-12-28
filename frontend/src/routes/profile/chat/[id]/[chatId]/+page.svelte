<script lang="ts">
	import MaterialSymbolsNewWindow from '~icons/material-symbols/new-window';
	import { createGetQuery } from '$lib/api';
	import { createQuery, useQueryClient } from '@tanstack/svelte-query';
	import { dateFormatter, type Chat, type Message, type Note, formatTime } from '../interFace';
	import { onMount, tick } from 'svelte';
	import { writable } from 'svelte/store';

	const queryClient = useQueryClient();

	const groupBy = <T,>(array: T[], keyFunc: (item: T) => string) =>
		array.reduce((result: Record<string, T[]>, item) => {
			const key = keyFunc(item);
			result[key] = [...(result[key] || []), item];
			return result;
		}, {});

	$: lastId = writable('');

	onMount(() => {
		const url = window.location.href;
		const parts = url.split("/");
		lastId.set(parts.pop() || '');
	});

	let newMessageText = '';

	// Запрос на получение данных о чате
	$: messagesNotesGet = createGetQuery<Chat>(`/api/v1/chats/${$lastId}`);

	// Запрос на получение сообщений чата с использованием библиотеки svelte-query
	$: queryMessage = createQuery({
		queryKey: messagesNotesGet.key,
		async queryFn() {
			try {
				const res = await messagesNotesGet.runQuery();
				const data = res.data || { chat_name: '', messages: [] };

				return {
					chat_name: data.chat_name,
					messages: (data.messages || []).map((message: Message) => ({
						text: message.text || null,
						own: message.own || null,
						created_at: message.created_at || null
					}))
				};
			} catch (error) {
				throw error;
			}
		}
	});

	$: queryNotes = createQuery({
    queryKey: messagesNotesGet.key,
    async queryFn() {
        try {
            const res = await messagesNotesGet.runQuery();
            const data = res.data || [];

            return data.map((note: Note) => ({
                custom_id: note.custom_id || null,
                related_id: note.related_id || null,
                created_at: note.created_at || null,
                note_text: note.note_text || null
            }));
        } catch (error) {
            throw error;
        }
    }
});

	// Прокрутка вниз при получении новых сообщений
	$: if ($queryMessage.isSuccess && $queryMessage.data) {
		tick().then(() => {
			const chatBottom = document.getElementById('chatBottom');
			if (chatBottom) {
				chatBottom.scrollIntoView({ behavior: 'smooth' });
			}
		});
	}

	// Функция для отправки нового сообщения
	async function sendMessage() {
		try {
			const response = await fetch('/api/v1/chats/add_message', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					related_id: $lastId,
					text: newMessageText
				})
			});

			if (!response.ok) {
				throw new Error('Failed to send message');
			}

			newMessageText = '';

			// После успешной отправки сообщения вызываем invalidateQueries для обновления данных
			queryClient.invalidateQueries(messagesNotesGet.key as any);
		} catch (error) {
			console.error('Error sending message:', error);
			// Обработка ошибки по необходимости
		}
	}
</script>

{#if $queryMessage.isSuccess && $queryMessage.data}
	{@const messageGroups = Object.entries(
		groupBy($queryMessage.data.messages, (msg) => dateFormatter(msg.created_at))
	)}

	<div class="grid grow h-full grid-rows-5 border-2 border-l-0 border-sky-900">
		<div class="row-span-4 flex flex-col transition-opacity">
			<p class="bg-app-blue-50 py-4 text-center text-xl outline outline-2 outline-sky-900">
				{$queryMessage.data.chat_name}
			</p>
			<div class="overflow-y-hidden p-5">
				<div class="h-full overflow-y-auto px-10 text-xl">
					{#each messageGroups as [date, messages]}
						{#if messages.length > 0}
							<p class="p-3 text-center">{date}</p>
							<div class="flex flex-col gap-2">
								{#each messages as msg (msg.created_at)}
									{@const isYourMessage = msg.own}
									<div class="max-w-lg {isYourMessage && 'self-end'}">
										<div
											class="rounded-lg px-4 py-2 {isYourMessage
												? 'bg-app-blue-50'
												: 'bg-app-blue-100'}"
										>
											{msg.text}
										</div>
										<p class="text-neutral-700/50 {isYourMessage && 'max-2xl text-right'}">
											{formatTime(msg.created_at)}
										</p>
									</div>
								{/each}
							</div>
						{/if}
					{/each}
					<div id="chatBottom"></div>
				</div>
			</div>
		</div>
		<div class="flex gap-2 px-16 py-6 font-title outline outline-2 outline-sky-900">
			<div
				class="grow rounded-3xl p-4 outline outline-1 outline-app-blue-600 focus-within:outline-2"
			>
				<textarea
					bind:value={newMessageText}
					placeholder="Type your message..."
					class="w-full flex-grow rounded-lg focus:outline-none"
					on:keydown={(event) => event.key === 'Enter' && sendMessage()}
				/>
			</div>
			<button
				on:click={sendMessage}
				class="flex items-center justify-center rounded-3xl bg-app-blue-600 px-12 text-2xl text-white"
			>
				SEND
			</button>
		</div>
	</div>
{:else}
	<!-- <div class="row-span-full m-auto">Loading...</div> -->
{/if}

<div class="flex w-80 flex-col border-r-0 overflow-y-hidden border-2 border-sky-900">
	<p class="bg-app-blue-50 py-4 text-center text-xl outline outline-2 outline-sky-900">Notes</p>
	<div class="flex flex-col justify-between overflow-y-auto pl-5 pr-5 pt-3">
			<button aria-label={'create notion'} class="flex items-center pb-5">
					<MaterialSymbolsNewWindow class="mr-4 text-3xl" />ADD NEW NOTE
			</button>

{#if $queryNotes.isSuccess}
    {#if $queryNotes.data.length > 0}
        <ul class="flex flex-col gap-3 overflow-y-auto pr-5">
            {#each $queryNotes.data as { custom_id, note_text } (custom_id)}
                <li class="max-w-lg rounded-lg bg-app-blue-50 p-3">
                    <p class="p-1">{custom_id}. {note_text}</p>
                </li>
            {/each}
        </ul>
    {:else}
        <div class="flex h-full w-full items-center justify-center">
            <span>No notes available.</span>
        </div>
    {/if}
{:else}
    <div class="flex h-full w-full items-center justify-center">
        <span>Loading...</span>
    </div>
{/if}
	</div>
</div>