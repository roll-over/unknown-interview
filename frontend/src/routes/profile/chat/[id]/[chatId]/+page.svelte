<script lang="ts">
  import { page } from '$app/stores';
  import { createGetQuery } from '$lib/api';
  import { createQuery } from '@tanstack/svelte-query';
	import { dateFormatter, type Chat, type Message, formatTimestamp } from '../interFace';

 function groupBy<T>(array: T[], keyFunc: (item: T) => string) {
    return array.reduce((result: Record<string, T[]>, item) => {
      const key = keyFunc(item);
      result[key] = result[key] || [];
      result[key].push(item);
      return result;
    }, {});
  }

  $: messagesGet = createGetQuery<Chat>(`/api/v1/chats/${$page.params.id || ''}`);

		$: queryMessage = createQuery({
  queryKey: messagesGet.key,
  async queryFn() {
    try {
      const res = await messagesGet.runQuery();
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
</script>

{#if $queryMessage.isSuccess && $queryMessage.data}
  {@const messageGroups = groupBy($queryMessage.data.messages, (msg) =>
    dateFormatter(msg.created_at)
  )}

  {#each Object.entries(messageGroups) as [date, messages]}
    {#if messages.length > 0}
      <div class="grid h-full grid-rows-5 border-2 border-l-0 border-sky-900">
        <div class="row-span-4 flex flex-col transition-opacity">
          <p class="bg-app-blue-50 py-4 text-center text-xl outline outline-2 outline-sky-900">{$queryMessage.data.chat_name}</p>
          <div class="overflow-y-hidden p-5">
            <div class="h-full overflow-y-auto px-10 text-xl">
              <p class="p-3 text-center">{date}</p>
              <div class="flex flex-col gap-2">
                {#each messages as msg (msg.created_at)}
                  {@const isYourMessage = msg.own}
                  <div
                    class="max-w-lg"
                    class:max-2xl:self-end={isYourMessage}
                  >
                    <div
                      class="rounded-lg px-4 py-2 {isYourMessage
                        ? 'bg-app-blue-50'
                        : 'bg-app-blue-100'}"
                    >
                      {msg.text}
                    </div>
                    <p
                      class="text-neutral-700/50"
                      class:max-2xl:text-right={isYourMessage}
                    >
                      {formatTimestamp(msg.created_at)}
                    </p>
                  </div>
                {/each}
              </div>
            </div>
          </div>
        </div>
      </div>
    {/if}
  {/each}
{:else}
  <div class="row-span-full m-auto">Loading...</div>
{/if}
