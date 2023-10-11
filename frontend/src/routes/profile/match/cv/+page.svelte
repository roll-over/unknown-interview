<script lang="ts">
	import api from '$lib/api';
	import { route } from '$lib/utils/route';
	import { createQuery } from '@tanstack/svelte-query';

	$: listQuery = createQuery({
		queryKey: ['user CVs & Vacancies'],
		queryFn() {
			return api.GET('/api/v1/users/records', {});
		}
	});
</script>

{#if $listQuery.isSuccess}
	{#if !!$listQuery.data.data?.cv_ids?.length}
		{@const list = $listQuery.data.data.cv_ids}
		<div>YOUR CVs</div>
		<div class="flex flex-col gap-1">
			{#each list as id (id)}
				<a href={route((p) => `/profile/match/cv/${p(id)}`)}>CV ID - {id}</a>
			{/each}
		</div>
	{:else}
		<a href={route('/create/cv')}>Create your first CV!</a>
	{/if}
	{#if !!$listQuery.data.data?.cv_ids?.length}
		{@const list = $listQuery.data.data.cv_ids}
		<div>YOUR Vacancies</div>
		<div class="flex flex-col gap-1">
			{#each list as id (id)}
				<a href={route((p) => `/profile/match/vacancy/${p(id)}`)}>Vacancy ID - {id}</a>
			{/each}
		</div>
	{:else}
		<a href={route('/create/vacancy')}>Create your first Vacancy!</a>
	{/if}
{:else}
	Loading...
{/if}
