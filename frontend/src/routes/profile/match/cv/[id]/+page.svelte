<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import api from '$lib/api';
	import type { components } from '$lib/openapi';
	import { isRangeOverlap, mapWithFilter } from '$lib/utils';
	import { route } from '$lib/utils/route';
	import { createQuery } from '@tanstack/svelte-query';
	import DeleteIcon from '~icons/material-symbols/delete-outline';
	import EditIcon from '~icons/material-symbols/edit-outline';
	import ThumbsUpIcon from '~icons/material-symbols/thumb-up-outline';
	import Chip from '../../Chip.svelte';
	import { cvContent, getRandomMatch } from '../../mock';

	export let data;

	type Cv = components['schemas']['CVResponseSchema'];
	type Vacancy = components['schemas']['VacancyResponseSchema'];

	$: userMatchQuery = createQuery({
		queryKey: ['cv', $page.params.id],
		async queryFn() {
			const res = await api.GET('/api/v1/cvs/{cv_id}', { params: { path: { cv_id: data.id } } });
			if (!res.data) {
				await goto(route('/profile/match/cv'));
				return null;
			}
			return res;
		}
	});

	$: randomVacancyQuery = createQuery({
		queryKey: ['random vacancy'],
		queryFn() {
			return getRandomMatch();
		},
		staleTime: Infinity
	});

	// #region matcher
	function compareStrings(user: string, match: string) {
		return user.toLowerCase() === match.toLowerCase();
	}
	function compareSkills(userSkills: Cv['skillset'], matchSkill: Vacancy['skillset']) {
		if (!userSkills || !matchSkill) return () => false;

		const setB = new Set(matchSkill.map((x) => x.name.toLowerCase()));

		const result = new Set(
			mapWithFilter(
				userSkills,
				(x) => x.name.toLowerCase(),
				(x) => setB.has(x)
			)
		);

		return (value: string) => result.has(value.toLowerCase());
	}
	function compareSalaries(userSalary: Cv['salary'], matchSalary: Vacancy['salary']) {
		if (!userSalary || !matchSalary) return false;
		// todo - currency conversion?
		return isRangeOverlap(
			userSalary.min_level ?? 0,
			userSalary.max_level ?? Infinity,
			matchSalary.min_level ?? 0,
			matchSalary.max_level ?? Infinity
		);
	}
	function constructMatcher(userMatch?: Cv, randomVacancy?: Vacancy) {
		if (!userMatch || !randomVacancy) return {};

		return {
			profession: compareStrings(userMatch.profession.name, randomVacancy.profession.name),
			grade: compareStrings(userMatch.grade, randomVacancy.grade),
			title: compareStrings(userMatch.title, randomVacancy.title),
			skills: compareSkills(userMatch.skillset, randomVacancy.skillset),
			salary: compareSalaries(userMatch.salary, randomVacancy.salary)
		};
	}
	$: matchers = constructMatcher($userMatchQuery.data?.data, $randomVacancyQuery.data);
	// #endregion matcher
</script>

<div class="grid h-full grid-cols-[2fr,3fr] gap-x-5 px-12 py-5 text-2xl">
	<div class="flex h-full min-h-0 flex-col">
		<div class="h-full space-y-5 overflow-y-auto rounded-lg bg-app-blue-50 p-5">
			{#if $userMatchQuery.data}
				{@const userMatch = $userMatchQuery.data.data}
				<div class="flex items-center gap-1">
					<h2 class="font-title text-3xl">CV</h2>
					<a
						class="ml-auto rounded-full bg-app-blue-600 p-1 text-white transition-colors current:bg-white current:text-app-blue-600"
						href={route('/create/cv')}
					>
						<EditIcon />
					</a>
					<button
						aria-label="delete cv"
						class="rounded-full bg-red-600 p-1 text-white transition-colors current:bg-white current:text-red-600"
						on:click={async () => {
							await api.DELETE('/api/v1/cvs/{cv_id}', { params: { path: { cv_id: data.id } } });
							data.queryClient.invalidateQueries({ queryKey: ['user cvs and vacancies'] });
							goto(route('/profile/match/cv'));
						}}
					>
						<DeleteIcon />
					</button>
				</div>
				<div>
					Profession:
					<Chip highlight={matchers.profession}>{userMatch.profession.name}</Chip>
				</div>
				<div>
					Grade:
					<Chip highlight={matchers.grade}>{userMatch.grade}</Chip>
				</div>
				<div>
					Title:
					<Chip highlight={matchers.title}>{userMatch.title}</Chip>
				</div>
				{#if userMatch.skillset?.length}
					{@const skills = userMatch.skillset}
					<div class="flex flex-wrap items-center gap-2">
						Skills:
						{#each skills as { name: skill } (skill)}
							<Chip highlight={matchers.skills?.(skill)}>{skill}</Chip>
						{/each}
					</div>
				{/if}
				{#if userMatch.salary}
					{@const salary = userMatch.salary}
					<div>
						Salary
						{#if salary.min_level}
							from <Chip highlight={matchers.salary}>{salary.min_level}{salary.currency}</Chip>
						{/if}
						{#if salary.max_level}
							to
							<Chip highlight={matchers.salary}>{salary.max_level}{salary.currency}</Chip>
						{/if}
					</div>
				{/if}
				<p class="whitespace-pre-wrap">
					{userMatch.extra_info ?? cvContent}
				</p>
			{:else}
				Loading...
			{/if}
		</div>
		<div class="flex h-16 gap-9 pt-5 text-base">
			<span>Views: 16</span>
			<span>Match: 7</span>
		</div>
	</div>
	<div class="flex h-full min-h-0 flex-col">
		<div class="h-full space-y-5 overflow-y-auto rounded-lg bg-app-blue-50 p-5 pb-16">
			{#if $randomVacancyQuery.data}
				{@const randomVacancy = $randomVacancyQuery.data}
				<h2 class="mx-auto w-fit text-center font-title text-3xl capitalize">
					{randomVacancy.grade}
					{randomVacancy.profession.name}
				</h2>
				<div>
					Profession:
					<Chip highlight={matchers.profession}>{randomVacancy.profession.name}</Chip>
				</div>
				<div>
					Grade:
					<Chip highlight={matchers.grade}>{randomVacancy.grade}</Chip>
				</div>
				<div>
					Title:
					<Chip highlight={matchers.title}>{randomVacancy.title}</Chip>
				</div>
				{#if randomVacancy.skillset?.length}
					{@const skills = randomVacancy.skillset}
					<div class="flex flex-wrap items-center gap-2">
						Skills:
						{#each skills as { name: skill } (skill)}
							<Chip highlight={matchers.skills?.(skill)}>{skill}</Chip>
						{/each}
					</div>
				{/if}
				{#if randomVacancy.salary}
					{@const salary = randomVacancy.salary}
					<div>
						Salary
						{#if salary.min_level}
							from <Chip highlight={matchers.salary}>{salary.min_level}{salary.currency}</Chip>
						{/if}
						{#if salary.max_level}
							to
							<Chip highlight={matchers.salary}>{salary.max_level}{salary.currency}</Chip>
						{/if}
					</div>
				{/if}
				<p class="whitespace-pre-wrap">
					{randomVacancy.extra_info}
				</p>
			{:else}
				Loading...
			{/if}
		</div>
		<div class="flex h-16 -translate-y-full justify-between">
			<button
				aria-label="dislike"
				class="aspect-square h-32 -scale-100 rounded-full bg-app-blue-600 p-4 text-white transition-colors current:bg-red-400"
				on:click={() => {
					data.queryClient.invalidateQueries({ queryKey: ['random vacancy'] });
				}}
			>
				<ThumbsUpIcon class="h-full w-full" />
			</button>
			<button
				aria-label="like"
				class="aspect-square h-32 rounded-full bg-app-blue-600 p-4 text-white transition-colors current:bg-green-400"
				on:click={() => {
					data.queryClient.invalidateQueries({ queryKey: ['random vacancy'] });
				}}
			>
				<ThumbsUpIcon class="h-full w-full" />
			</button>
		</div>
	</div>
</div>
