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

<ul class="flex flex-col gap-3 overflow-y-auto pr-10">
	{#each chats as chat, i (chat.id)}
		<li>
			<a
				href={route((p) => `/profile/chat/${p(chat.id)}`)}
				class="group relative block overflow-hidden rounded-lg text-neutral-800 transition after:absolute after:-right-3 after:top-0 after:h-full after:w-3 after:bg-sky-900 after:transition-transform aria-[current]:translate-x-4 aria-[current]:bg-app-blue-100 aria-[current]:after:-translate-x-3"
				aria-current={$page.params.id === chat.id || undefined}
				bind:this={chatNodes[i]}
			>
				<div class="rounded-lg border-2 border-app-blue-100 p-3">
					<span class="text-xl">{chat.label}</span>
					{#if chat.lastMessage}
						{@const isYourMessage = chat.lastMessage.author.id === YourID}
						<span
							class="block w-full overflow-x-hidden text-ellipsis whitespace-nowrap transition-[font-weight] {isYourMessage
								? ''
								: 'font-bold group-aria-[current]:font-normal'}"
						>
							{#if isYourMessage}
								<span class="text-app-blue-600">You:</span>
							{/if}
							{chat.lastMessage.content}
						</span>
					{/if}
				</div>
			</a>
		</li>
	{/each}
</ul>
