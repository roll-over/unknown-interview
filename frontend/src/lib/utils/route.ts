import type { Param, Route } from '$lib/router';

const _param = (x: string | number) => x as Param;
export const route = (path: Route | ((param: typeof _param) => Route)) =>
	typeof path === 'string' ? path : path(_param);
