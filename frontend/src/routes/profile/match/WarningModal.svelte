<script lang="ts">
	import CheerIcon from '~icons/material-symbols/cheer-outline';

	export let hasMatches: boolean;
</script>

<div
	class="flex max-w-3xl flex-col items-center justify-center gap-5 rounded-lg bg-app-blue-50 px-20 py-40"
>
	<p class="text-center text-6xl">
		{hasMatches ? 'Please select a CV' : 'Fill out a resume for further use of the service'}
	</p>
	<CheerIcon class="h-60 w-60 text-app-blue-600" />
</div>
