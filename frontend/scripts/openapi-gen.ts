import { writeFile } from 'fs/promises';
import generateOpenApiTypes, { type OpenAPI3 } from 'openapi-typescript';

export default async function generateOpenApi() {
	const spec = await getOpenApiSpec().catch(console.error);
	if (!spec) return;

	const types = await generateOpenApiTypes(spec);
	writeFile('./src/lib/openapi.d.ts', types)
		.then(() => {
			console.log('Sucessfully saved openapi.d.ts file');
		})
		.catch((e) => {
			console.error(e);
			console.error('Error while trying to write openapi.d.ts file');
		});
}

let retries = 0;
function getOpenApiSpec() {
	return new Promise<OpenAPI3>((resolve, reject) => {
		fetch(
			new URL(
				'api/openapi.json',
				process.env.PUBLIC_IS_DOCKER
					? process.env.PUBLIC_INTERNAL_URL
					: process.env.PUBLIC_EXTERNAL_URL
			)
		)
			.then((x) => x.json())
			.then(resolve)
			.catch(() => {
				if (++retries >= 5) {
					throw Error("Couldn't reach the server in 5 retries. Aborting generating openAPI types");
				}
				console.error("Couldn't reach the server, retrying in 10 seconds");
				setTimeout(() => resolve(getOpenApiSpec()), 10000);
			})
			.catch(reject);
	});
}
