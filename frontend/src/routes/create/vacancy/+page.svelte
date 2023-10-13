<script lang="ts">
	import api from '$lib/api';
	import RadioGroup from '$lib/components/RadioGroup.svelte';
	import type { components } from '$lib/openapi';
	import { createMutation, createQuery } from '@tanstack/svelte-query';
	import { persisted } from 'svelte-local-storage-store';
	import Profession from '../Profession.svelte';
	import Skills from '../Skills.svelte';
	import { currencies, defaultVacancyState, grades, titles } from '../common';

	const jobOfferData = persisted('jobOfferState', defaultVacancyState);
	$: submitMutation = createMutation({
		mutationKey: ['create', 'vanacy'],
		mutationFn(data: components['schemas']['VacancyRequestSchema']) {
			return api.POST('/api/v1/vacancies/', { body: data });
		}
	});

	function handleSubmit() {
		const { skillset, ...rest } = $jobOfferData;

		$submitMutation.mutate(
			{ ...rest, skillset: skillset.map((name) => ({ name })) },
			{
				onSettled(d, e) {
					console.log({ d, e });
				},
				onSuccess(d) {
					console.log(d);
					if (!d.data) return;
					if ('custom_id' in d.data) {
						vacancyId = d.data.custom_id;
					}
				}
			}
		);
	}

	// just a showcase that cv gets saved
	let vacancyId: string;
	$: vacancyInfo = createQuery({
		queryKey: ['vanacy', vacancyId],
		async queryFn() {
			return api
				.GET('/api/v1/vacancies/{vacancy_id}', {
					params: { path: { vacancy_id: vacancyId } },
					body: undefined
				})
				.catch((e) => {
					console.error(e);
					return null;
				});
		},
		enabled: !!vacancyId
	});
</script>

<div>
	{JSON.stringify(
		$vacancyInfo.data?.data ?? 'Your review will by displayed here after you save it'
	)}
</div>
<form
	class="flex flex-col items-start gap-3 p-3"
	on:submit={handleSubmit}
>
	<h1>Job Posting</h1>
	<fieldset>
		<legend>Necessary title</legend>
		<RadioGroup
			options={titles}
			bind:value={$jobOfferData.title}
			name="title"
		/>
	</fieldset>
	<fieldset>
		<legend>Necessary grade</legend>
		<RadioGroup
			options={grades}
			bind:value={$jobOfferData.grade}
			name="position"
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
					bind:value={$jobOfferData.salary.min_level}
				/>
			</label>
			<label>
				max:
				<input
					type="number"
					min={$jobOfferData.salary?.min_level}
					class="rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500"
					bind:value={$jobOfferData.salary.max_level}
				/>
			</label>
			<label>
				currency:
				<select
					class="rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500"
					bind:value={$jobOfferData.salary.currency}
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
		<Profession bind:selectedProfession={$jobOfferData.profession.name} />
	</fieldset>
	<fieldset class="w-80">
		<h2>Necessary skills</h2>
		<Skills bind:selectedSkills={$jobOfferData.skillset} />
	</fieldset>
	<button
		class="rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white shadow-blue-300 focus-within:outline-none focus-within:ring-4 focus-within:ring-blue-300 hover:bg-blue-800"
	>
		SUBMIT
	</button>
</form>
