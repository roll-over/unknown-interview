import { writeFile } from 'fs/promises';
import { glob } from 'glob';
import { format } from 'prettier';
import { watch } from 'chokidar';

export default async function generateRoutes() {
	const routes = await glob('./src/routes/**/+page.svelte', { withFileTypes: true }).then((files) =>
		files
			.filter((file) => file.isFile())
			.map<Route>((file) =>
				file
					.relative()
					.split(file.sep)
					// slice removes first 2 elements("src" & "routes") and last one("+page.svelte")
					.slice(2, -1)
					.map(stringToSegment)
					.filter((x): x is Segment => !!x)
			)
	);
	const routeType = routesToType(routes);
	writeRouteFile(routeType);
}

export function generateRoutesWatcher() {
	const watcher = watch('./src/routes/**/+page.svelte');
	watcher.on('add', generateRoutes);
	watcher.on('unlink', generateRoutes);
}

function routesToType(routes: Route[]) {
	const types = routes
		.flatMap((route) => {
			const routeForks = forkify(route.map(segmentToType));
			return routeForks.map((fork) => '/' + fork.filter(Boolean).join('/'));
		})
		.map((route) => `\`${route}\``);
	return [...new Set(types)].join(' | ');
}

type Segment = { type: 'STATIC' | 'DYNAMIC' | 'OPTIONAL' | 'REST'; key: string };
type Route = Segment[];
function stringToSegment(segment: string): Segment | null {
	if (segment.startsWith('(') && segment.endsWith(')')) return null;
	if (!(segment.startsWith('[') || segment.endsWith(']'))) return { type: 'STATIC', key: segment };

	// remove [], dots & matchers(=matcher)
	const key = segment.replaceAll(/[[\].]|(=.+)/g, '');
	if (segment.startsWith('[[')) return { type: 'OPTIONAL', key };
	if (segment.startsWith('[...')) return { type: 'REST', key };
	return { type: 'DYNAMIC', key };
}

function segmentToType(segment: Segment): string | [string, null] {
	switch (segment.type) {
		case 'STATIC':
			return segment.key;
		case 'DYNAMIC':
			return '${Param}';
		case 'OPTIONAL':
			return ['${Param}', null];
		case 'REST':
			return ['${Param}', null];
		default: {
			const x: never = segment.type;
			return x;
		}
	}
}

async function writeRouteFile(routeType: string) {
	const fileData = `
	// This file is auto-generated. Please do not modify it.
	declare const ParamBrand: unique symbol;
	type Param = (string | number) & { readonly [ParamBrand]: unique symbol };
	type Route = ${routeType};
	export { Param, Route }
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
