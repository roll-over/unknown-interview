<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import api from '$lib/api';
	import { route } from '$lib/utils/route';
	import { createQuery } from '@tanstack/svelte-query';
	import DeleteIcon from '~icons/material-symbols/delete-outline';
	import EditIcon from '~icons/material-symbols/edit-outline';
	import Match, { constructMatcher } from '../../Match.svelte';
	import RandomMatch from '../../RandomMatch.svelte';
	import { getRandomVacancy } from '../../mock';

	export let data;
	$: userMatchQuery = createQuery({
		queryKey: ['cv', $page.params.id],
		async queryFn() {
			const res = await api.GET('/api/v1/cvs/{cv_id}', { params: { path: { cv_id: data.id } } });
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

	$: randomVacancyQuery = createQuery({
		queryKey: ['random vacancy'],
		queryFn() {
			return getRandomVacancy();
		},
		staleTime: Infinity
	});

	$: matcher = constructMatcher($userMatchQuery.data, $randomVacancyQuery.data);
</script>

<Match
	{matcher}
	matchQuery={$userMatchQuery}
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
					await api.DELETE('/api/v1/cvs/{cv_id}', { params: { path: { cv_id: data.id } } });
					data.queryClient.invalidateQueries({ queryKey: ['user cvs and vacancies'] });
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
<RandomMatch
	{matcher}
	matchQuery={$randomVacancyQuery}
	like={() => data.queryClient.invalidateQueries({ queryKey: ['random vacancy'] })}
	dislike={() => data.queryClient.invalidateQueries({ queryKey: ['random vacancy'] })}
/>
