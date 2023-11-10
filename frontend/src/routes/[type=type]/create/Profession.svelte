<script lang="ts">
	import { Autocomplete, type AutocompleteOption } from '@skeletonlabs/skeleton';

	const professions = [
		'programmer',
		'designer',
		'project manager',
		'engineer',
		'devops',
		'full-stack',
		'frontend',
		'backend'
	];

	export let selectedProfession: string;
	$: autocompleteProfessions = professions.map((profession) => ({
		value: profession,
		label: profession
	})) satisfies AutocompleteOption[];
</script>

<div class="flex flex-col gap-2">
	<input
		bind:value={selectedProfession}
		class="w-full rounded-md bg-app-blue-50 p-2 text-xs text-black caret-app-blue-600"
		placeholder="profession..."
	/>
	<Autocomplete
		input={selectedProfession}
		options={autocompleteProfessions}
		denylist={[selectedProfession]}
		on:selection={(e) => {
			selectedProfession = e.detail.value;
		}}
		class="rounded bg-app-blue-50 p-4"
		regionList="flex flex-col gap-2"
		regionItem="bg-app-blue-600 hover:bg-app-blue-400 transition-colors rounded-md"
		regionButton="w-full text-left text-white px-3"
	/>
</div>
