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
	import { blueButtonClass, defaultInputClass } from '$lib/components/classes';

	const newJobState = persisted<NewJobState>('newJobState', defaultNewJobState);
</script>

{#if !$newJobState.position}
	<h1>Necessary position</h1>
	{#each positions as position}
		<button
			on:click={() => newJobState.update((a) => ({ ...a, position }))}
			class={blueButtonClass}>{position}</button
		>
	{/each}
{:else if !$newJobState.grade}
	<h1>Necessary grade</h1>
	{#each grades as grade}
		<button
			on:click={() => newJobState.update((a) => ({ ...a, grade }))}
			class={blueButtonClass}>{grade}</button
		>
	{/each}
{:else if $newJobState.salaryFork && (!$newJobState.salaryFork?.min || !$newJobState.salaryFork?.max || !$newJobState.salaryFork?.applied)}
	<h1>Available salary</h1>
	<input
		type="number"
		placeholder="min"
		class={defaultInputClass}
		bind:value={$newJobState.salaryFork.min}
	/>
	<input
		type="number"
		placeholder="max"
		class={defaultInputClass}
		bind:value={$newJobState.salaryFork.max}
	/>
	<select
		class={defaultInputClass}
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
		class={blueButtonClass}>Save</button
	>
{:else if !$newJobState.profession}
	<h1>Necessary profession</h1>
	{#each professions as profession}
		<button
			on:click={() => newJobState.update((a) => ({ ...a, profession }))}
			class={blueButtonClass}>{profession}</button
		>
	{/each}
{:else if $newJobState.skills && !$newJobState.skills.length}
	<h1>Necessary skills</h1>
	{#each skills.programmer as skill}
		<button
			on:click={() => newJobState.update((a) => ({ ...a, skills: [...(a.skills || []), skill] }))}
			class={blueButtonClass}>{skill}</button
		>
	{/each}
{:else}
	<h1>Job search</h1>
{/if}
