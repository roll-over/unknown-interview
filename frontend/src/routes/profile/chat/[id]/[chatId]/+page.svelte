<script lang="ts">
  import { page } from '$app/stores';
  import { createGetQuery } from '$lib/api';
  import { createQuery, createMutation } from '@tanstack/svelte-query';
  import { dateFormatter, type Chat, type Message, formatTimestamp } from '../interFace';

  // Функция для группировки элементов массива по заданному ключу
  function groupBy<T>(array: T[], keyFunc: (item: T) => string) {
    return array.reduce((result: Record<string, T[]>, item) => {
      const key = keyFunc(item);
      result[key] = result[key] || [];
      result[key].push(item);
      return result;
    }, {});
  }

  // Определение типа для чата с сообщениями
  type ChatWithMessages = {
    chat_name: string;
    messages: (Message & { chat_name: string })[];
  } | undefined;

  // Инициализация переменной для текста нового сообщения
	let newMessageText = '';

// Создание мутации для добавления нового сообщения
const addMessageMutation = createMutation<
  string, // Тип для нового текста сообщения
  Error,
  Message, // Тип для данных сообщения
  { newMessageText: string } // Тип для параметров мутации
>({
  onMutate: async (newMessageText: string) => {
    // Сохранение текущего состояния сообщений перед мутацией
    const prevMessages = $queryMessage.data?.messages || [];

    // Создание сообщения
    const optimisticMessage: Message = {
      text: newMessageText,
      own: true,
      created_at: new Date().toISOString(),
      chat_name: $queryMessage.data?.chat_name || 'Default Chat Name',
    };

    // Обновление данных запроса
    $queryMessage.data = {
      ...$queryMessage.data!,
      messages: [...prevMessages, optimisticMessage],
    };

    // Очистка поля ввода
    newMessageText = '';

    // Возврат предыдущего состояния для возможной отмены в случае ошибки
    return () => {
      $queryMessage.data = {
        ...$queryMessage.data!,
        messages: prevMessages,
      };
    };
  },
  onSuccess: async (data) => {
    // Проверка структуры полученных данных
    const receivedMessage: Message = {
      text: (data as Message).text || null,
      own: (data as Message).own || null,
      created_at: (data as Message).created_at || null,
      chat_name: $queryMessage.data?.chat_name || 'Default Chat Name',
    };

    // Обновление данных запроса после успешной мутации
    $queryMessage.data = {
      ...$queryMessage.data!,
      messages: [...($queryMessage.data?.messages || []), receivedMessage],
    };
  },
});

// Функция для отправки сообщения
const sendMessage = async () => {
  // Проверка, что текст нового сообщения не пустой
  if (newMessageText.trim() !== '') {
    try {
      // Выполнение мутации (отправка сообщения на сервер)
      await addMessageMutation.mutate({ newMessageText });
    } catch (error) {
      // Обработка ошибки при необходимости
      console.error('Error sending message:', error);
    }
  }
};

  // Создание запроса для получения чата
  $: messagesGet = createGetQuery<Chat>(`/api/v1/chats/${$page.params.id || ''}`);

  // Создание запроса с использованием Svelte Query
  $: queryMessage = createQuery({
    queryKey: messagesGet.key,
    async queryFn() {
      try {
        // Выполнение запроса для получения данных о чате
        const res = await messagesGet.runQuery();
        const data = res.data || { chat_name: '', messages: [] };

        // Возврат данных
        return {
          chat_name: data.chat_name,
          messages: (data.messages || []).map((message: Message) => ({
            text: message.text || null,
            own: message.own || null,
            created_at: message.created_at || null,
            chat_name: data.chat_name || 'Default Chat Name',
          })),
        };
      } catch (error) {
        throw error;
      }
    },
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
  
  <div class="flex gap-2 px-16 py-10 font-title outline outline-2 outline-sky-900">
    <div class="grow rounded-3xl p-4 outline outline-1 outline-app-blue-600 focus-within:outline-2">
      <input
        bind:value={newMessageText}
        placeholder="Type your message..."
        class="flex-grow px-4 py-2 mr-4 border rounded-lg focus:outline-none"
      />
    </div>
    <button on:click={sendMessage} class="px-4 py-2 text-white bg-blue-500 rounded-lg">
      Send
    </button>
  </div>
{:else}
  <div class="row-span-full m-auto">Loading...</div>
{/if}
