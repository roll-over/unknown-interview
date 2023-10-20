<script lang="ts">
	export let data;
</script>

<div class="space-y-14 p-5">
	<div class="space-y-8">
		<h1 class="text-6xl text-gray-900">Hide-Hire</h1>
		<p class="text-2xl">
			A project for anonymous job search - where before the first call and/or within correspondence,
			the candidate and the employer will not know anything about each other except what is
			indicated in the cv.
		</p>
	</div>

	<div class="space-y-8">
		<h2 class="text-5xl text-gray-900">Contributors</h2>
		<p class="text-2xl">These guys made this awesome</p>
		<ul class="grid grid-cols-4 gap-5">
			{#each data.contributorsList as contributor (contributor.id)}
				<li class="flex flex-col items-center gap-2">
					<img
						class="grow px-8 drop-shadow-lg"
						src={contributor.avatar_url}
						alt="avatar contributor"
					/>
					<div class="text-2xl">
						{#if contributor.html_url}
							<a
								href={contributor.html_url}
								target="_blank"
								rel="noreferrer"
							>
								{contributor.login}
							</a>
						{:else}
							<p>{contributor.login}</p>
						{/if}
					</div>
				</li>
			{/each}
		</ul>
	</div>
</div>
