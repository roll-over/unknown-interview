import { browser } from '$app/environment';
import { PUBLIC_EXTERNAL_URL, PUBLIC_INTERNAL_URL, PUBLIC_IS_DOCKER } from '$env/static/public';
import type { paths } from '$lib/openapi'; // generated from openapi-typescript
import type { QueryFunction } from '@tanstack/svelte-query';
import createClient, { type FetchOptions } from 'openapi-fetch';

const baseUrl = browser ? undefined : PUBLIC_IS_DOCKER ? PUBLIC_INTERNAL_URL : PUBLIC_EXTERNAL_URL;

const api = createClient<paths>({ baseUrl });
export default api;

function createApiCall<A, R>(
	queryKey: (arg: A) => ReadonlyArray<unknown>,
	fn: (arg: A, signal: AbortSignal) => Promise<R> | R
): (arg: A) => { queryKey: ReadonlyArray<unknown>; queryFn: QueryFunction<R> } {
	return (arg) => ({
		queryKey: queryKey(arg),
		queryFn: ({ signal }) => fn(arg, signal)
	});
}

export const testQuery = createApiCall(
	(id: number) => ['test', id],
	(id, signal) => {
		return api.GET('/api/v1/auth/user_info', {});
	}
);

async function wait(ms: number) {
	return new Promise<void>((r) => {
		setTimeout(() => {
			r();
		}, ms);
	});
}

function produceApiCall<A extends any[], R>(fn: (...args: A) => R) {
	return (...args: A) => {
		return [fn(...args), otherStuff(args)] as const;
	};
}
const testApiCall = produceApiCall(api.GET)('/api/v1/cvs/{cv_id}', {});

api.GET('/api/v1/cvs/{cv_id}', { params: { path: { cv_id: '1' } } });

function otherStuff<T>(x: T) {
	return { whatever: x };
}
