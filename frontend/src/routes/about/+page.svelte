<script lang="ts">
	export let data;
</script>

<div class="flex flex-col items-center justify-center">
	<div
		class="flex w-full items-center justify-between bg-gradient-to-b from-[#8cd1fc] to-[#EAF4FD] px-5 py-16"
	>
		<div class="max-w-[690px] space-y-12">
			<p class="text-2xl font-medium">
				Service for job search and candidates. Project for anonymous job search - where until the
				first phone call and/or during correspondence.
			</p>
			<p class="text-2xl font-medium">
				The candidate and the employer will not know anything about each other except what is stated
				in the CV and basic questions about experience, tech stack, level, salary range, and other
				non-deanonymizing information.
			</p>
		</div>
		<div class="items-cente flex flex-col space-y-8">
			<img
				src="/hidehire.webp"
				class=""
				alt="hide hire"
			/>
			<p class="text-center text-2xl uppercase">Skills first<br />Unbiased Hiring</p>
		</div>
	</div>

	<div class="flex w-full items-center justify-between bg-[#EAF4FD] px-5 py-16">
		<div class="space-y-8">
			<div class="max-w-2xl space-y-4">
				<p class="text-3xl font-normal uppercase">Our mission</p>
				<p class="text-2xl">Make hiring fair and transparent and fight against discrimination</p>
			</div>
			<div class="flex items-center gap-2">
				<p class="text-3xl font-normal uppercase">we are here:</p>
				<a
					class="inline-block"
					target="_blank"
					href="https://twitter.com/roll_over_group"
				>
					<img
						src="/linkedin.webp"
						class="h-20 w-20"
						alt="linkedin logo"
					/>
				</a>
				<a
					class="inline-block"
					target="_blank"
					href="https://www.linkedin.com/company/hide-hire"
				>
					<img
						src="/twitter.webp"
						class="h-20 w-20"
						alt="twitter logo"
					/>
				</a>
			</div>
			<div class="flex items-center gap-2">
				<p class="max-w-sm text-2xl">
					hide-hire is part of the roll-over group of open source projects
				</p>
				<a
					class="inline-block"
					target="_blank"
					href="mailto:red.flags.service@gmail.com"
				>
					<img
						src="/roll-over.webp"
						class="h-16 w-24"
						alt="roll-over logo"
					/>
				</a>
			</div>
		</div>

		<div class="flex flex-col items-center space-y-8">
			<p class="max-w-sm text-center text-2xl font-normal uppercase">
				the people who created this product for you
			</p>
			<ul class="grid max-w-md grid-cols-4 gap-2">
				{#each data.contributorsList as contributor (contributor.id)}
					<li class="">
						<img
							class="grow"
							src={contributor.avatar_url}
							alt="avatar contributor"
						/>
					</li>
				{/each}
			</ul>
		</div>
	</div>
</div>
