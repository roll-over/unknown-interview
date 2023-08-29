import { writeFile } from 'fs/promises';
import openApiTs, { type OpenAPI3 } from 'openapi-typescript';

async function generateOpenAPI() {
	const spec = await getOpenAPISpec();
	const types = await openApiTs(spec);
	writeFile('./src/openapi.d.ts', types);
}

async function getOpenAPISpec(): Promise<OpenAPI3> {
	return new Promise((r) => {
		fetch('http://localhost:2080/api/openapi.json')
			.then((x) => x.json())
			.then(r)
			.catch(() => {
				console.error("Couldn't reacth the server, retrying in 1 second");
				setTimeout(() => r(getOpenAPISpec()), 1000);
			});
	});
}

generateOpenAPI();
