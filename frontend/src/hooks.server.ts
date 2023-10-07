import { INTERNAL_URL } from '$env/static/private';
import type { Handle, HandleFetch } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
	return resolve(event, {
		filterSerializedResponseHeaders(name) {
			// fixes some bizzare behavior with undici, openapi-fetch & svelte's custom fetch during prefetching on server
			return name === 'content-length';
		}
	});
};

export const handleFetch: HandleFetch = async ({ event, fetch, request }) => {
	const cookies = event.request.headers.get('cookie');
	// todo - this needs a more robust check if fetch request we're making is to our backend to pass along session cookie
	if (cookies && request.url.startsWith(INTERNAL_URL.slice(0, -3))) {
		request.headers.set('cookie', cookies);
	}

	return fetch(request);
};
