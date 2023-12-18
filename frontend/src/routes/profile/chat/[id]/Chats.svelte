<script lang="ts">
  import { page } from '$app/stores';
  import { onMount } from 'svelte';
  import { route } from '$lib/utils/route';
  import { createGetQuery } from '$lib/api';
  import { createQuery } from '@tanstack/svelte-query';
	import type { Chats } from './interFace';
  
	const getChats = createGetQuery('/api/v1/chats/', {
  params: { query: { record_id: $page.params.id || '' } }
	});
 
 $: queryChats = createQuery({
  queryKey: getChats.key,
  async queryFn() {
    const res = await getChats.runQuery();
    return (res.data || []).map((chat: Chats) => {
      const lastMessage = chat.last_message && chat.last_message.length > 0 ? chat.last_message[0] : null;
      return {
        chat_id: chat.chat_id,
        chat_name: chat.chat_name,
        last_message_text: lastMessage ? lastMessage.text : null,
        own: lastMessage ? lastMessage.own : null
      };
    });
  }
});

 </script> 
 <ul class="flex flex-col gap-3 overflow-y-auto pr-10">
  {#if $queryChats.data && $queryChats.data.length > 0}
    {#each $queryChats.data as { chat_id, chat_name, last_message_text, own } (chat_id)}
      <li>
        <a
          href={`/profile/chat/${chat_id}`}
          class="group relative block overflow-hidden rounded-lg transition after:absolute after:-right-3 after:top-0 after:h-full after:w-3 after:bg-sky-900 after:transition-transform"
          aria-current="page">
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