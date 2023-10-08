import { writeFile } from 'fs/promises';
import { glob } from 'glob';
import { format } from 'prettier';
import { watch } from 'chokidar';

const pageGlobMatcher = './src/routes/**/+page?(@)*.svelte';

export default async function generateRoutes() {
	const routes = await glob(pageGlobMatcher, { withFileTypes: true }).then((files) =>
		files
			.filter((file) => file.isFile())
			.sort((a, b) => (a.path > b.path ? 1 : -1))
			.map<Route>((file) =>
				file
					.relative()
					.split(file.sep)
					// slice removes first 2 elements("src" & "routes") and last one("+page.svelte")
					.slice(2, -1)
					.map(parseSegment)
					.filter((x): x is Segment => !!x)
			)
	);
	const routeType = stringifyRoutes(routes).join(' | ');
	return writeRouteFile(routeType).catch(console.error);
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
	dirWatcher.on('addDir', handler);
	dirWatcher.on('unlinkDir', handler);
	return () => {
		pageWatcher.close();
		dirWatcher.close();
	};
}

type Chunk = { type: 'STATIC' | 'DYNAMIC' | 'OPTIONAL' | 'REST'; key: string };
function parseChunk(chunk: string): Chunk {
	if (!chunk.startsWith('[') && !chunk.endsWith(']')) return { type: 'STATIC', key: chunk };

	// remove [], dots & matchers(=matcher)
	const key = chunk.replaceAll(/[[\].]|(=.+)/g, '');
	if (chunk.startsWith('[[')) return { type: 'OPTIONAL', key };
	if (chunk.startsWith('[...')) return { type: 'REST', key };
	return { type: 'DYNAMIC', key };
}

type Segment = Chunk[];
function parseSegment(segment: string): Segment | null {
	if (segment.startsWith('(') && segment.endsWith(')')) return null;

	return segment
		.split(/(\[+.+?\]+)/)
		.filter(Boolean)
		.map(parseChunk);
}

function stringifyChunk(chunk: Chunk): string | [string, null] {
	switch (chunk.type) {
		case 'STATIC':
			return chunk.key;
		case 'DYNAMIC':
			return '${Param}';
		case 'OPTIONAL':
			return ['${Param}', null];
		case 'REST':
			return ['${RestParam}', null];
		default: {
			const x: never = chunk.type;
			return x;
		}
	}
}

function stringifySegment(segment: Segment): string[] {
	return forkify(segment.map(stringifyChunk))
		.map((fork) => fork.filter(Boolean).join(''))
		.filter(Boolean);
}

type Route = Segment[];
function stringifyRoute(route: Route): string[] {
	return forkify(route.map(stringifySegment)).map((fork) => '`/' + fork.join('/') + '`');
}

function stringifyRoutes(routes: Route[]): string[] {
	return [...new Set(routes.flatMap(stringifyRoute))];
}

async function writeRouteFile(routeType: string) {
	const fileData = `
	// This file is auto-generated. Please do not modify it.
	declare const Brand: unique symbol;
	type TemplateToken = string | number;
	type Param = TemplateToken & { readonly [Brand]: unique symbol };
	type RestParam = (TemplateToken & { readonly [Brand]: unique symbol }) | Param;
	type Route = ${routeType};
	export { Param, RestParam, Route, TemplateToken }
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
