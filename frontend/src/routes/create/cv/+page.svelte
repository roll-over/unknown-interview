<script lang="ts">
	import { persisted } from 'svelte-local-storage-store';
	import Skills from '../Skills.svelte';
	import {
		currencies,
		defaultCVState,
		grades,
		positions,
		professions,
		type CVState
	} from '../common';

	const CVStateData = persisted<CVState>('CVState', defaultCVState);
</script>

<form class="flex flex-col items-start gap-3 p-3">
	<h1>Your Resume</h1>
	<fieldset>
		<legend>Necessary position</legend>
		<div class="flex gap-4">
			{#each positions as position}
				<label
					class="rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white shadow-blue-300 focus-within:outline-none focus-within:ring-4 focus-within:ring-blue-300 hover:bg-blue-800"
					class:shadow-md={$CVStateData.position === position}
				>
					{position}
					<input
						type="radio"
						name="position"
						bind:group={$CVStateData.position}
						value={position}
						class="absolute w-0 opacity-0"
					/>
				</label>
			{/each}
		</div>
	</fieldset>
	<fieldset>
		<legend>Necessary grade</legend>
		<div class="flex gap-4">
			{#each grades as grade}
				<label
					class="rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white shadow-blue-300 focus-within:outline-none focus-within:ring-4 focus-within:ring-blue-300 hover:bg-blue-800"
					class:shadow-md={$CVStateData.grade === grade}
				>
					{grade}
					<input
						type="radio"
						name="grade"
						bind:group={$CVStateData.grade}
						value={grade}
						class="absolute w-0 opacity-0"
					/>
				</label>
			{/each}
		</div>
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
					bind:value={$CVStateData.salaryFork.min}
				/>
			</label>
			<label>
				max:
				<input
					type="number"
					min={$CVStateData.salaryFork.min}
					class="rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500"
					bind:value={$CVStateData.salaryFork.max}
				/>
			</label>
			<label>
				currency:
				<select
					class="rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500"
					bind:value={$CVStateData.salaryFork.currency}
				>
					{#each currencies as currency}
						<option value={currency}>{currency}</option>
					{/each}
				</select>
			</label>
		</div>
	</fieldset>
	<fieldset>
		<legend>Necessary profession</legend>
		<div class="flex gap-4">
			{#each professions as profession}
				<label
					class="rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white shadow-blue-300 focus-within:outline-none focus-within:ring-4 focus-within:ring-blue-300 hover:bg-blue-800"
					class:shadow-md={$CVStateData.profession === profession}
				>
					{profession}
					<input
						type="radio"
						name="profession"
						bind:group={$CVStateData.profession}
						value={profession}
						class="absolute w-0 opacity-0"
					/>
				</label>
			{/each}
		</div>
	</fieldset>
	<fieldset>
		<h2>Necessary skills</h2>
		<Skills bind:selectedSkills={$CVStateData.skills} />
	</fieldset>
	<button
		class="rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white shadow-blue-300 focus-within:outline-none focus-within:ring-4 focus-within:ring-blue-300 hover:bg-blue-800"
	>
		SUBMIT
	</button>
</form>
