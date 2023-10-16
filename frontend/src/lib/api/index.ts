import { browser } from '$app/environment';
import { PUBLIC_EXTERNAL_URL, PUBLIC_INTERNAL_URL, PUBLIC_IS_DOCKER } from '$env/static/public';
import type { paths } from '$lib/openapi'; // generated from openapi-typescript
import createClient from 'openapi-fetch';

const baseUrl = browser ? undefined : PUBLIC_IS_DOCKER ? PUBLIC_INTERNAL_URL : PUBLIC_EXTERNAL_URL;

const api = createClient<paths>({ baseUrl });
export default api;

function createApiQuery<A extends unknown[], K extends keyof typeof api, R>(
	fn: (...args: A) => R,
	verb: K
) {
	return (...args: A) => {
		return {
			invoke: () => fn(...args),
			keys: otherStuff({ args, verb })
		};
	};
}

export const createGetCall = createApiQuery(api.GET, 'GET');

function otherStuff<T>(x: T) {
	return { whatever: x };
}

export function wait(ms: number) {
	return new Promise<void>((r) => {
		setTimeout(() => {
			r();
		}, ms);
	});
}
