<script lang="ts">
	let Profile =
		'https://images.unsplash.com/photo-1511367461989-f85a21fda167?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D&w=1000&q=80';

	const team = [
		{
			login: 'orby-tech',
			id: 59844758,
			avatar: Profile,
			github_url: 'https://github.com/orby-tech',
			linkedin_url: 'https://www.linkedin.com/in/timur-bondarenko'
		},
		{
			login: 'Dzigr',
			id: 109955706,
			avatar: Profile,
			github_url: 'https://github.com/Dzigr',
			linkedin_url: 'https://www.linkedin.com/in/ibragimov-dmitry/'
		},
		{
			login: 'gmalanchuk',
			id: 69295468,
			avatar: Profile,
			github_url: 'https://github.com/gmalanchuk'
		},
		{
			login: 'HugeLetters',
			id: 119697239,
			avatar: Profile,
			github_url: 'https://github.com/HugeLetters'
		},
		{
			login: 'OvchariK3208',
			id: 68857173,
			avatar: Profile,
			github_url: 'https://github.com/OvchariK3208'
		},
		{
			login: 'Ocean50ul',
			id: 67197290,
			avatar: Profile,
			github_url: 'https://github.com/Ocean50ul'
		}
	];
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
				{#each team as member, i (member.id)}
					<li class="flex w-1/4 flex-col items-center px-4">
						<img
							class="w-4/5"
							src={member.avatar}
							alt="avatar contributor"
						/>
						<p class="py-2 text-2xl">{member.login}</p>
						{#if member.github_url}
							<a
								href={member.github_url}
								class="py-2 text-xl">github icon</a
							>
						{/if}
						{#if member.linkedin_url}
							<a
								href={member.linkedin_url}
								class="py-2 text-xl">linkedin icon</a
							>
						{/if}
					</li>
				{/each}
			</ul>
		</div>
	</div>
</div>
