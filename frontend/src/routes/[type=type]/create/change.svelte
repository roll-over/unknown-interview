<script lang="ts">
	import RadioGroup from '$lib/components/RadioGroup.svelte';
	import type { CvRequest, StrictOmit, VacancyRequest } from '$lib/utils/types';
	import { createMutation } from '@tanstack/svelte-query';
	import { persisted } from 'svelte-local-storage-store';
	import CilArrowRight from '~icons/cil/arrow-right';
	import MaterialSymbolsSearch from '~icons/material-symbols/search';
	import Profession from '../create/Profession.svelte';
	import Skills from '../create/Skills.svelte';
	import { goto } from '$app/navigation';
	import { createPatchMutation } from '$lib/api';

	export let data;

	type FormState = StrictOmit<CvRequest | VacancyRequest, 'skillset'> & { skillset: string[] };

	const titles: FormState['title'][] = ['member', 'lead', 'teamlead', 'manager', 'director'];
	const grades: FormState['grade'][] = ['junior', 'middle', 'senior', 'lead', 'principal'];
	const currencies = ['USD', 'EUR'];

	const defaultFormState = {
		title: 'member',
		grade: 'junior',
		salary: {
			min_level: 0,
			max_level: 0,
			currency: 'USD'
		},
		profession: { name: '' },
		skillset: [] as string[],
		extra_info: null
	} satisfies FormState;

	const formData = persisted(data.isCvRoute ? 'CvForm' : 'VacancyForm', defaultFormState);

	$: submitPost = data.isCvRoute
		? { type: data.isCvRoute, value: createPatchMutation('/api/v1/cvs/{cv_id}') }
		: { type: data.isCvRoute, value: createPatchMutation('/api/v1/vacancies/{vacancy_id}') };

	$: submitMutation = createMutation({
		mutationFn(_data: CvRequest | VacancyRequest) {
			return submitPost.type
				? submitPost.value.runMutation({ params: { path: { cv_id: data.id } }, body: _data })
				: submitPost.value.runMutation({ params: { path: { vacancy_id: data.id } }, body: _data });
		}
	});

	async function handleSubmit(e: SubmitEvent) {
		e.preventDefault();

		const { skillset, ...rest } = $formData;

		try {
			console.log('Submitting data:', { ...rest, skillset: skillset.map((name) => ({ name })) });

			// Wait for the mutation to complete
			await $submitMutation.mutate({
				...rest,
				skillset: skillset.map((name) => ({ name }))
			});

			// Navigate to the desired route after successful form submission
			goto(data.isCvRoute ? '/cv/match' : '/vacancy/match');
		} catch (error) {
			// Handle any errors that occurred during the mutation
			console.error('Form submission error:', error);
		}
	}
</script>

<div class="flex w-full items-center justify-center">
	<form
		class="flex w-full max-w-3xl flex-col items-start gap-7 p-4 text-base dark:text-white md:px-12 md:py-7 md:text-xl"
		on:submit={handleSubmit}
	>
		<fieldset class=" flex flex-col gap-2">
			<legend class="pb-2 text-xl">Profession</legend>
			<Profession bind:selectedProfession={$formData.profession.name} />
		</fieldset>
		<fieldset class=" flex flex-col gap-2">
			<legend class="pb-2 text-xl">Grade</legend>
			<RadioGroup
				options={grades}
				bind:value={$formData.grade}
				name="position"
			/>
		</fieldset>
		<fieldset class=" flex flex-col gap-2">
			<legend class="pb-2 text-xl">Position</legend>
			<RadioGroup
				options={titles}
				bind:value={$formData.title}
				name="title"
			/>
		</fieldset>

		<fieldset class=" flex flex-col gap-2">
			<legend class="flex items-center gap-0.5 pb-2 text-xl"
				>Skills
				<MaterialSymbolsSearch />
			</legend>
			<Skills bind:selectedSkills={$formData.skillset} />
		</fieldset>

		<fieldset class=" flex flex-col gap-2">
			<legend class="pb-2 text-xl">Estimated salary</legend>
			<div class="flex flex-col gap-2">
				<div class="align-center flex content-center items-center justify-center gap-5 pl-2">
					<label for="from"> from: </label>
					<input
						type="number"
						id="from"
						min="0"
						class="rounded-lg bg-app-blue-50 px-4 py-0.5 focus:border-blue-500 focus:ring-blue-500 dark:bg-app-dark-gray dark:outline-white dark:focus:border-white dark:focus:ring-white"
						bind:value={$formData.salary.min_level}
					/>
				</div>
				<div class="align-center flex content-center items-center justify-between gap-5 pl-2">
					<label for="to"> to: </label>
					<input
						type="number"
						id="to"
						min={$formData.salary.min_level}
						class="rounded-lg bg-app-blue-50 px-4 py-0.5 focus:border-blue-500 focus:ring-blue-500 dark:bg-app-dark-gray dark:outline-white dark:focus:border-white dark:focus:ring-white"
						bind:value={$formData.salary.max_level}
					/>
				</div>
			</div>
			<div class="align-center flex content-center gap-5 pl-2">
				<label
					class="flex items-center gap-1"
					for="currency"
				>
					Currency:
				</label>
				<select
					id="currency"
					class="rounded-lg bg-app-blue-50 px-4 py-0.5 focus:border-blue-500 focus:ring-blue-500 dark:bg-app-dark-gray dark:outline-white dark:focus:border-white dark:focus:ring-white"
					bind:value={$formData.salary.currency}
				>
					{#each currencies as currency}
						<option value={currency}>{currency}</option>
					{/each}
				</select>
			</div>
		</fieldset>
		<fieldset class="w-full">
			<legend class="pb-2 text-xl">About Me:</legend>
			<label>
				<textarea
					class="h-80 w-full rounded-lg bg-app-blue-50 p-2 focus:border-blue-500 focus:ring-blue-500 dark:bg-app-dark-gray dark:outline-white dark:focus:border-white dark:focus:ring-white md:p-10"
					bind:value={$formData.extra_info}
					placeholder="tell us about yourself..."
				></textarea>
			</label>
		</fieldset>
		<button
			class="flex w-full items-center justify-center gap-8 rounded-md bg-app-blue-100 px-10 py-1.5 text-xl transition-colors current:bg-app-blue-400 current:text-white dark:bg-app-dark-light dark:hover:bg-app-dark-gray"
		>
			Save Changes
			<CilArrowRight class="h-12 w-12" />
		</button>
	</form>
</div>
