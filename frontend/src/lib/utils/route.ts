import type { Param, RestParam, Route, TemplateToken } from '$lib/router';

function parseParam<T extends TemplateToken | [TemplateToken, ...TemplateToken[]]>(x: T) {
	return (Array.isArray(x) ? x.join('/') : x) as T extends TemplateToken[] ? RestParam : Param;
}

/**
 * Function which ensures that provided route exists in SvelteKit's file-router.
 * @param path for static paths you may provide just a string.
 *
 * For dynamic routes it has to be a function. It's first argument will be a transform function through which you will need to pass route params.
 *
 * Exmaple: `route(p => '/user/${p(id)}')`
 *
 * For multiple rest params an array needs to be passed in:
 *
 * Example:  `route(p => '/compare/${p([id1, id2, id3])}')`
 * @returns a string with a resolved route
 */
export function route(path: Route | ((param: typeof parseParam) => Route)) {
	return typeof path === 'string' ? path : path(parseParam);
}
