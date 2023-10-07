import createClient from 'openapi-fetch';
import type { paths } from '$lib/openapi'; // generated from openapi-typescript
import { browser } from '$app/environment';

const baseUrl = browser
	? undefined
	: process.env.isDocker
	? process.env.INTERNAL_URL
	: process.env.EXTERNAL_URL;

const api = createClient<paths>({ baseUrl });

export default api;
