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
	import { getRandomVacancy } from '../../mock';

	export let data;
	$: userMatchGet = createGetQuery('/api/v1/cvs/{cv_id}', { params: { path: { cv_id: data.id } } });
	$: userMatchQuery = createQuery({
		queryKey: userMatchGet.key,
		async queryFn() {
			const res = await userMatchGet.runQuery();
			if (!res.data) {
				await goto(route('/profile/match/cv'));
				return null;
			}
			return res;
		},
		select(data) {
			return data?.data ?? null;
		}
	});

	$: userMatchDelete = createDeleteMutation('/api/v1/cvs/{cv_id}');
	$: userMatchMutation = createMutation({
		mutationFn() {
			return userMatchDelete.runMutation({ params: { path: { cv_id: data.id } } });
		}
	});

	$: randomVacancyQuery = createQuery({
		queryKey: ['random vacancy'],
		queryFn() {
			return getRandomVacancy();
		},
		staleTime: Infinity
	});

	$: matcher = constructMatcher($userMatchQuery.data, $randomVacancyQuery.data);
</script>

{#if $userMatchQuery.isSuccess && $userMatchQuery.data}
	<Match
		{matcher}
		matchData={$userMatchQuery.data}
		footerClass="gap-9 flex pt-5 text-base"
	>
		<svelte:fragment slot="header">
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
						$userMatchMutation.mutate();
						data.queryClient.invalidateQueries({
							queryKey: getQueryKey(createGetQuery('/api/v1/users/records'), 'invalidate route')
						});
						goto(route('/profile/match/cv'));
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
{#if $randomVacancyQuery.isSuccess}
	<RandomMatch
		{matcher}
		matchData={$randomVacancyQuery.data}
		like={() => data.queryClient.invalidateQueries({ queryKey: ['random vacancy'] })}
		dislike={() => data.queryClient.invalidateQueries({ queryKey: ['random vacancy'] })}
	/>
{:else}
	<Loading />
{/if}
