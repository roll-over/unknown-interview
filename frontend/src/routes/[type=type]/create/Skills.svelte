<script lang="ts">
	import { Autocomplete, type AutocompleteOption } from '@skeletonlabs/skeleton';
	import { slide } from 'svelte/transition';

	const skills = ['java', 'javascript', 'python', 'c#', 'c++', 'php', 'swift'];

	export let selectedSkills: string[];
	let newSkill = '';

	// As of now Autocomplete uses whole value as a key so these values have to be stable
	// otherwise it messes up transitions
	$: autocompleteSkills = skills.map((skill) => ({
		value: skill,
		label: skill
	})) satisfies AutocompleteOption[];
</script>

<div class="flex flex-col gap-2 text-xl">
	<div class="rounded-md bg-app-blue-50 px-2 py-1 dark:bg-app-dark-gray">
		<div class="flex flex-wrap gap-2">
			{#each selectedSkills as skill, i (skill)}
				<button
					class="chip bg-app-blue-100 text-xl dark:bg-app-dark-light"
					type="button"
					on:click={() => {
						selectedSkills.splice(i, 1);
						selectedSkills = selectedSkills;
					}}
					transition:slide={{ axis: 'x' }}
				>
					{skill}
				</button>
			{/each}
			<input
				class="w-20 rounded p-2 text-xl caret-app-blue-600"
				bind:value={newSkill}
				on:keydown={(e) => {
					if (e.key === 'Enter') {
						e.preventDefault();
						if (!newSkill || selectedSkills.includes(newSkill)) return;
						selectedSkills.push(newSkill);
						selectedSkills = selectedSkills;
						newSkill = '';
					}
				}}
				placeholder="skill..."
			/>
		</div>
	</div>
	<div>
		<Autocomplete
			input={newSkill}
			options={autocompleteSkills}
			denylist={selectedSkills}
			on:selection={(e) => {
				selectedSkills.push(e.detail.value);
				selectedSkills = selectedSkills;
			}}
			class="rounded bg-app-blue-50 p-4 dark:bg-app-dark-gray"
			regionList="flex flex-col gap-2"
			regionItem="bg-app-blue-600 dark:hover:bg-app-dark-light hover:bg-app-blue-400 dark:bg-app-dark-blue transition-colors rounded-md"
			regionButton="w-full text-left text-white px-3"
		/>
	</div>
</div>
