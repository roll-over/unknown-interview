import { browser } from '$app/environment';
import { PUBLIC_EXTERNAL_URL, PUBLIC_INTERNAL_URL, PUBLIC_IS_DOCKER } from '$env/static/public';
import type { paths } from '$lib/openapi'; // generated from openapi-typescript
import type { StrictOmit, StrictPick } from '$lib/utils/types';
import createClient, { type FetchOptions } from 'openapi-fetch';

const baseUrl = browser ? undefined : PUBLIC_IS_DOCKER ? PUBLIC_INTERNAL_URL : PUBLIC_EXTERNAL_URL;
export const api = createClient<paths>({ baseUrl });

type Api = typeof api;
type HttpVerb = keyof Api;
type PathId = keyof paths;

// TODO - DOCUMENT THIS SHIT
type Options =
	// Post requests
	| FetchOptions<{ requestBody?: { content?: { [x: `${string}/${string}`]: unknown } } }>
	// Patch requests
	| FetchOptions<{
			requestBody?: { content?: { [x: `${string}/${string}`]: unknown } };
			parameters: unknown;
	  }>
	// Get requests & others
	// eslint-disable-next-line @typescript-eslint/no-explicit-any
	| FetchOptions<any>;
type MOptions = Options | undefined;
type InputOptions = StrictPick<Options, 'params' | 'body'>;
type ExtraOptions<O extends MOptions = Options> = StrictOmit<NonNullable<O>, 'params' | 'body'>;
/**
 * Key used to identify queries.
 * Consists of two elements - domain and input.
 * Domain itself consists of two elements - path and http-verb.
 * Allows to invalidate queries hierarchically - all queries on a given path for specific or all verbs, with or w/o specific input
 */
type DataKey<RequireVerb extends boolean = true> = [
	[path: PathId, ...(RequireVerb extends true ? [verb: HttpVerb] : [verb?: HttpVerb])],
	InputOptions?
];
type Query<A extends Options = Options, R = unknown> = {
	runQuery: (arg?: ExtraOptions<A>) => R;
	key: DataKey;
};
type Mutation<A extends unknown[] = unknown[], R = unknown> = {
	runMutation: (...args: A) => R;
	key: DataKey;
};

function createApiQuery<A1 extends PathId, A2 extends [Options?], V extends HttpVerb, R>(
	fn: (path: A1, ...opts: A2) => R,
	verb: V
) {
	return function (path: A1, ...[opts]: A2): Query<NonNullable<A2[0]>, R> {
		return {
			runQuery: (arg?: ExtraOptions<A2[0]>) =>
				(fn as unknown as (path: A1, opts: A2[0]) => R)(path, arg ? { ...opts, ...arg } : opts),
			key: createKey(path, verb, opts)
		};
	};
}
function createApiMutation<A1 extends PathId, A2 extends [Options?], V extends HttpVerb, R>(
	fn: (path: A1, ...opts: A2) => R,
	verb: V
) {
	return function (path: A1): Mutation<A2, R> {
		return {
			runMutation: (...opts: A2) => fn(path, ...opts),
			key: createKey(path, verb)
		};
	};
}

function createKey(path: PathId, verb: HttpVerb, opts?: Options): DataKey {
	const domainKey: DataKey[0] = [path, verb];
	if (!opts) return [domainKey];

	return [domainKey, { body: opts.body, params: opts.params }];
}

export const createGetQuery = createApiQuery(api.GET, 'GET');
export const createHeadQuery = createApiQuery(api.HEAD, 'HEAD');
export const createOptionsQuery = createApiQuery(api.OPTIONS, 'OPTIONS');
export const createTraceQuery = createApiQuery(api.TRACE, 'TRACE');

export const createPostMutation = createApiMutation(api.POST, 'POST');
export const createPutMutation = createApiMutation(api.PUT, 'PUT');
export const createDeleteMutation = createApiMutation(api.DELETE, 'DELETE');
export const createPatchMutation = createApiMutation(api.PATCH, 'PATCH');

// todo - better config
export function getQueryKey(
	{ key }: StrictPick<Query | Mutation, 'key'>,
	opts?: { allVerbs?: boolean; includeParams?: boolean }
): DataKey<false> {
	if (!opts) return key;

	const domain: DataKey<false>[0] = opts.allVerbs ? [key[0][0]] : key[0];
	if (opts.includeParams) {
		return [domain, key[1]];
	}
	return [domain];
}
export const getMutationKey = getQueryKey;
