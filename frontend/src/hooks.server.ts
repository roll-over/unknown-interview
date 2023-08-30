import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
	return resolve(event, {
		filterSerializedResponseHeaders(name) {
			// fixes some bizzare behavior with undici, openapi-fetch & svelte's custom fetch during prefetching on server
			return name === 'content-length';
		}
	});
};
