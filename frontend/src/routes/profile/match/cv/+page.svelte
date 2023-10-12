<script lang="ts">
	import api from '$lib/api';
	import { route } from '$lib/utils/route';
	import { createQuery } from '@tanstack/svelte-query';

	$: userCvsQuery = createQuery({
		queryKey: ['user cvs and vacancies'],
		queryFn() {
			return api.GET('/api/v1/users/records');
		},
		select(data) {
			return data.data?.cv_ids ?? [];
		}
	});
</script>

<div>
	{#if $userCvsQuery.isSuccess}
		<div class="flex flex-col">
			{#each $userCvsQuery.data as id (id)}
				<a href={route((p) => `/profile/match/cv/${p(id)}`)}>CV {id}</a>
			{:else}
				<a href={route('/create/cv')}>Create your first CV!</a>
			{/each}
		</div>
	{:else}
		Loading...
	{/if}
</div>
