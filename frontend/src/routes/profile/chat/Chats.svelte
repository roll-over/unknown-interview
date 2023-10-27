<script lang="ts">
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	import { YourID, type ChatGist } from './getChats';
	import { route } from '$lib/utils/route';

	export let chats: ChatGist[];
	let chatNodes: HTMLAnchorElement[] = [];
	onMount(() => {
		const selectedChatNode = chatNodes.find((node) => node.ariaCurrent);
		if (!selectedChatNode) return;
		selectedChatNode.scrollIntoView({ block: 'nearest' });
	});
</script>

<ul class="h-full overflow-y-scroll">
	{#each chats as chat, i (chat.id)}
		<li class="mb-4 rounded-md border-2 border-blue-100">
			<a
				href={route((p) => `/profile/chat/${p(chat.id)}`)}
				class="flex flex-col p-1 transition-colors aria-[current]:bg-app-blue-50"
				aria-current={$page.params.id === chat.id || undefined}
				bind:this={chatNodes[i]}
			>
				<span class="font-bold">{chat.label}</span>
				{#if chat.lastMessage}
					<span class="overflow-hidden text-ellipsis whitespace-nowrap">
						{#if chat.lastMessage.author.id === YourID}
							<span class="opacity-80">You:</span>
						{/if}
						{chat.lastMessage.content}
					</span>
				{/if}
			</a>
		</li>
	{/each}
</ul>
