import { watch } from 'chokidar';
import { writeFile } from 'fs/promises';
import { glob } from 'glob';
import { format } from 'prettier';

// if some matcher have known values you can put them here and they will replace parameter values
// doesn't work for rest params because I don't want to
const matcherTypes: Record<string, string[]> = {
	type: ['cv', 'vacancy']
};

const pageGlobMatcher = './src/routes/**/+page?(@)*.svelte';

export default async function generateRoutes() {
	const paths = await getPaths();
	const routes = paths.map(parsePath);
	const type = stringifyRoutes(routes);
	return writeRouteFile(type).catch(console.error);
}

export function generateRoutesWatcher() {
	let isGenerating = false;
	async function handler() {
		if (isGenerating) return;
		isGenerating = true;
		await generateRoutes();
		isGenerating = false;
	}

	const pageWatcher = watch(pageGlobMatcher);
	pageWatcher.on('add', handler);
	pageWatcher.on('unlink', handler);

	const dirWatcher = watch('./src/routes');
	dirWatcher.on('unlinkDir', handler);
	return () => {
		pageWatcher.close();
		dirWatcher.close();
	};
}

function getPaths() {
	return glob(pageGlobMatcher, { withFileTypes: true }).then((files) =>
		files
			.filter((file) => file.isFile())
			.sort((a, b) => (a.path > b.path ? 1 : -1))
			// slice removes first 2 elements("src" & "routes") and last one("+page.svelte")
			.map((path) => path.relative().split(path.sep).slice(2, -1))
	);
}

type Chunk =
	| { type: 'STATIC'; key: string }
	| { type: 'DYNAMIC' | 'OPTIONAL' | 'REST'; key: string; matcher?: string };
type Segment = Chunk[];
type Route = Segment[];
export function parsePath(path: string[]): Route {
	// filter null segments - null segments are a result of group routes
	return path.map(parseSegment).filter((x): x is Segment => !!x);
}

function parseSegment(segment: string): Segment | null {
	if (segment.startsWith('(') && segment.endsWith(')')) return null;

	// filter empty strings which appear after split if matched splitter is at the start/end
	return segment
		.split(/(\[+.+?\]+)/)
		.filter(Boolean)
		.map(parseChunk);
}

function parseChunk(chunk: string): Chunk {
	if (!chunk.startsWith('[') && !chunk.endsWith(']')) return { type: 'STATIC', key: chunk };

	// extract matcher if any
	const matcher = chunk.match(/\[.+=(.+?)\]/)?.[1];

	// remove [], dots & matchers(=matcher)
	const key = chunk.replaceAll(/[[\].]|(=.+)/g, '');
	if (chunk.startsWith('[[')) return { type: 'OPTIONAL', key, matcher };
	if (chunk.startsWith('[...')) return { type: 'REST', key, matcher };
	return { type: 'DYNAMIC', key, matcher };
}

function stringifyRoutes(routes: Route[]): string {
	return [...new Set(routes.flatMap(stringifyRoute))].join(' | ');
}

export function stringifyRoute(route: Route): string[] {
	return forkify(route.map(stringifySegment)).map(
		// filter empty strings which are results of optional chunks
		(fork) => '`/' + fork.filter(Boolean).join('/') + '`'
	);
}

function stringifySegment(segment: Segment): string[] {
	return forkify(segment.map(stringifyChunk)).map((fork) => fork.join(''));
}

const PARAM = 'Param';
const REST_PARAM = 'RestParam';
export const templateParam = '${' + PARAM + '}';
export const templateRest = '${' + REST_PARAM + '}';

function stringifyChunk(chunk: Chunk): string | Array<string | null> {
	const matcherType = chunk.type !== 'STATIC' && chunk.matcher ? matcherTypes[chunk.matcher] : null;

	switch (chunk.type) {
		case 'STATIC':
			return chunk.key;
		case 'DYNAMIC':
			return matcherType ? matcherType : templateParam;
		case 'OPTIONAL':
			return matcherType ? [...matcherType, null] : [templateParam, null];
		case 'REST':
			return [templateRest, null];
		default: {
			const x: never = chunk;
			return x;
		}
	}
}

async function writeRouteFile(routeType: string) {
	const fileData = `
	// This file is auto-generated. Please do not modify it.
	declare const Brand: unique symbol;
	type TemplateToken = string | number;
	type ${PARAM} = TemplateToken & { readonly [Brand]: unique symbol };
	type ${REST_PARAM} = (TemplateToken & { readonly [Brand]: unique symbol }) | ${PARAM};
	type Route = ${routeType};
	export { ${PARAM}, ${REST_PARAM}, Route, TemplateToken }
	`;

	writeFile('./src/lib/router.d.ts', await format(fileData, { parser: 'typescript' }))
		.catch((e) => {
			console.error('Error while trying to write router.d.ts file');
			console.error(e);
		})
		.then(() => {
			console.log('Sucessfully saved router.d.ts file');
		});
}

/**
 * Flattens the array producing forks from provided array-elements.
 *
 * Example: `[1, [2, 3], 4]` will produce `[[1, 2, 4], [1, 3, 4]]`
 */
function forkify<T>(array: Array<T | T[]>) {
	return array.reduce<T[][]>(
		(forks, value) => {
			if (!Array.isArray(value)) {
				forks.forEach((fork) => fork.push(value));
				return forks;
			}

			return value.flatMap((variant) => forks.map((fork) => [...fork, variant]));
		},
		[[]]
	);
}
