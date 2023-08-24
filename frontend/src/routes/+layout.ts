import { browser } from '$app/environment';
import { QueryClient } from '@tanstack/svelte-query';
import type { LayoutLoad } from './$types';

export const load: LayoutLoad = async () => {
	const queryClient = new QueryClient({
		defaultOptions: {
			queries: {
				// make sure queries don't run on the server during SSR
				enabled: browser
			}
		}
	});

	return { queryClient };
};
