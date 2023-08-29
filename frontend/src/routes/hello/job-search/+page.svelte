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
	} from '../common';

	const newJobState = persisted<NewJobState>('newJobState', defaultNewJobState);
</script>

<h1>Job search</h1>
<h2>Necessary position</h2>
{#each positions as position}
	<button
		on:click={() => ($newJobState.position = position)}
		class="mb-2 mr-2 rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300"
		>{position}</button
	>
{/each}
<h2>Necessary grade</h2>
{#each grades as grade}
	<button
		on:click={() => ($newJobState.grade = grade)}
		class="mb-2 mr-2 rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300"
		>{grade}</button
	>
{/each}
<h2>Available salary</h2>
<input
	type="number"
	placeholder="min"
	class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500"
	bind:value={$newJobState.salaryFork.min}
/>
<input
	type="number"
	placeholder="max"
	class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500"
	bind:value={$newJobState.salaryFork.max}
/>
<select
	class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500"
	bind:value={$newJobState.salaryFork.currency}
>
	{#each currencies as currency}
		<option value={currency}>{currency}</option>
	{/each}
</select>
<h2>Necessary profession</h2>
{#each professions as profession}
	<button
		on:click={() => ($newJobState.profession = profession)}
		class="mb-2 mr-2 rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300"
		>{profession}</button
	>
{/each}
<h2>Necessary skills</h2>
{#each skills.programmer as skill}
	<button
		on:click={() => ($newJobState.skills = [skill])}
		class="mb-2 mr-2 rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300"
		>{skill}</button
	>
{/each}
