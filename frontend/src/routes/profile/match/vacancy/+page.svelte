<script lang="ts">
	import api from '$lib/api';
	import { route } from '$lib/utils/route';
	import { getModalStore } from '@skeletonlabs/skeleton';
	import { createQuery } from '@tanstack/svelte-query';
	import RandomMatch from '../RandomMatch.svelte';
	import { showWarningModal } from '../WarningModal.svelte';
	import { getRandomCv } from '../mock';

	$: userVacanciesQuery = createQuery({
		queryKey: ['user cvs and vacancies'],
		queryFn() {
			return api.GET('/api/v1/users/records');
		},
		select(data) {
			return data.data?.vacancy_ids ?? [];
		}
	});

	$: randomCvQuery = createQuery({
		queryKey: ['random cv'],
		queryFn() {
			return getRandomCv();
		},
		staleTime: Infinity
	});

	const modalStore = getModalStore();
	function showModal() {
		showWarningModal(modalStore, {
			hasMatches: !!$userVacanciesQuery.data?.length,
			isCvRoute: false
		});
	}
</script>

<div class="mb-16 space-y-5 rounded-lg bg-app-blue-50 p-5">
	<h2 class="font-title text-3xl">Vacancy</h2>
	{#if $userVacanciesQuery.isSuccess}
		<div class="flex flex-col">
			{#each $userVacanciesQuery.data as id (id)}
				<a href={route((p) => `/profile/match/vacancy/${p(id)}`)}>Vacancy {id}</a>
			{:else}
				<a href={route('/create/vacancy')}>Fill out Vacancy</a>
			{/each}
		</div>
	{:else}
		Loading...
	{/if}
</div>
<RandomMatch
	matchData={$randomCvQuery.data}
	like={showModal}
	dislike={showModal}
/>
