<script lang="ts">
	import { createQuery, keepPreviousData } from '@tanstack/svelte-query';
	import { _getPosts } from './+page';

	export let data;
	let post = data.post;

	$: hybridQuery = createQuery({
		queryKey: ['hybridQuery', post],
		queryFn: () => _getPosts(post),
		placeholderData: keepPreviousData
	});
	$: clientQuery = createQuery({
		queryKey: ['clientQuery', post],
		queryFn: () => _getPosts(post),
		placeholderData: keepPreviousData
	});
</script>

<div class="flex h-full flex-col items-center justify-center">
	<h1 class="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl">
		Home
	</h1>
	<a
		href="/hello"
		class="mb-2 mr-2 rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300"
		>Hello</a
	>
</div>
<input
	bind:value={post}
	class="m-4 text-black outline outline-black"
	placeholder="post id"
/>
<p>{$hybridQuery.data}</p>
<div class="my-4 h-1 w-full rounded-full bg-slate-200" />
<p>{$clientQuery.data}</p>
