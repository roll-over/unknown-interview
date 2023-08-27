<script lang="ts">
	import { createQuery, keepPreviousData } from '@tanstack/svelte-query';
	import { _getPosts } from './+page';
	import { blueLinkLikeButtonClass, h1Class } from '$lib/components/classes';

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
	<h1 class={h1Class}>Home</h1>
	<a
		href="/hello"
		class={blueLinkLikeButtonClass}>Hello</a
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
