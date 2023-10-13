import type { Param, RestParam, Route, TemplateToken } from '$lib/router';

function parseParam<P extends TemplateToken, R extends TemplateToken[]>(p: P, ...r: R) {
	return (r.length ? `${p}/${r.join('/')}` : p) as R extends [TemplateToken, ...TemplateToken[]]
		? RestParam
		: Param;
}

/**
 * Function which ensures that provided route exists in SvelteKit's file-router.
 * @param path for static paths you may provide just a string.
 *
 * For dynamic routes it has to be a function. It's first argument will be a transform function through which you will need to pass route params.
 *
 * Exmaple: `route(p => '/user/${p(id)}')`
 *
 * For rest params a list of value is accepted:
 *
 * Example:  `route(p => '/compare/${p(id1, id2, id3)}')`
 * @returns a string with a resolved route
 */
export function route(path: Route | ((param: typeof parseParam) => Route)) {
	return typeof path === 'string' ? path : path(parseParam);
}
