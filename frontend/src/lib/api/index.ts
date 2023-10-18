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

type Options =
	// Post requests
	| FetchOptions<{ requestBody?: { content?: { [x: `${string}/${string}`]: unknown } } }>
	// Patch requests
	| FetchOptions<{
			requestBody?: { content?: { [x: `${string}/${string}`]: unknown } };
			parameters: unknown;
	  }>
	// Get requests & the rest
	// eslint-disable-next-line @typescript-eslint/no-explicit-any
	| FetchOptions<any>;
type InputOptions = StrictPick<Options, 'params' | 'body'>;
type ExtraOptions<O extends Options | undefined = Options> = StrictOmit<
	NonNullable<O>,
	'params' | 'body'
>;
/**
 * Key used to identify queries/mutations.
 * Consists of two elements - domain and input.
 * Domain itself consists of two elements - path and http-verb.
 * Allows to invalidate queries hierarchically - all queries on a given path for specific or all verbs, with or w/o input
 */
type DataKey<RequireVerb extends boolean = true> = [
	[path: PathId, ...(RequireVerb extends true ? [verb: HttpVerb] : [verb?: HttpVerb])],
	InputOptions?
];
type Query<A extends Options = Options, R = unknown> = {
	/**
	 * Run a network query to specified resource.
	 * @param opts these options will be merged with the options from create{Verb}Query
	 */
	runQuery: (opts?: ExtraOptions<A>) => R;
	/**
	 * Unique key to identify that query including path, verb & input.
	 */
	key: DataKey;
};
type Mutation<A extends unknown[] = unknown[], R = unknown> = {
	/**
	 * Run a network mutation to specified resource.
	 * @param opts input accepted by the resource.
	 */
	runMutation: (...opts: A) => R;
	/**
	 * Unique key to identify that mutation including path & verb.
	 */
	key: DataKey;
};

/**
 * Generic function to create API queries.
 * @param apiFn api call function like api.GET/HEAD/OPTIONS/TRACE
 * @param verb verb corresponding to {@link apiFn}
 * @returns a function which returns a {@link Query}
 */
function createApiQuery<P extends PathId, O extends [Options?], V extends HttpVerb, R>(
	apiFn: (path: P, ...opts: O) => R,
	verb: V
) {
	return function (path: P, ...[opts]: O): Query<NonNullable<O[0]>, R> {
		return {
			runQuery: (arg?: ExtraOptions<O[0]>) =>
				apiFn(path, ...([arg ? { ...opts, ...arg } : opts] as unknown as O)),
			get key() {
				return createKey(path, verb, opts);
			}
		};
	};
}
/**
 * Generic function to create API mutations.
 * @param apiFn api call function like api.POST/PATCH/DELETE/PUT
 * @param verb verb corresponding to {@link apiFn}
 * @returns a function which returns a {@link Mutation}
 */
function createApiMutation<P extends PathId, O extends [Options?], V extends HttpVerb, R>(
	apiFn: (path: P, ...opts: O) => R,
	verb: V
) {
	return function (path: P): Mutation<O, R> {
		return {
			runMutation: (...opts: O) => apiFn(path, ...opts),
			get key() {
				return createKey(path, verb);
			}
		};
	};
}

function createKey(path: PathId, verb: HttpVerb, opts?: InputOptions): DataKey {
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

/**
 * A helper to get query key with required precision
 * @param query your {@link Query}
 * @param type whether the key should invalidate all verbs on a given path or only the current one
 */
export function getQueryKey(
	{ key }: StrictPick<Query | Mutation, 'key'>,
	type?: 'invalidate route' | 'invalidate verb'
): DataKey<false> {
	switch (type) {
		case 'invalidate route':
			return [[key[0][0]]];
		case 'invalidate verb':
			return [key[0]];
		default:
			return key;
	}
}

/**
 * Alias for {@link getQueryKey}
 */
export const getMutationKey = getQueryKey;
