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

<div class="flex h-full flex-col items-center justify-center">
	<div>THIS IS PREFETCHED: {$prefetchedQuery.data?.data}</div>
	<div>THI IS FETCHED ONLY ON CLIENT: {$clientQuery.data?.data}</div>
	<div class="my-4 h-1 w-full rounded-full bg-slate-200" />
	<h1 class="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl">
		Home
	</h1>
	<a
		href="/hello"
		class="mb-2 mr-2 rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300"
	>
		Hello
	</a>
</div>
