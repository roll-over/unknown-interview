<script lang="ts">
	import type { QueryObserverResult } from '@tanstack/svelte-query';
	import ThumbsUpIcon from '~icons/material-symbols/thumb-up-outline';
	import Match, { type MatchData, type Matcher } from './Match.svelte';

	export let matcher: Matcher = {};
	export let matchQuery: QueryObserverResult<MatchData>;
	export let like: () => void;
	export let dislike: () => void;
</script>

<Match
	{matcher}
	{matchQuery}
	mainClass="pb-16"
	footerClass="flex -translate-y-full justify-between"
>
	<svelte:fragment slot="header">
		{#if matchQuery.data}
			{@const { data } = matchQuery}
			<h2 class="mx-auto w-fit text-center font-title text-3xl capitalize">
				{data.grade}
				{data.profession.name}
			</h2>
		{/if}
	</svelte:fragment>

	<svelte:fragment slot="footer">
		<button
			aria-label="dislike"
			class="aspect-square h-32 -scale-100 rounded-full bg-app-blue-600 p-4 text-white transition-colors current:bg-red-400"
			on:click={dislike}
		>
			<ThumbsUpIcon class="h-full w-full" />
		</button>
		<button
			aria-label="like"
			class="aspect-square h-32 rounded-full bg-app-blue-600 p-4 text-white transition-colors current:bg-green-400"
			on:click={like}
		>
			<ThumbsUpIcon class="h-full w-full" />
		</button>
	</svelte:fragment>
</Match>
