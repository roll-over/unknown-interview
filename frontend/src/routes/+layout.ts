import { browser } from '$app/environment';
import { QueryClient } from '@tanstack/svelte-query';
import { createGetQuery } from '../lib/api';

export const load = async ({ fetch }) => {
	const queryClient = new QueryClient({
		defaultOptions: {
			queries: {
				// make sure queries don't run on the server during SSR
				enabled: browser
			}
		}
	});

	const userInfoGet = createGetQuery('/api/v1/auth/user_info');
	await queryClient.prefetchQuery({
		queryKey: userInfoGet.key,
		queryFn: () => userInfoGet.runQuery({ fetch })
	});
	return { queryClient };
};
