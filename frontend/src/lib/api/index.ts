import createClient from 'openapi-fetch';
import type { paths } from '../../openapi'; // generated from openapi-typescript
import { browser } from '$app/environment';

const api = createClient<paths>({
	baseUrl: browser ? undefined : process.env.isDocker ? 'http://client:80' : 'http://localhost:2080'
});
export default api;
