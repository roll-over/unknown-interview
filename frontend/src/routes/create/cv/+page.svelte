<script lang="ts">
	import { createGetQuery, createPostMutation, getQueryKey } from '$lib/api';
	import RadioGroup from '$lib/components/RadioGroup.svelte';
	import type { components } from '$lib/openapi';
	import { createMutation, createQuery } from '@tanstack/svelte-query';
	import { persisted } from 'svelte-local-storage-store';
	import Profession from '../Profession.svelte';
	import Skills from '../Skills.svelte';
	import { currencies, defaultCVState, grades, titles } from '../common';
	import MaterialSymbolsSearch from '~icons/material-symbols/search';
	import CilArrowRight from '~icons/cil/arrow-right';

	export let data;
	const CVStateData = persisted('CVState', defaultCVState);
	$: submitPost = createPostMutation('/api/v1/cvs/');
	$: submitMutation = createMutation({
		mutationFn(data: components['schemas']['CVRequestSchema']) {
			return submitPost.runMutation({ body: data });
		},
		onSuccess(res) {
			if (res.error) return;
			cvId = res.data.custom_id;

			data.queryClient.invalidateQueries({
				queryKey: getQueryKey(createGetQuery('/api/v1/users/records'), 'invalidate route')
			});
		},
		onSettled(res, err) {
			console.log({ res, err });
		}
	});
	function handleSubmit(e: SubmitEvent) {
		e.preventDefault();

		const { skillset, ...rest } = $CVStateData;

		$submitMutation.mutate({ ...rest, skillset: skillset.map((name) => ({ name })) });
	}

	// just a showcase that cv gets saved
	let cvId: string;
	$: cvInfoGet = createGetQuery('/api/v1/cvs/{cv_id}', { params: { path: { cv_id: cvId } } });
	$: cvInfoQuery = createQuery({
		queryKey: cvInfoGet.key,
		async queryFn() {
			return cvInfoGet.runQuery();
		},
		enabled: !!cvId
	});
</script>

<div>
	{JSON.stringify($cvInfoQuery.data?.data) ??
		'Your review will by displayed here after you save it'}
</div>
<form
	class="flex flex-col items-start gap-5 p-3"
	on:submit={handleSubmit}
>
	<h1>Your CV</h1>

	<fieldset class="w-80">
		<legend class="pb-2">Profession</legend>
		<Profession bind:selectedProfession={$CVStateData.profession.name} />
	</fieldset>
	<fieldset>
		<legend class="pb-2">Grade</legend>
		<RadioGroup
			options={grades}
			bind:value={$CVStateData.grade}
			name="position"
		/>
	</fieldset>

	<fieldset>
		<legend class="pb-2">Position</legend>
		<RadioGroup
			options={titles}
			bind:value={$CVStateData.title}
			name="title"
		/>
	</fieldset>

	<fieldset class="w-80">
		<legend class="flex items-center gap-0.5 pb-2"
			>Skills
			<MaterialSymbolsSearch />
		</legend>
		<Skills bind:selectedSkills={$CVStateData.skillset} />
	</fieldset>

	<fieldset>
		<div class="flex items-center gap-1">
			<legend>Estimated salary</legend>
			<label>
				from
				<input
					type="number"
					min="0"
					class="rounded-lg bg-app-blue-50 p-1 text-sm focus:border-blue-500 focus:ring-blue-500"
					bind:value={$CVStateData.salary.min_level}
				/>
			</label>
			<label>
				to
				<input
					type="number"
					min={$CVStateData.salary.min_level}
					class="rounded-lg bg-app-blue-50 p-1 text-sm focus:border-blue-500 focus:ring-blue-500"
					bind:value={$CVStateData.salary.max_level}
				/>
			</label>
		</div>
		<label>
			Currency:
			<select
				class="rounded-lg bg-app-blue-50 p-1 text-sm focus:border-blue-500 focus:ring-blue-500"
				bind:value={$CVStateData.salary.currency}
			>
				{#each currencies as currency}
					<option value={currency}>{currency}</option>
				{/each}
			</select>
		</label>
	</fieldset>

	<!-- <fieldset>
		<label>Volunteering
		<input type="checkbox" class="" bind:value={$CVStateData.volunteering} />
		</label>
	</fieldset> -->

	<!-- <fieldset class="w-80">
		<legend class="pb-2 flex items-center gap-0.5">Location
			<MaterialSymbolsSearch/>
		</legend>
		<Profession bind:selectedProfession={$CVStateData.profession.name} />
	</fieldset>

	<fieldset>
		<legend class="pb-2">Schedule</legend>
		<RadioGroup
			options={grades}
			bind:value={$CVStateData.grade}
			name="position"
		/>
	</fieldset>

	<fieldset>
		<legend class="pb-2">Employment type</legend>
		<RadioGroup
			options={grades}
			bind:value={$CVStateData.grade}
			name="position"
		/>
	</fieldset>
	
	<fieldset>
		<legend class="pb-2">About Me</legend>
		<RadioGroup
			options={titles}
			bind:value={$CVStateData.title}
			name="title"
		/>
	</fieldset> -->

	<button
		class="group ml-auto flex items-center gap-8 rounded-md bg-app-blue-100 px-10 py-1.5 text-xl transition-colors current:bg-app-blue-400"
	>
		View resume
		<CilArrowRight class="h-12 w-12" />
	</button>
</form>
