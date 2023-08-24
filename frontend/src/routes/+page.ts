import type { PageLoad } from './$types';

export const load: PageLoad = async ({ parent, fetch }) => {
	const { queryClient } = await parent();

	const post = 20;
	await queryClient.prefetchQuery({
		queryKey: ['hybridQuery', post],
		queryFn: () => _getPosts(post, fetch)
	});

	return { post };
};

export function _getPosts(post: number, _fetch = fetch) {
	if (!post) return null;
	return _fetch(`https://jsonplaceholder.typicode.com/posts/${post}`).then((x) => x.text());
}
