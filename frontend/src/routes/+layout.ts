import { browser } from '$app/environment';
import api from '$lib/api';
import { QueryClient } from '@tanstack/svelte-query';

export const load = async ({ fetch }) => {
	const queryClient = new QueryClient({
		defaultOptions: {
			queries: {
				// make sure queries don't run on the server during SSR
				enabled: browser
			}
		}
	});

	await queryClient.prefetchQuery({
		queryKey: ['userInfo'],
		queryFn: () => api.GET('/api/v1/auth/user_info', {}, fetch)
	});
	return { queryClient };
};
