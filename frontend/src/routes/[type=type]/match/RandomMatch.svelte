<script lang="ts">
	import ThumbsUpIcon from '~icons/material-symbols/thumb-up-outline';
	import Match, { type MatchData, type Matcher } from './Match.svelte';
	import { page } from '$app/stores';

	export let matcher: Matcher = {};
	export let matchData: MatchData;
	export let like: () => void;
	export let dislike: () => void;

	const sendRelation = async (relation: string) => {
		let cv_id = matcher.random_id;
		let vacancy_id = matcher.user_id;

		if ($page.params.type === 'cv') {
			cv_id = matcher.user_id;
			vacancy_id = matcher.random_id;
		}

		try {
			const response = await fetch('/api/v1/relation', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					cv_id,
					vacancy_id,
					relation
				})
			});
			if (response.ok) {
				console.log('Relation sent successfully');
				location.reload();
			} else {
				console.error('Failed to send relation:', response.status, response.statusText);
			}
		} catch (error) {
			console.error('Error during fetch:', error);
		}
	};

	const handleLike = () => {
		like();
		sendRelation('liked');
	};

	const handleDislike = () => {
		dislike();
		sendRelation('disliked');
	};

	const isMatchDataAvailable: boolean = !!matchData;
</script>

<Match
	{matcher}
	{matchData}
	mainClass="pb-16 md:text-3xl text-sm"
	footerClass="flex -translate-y-full justify-between"
>
	<svelte:fragment slot="header">
		{#if isMatchDataAvailable}
			<h2 class="mx-auto w-fit text-center font-title capitalize">
				{matchData.grade}
				{matchData.profession.name}
			</h2>
		{:else}
			<p class="text-center">Please wait. We are looking for the best match</p>
		{/if}
	</svelte:fragment>

	<svelte:fragment slot="footer">
		<button
			aria-label="dislike"
			class="aspect-square h-20 -scale-100 rounded-full bg-app-blue-600 p-4 text-white transition-colors current:bg-red-400 dark:bg-app-dark-blue dark:current:bg-red-400 md:h-32"
			on:click={handleDislike}
		>
			<ThumbsUpIcon class="h-full w-full" />
		</button>
		<button
			aria-label="like"
			class="aspect-square h-20 rounded-full bg-app-blue-600 p-4 text-white transition-colors current:bg-green-400 dark:bg-app-dark-blue dark:current:bg-green-400 md:h-32"
			on:click={handleLike}
		>
			<ThumbsUpIcon class="h-full w-full" />
		</button>
	</svelte:fragment>
</Match>
