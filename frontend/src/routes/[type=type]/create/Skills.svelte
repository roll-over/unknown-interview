<script lang="ts">
	import { Autocomplete, type AutocompleteOption } from '@skeletonlabs/skeleton';
	import { slide } from 'svelte/transition';
	import { onMount } from 'svelte';

	let skills: string[] = [];
	async function fetchSkills() {
		try {
			const response = await fetch('/api/v1/skills/');
			const data = await response.json();
			skills = data.map((skill) => skill.name);
		} catch (error) {
			console.error('Error fetching skills:', error);
		}
	}
	onMount(fetchSkills);

	export let selectedSkills: string[] = [];
	let newSkill = '';

	$: autocompleteSkills = skills.map((skill) => ({
		value: skill,
		label: skill
	})) satisfies AutocompleteOption[];

	// Add a reactive variable to control Autocomplete visibility
	$: showAutocomplete =
		newSkill &&
		newSkill.length > 0 &&
		autocompleteSkills.some((option) =>
			option.label.toLowerCase().startsWith(newSkill.toLowerCase())
		) &&
		!selectedSkills.includes(newSkill);
</script>

<div class="flex flex-col gap-2 text-xl">
	<div class="rounded-md bg-app-blue-50 px-2 py-1 dark:bg-app-dark-gray">
		<div class="flex flex-wrap gap-2">
			{#each selectedSkills as skill, i (skill)}
				<button
					class="chip bg-app-blue-100 px-4 py-0.5 text-xl dark:bg-app-dark-light"
					type="button"
					on:click={() => {
						selectedSkills = selectedSkills.filter((_, index) => index !== i);
					}}
					transition:slide={{ axis: 'x' }}
				>
					{skill}
				</button>
			{/each}
			<input
				class="w-28 rounded bg-transparent px-4 py-0.5 pl-3 text-xl caret-app-blue-600 dark:outline-white"
				bind:value={newSkill}
				on:keydown={(e) => {
					if (e.key === 'Enter') {
						e.preventDefault();
						if (!newSkill || selectedSkills.includes(newSkill)) return;
						selectedSkills = [...selectedSkills, newSkill];
						newSkill = '';
					}
				}}
				placeholder="new skill"
			/>
		</div>
	</div>
	{#if showAutocomplete}
		<Autocomplete
			input={newSkill}
			options={autocompleteSkills}
			denylist={selectedSkills}
			on:selection={(e) => {
				selectedSkills = [...selectedSkills, e.detail.value];
				newSkill = '';
			}}
			class="rounded-md bg-app-blue-50 p-4 px-4 py-2 dark:bg-app-dark-gray"
			regionList="flex flex-col gap-2"
			regionItem="bg-app-blue-600 dark:hover:bg-app-dark-light hover:bg-app-blue-400 dark:bg-app-dark-blue transition-colors rounded-md"
			regionButton="w-full  text-left text-white px-4 py-0.5"
		/>
	{/if}
</div>
