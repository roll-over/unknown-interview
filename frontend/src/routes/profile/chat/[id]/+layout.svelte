<script lang="ts">
	import { page } from '$app/stores';
	import Chats from './Chats.svelte';

	let chat_id: string | undefined;
</script>

<div class="grid h-full grid-rows-4 dark:text-white">
	<div class="row-span-4 grid grid-cols-1 md:grid-cols-4">
		<div
			class="{$page.params.chatId === chat_id
				? 'md:flex'
				: 'hidden'} col-span-1 flex-col overflow-y-hidden border-2 border-l-0 border-white bg-white p-5 pr-5 dark:border-black dark:bg-app-dark-amber md:flex md:border-sky-900 md:bg-app-blue-50 md:pr-1 md:dark:border-app-dark-light md:dark:bg-app-dark-gray"
		>
			<h1 class="pb-5 text-center font-title text-lg md:text-xl">Chats</h1>
			<Chats />
		</div>
		<div class="col-span-3 flex justify-center overflow-y-hidden">
			<slot />
		</div>
	</div>
</div>
