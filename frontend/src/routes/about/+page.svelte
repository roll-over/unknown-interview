<script lang="ts">
	export let data;
	const { contributorsList } = data;
</script>

<div class="flex min-h-screen items-center justify-center">
	<div class="flex flex-col items-center gap-14">
		
		<div class="flex w-full flex-col gap-8 px-5">
			<h1 class="text-6xl text-gray-900">Hide-Hire</h1>
			<p class="text-2xl">
				A project for anonymous job search - where before the first
				call and/or within correspondence, the candidate and the employer
				will not know anything about each other except what is indicated in the cv.
			</p>
		</div>
		
		<div class="w-full flex flex-col gap-8 px-5">
			<h2 class="text-5xl text-gray-900">Contributors</h2>
			<p class="text-2xl">These guys made this awesome</p>
			<ul class="w-full overflow-y-scroll flex flex-wrap">
				{#each contributorsList as contributor, i (contributor.id)}
					<li class="w-1/4 flex flex-col items-center px-4">
						<img class="w-4/5" 
							src={contributor.avatar_url}
							alt="avatar contributor"
						/>
						<p class="text-2xl py-2">{member.login}</p>
						{#if member.html_url}
							<a
								href={member.html_url}
								class="text-xl py-2"
							>github icon</a>
						{/if}
						{#if member.linkedin_url}
							<a
								href={member.linkedin_url}
								class="text-xl py-2"
							>linkedin icon</a>
						{/if}
					</li>
				{/each}
			</ul>
		</div>	
	</div>
</div>