<script lang="ts">
	import MaterialSymbolsNewWindow from '~icons/material-symbols/new-window';
	import { page } from '$app/stores';
  import { createGetQuery } from '$lib/api';
  import { createQuery } from '@tanstack/svelte-query';
 
	$: notionGet = createGetQuery(`/api/v1/chats/${$page.params.id || ''}`);

	$: queryNotion = createQuery({
		queryKey: notionGet.key,
		async queryFn() {
			const res = await notionGet.runQuery();
			return res;
		}
	});

	const notes = [
		{ text: 'Modi laboriosam quidem accusantium fugiat repellendus 1', id: '1' },
		{ text: 'Modi laboriosam quidem accusantium fugiat repellendus 2', id: '2' },
		{ text: 'Modi laboriosam quidem accusantium fugiat repellendus 3', id: '3' },
		{ text: 'Modi laboriosam quidem accusantium fugiat repellendus 3', id: '4' },
		{ text: 'Modi laboriosam quidem accusantium fugiat repellendus 3', id: '5' },
		{ text: 'Modi laboriosam quidem accusantium fugiat repellendus 3', id: '6' },
		{ text: 'Modi laboriosam quidem accusantium fugiat repellendus 3', id: '7' },
		{ text: 'Modi laboriosam quidem accusantium fugiat repellendus 3', id: '8' }
	];
</script>
<div class="flex flex-col overflow-y-hidden border-2 border-sky-900">
	<p class="bg-app-blue-50 py-4 text-center text-xl outline outline-2 outline-sky-900">Notes</p>
	<div class="flex flex-col justify-between overflow-y-auto pl-5 pr-5 pt-3">
		<button
			aria-label={'create notion'}
			class="flex items-center pb-5"
			><MaterialSymbolsNewWindow class="mr-4 text-3xl" />ADD NEW NOTE</button
		>
		{#if notes.length}
			<ul class="flex flex-col gap-3 overflow-y-auto pr-5">
				{#each notes as { text, id } (id)}
					<li class="max-w-lg rounded-lg bg-app-blue-50 p-3">
						<p class="p-1">{id}. {text}</p>
					</li>
				{/each}
			</ul>
		{:else}
			<div class="flex h-full w-full items-center justify-center">
				<span> Loading... </span>
			</div>
		{/if}
	</div>
</div>
