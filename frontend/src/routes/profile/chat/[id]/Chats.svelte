
<script lang="ts">
  import { onMount } from 'svelte';
  import { createGetQuery } from '$lib/api';
  import { createQuery } from '@tanstack/svelte-query';
  import type { Chats } from './interFace';
  import { page } from '$app/stores';
  import { route } from '$lib/utils/route';

  // Создание запроса на получение чатов
  const getChats = createGetQuery('/api/v1/chats/', {
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

  // Массив для хранения DOM-элементов чатов
  let chatNodes: HTMLAnchorElement[] = [];

  // После монтирования компонента прокрутить к выбранному чату
  onMount(() => {
    const selectedChatNode = chatNodes.find((node) => node.ariaCurrent);
    if (!selectedChatNode) return;
    selectedChatNode.scrollIntoView({ block: 'nearest' });
  });
</script>

<ul class="flex flex-col gap-3 overflow-y-auto pr-10">
  {#if $queryChats.data && $queryChats.data.length > 0}
    {#each $queryChats.data as { chat_id, chat_name, last_message_text, own }, i (chat_id)}
      <li>
        <a
          href={route((p) => `/profile/chat/${p(chat_id)}`)}
          class="group relative block overflow-hidden rounded-lg transition after:absolute after:-right-3 after:top-0 after:h-full after:w-3 after:bg-sky-900 after:transition-transform"
          aria-current="page"
          bind:this={chatNodes[i]}
        >
          <div class="rounded-lg border-2 border-app-blue-100 p-3">
            <span class="text-xl">{chat_name}</span>
            {#if own}
              <span
                class="block w-full overflow-x-hidden text-ellipsis whitespace-nowrap transition-[font-weight] font-normal"
              >
                <span class="text-app-blue-600">You:</span> {last_message_text}
              </span>
            {:else}
              <span class="block w-full overflow-x-hidden text-ellipsis whitespace-nowrap transition-[font-weight] font-bold">
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
