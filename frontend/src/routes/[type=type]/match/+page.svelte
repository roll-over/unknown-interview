<script lang="ts">
	import { createGetQuery } from '$lib/api';
	import { route } from '$lib/utils/route';
	import { getModalStore } from '@skeletonlabs/skeleton';
	import { createQuery } from '@tanstack/svelte-query';
	import Loading from './Loading.svelte';
	import RandomMatch from './RandomMatch.svelte';
	import { showWarningModal } from './WarningModal.svelte';
	import { getRandomCv, getRandomVacancy } from './mock';

	export let data;

	$: userRecordsGet = createGetQuery('/api/v1/users/records');
	$: userRecordsQuery = createQuery({
		queryKey: userRecordsGet.key,
		queryFn() {
			return userRecordsGet.runQuery();
		},
		select(res) {
			return (data.isCvRoute ? res.data?.cv_ids : res.data?.vacancy_ids) ?? [];
		}
	});

	$: randomMatchQuery = createQuery({
		queryKey: data.isCvRoute ? ['random vacancy'] : ['random cv'],
		queryFn() {
			return data.isCvRoute ? getRandomVacancy() : getRandomCv();
		},
		staleTime: Infinity
	});

	const modalStore = getModalStore();
	function showModal() {
		showWarningModal(modalStore, {
			hasMatches: !!$userRecordsQuery.data?.length,
			isCvRoute: data.isCvRoute
		});
	}
</script>

<div class="overflow-y-hidden pb-16">
	<div class="flex max-h-full flex-col space-y-5 rounded-lg bg-app-blue-50 p-5">
		<h2 class="font-title text-3xl">{data.isCvRoute ? 'CV' : 'Vacancy'}</h2>
		{#if $userRecordsQuery.isSuccess}
			<div class="flex flex-col overflow-y-auto">
				{#each $userRecordsQuery.data as id (id)}
					<a
						href={route((p) => (data.isCvRoute ? `/cv/match/${p(id)}` : `/vacancy/match/${p(id)}`))}
					>
						{data.isCvRoute ? 'CV' : 'Vacancy'}
						{id}
					</a>
				{:else}
					<a href={route(data.isCvRoute ? '/cv/create' : '/vacancy/create')}>
						Fill out {data.isCvRoute ? 'CV' : 'Vacancy'}
					</a>
				{/each}
			</div>
		{:else}
			Loading...
		{/if}
	</div>
</div>
{#if $randomMatchQuery.isSuccess}
	<RandomMatch
		matchData={$randomMatchQuery.data}
		like={showModal}
		dislike={showModal}
	/>
{:else}
	<Loading />
{/if}
