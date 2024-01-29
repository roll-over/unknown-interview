<script lang="ts">
	import { Autocomplete, type AutocompleteOption } from '@skeletonlabs/skeleton';
	import { onMount } from 'svelte';

	let professions: string[] = [];

	async function fetchProfessions() {
		try {
			const response = await fetch('/api/v1/professions/');
			const data = await response.json();
			professions = data.map((profession) => profession.name);
		} catch (error) {
			console.error('Error fetching professions:', error);
		}
	}
	onMount(fetchProfessions);

	export let selectedProfession: string;
	$: autocompleteProfessions = professions.map((profession) => ({
		value: profession,
		label: profession
	})) satisfies AutocompleteOption[];

	// Improved the condition for better readability
	$: showAutocomplete =
		selectedProfession &&
		selectedProfession.length > 0 &&
		autocompleteProfessions.some((option) =>
			option.label.toLowerCase().startsWith(selectedProfession.toLowerCase())
		) &&
		!professions.includes(selectedProfession);
</script>

<div class="flex flex-col gap-2 md:text-xl text-base">
	<input
		bind:value={selectedProfession}
		class="w-full rounded-md bg-app-blue-50 px-4 py-0.5 md:text-xl text-base text-black caret-app-blue-600 dark:bg-app-dark-gray dark:text-white dark:outline-white"
		placeholder="profession..."
	/>
	{#if showAutocomplete}
		<Autocomplete
			input={selectedProfession}
			options={autocompleteProfessions}
			denylist={[selectedProfession]}
			on:selection={(e) => {
				selectedProfession = e.detail.value;
			}}
			class="rounded-md bg-app-blue-50 px-4 py-2 dark:bg-app-dark-gray"
			regionList="flex flex-col gap-2"
			regionItem="bg-app-blue-600 dark:hover:bg-app-dark-light dark:bg-app-dark-blue hover:bg-app-blue-400 transition-colors rounded-md"
			regionButton="w-full md:text-xl text-base text-white px-4 py-0.5"
		/>
	{/if}
</div>
