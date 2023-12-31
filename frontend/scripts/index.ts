// this file is run by script.ts to execute default export of provided module
main();
async function main() {
	const moduleName = process.argv[2];
	if (!moduleName) throw Error(`Module name wasn't provided`);

	const moduleFile = `./${moduleName}.ts`;
	const module: unknown = await import(moduleFile);

	if (!(module && typeof module === 'object'))
		throw Error(`No module with name ${moduleFile} was found`);

	if (!('default' in module)) throw Error(`Module ${moduleFile} has no default export`);

	if (typeof module.default !== 'function')
		throw Error(`Module ${moduleFile} default export is not of type Function`);

	if (!process.env.PUBLIC_IS_DOCKER) {
		const dotenv = await import('dotenv');
		dotenv.config({ path: '../.env' });
	}
	try {
		module.default();
	} catch (error) {
		console.error(error);
	}
}
