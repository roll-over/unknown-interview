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
	<div class="bg-app-blue-50 dark:bg-app-dark-gray rounded-md px-2 py-1">
		<div class="flex flex-wrap gap-2">
			{#each selectedSkills as skill, i (skill)}
				<button
					class="chip bg-app-blue-100 dark:bg-app-dark-light text-xl"
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
				class="caret-app-blue-600 w-28 rounded pl-3 p-2 text-xl"
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
				placeholder="new skill"
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
			class="bg-app-blue-50 dark:bg-app-dark-gray rounded p-4"
			regionList="flex flex-col gap-2"
			regionItem="bg-app-blue-600 dark:hover:bg-app-dark-light hover:bg-app-blue-400 dark:bg-app-dark-blue transition-colors rounded-md"
			regionButton="w-full text-left text-white px-3"
		/>
	</div>
</div>
