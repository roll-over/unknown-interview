<script lang="ts">
	import { Autocomplete, type AutocompleteOption } from '@skeletonlabs/skeleton';
	import { professions } from './common';

	export let selectedProfession: string;
	$: autocompleteProfessions = professions.map((profession) => ({
		value: profession,
		label: profession
	})) satisfies AutocompleteOption[];
</script>

<div class="flex flex-col gap-2">
	<input
		bind:value={selectedProfession}
		class="bg-app-blue-50 caret-app-blue-600 w-full rounded p-2 text-xs text-black/60"
		placeholder="profession..."
	/>
	<Autocomplete
		input={selectedProfession}
		options={autocompleteProfessions}
		denylist={[selectedProfession]}
		on:selection={(e) => {
			selectedProfession = e.detail.value;
		}}
		class="bg-app-blue-50 rounded-xl p-4"
		regionList="flex flex-col gap-1"
		regionItem="bg-app-blue-400 rounded-lg"
		regionButton="w-full text-left px-3"
	/>
</div>
