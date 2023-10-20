<script lang="ts">
	import { route } from '$lib/utils/route';
	import { getModalStore } from '@skeletonlabs/skeleton';
	import { createQuery } from '@tanstack/svelte-query';
	import RandomMatch from '../RandomMatch.svelte';
	import { showWarningModal } from '../WarningModal.svelte';
	import { getRandomVacancy } from '../mock';
	import Loading from '../Loading.svelte';
	import { createGetQuery } from '$lib/api';

	$: userCvsGet = createGetQuery('/api/v1/users/records');
	$: userCvsQuery = createQuery({
		queryKey: userCvsGet.key,
		queryFn() {
			return userCvsGet.runQuery();
		},
		select(data) {
			return data.data?.cv_ids ?? [];
		}
	});

	$: randomVacancyQuery = createQuery({
		queryKey: ['random vacancy'],
		queryFn() {
			return getRandomVacancy();
		},
		staleTime: Infinity
	});

	const modalStore = getModalStore();
	function showModal() {
		showWarningModal(modalStore, {
			hasMatches: !!$userCvsQuery.data?.length,
			isCvRoute: true
		});
	}
</script>

<div class="mb-16 space-y-5 rounded-lg bg-app-blue-50 p-5">
	<h2 class="font-title text-3xl">CV</h2>
	{#if $userCvsQuery.isSuccess}
		<div class="flex flex-col">
			{#each $userCvsQuery.data as id (id)}
				<a href={route((p) => `/profile/match/cv/${p(id)}`)}>CV {id}</a>
			{:else}
				<a href={route('/create/cv')}>Fill out CV</a>
			{/each}
		</div>
	{:else}
		Loading...
	{/if}
</div>
{#if $randomVacancyQuery.isSuccess}
	<RandomMatch
		matchData={$randomVacancyQuery.data}
		like={showModal}
		dislike={showModal}
	/>
{:else}
	<Loading />
{/if}
