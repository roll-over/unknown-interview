<script lang="ts">
	import { createGetQuery } from '$lib/api';
	import { createQuery } from '@tanstack/svelte-query';
	import type { Chats } from './interFace';
	import { page } from '$app/stores';

	// Создание запроса на получение чатов
	$: getChats = createGetQuery('/api/v1/chats/', {
		params: { query: { record_id: $page.params.id || '' } }
	});

	// Создание запроса с использованием Svelte Query
	$: queryChats = createQuery({
		queryKey: getChats.key,
		async queryFn() {
			const res = await getChats.runQuery();
			// Преобразование данных о чатах для отображения в списке
			return (res.data || []).map((chat: Chats) => {
				const lastMessage = chat.last_message?.[0];
				return {
					chat_id: chat.chat_id,
					chat_name: chat.chat_name,
					last_message_text: lastMessage?.text || null,
					own: lastMessage?.own || null
				};
			});
		}
	});
</script>

<ul class="flex flex-col gap-3 overflow-y-auto pr-0 md:pr-7">
	{#if $queryChats.data && $queryChats.data.length > 0}
		{#each $queryChats.data as { chat_id, chat_name, last_message_text, own }}
			<li>
				<a
					href={`/profile/chat/${$page.params.id}/${chat_id}`}
					class="group relative block overflow-hidden rounded-lg transition after:absolute after:-right-3 after:top-0 after:h-full after:w-3 after:bg-sky-900 after:transition-transform aria-[current]:translate-x-4 aria-[current]:bg-app-blue-100 aria-[current]:after:-translate-x-3 dark:aria-[current]:bg-app-dark-light"
					aria-current={$page.params.chatId === chat_id ? 'page' : null}
				>
					<div
						class="rounded-lg border-2 border-app-blue-100 bg-app-blue-50 p-3 dark:border-app-dark-light dark:bg-app-dark-blue md:bg-transparent md:dark:bg-transparent"
					>
						<span class="text-base md:text-xl">{chat_name}</span>
						{#if own}
							<span
								class="block w-full overflow-x-hidden text-ellipsis whitespace-nowrap text-xs font-normal transition-[font-weight] md:text-base"
							>
								<span class="text-app-blue-600">You:</span>
								{last_message_text}
							</span>
						{:else}
							<span
								class="block w-full overflow-x-hidden text-ellipsis whitespace-nowrap text-xs font-bold transition-[font-weight] md:text-base"
							>
								{last_message_text}
							</span>
						{/if}
					</div>
				</a>
			</li>
		{/each}
	{:else}
		<p>No chats available</p>
	{/if}
</ul>
