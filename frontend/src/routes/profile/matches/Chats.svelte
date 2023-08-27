<script lang="ts">
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	import { YourID, type ChatGist } from './getChats';

	export let chats: ChatGist[];
	let chatNodes: HTMLAnchorElement[] = [];
	onMount(() => {
		const selectedChatNode = chatNodes.find((node) => node.ariaCurrent);
		if (!selectedChatNode) return;
		selectedChatNode.scrollIntoView({ block: 'nearest' });
	});
</script>

<ul class="overflow-y-scroll p-1">
	{#each chats as chat, i (chat.id)}
		<li class="border-b border-b-blue-500 last:border-b-0">
			<a
				href="/profile/matches/{chat.id}"
				class="flex flex-col rounded-md p-1 transition-colors aria-[current]:bg-slate-800"
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
