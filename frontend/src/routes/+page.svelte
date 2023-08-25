<script lang="ts">
	import { createQuery } from '@tanstack/svelte-query';
	import { _getPosts } from './+page';
	const clientQuery = createQuery({
		queryKey: ['cliendQuery'],
		queryFn() {
			return fetch('https://jsonplaceholder.typicode.com/posts/1').then((response) =>
				response.text()
			);
		}
	});

	export let data;
	let post = data.post;
	$: hybridQuery = createQuery({
		queryKey: ['hybridQuery', post],
		queryFn: () => _getPosts(post)
	});
</script>

<h1>Welcome to SvelteKit</h1>
<div>HELLO HERE BUDDY</div>
<p>
	Visit <a href="https://kit.svelte.dev" class="bg-green-400 text-red-500">kit.svelte.dev</a> to read
	the documentation
</p>
<p>{$clientQuery.data}</p>
<p>{$hybridQuery.data}</p>
<input bind:value={post} class="m-4 outline outline-black" placeholder="post id" />
