<script lang="ts">
	export let data;
	const { contributorsList } = data;
</script>

<div class="flex min-h-screen items-center justify-center">
	<div class="flex flex-col items-center gap-14">
		<div class="flex w-full flex-col gap-8 px-5">
			<h1 class="text-6xl text-gray-900">Hide-Hire</h1>
			<p class="text-2xl">
				A project for anonymous job search - where before the first call and/or within
				correspondence, the candidate and the employer will not know anything about each other
				except what is indicated in the cv.
			</p>
		</div>

		<div class="flex w-full flex-col gap-8 px-5">
			<h2 class="text-5xl text-gray-900">Contributors</h2>
			<p class="text-2xl">These guys made this awesome</p>
			<ul class="flex w-full flex-wrap overflow-y-scroll">
				{#each contributorsList as contributor, i (contributor.id)}
					<li class="flex w-1/4 flex-col items-center px-4">
						<img
							class="w-4/5"
							src={contributor.avatar_url}
							alt="avatar contributor"
						/>
						<p class="py-2 text-2xl">{contributor.login}</p>
						{#if contributor.html_url}
							<a
								href={contributor.html_url}
								class="py-2 text-xl">github icon</a
							>
						{/if}
						{#if contributor.linkedin_url}
							<a
								href={contributor.linkedin_url}
								class="py-2 text-xl">linkedin icon</a
							>
						{/if}
					</li>
				{/each}
			</ul>
		</div>
	</div>
</div>
