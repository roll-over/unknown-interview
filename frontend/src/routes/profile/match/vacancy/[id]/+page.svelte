<script lang="ts">
	import { goto } from '$app/navigation';
	import { createDeleteMutation, createGetQuery, getQueryKey } from '$lib/api';
	import { route } from '$lib/utils/route';
	import { createMutation, createQuery } from '@tanstack/svelte-query';
	import DeleteIcon from '~icons/material-symbols/delete-outline';
	import EditIcon from '~icons/material-symbols/edit-outline';
	import Loading from '../../Loading.svelte';
	import Match, { constructMatcher } from '../../Match.svelte';
	import RandomMatch from '../../RandomMatch.svelte';
	import { getRandomCv } from '../../mock';

	export let data;
	$: userMatchGet = createGetQuery('/api/v1/vacancies/{vacancy_id}', {
		params: { path: { vacancy_id: data.id } }
	});
	$: userMatchQuery = createQuery({
		queryKey: userMatchGet.key,
		async queryFn() {
			const data = await userMatchGet.runQuery();
			if (!data.data) {
				await goto(route('/profile/match/vacancy'));
				return null;
			}
			return data;
		},
		select(data) {
			return data?.data ?? null;
		}
	});
	$: userMatchDelete = createDeleteMutation('/api/v1/vacancies/{vacancy_id}');
	$: userMatchMutation = createMutation({
		mutationFn() {
			return userMatchDelete.runMutation({ params: { path: { vacancy_id: data.id } } });
		}
	});

	$: randomCvQuery = createQuery({
		queryKey: ['random cv'],
		queryFn() {
			return getRandomCv();
		},
		staleTime: Infinity
	});

	$: matcher = constructMatcher($userMatchQuery.data, $randomCvQuery.data);
</script>

{#if $userMatchQuery.isSuccess && $userMatchQuery.data}
	<Match
		{matcher}
		matchData={$userMatchQuery.data}
		footerClass="gap-9 flex pt-5 text-base"
	>
		<svelte:fragment slot="header">
			<div class="flex items-center gap-1">
				<h2 class="font-title text-3xl">Vacancy</h2>
				<a
					class="ml-auto rounded-full bg-app-blue-600 p-1 text-white transition-colors current:bg-white current:text-app-blue-600"
					href={route('/create/vacancy')}
				>
					<EditIcon />
				</a>
				<button
					aria-label="delete vacancy"
					class="rounded-full bg-red-600 p-1 text-white transition-colors current:bg-white current:text-red-600"
					on:click={async () => {
						$userMatchMutation.mutate();
						data.queryClient.invalidateQueries({
							queryKey: getQueryKey(createGetQuery('/api/v1/users/records'), 'invalidate route')
						});
						goto(route('/profile/match/vacancy'));
					}}
				>
					<DeleteIcon />
				</button>
			</div>
		</svelte:fragment>
		<svelte:fragment slot="footer">
			<span>Views: 16</span>
			<span>Match: 7</span>
		</svelte:fragment>
	</Match>
{:else}
	<Loading />
{/if}
{#if $randomCvQuery.isSuccess}
	<RandomMatch
		{matcher}
		matchData={$randomCvQuery.data}
		like={() => data.queryClient.invalidateQueries({ queryKey: ['random cv'] })}
		dislike={() => data.queryClient.invalidateQueries({ queryKey: ['random cv'] })}
	/>
{:else}
	<Loading />
{/if}
