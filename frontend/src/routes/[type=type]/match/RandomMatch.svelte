<script lang="ts">
	import ThumbsUpIcon from '~icons/material-symbols/thumb-up-outline';
	import Match, { type MatchData, type Matcher } from './Match.svelte';

	export let matcher: Matcher = {};
	export let matchData: MatchData;
	export let like: () => void;
	export let dislike: () => void;

	const sendRelation = async (relation: string) => {
   let cv_id = matcher.random_id;
   let vacancy_id = matcher.user_id;

   if (window.location.pathname.includes('/cv/match/')) {
       cv_id = matcher.user_id;
       vacancy_id = matcher.random_id;
   }

   await fetch('/api/v1/relation', {
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
};

const handleLike = () => {
   like();
   sendRelation('liked');
};

const handleDislike = () => {
   dislike();
   sendRelation('disliked');
};
</script>

<Match
	{matcher}
	{matchData}
	mainClass="pb-16"
	footerClass="flex -translate-y-full justify-between"
>
	<svelte:fragment slot="header">
		<h2 class="mx-auto w-fit text-center font-title text-3xl capitalize">
			{matchData.grade}
			{matchData.profession.name}
		</h2>
	</svelte:fragment>

	<svelte:fragment slot="footer">
		<button
			aria-label="dislike"
			class="aspect-square h-32 -scale-100 rounded-full bg-app-blue-600 p-4 text-white transition-colors current:bg-red-400"
			on:click={handleDislike}
		>
			<ThumbsUpIcon class="h-full w-full" />
		</button>
		<button
			aria-label="like"
			class="aspect-square h-32 rounded-full bg-app-blue-600 p-4 text-white transition-colors current:bg-green-400"
			on:click={handleLike}
		>
			<ThumbsUpIcon class="h-full w-full" />
		</button>
	</svelte:fragment>
</Match>
