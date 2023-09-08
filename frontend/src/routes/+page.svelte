<script lang="ts">
	import api from '$lib/api';
	import { createQuery } from '@tanstack/svelte-query';

	$: prefetchedQuery = createQuery({
		queryKey: ['prefetchedQuery'],
		queryFn: () => api.GET('/api/ping', {})
	});
	$: clientQuery = createQuery({
		queryKey: ['clientQuery'],
		queryFn: () => api.GET('/api/ping', {})
	});
</script>

<div class="flex h-full flex-col items-center justify-center gap-4">
	<div>
		<div>THIS IS PREFETCHED: {$prefetchedQuery.data?.data}</div>
		<div>THI IS FETCHED ONLY ON CLIENT: {$clientQuery.data?.data}</div>
	</div>
	<hr class="h-1 w-full rounded-full bg-white" />
	<h1 class="text-4xl font-extrabold">Home</h1>
</div>
