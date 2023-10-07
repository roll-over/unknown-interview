<script lang="ts">
	import api from '$lib/api';
	import { route } from '$lib/utils/route';
	import { createQuery } from '@tanstack/svelte-query';

	export let type: 'cv' | 'vacancy';
	$: isVacancy = type === 'vacancy';
	$: listQuery = createQuery({
		queryKey: ['user CVs & Vacancies'],
		queryFn() {
			return api.GET('/api/v1/users/records', {});
		},
		select(data) {
			return isVacancy ? data.data?.vacancy_ids : data.data?.cv_ids;
		}
	});
</script>

{#if $listQuery.isSuccess}
	{#if !!$listQuery.data?.length}
		<div>YOUR {isVacancy ? 'Vacancies' : 'CVs'}</div>
		<div class="flex flex-col gap-1">
			{#each $listQuery.data as id (id)}
				<a href={route((p) => `/profile/${isVacancy ? 'vacancy' : 'cv'}/${p(id)}`)}
					>{isVacancy ? 'Vacancy' : 'CV'} ID - {id}</a
				>
			{/each}
		</div>
	{:else}
		<a href={route(isVacancy ? '/create/vacancy' : '/create/cv')}
			>Create your first {isVacancy ? 'Vacancy' : 'CV'}!</a
		>
	{/if}
{:else}
	Loading...
{/if}
