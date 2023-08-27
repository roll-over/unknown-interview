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
	} from '../types/common';
	import { blueButtonClass, defaultInputClass } from '$lib/components/classes';

	const newEmployState = persisted<NewEmployeState>('newEmployState', defaultNewEmployeState);
</script>

{#if !$newEmployState.position}
	<h1>Potential position</h1>
	{#each positions as position}
		<button
			on:click={() => newEmployState.update((a) => ({ ...a, position }))}
			class={blueButtonClass}>{position}</button
		>
	{/each}
{:else if !$newEmployState.grade}
	<h1>Potential grade</h1>
	{#each grades as grade}
		<button
			on:click={() => newEmployState.update((a) => ({ ...a, grade }))}
			class={blueButtonClass}>{grade}</button
		>
	{/each}
{:else if $newEmployState.salaryFork && (!$newEmployState.salaryFork?.min || !$newEmployState.salaryFork?.max || !$newEmployState.salaryFork?.applied)}
	<h1>Potential salary</h1>
	<input
		type="number"
		placeholder="min"
		class={defaultInputClass}
		bind:value={$newEmployState.salaryFork.min}
	/>
	<input
		type="number"
		placeholder="max"
		class={defaultInputClass}
		bind:value={$newEmployState.salaryFork.max}
	/>
	<select
		class={defaultInputClass}
		bind:value={$newEmployState.salaryFork.currency}
	>
		{#each currencies as currency}
			<option value={currency}>{currency}</option>
		{/each}
	</select>
	<button
		disabled={!$newEmployState.salaryFork?.min ||
			!$newEmployState.salaryFork?.max ||
			!$newEmployState.salaryFork?.currency}
		on:click={() => {
			const salaryFork = $newEmployState.salaryFork;
			if (!salaryFork) return;
			newEmployState.update((a) => ({ ...a, salaryFork: { ...salaryFork, applied: true } }));
		}}
		class={blueButtonClass}>Save</button
	>
{:else if !$newEmployState.profession}
	<h1>Potential profession</h1>
	{#each professions as profession}
		<button
			on:click={() => newEmployState.update((a) => ({ ...a, profession }))}
			class={blueButtonClass}>{profession}</button
		>
	{/each}
{:else if $newEmployState.skills && !$newEmployState.skills.length}
	<h1>Your skills</h1>
	{#each skills.programmer as skill}
		<button
			on:click={() =>
				newEmployState.update((a) => ({ ...a, skills: [...(a.skills || []), skill] }))}
			class={blueButtonClass}>{skill}</button
		>
	{/each}
{:else}
	<h1>Job search</h1>
{/if}
