<script lang="ts">
	import type { AutocompleteOption } from '@skeletonlabs/skeleton';
	import { Autocomplete } from '@skeletonlabs/skeleton';
	import { skills } from './common';
	import { slide } from 'svelte/transition';

	export let selectedSkills: string[];
	let newSkill = '';

	// As of now Autocomplete uses whole value as a key so these values have to be stable
	// otherwise it messes up transitions
	$: autocompleteSkills = skills.map((skill) => ({
		value: skill,
		label: skill
	})) satisfies AutocompleteOption[];

	$: filteredSkills = autocompleteSkills.filter((x) => !selectedSkills.includes(x.value));
</script>

<div class="flex flex-col gap-2">
	<div class="bg-app-blue-100 w-80 rounded-xl p-4">
		<div class="flex flex-wrap gap-2">
			{#each selectedSkills as skill, i (skill)}
				<button
					class="chip bg-app-blue-300"
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
				class="caret-app-blue-900 w-11 rounded px-2 text-xs text-black/[.64]"
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
			options={filteredSkills}
			on:selection={(e) => {
				const { value } = e.detail;
				if (selectedSkills.includes(value)) return;

				selectedSkills.push(value);
				selectedSkills = selectedSkills;
			}}
			class="bg-app-blue-100 rounded-xl p-8"
			regionList="flex flex-col gap-1"
			regionItem="bg-app-blue-500 rounded-lg"
		/>
	</div>
</div>
