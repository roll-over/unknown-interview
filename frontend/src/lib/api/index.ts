import { browser } from '$app/environment';
import { PUBLIC_EXTERNAL_URL, PUBLIC_INTERNAL_URL, PUBLIC_IS_DOCKER } from '$env/static/public';
import type { paths } from '$lib/openapi'; // generated from openapi-typescript
import type { StrictOmit, StrictPick } from '$lib/utils/types';
import createClient, { type FetchOptions } from 'openapi-fetch';

const baseUrl = browser ? undefined : PUBLIC_IS_DOCKER ? PUBLIC_INTERNAL_URL : PUBLIC_EXTERNAL_URL;
const api = createClient<paths>({ baseUrl });
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
type InputOptions<O extends MOptions = Options> = StrictPick<NonNullable<O>, 'params' | 'body'>;
type ExtraOptions<O extends MOptions = Options> = StrictOmit<NonNullable<O>, 'params' | 'body'>;
/**
 * QueryKey used to identify queries.
 * Consists of two elements - domain and input.
 * Domain itself consists of two elements - path and http-verb.
 * Allows to invalidate queries hierarchically - all queries on a given path for specific or all verbs, with or w/o specific input
 */
type QueryKey<WithVerb extends boolean = true> = [
	[path: PathId, ...(WithVerb extends true ? [verb: HttpVerb] : [verb?: HttpVerb])],
	InputOptions?
];
type Query<A extends Options = Options, R = unknown> = {
	/**
	 *
	 * @param arg extra options which you may pass in, they will be merged with FetchOptions
	 * @returns
	 */
	runQuery: (arg?: ExtraOptions<A>) => R;
	key: QueryKey;
};

type twoArgFn<A extends unknown[], R> = (...x: [A[0], A[1]]) => R;
function createApiRequest<A1 extends PathId, A2 extends [Options?], V extends HttpVerb, R>(
	fn: (path: A1, ...opts: A2) => R,
	verb: V
) {
	return function (path: A1, ...[opts]: A2): Query<NonNullable<A2[0]>, R> {
		return {
			runQuery: (arg?: ExtraOptions<A2[0]>) =>
				(fn as unknown as twoArgFn<[A1, A2[0]], R>)(path, arg ? { ...opts, ...arg } : opts),
			key: createQueryKey(path, verb, opts)
		};
	};
}

function createQueryKey(path: PathId, verb: HttpVerb, opts?: Options): QueryKey {
	const domainKey: QueryKey[0] = [path, verb];
	if (!opts) return [domainKey];

	return [domainKey, { body: opts.body, params: opts.params }];
}

export const createGetQuery = createApiRequest(api.GET, 'GET');
export const createHeadQuery = createApiRequest(api.HEAD, 'HEAD');
export const createOptionsQuery = createApiRequest(api.OPTIONS, 'OPTIONS');
export const createTraceQuery = createApiRequest(api.TRACE, 'TRACE');

export const createPostMutation = createApiRequest(api.POST, 'POST');
export const createPutMutation = createApiRequest(api.PUT, 'PUT');
export const createDeleteMutation = createApiRequest(api.DELETE, 'DELETE');
export const createPatchMutation = createApiRequest(api.PATCH, 'PATCH');

export function getQueryKey<O extends Options>(
	{ key }: Query<O>,
	opts?: { allVerbs?: boolean; includeParams?: boolean }
): QueryKey<false> {
	if (!opts) return key;

	const domain: QueryKey<false>[0] = opts.allVerbs ? key[0] : [key[0][0]];
	if (opts.includeParams) {
		return [domain, key[1]];
	}
	return [domain];
}
