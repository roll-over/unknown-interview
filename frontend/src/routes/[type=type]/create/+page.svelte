<script lang="ts">
	import { createGetQuery, createPostMutation, getQueryKey } from '$lib/api';
	import RadioGroup from '$lib/components/RadioGroup.svelte';
	import type { CvRequest, StrictOmit, VacancyRequest } from '$lib/utils/types';
	import { createMutation, createQuery } from '@tanstack/svelte-query';
	import { persisted } from 'svelte-local-storage-store';
	import CilArrowRight from '~icons/cil/arrow-right';
	import MaterialSymbolsSearch from '~icons/material-symbols/search';
	import Profession from './Profession.svelte';
	import Skills from './Skills.svelte';
	import { goto } from '$app/navigation';

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
		? createPostMutation('/api/v1/cvs/')
		: createPostMutation('/api/v1/vacancies/');
	$: submitMutation = createMutation({
		mutationFn(data: CvRequest | VacancyRequest) {
			return submitPost.runMutation({ body: data });
		},
		onSuccess(res) {
			if (res.error) return;
			savedFormId = res.data.custom_id;

			data.queryClient.invalidateQueries({
				queryKey: getQueryKey(createGetQuery('/api/v1/users/records'), 'invalidate route')
			});
		},
		onSettled(res, err) {
			console.log({ res, err });
		}
	});
	async function handleSubmit(e: SubmitEvent) {
		e.preventDefault();

		const { skillset, ...rest } = $formData;

		try {
			// Wait for the mutation to complete
			await $submitMutation.mutate({ ...rest, skillset: skillset.map((name) => ({ name })) });

			// Navigate to the desired route after successful form submission
			goto(data.isCvRoute ? '/cv/match' : '/vacancy/match');
		} catch (error) {
			// Handle any errors that occurred during the mutation
			console.error('Form submission error:', error);
		}
	}

	// just a showcase that form gets saved
	let savedFormId: string;
	$: formInfoGet = data.isCvRoute
		? createGetQuery('/api/v1/cvs/{cv_id}', { params: { path: { cv_id: savedFormId } } })
		: createGetQuery('/api/v1/vacancies/{vacancy_id}', {
				params: { path: { vacancy_id: savedFormId } }
		  });
	$: formInfoQuery = createQuery({
		queryKey: formInfoGet.key,
		async queryFn() {
			return formInfoGet.runQuery();
		},
		enabled: !!savedFormId
	});
</script>

<div class="pl-2 dark:text-white">
	{JSON.stringify($formInfoQuery.data?.data) ??
		'Your review will by displayed here after you save it'}
</div>
<div class="flex w-full items-center justify-center">
	<form
		class="flex w-full max-w-2xl flex-col items-start gap-7 p-2 text-xl dark:text-white md:px-12 md:py-7"
		on:submit={handleSubmit}
	>
		<fieldset class=" flex flex-col gap-2">
			<legend class="pb-2">Profession</legend>
			<Profession bind:selectedProfession={$formData.profession.name} />
		</fieldset>
		<fieldset class=" flex flex-col gap-2">
			<legend class="pb-2">Grade</legend>
			<RadioGroup
				options={grades}
				bind:value={$formData.grade}
				name="position"
			/>
		</fieldset>
		<fieldset class=" flex flex-col gap-2">
			<legend class="pb-2">Position</legend>
			<RadioGroup
				options={titles}
				bind:value={$formData.title}
				name="title"
			/>
		</fieldset>

		<fieldset class=" flex flex-col gap-2">
			<legend class="flex items-center gap-0.5 pb-2"
				>Skills
				<MaterialSymbolsSearch />
			</legend>
			<Skills bind:selectedSkills={$formData.skillset} />
		</fieldset>

		<fieldset class=" flex flex-col gap-2">
			<legend>Estimated salary</legend>
			<div class="flex flex-col gap-2">
				<div class="align-center flex content-center items-center justify-center gap-5 pl-2">
					<label for="from"> from: </label>
					<input
						type="number"
						id="from"
						min="0"
						class="rounded-lg bg-app-blue-50 p-1 focus:border-blue-500 focus:ring-blue-500 dark:bg-app-dark-gray dark:outline-white dark:focus:border-white dark:focus:ring-white"
						bind:value={$formData.salary.min_level}
					/>
				</div>
				<div class="align-center flex content-center items-center justify-between gap-5 pl-2">
					<label for="to"> to: </label>
					<input
						type="number"
						id="to"
						min={$formData.salary.min_level}
						class="rounded-lg bg-app-blue-50 p-1 focus:border-blue-500 focus:ring-blue-500 dark:bg-app-dark-gray dark:outline-white dark:focus:border-white dark:focus:ring-white"
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
					class="rounded-lg bg-app-blue-50 p-1 focus:border-blue-500 focus:ring-blue-500 dark:bg-app-dark-gray dark:outline-white dark:focus:border-white dark:focus:ring-white"
					bind:value={$formData.salary.currency}
				>
					{#each currencies as currency}
						<option value={currency}>{currency}</option>
					{/each}
				</select>
			</div>
		</fieldset>
		<fieldset class="w-full">
			<legend class="pb-2">About Me:</legend>
			<label>
				<textarea
					class="h-80 w-full rounded-lg bg-app-blue-50 p-2 focus:border-blue-500 focus:ring-blue-500 dark:bg-app-dark-gray dark:outline-white dark:focus:border-white dark:focus:ring-white md:p-10"
					bind:value={$formData.extra_info}
					placeholder="tell us about yourself..."
				></textarea>
			</label>
		</fieldset>
		<button
			class="ml-auto flex items-center gap-8 rounded-md bg-app-blue-100 px-10 py-1.5 text-xl transition-colors current:bg-app-blue-400 current:text-white dark:bg-app-dark-light dark:hover:bg-app-dark-gray"
		>
			{data.isCvRoute ? 'View vacancies' : 'View resume'}
			<CilArrowRight class="h-12 w-12" />
		</button>
	</form>
</div>
