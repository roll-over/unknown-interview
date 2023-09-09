<script lang="ts">
	import { persisted } from 'svelte-local-storage-store';
	import Profession from '../Profession.svelte';
	import Skills from '../Skills.svelte';
	import {
		currencies,
		defaultJobOfferState,
		grades,
		positions,
		type JobOfferState
	} from '../common';
	import RadioGroup from '$lib/components/RadioGroup.svelte';

	const jobOfferData = persisted<JobOfferState>('jobOfferState', defaultJobOfferState);
</script>

<form class="flex flex-col items-start gap-3 p-3">
	<h1>Job Posting</h1>
	<fieldset>
		<legend>Necessary position</legend>
		<RadioGroup
			options={positions}
			bind:value={$jobOfferData.position}
		/>
	</fieldset>
	<fieldset>
		<legend>Necessary grade</legend>
		<RadioGroup
			options={grades}
			bind:value={$jobOfferData.grade}
		/>
	</fieldset>
	<fieldset>
		<legend>Available salary</legend>
		<div class="flex gap-4">
			<label>
				min:
				<input
					type="number"
					min="0"
					class="rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500"
					bind:value={$jobOfferData.salaryFork.min}
				/>
			</label>
			<label>
				max:
				<input
					type="number"
					min={$jobOfferData.salaryFork.min}
					class="rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500"
					bind:value={$jobOfferData.salaryFork.max}
				/>
			</label>
			<label>
				currency:
				<select
					class="rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500"
					bind:value={$jobOfferData.salaryFork.currency}
				>
					{#each currencies as currency}
						<option value={currency}>{currency}</option>
					{/each}
				</select>
			</label>
		</div>
	</fieldset>
	<fieldset class="w-80">
		<legend>Necessary profession</legend>
		<Profession bind:selectedProfession={$jobOfferData.profession} />
	</fieldset>
	<fieldset class="w-80">
		<h2>Necessary skills</h2>
		<Skills bind:selectedSkills={$jobOfferData.skills} />
	</fieldset>
	<button
		class="rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white shadow-blue-300 focus-within:outline-none focus-within:ring-4 focus-within:ring-blue-300 hover:bg-blue-800"
	>
		SUBMIT
	</button>
</form>
