import { watch } from 'chokidar';
import { writeFile } from 'fs/promises';
import { glob } from 'glob';
import { format } from 'prettier';

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
			.map((path) =>
				path
					.relative()
					.split(path.sep)
					// slice removes first 2 elements("src" & "routes") and last one("+page.svelte")
					.slice(2, -1)
			)
	);
}

type Chunk = { type: 'STATIC' | 'DYNAMIC' | 'OPTIONAL' | 'REST'; key: string };
type Segment = Chunk[];
type Route = Segment[];
export function parsePath(path: string[]): Route {
	return (
		path
			.map(parseSegment)
			// filter null segments - null segments are a result of group routes
			.filter((x): x is Segment => !!x)
	);
}

function parseSegment(segment: string): Segment | null {
	if (segment.startsWith('(') && segment.endsWith(')')) return null;

	return (
		segment
			.split(/(\[+.+?\]+)/)
			// filter empty strings which appear after split if matched splitter is at the start/end
			.filter(Boolean)
			.map(parseChunk)
	);
}

function parseChunk(chunk: string): Chunk {
	if (!chunk.startsWith('[') && !chunk.endsWith(']')) return { type: 'STATIC', key: chunk };

	// remove [], dots & matchers(=matcher)
	const key = chunk.replaceAll(/[[\].]|(=.+)/g, '');
	if (chunk.startsWith('[[')) return { type: 'OPTIONAL', key };
	if (chunk.startsWith('[...')) return { type: 'REST', key };
	return { type: 'DYNAMIC', key };
}

function stringifyRoutes(routes: Route[]): string {
	return [...new Set(routes.flatMap(stringifyRoute))].join(' | ');
}

export function stringifyRoute(route: Route): string[] {
	return forkify(route.map(stringifySegment)).map(
		(fork) =>
			'`/' +
			fork
				// filter empty strings which are results of optional chunks
				.filter(Boolean)
				.join('/') +
			'`'
	);
}

function stringifySegment(segment: Segment): string[] {
	return forkify(segment.map(stringifyChunk)).map((fork) => fork.filter(Boolean).join(''));
}

const PARAM = 'Param';
const REST_PARAM = 'RestParam';
export const templateParam = '${' + PARAM + '}';
export const templateRest = '${' + REST_PARAM + '}';
function stringifyChunk(chunk: Chunk): string | [string, null] {
	switch (chunk.type) {
		case 'STATIC':
			return chunk.key;
		case 'DYNAMIC':
			return templateParam;
		case 'OPTIONAL':
			return [templateParam, null];
		case 'REST':
			return [templateRest, null];
		default: {
			const x: never = chunk.type;
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
