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

<a href="/auth/login">Log-in</a>
<p>{$clientQuery.data}</p>
<p>{$hybridQuery.data}</p>
<input
	bind:value={post}
	class="m-4 outline outline-black"
	placeholder="post id"
/>
