<script
	lang="ts"
	context="module"
>
	import { isRangeOverlap, mapWithFilter } from '$lib/utils';
	import type { CvResponse, VacancyResponse } from '$lib/utils/types';

	export type MatchData = CvResponse | VacancyResponse;

	function compareStrings(user: string, match: string) {
		return user.toLowerCase() === match.toLowerCase();
	}
	function compareSkills(userSkills: MatchData['skillset'], matchSkill: MatchData['skillset']) {
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
	function compareSalaries(userSalary: MatchData['salary'], matchSalary: MatchData['salary']) {
		if (!userSalary || !matchSalary) return false;
		// todo - currency conversion?
		return isRangeOverlap(
			userSalary.min_level ?? 0,
			userSalary.max_level ?? Infinity,
			matchSalary.min_level ?? 0,
			matchSalary.max_level ?? Infinity
		);
	}
	export function constructMatcher(userMatch?: MatchData | null, randomMatch?: MatchData | null) {
		if (!userMatch || !randomMatch) return {};

		return {
			profession: compareStrings(userMatch.profession.name, randomMatch.profession.name),
			grade: compareStrings(userMatch.grade, randomMatch.grade),
			title: compareStrings(userMatch.title, randomMatch.title),
			skills: compareSkills(userMatch.skillset, randomMatch.skillset),
			salary: compareSalaries(userMatch.salary, randomMatch.salary),
			user_id: userMatch.custom_id,
			random_id: randomMatch.custom_id
		};
	}
	export type Matcher = ReturnType<typeof constructMatcher>;
</script>

<script lang="ts">
	import Chip from './Chip.svelte';

	export let matcher: Matcher = {};
	export let matchData: MatchData;
	export let hideClass = '';
	export let mainClass = '';
	export let footerClass = '';
</script>

<div class="flex h-full min-h-0 flex-col {hideClass}">
	<div
		class="mb-8 h-full space-y-5 overflow-y-auto rounded-lg bg-app-blue-50 p-5 dark:bg-app-dark-gray md:mb-0 {mainClass}"
	>
		<slot name="header" />
		{#if matchData}
			<div class="flex items-center gap-2">
				Profession:
				<Chip highlight={matcher.profession}>{matchData.profession.name}</Chip>
			</div>
			<div class="flex items-center gap-2">
				Grade:
				<Chip highlight={matcher.grade}>{matchData.grade}</Chip>
			</div>
			<div class="flex items-center gap-2">
				Title:
				<Chip highlight={matcher.title}>{matchData.title}</Chip>
			</div>
			{#if matchData.skillset?.length}
				{@const skills = matchData.skillset}
				<div class="flex flex-wrap items-center gap-2">
					Skills:
					{#each skills as { name: skill } (skill)}
						<Chip highlight={matcher.skills?.(skill)}>{skill}</Chip>
					{/each}
				</div>
			{/if}
			{#if matchData.salary}
				{@const salary = matchData.salary}
				<div class="leading-[1.8em]">
					Salary
					{#if salary.min_level}
						from <Chip highlight={matcher.salary}>{salary.min_level} {salary.currency}</Chip>
					{/if}
					{#if salary.max_level}
						to
						<Chip highlight={matcher.salary}>{salary.max_level} {salary.currency}</Chip>
					{/if}
				</div>
			{/if}
			<p class="whitespace-pre-wrap">
				{matchData.extra_info}
			</p>
		{/if}
	</div>
	<div class="h-16 shrink-0 {footerClass}">
		<slot name="footer" />
	</div>
</div>
