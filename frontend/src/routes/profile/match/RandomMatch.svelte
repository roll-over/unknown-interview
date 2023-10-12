<script lang="ts">
	import ThumbsUpIcon from '~icons/material-symbols/thumb-up-outline';
	import Match, { type MatchData, type Matcher } from './Match.svelte';

	export let matcher: Matcher | undefined = undefined;
	export let matchData: MatchData | undefined = undefined;
	export let like: () => void;
	export let dislike: () => void;
</script>

<div class="flex h-full min-h-0 flex-col">
	<div class="h-full space-y-5 overflow-y-auto rounded-lg bg-app-blue-50 p-5 pb-16">
		{#if matchData}
			<h2 class="mx-auto w-fit text-center font-title text-3xl capitalize">
				{matchData.grade}
				{matchData.profession.name}
			</h2>
			<Match
				{matcher}
				{matchData}
			/>
		{:else}
			Loading...
		{/if}
	</div>
	<div class="flex h-16 -translate-y-full justify-between">
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
	</div>
</div>
