<script lang="ts">
	import { createGetQuery, createPostMutation, getQueryKey } from '$lib/api';
	import RadioGroup from '$lib/components/RadioGroup.svelte';
	import { route } from '$lib/utils/route';
	import type { CvRequest, StrictOmit, VacancyRequest } from '$lib/utils/types';
	import { createMutation, createQuery } from '@tanstack/svelte-query';
	import { persisted } from 'svelte-local-storage-store';
	import CilArrowRight from '~icons/cil/arrow-right';
	import MaterialSymbolsSearch from '~icons/material-symbols/search';
	import Profession from './Profession.svelte';
	import Skills from './Skills.svelte';

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
	function handleSubmit(e: SubmitEvent) {
		e.preventDefault();

		const { skillset, ...rest } = $formData;

		$submitMutation.mutate({ ...rest, skillset: skillset.map((name) => ({ name })) });
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

<div>
	{JSON.stringify($formInfoQuery.data?.data) ??
		'Your review will by displayed here after you save it'}
</div>
<form
	class="flex flex-col items-start gap-5 p-3"
	on:submit={handleSubmit}
>
	<fieldset class="w-80">
		<legend class="pb-2">Profession</legend>
		<Profession bind:selectedProfession={$formData.profession.name} />
	</fieldset>
	<fieldset>
		<legend class="pb-2">Grade</legend>
		<RadioGroup
			options={grades}
			bind:value={$formData.grade}
			name="position"
		/>
	</fieldset>
	<fieldset>
		<legend class="pb-2">Position</legend>
		<RadioGroup
			options={titles}
			bind:value={$formData.title}
			name="title"
		/>
	</fieldset>

	<fieldset class="w-80">
		<legend class="flex items-center gap-0.5 pb-2"
			>Skills
			<MaterialSymbolsSearch />
		</legend>
		<Skills bind:selectedSkills={$formData.skillset} />
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
					bind:value={$formData.salary.min_level}
				/>
			</label>
			<label>
				to
				<input
					type="number"
					min={$formData.salary.min_level}
					class="rounded-lg bg-app-blue-50 p-1 text-sm focus:border-blue-500 focus:ring-blue-500"
					bind:value={$formData.salary.max_level}
				/>
			</label>
		</div>
		<label>
			Currency:
			<select
				class="rounded-lg bg-app-blue-50 p-1 text-sm focus:border-blue-500 focus:ring-blue-500"
				bind:value={$formData.salary.currency}
			>
				{#each currencies as currency}
					<option value={currency}>{currency}</option>
				{/each}
			</select>
		</label>
	</fieldset>
	<button
		class="rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white shadow-blue-300 focus-within:outline-none focus-within:ring-4 focus-within:ring-blue-300 hover:bg-blue-800"
	>
		Submit
	</button>
	<a
		href={route(data.isCvRoute ? '/cv/match' : '/vacancy/match')}
		class="ml-auto flex items-center gap-8 rounded-md bg-app-blue-100 px-10 py-1.5 text-xl transition-colors current:bg-app-blue-400 current:text-white"
	>
		{data.isCvRoute ? 'View CVs' : 'Your vacancies'}
		<CilArrowRight class="h-12 w-12" />
	</a>
</form>
