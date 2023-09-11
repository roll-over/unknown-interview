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

<div class="flex h-full bg-white flex-col items-center justify-center">
	
	<div class="text-black">
		<div>THIS IS PREFETCHED: {$prefetchedQuery.data?.data}</div>
		<div>THI IS FETCHED ONLY ON CLIENT: {$clientQuery.data?.data}</div>
	</div>

	<div class="my-4 h-1 w-full rounded-full bg-slate-200"></div>

	<div class="w-full p-5 flex flex-col items-center bg-no-repeat bg-center" style="background-image: url(/src/img/background.svg)">
		<img class="pb-7" src="/src/img/diversity-icon.svg" alt="diversity-icon.svg"/>
		<h1 class="font-title font-400 pb-2 text-6xl leading-none tracking-tight text-gray-900 md:text-6xl">
			Hello!
		</h1>
		<p class="font-title text-black text-2xl pb-7">
			Fill out a short form to get started!
		</p>
	</div>
	<div class="flex">
		<a href="/hello"
			class="font-body button-color text-2xl text-black rounded-lg bg-pattens-blue flex justify-center items-center flex-shrink-0 pt-3.5 pb-3.5 pr-24 pl-24 font-400 hover:bg-summer-sky focus:outline-none focus:ring-4 focus:bg-focus-blue">
		go to survey!
		<img class="pl-16" src="/src/img/arrow-right.svg" alt="diversity-icon.svg"/>
	</a>
	</div>
	
</div>
