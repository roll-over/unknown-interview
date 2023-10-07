import createClient from 'openapi-fetch';
import type { paths } from '$lib/openapi'; // generated from openapi-typescript
import { browser } from '$app/environment';

async function getBaseUrl(): Promise<string | undefined> {
	if (browser) return undefined;

	const env = await import('$env/static/private');
	return env.IS_DOCKER ? env.INTERNAL_URL : env.EXTERNAL_URL;
}

const api = createClient<paths>({ baseUrl: await getBaseUrl() });

export default api;
