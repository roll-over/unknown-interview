import { writeFile } from 'fs/promises';
import openApiTs, { type OpenAPI3 } from 'openapi-typescript';

async function generateOpenAPI() {
	const spec = await getOpenAPISpec();
	const types = await openApiTs(spec);
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
function getOpenAPISpec() {
	return new Promise<OpenAPI3>((resolve) => {
		fetch(
			new URL(
				'api/openapi.json',
				process.env.isDocker ? 'http://client:80' : 'http://localhost:2080'
			)
		)
			.then((x) => x.json())
			.then(resolve)
			.catch(() => {
				if (++retries >= 5) {
					throw new Error(
						"Couldn't reach the server in 5 retries. Aborting generating openAPI types"
					);
				}
				console.error("Couldn't reach the server, retrying in 10 seconds");
				setTimeout(() => resolve(getOpenAPISpec()), 10000);
			});
	});
}

generateOpenAPI();
