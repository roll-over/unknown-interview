<script lang="ts">
	import { persisted } from 'svelte-local-storage-store';
	import {
		positions,
		type NewEmployeState,
		grades,
		skills,
		professions,
		currencies,
		defaultNewEmployeState
	} from '../common';

	const newEmployState = persisted<NewEmployeState>('newEmployState', defaultNewEmployeState);
</script>

<form class="flex flex-col items-start gap-3 p-3">
	<h1>Employess search</h1>
	<fieldset>
		<legend>Necessary position</legend>
		<div class="flex gap-4">
			{#each positions as position}
				<label
					class="rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white shadow-blue-300 focus-within:outline-none focus-within:ring-4 focus-within:ring-blue-300 hover:bg-blue-800"
					class:shadow-md={$newEmployState.position === position}
				>
					{position}
					<input
						type="radio"
						name="position"
						bind:group={$newEmployState.position}
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
					class:shadow-md={$newEmployState.grade === grade}
				>
					{grade}
					<input
						type="radio"
						name="grade"
						bind:group={$newEmployState.grade}
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
					bind:value={$newEmployState.salaryFork.min}
				/>
			</label>
			<label>
				max:
				<input
					type="number"
					min={$newEmployState.salaryFork.min}
					class="rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500"
					bind:value={$newEmployState.salaryFork.max}
				/>
			</label>
			<label>
				currency:
				<select
					class="rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500"
					bind:value={$newEmployState.salaryFork.currency}
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
					class:shadow-md={$newEmployState.profession === profession}
				>
					{profession}
					<input
						type="radio"
						name="profession"
						bind:group={$newEmployState.profession}
						value={profession}
						class="absolute w-0 opacity-0"
					/>
				</label>
			{/each}
		</div>
	</fieldset>
	<fieldset>
		<h2>Necessary skills</h2>
		<div class="flex gap-4">
			{#each skills.programmer as skill}
				<label
					class="rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white shadow-blue-300 focus-within:outline-none focus-within:ring-4 focus-within:ring-blue-300 hover:bg-blue-800"
					class:shadow-md={$newEmployState.skills.includes(skill)}
				>
					{skill}
					<input
						type="checkbox"
						name="skills"
						bind:group={$newEmployState.skills}
						value={skill}
						class="absolute w-0 opacity-0"
					/>
				</label>
			{/each}
		</div>
	</fieldset>
	<button
		class="rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white shadow-blue-300 focus-within:outline-none focus-within:ring-4 focus-within:ring-blue-300 hover:bg-blue-800"
	>
		SUBMIT
	</button>
</form>
