import createClient from 'openapi-fetch';
import type { paths } from '$lib/openapi'; // generated from openapi-typescript
import { browser } from '$app/environment';
import { PUBLIC_EXTERNAL_URL, PUBLIC_INTERNAL_URL, PUBLIC_IS_DOCKER } from '$env/static/public';
import { createQuery } from '@tanstack/svelte-query';

const baseUrl = browser ? undefined : PUBLIC_IS_DOCKER ? PUBLIC_INTERNAL_URL : PUBLIC_EXTERNAL_URL;

const api = createClient<paths>({ baseUrl });

export default api;

const userInfoKey = 'userInfo';
export const getUserInfo = createApiCall([userInfoKey], () => api.GET('/api/v1/auth/user_info'));

function createApiCall<R>(key: string[], fn: () => Promise<R> | R) {
	return () =>
		createQuery({
			queryKey: key,
			queryFn: fn
		});
}
