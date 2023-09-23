import { glob } from 'glob';

async function generateRoutes() {
	const dir = await glob('./src/routes/**/+page.svelte', { withFileTypes: true }).then(
		(files) => files.filter((file) => file.isFile()).map((file) => file.relative())
		// .map((file) => file.match(/src.routes.(.*).+page.svelte/)?.[1])
	);
	console.log({ dir });
}

generateRoutes();

type Query = string & { readonly __tag: unique symbol };
type Template = `one` | `one/${Query}` | `one/${Query}/two` | `one/${Query}/two/${Query}`;

const t: Template = `one/${'1' as Query}/two`;

console.log(t);
