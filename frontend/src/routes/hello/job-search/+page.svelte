<script lang="ts">
	import { persisted } from 'svelte-local-storage-store';
	import {
		positions,
		type NewJobState,
		grades,
		skills,
		professions,
		currencies,

		defaultNewJobState

	} from '../types/common';

	const newJobState = persisted<NewJobState>('newJobState', defaultNewJobState);
</script>

{#if !$newJobState.position}
	<h1>Necessary position</h1>
	{#each positions as position}
		<button
			on:click={() => newJobState.update((a) => ({ ...a, position }))}
			class="mb-2 mr-2 rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
			>{position}</button
		>
	{/each}
{:else if !$newJobState.grade}
	<h1>Necessary grade</h1>
	{#each grades as grade}
		<button
			on:click={() => newJobState.update((a) => ({ ...a, grade }))}
			class="mb-2 mr-2 rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
			>{grade}</button
		>
	{/each}
{:else if $newJobState.salaryFork && (!$newJobState.salaryFork?.min || !$newJobState.salaryFork?.max || !$newJobState.salaryFork?.applied)}
	<h1>Available salary</h1>
	<input
		type="number"
		placeholder="min"
		class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500"
		bind:value={$newJobState.salaryFork.min}
	/>
	<input
		type="number"
		placeholder="max"
		class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500"
		bind:value={$newJobState.salaryFork.max}
	/>
	<select
		class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500"
		bind:value={$newJobState.salaryFork.currency}
	>
		{#each currencies as currency}
			<option value={currency}>{currency}</option>
		{/each}
	</select>
	<button
		disabled={!$newJobState.salaryFork?.min ||
			!$newJobState.salaryFork?.max ||
			!$newJobState.salaryFork?.currency}
		on:click={() => {
			const salaryFork = $newJobState.salaryFork;
			if (!salaryFork) return;
			newJobState.update((a) => ({ ...a, salaryFork: { ...salaryFork, applied: true } }));
		}}
		class="mb-2 mr-2 rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
		>Save</button
	>
{:else if !$newJobState.profession}
	<h1>Necessary profession</h1>
	{#each professions as profession}
		<button
			on:click={() => newJobState.update((a) => ({ ...a, profession }))}
			class="mb-2 mr-2 rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
			>{profession}</button
		>
	{/each}
{:else if $newJobState.skills && !$newJobState.skills.length}
	<h1>Necessary skills</h1>
	{#each skills.programmer as skill}
		<button
			on:click={() => newJobState.update((a) => ({ ...a, skills: [...(a.skills || []), skill] }))}
			class="mb-2 mr-2 rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
			>{skill}</button
		>
	{/each}
{:else}
	<h1>Job search</h1>
{/if}
