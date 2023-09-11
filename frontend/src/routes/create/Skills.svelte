<script lang="ts">
	import { Autocomplete, type AutocompleteOption } from '@skeletonlabs/skeleton';
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
</script>

<div class="flex flex-col gap-2">
	<div class="bg-app-blue-100 rounded-xl px-2 py-1">
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
				class="caret-app-blue-900 w-11 rounded p-2 text-xs text-black/60"
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
			class="bg-app-blue-100 rounded-xl p-4"
			regionList="flex flex-col gap-1"
			regionItem="bg-app-blue-500 rounded-lg"
			regionButton="w-full text-left px-3"
		/>
	</div>
</div>
