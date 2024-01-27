<script lang="ts">
	import { goto } from '$app/navigation';
	import { createDeleteMutation, createGetQuery, getQueryKey } from '$lib/api';
	import { route } from '$lib/utils/route';
	import { createMutation, createQuery } from '@tanstack/svelte-query';
	import DeleteIcon from '~icons/material-symbols/delete-outline';
	import EditIcon from '~icons/material-symbols/edit-outline';
	import Loading from '../Loading.svelte';
	import Match, { constructMatcher } from '../Match.svelte';
	import RandomMatch from '../RandomMatch.svelte';

	export let data;
	$: userMatchGet = data.isCvRoute
		? createGetQuery('/api/v1/cvs/{cv_id}', { params: { path: { cv_id: data.id } } })
		: createGetQuery('/api/v1/vacancies/{vacancy_id}', {
				params: { path: { vacancy_id: data.id } }
		  });

	$: userMatchQuery = createQuery({
		queryKey: userMatchGet.key,
		async queryFn() {
			const res = await userMatchGet.runQuery();
			if (!res.data) {
				await goto(route(data.isCvRoute ? '/cv/match' : '/vacancy/create'));
				return null;
			}
			return res;
		},
		select(data) {
			return data?.data ?? null;
		}
	});

	// whoever's reading this - sorry, dont know a better way to make ts inference work properly
	$: userMatchDelete = data.isCvRoute
		? { type: data.isCvRoute, value: createDeleteMutation('/api/v1/cvs/{cv_id}') }
		: { type: data.isCvRoute, value: createDeleteMutation('/api/v1/vacancies/{vacancy_id}') };
	$: userMatchMutation = createMutation({
		mutationFn() {
			return userMatchDelete.type
				? userMatchDelete.value.runMutation({ params: { path: { cv_id: data.id } } })
				: userMatchDelete.value.runMutation({ params: { path: { vacancy_id: data.id } } });
		}
	});

	$: randomMatchGet = createGetQuery(
		data.isCvRoute ? '/api/v1/vacancies/random_vacancy' : '/api/v1/vacancies/random_vacancy'
	);
	$: randomMatchQuery = createQuery({
		queryKey: randomMatchGet.key,
		queryFn() {
			return randomMatchGet.runQuery();
		},
		select(res) {
			return res.data;
		}
	});
	$: matcher = constructMatcher($userMatchQuery.data, $randomMatchQuery.data);
</script>

{#if $userMatchQuery.isSuccess && $userMatchQuery.data}
	<Match
		mainClass="xl:block hidden"
		{matcher}
		matchData={$userMatchQuery.data}
		footerClass="gap-9 xl:block hidden pt-5 text-base dark:text-white"
	>
		<svelte:fragment slot="header">
			<div class="flex items-center gap-1 dark:text-white">
				<h2 class="font-title text-2xl md:text-3xl">{data.isCvRoute ? 'CV' : 'Vacancy'}</h2>
				<a
					class="ml-auto rounded-full bg-app-blue-600 p-1 text-white transition-colors current:bg-white current:text-app-blue-600"
					href={route(data.isCvRoute ? '/cv/create' : '/vacancy/create')}
				>
					<EditIcon />
				</a>
				<button
					aria-label={data.isCvRoute ? 'delete cv' : 'delete vacancy'}
					class="rounded-full bg-red-600 p-1 text-white transition-colors current:bg-white current:text-red-600"
					on:click={async () => {
						$userMatchMutation.mutate();
						data.queryClient.invalidateQueries({
							queryKey: getQueryKey(createGetQuery('/api/v1/users/records'), 'invalidate route')
						});
						goto(route(data.isCvRoute ? '/cv/match' : '/vacancy/match'));
					}}
				>
					<DeleteIcon />
				</button>
			</div>
		</svelte:fragment>

		<svelte:fragment slot="footer">
			<div class="hidden xl:block">
				<span>Views: 16</span>
				<span>Match: 7</span>
			</div>
		</svelte:fragment>
	</Match>
{:else}
	<Loading />
{/if}
{#if $randomMatchQuery.isSuccess}
	<RandomMatch
		{matcher}
		matchData={$randomMatchQuery.data}
		like={() =>
			data.queryClient.invalidateQueries({
				queryKey: data.isCvRoute ? ['random vacancy'] : ['random cv']
			})}
		dislike={() =>
			data.queryClient.invalidateQueries({
				queryKey: data.isCvRoute ? ['random vacancy'] : ['random cv']
			})}
	/>
{:else}
	<Loading />
{/if}
