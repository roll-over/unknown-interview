<script lang="ts">
	import { Autocomplete, type AutocompleteOption } from '@skeletonlabs/skeleton';
	import { slide } from 'svelte/transition';
	import { skills } from './common';

	export let selectedSkills: string[];
	let newSkill = '';

	// As of now Autocomplete uses whole value as a key so these values have to be stable
	// otherwise it messes up transitions
	$: autocompleteSkills = skills.map((skill) => ({
		value: skill,
		label: skill
	})) satisfies AutocompleteOption[];
</script>

<div class="flex flex-col gap-2">
	<div class="rounded-md bg-app-blue-50 px-2 py-1">
		<div class="flex flex-wrap gap-2">
			{#each selectedSkills as skill, i (skill)}
				<button
					class="chip bg-app-blue-100"
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
				class="w-11 rounded p-2 text-xs caret-app-blue-600"
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
			class="rounded bg-app-blue-50 p-4"
			regionList="flex flex-col gap-1"
			regionItem="bg-app-blue-600 hover:bg-app-blue-400 transition-colors rounded-md"
			regionButton="w-full text-left text-white px-3"
		/>
	</div>
</div>
