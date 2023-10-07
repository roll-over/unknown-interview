import { PUBLIC_EXTERNAL_URL, PUBLIC_INTERNAL_URL } from '$env/static/public';
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

	if (cookies && isOurHost(request.url)) {
		request.headers.set('cookie', cookies);
	}

	return fetch(request);
};

function isOurHost(url: string) {
	// todo - this needs a more robust check if fetch request we're making is to our backend to pass along session cookie
	return (
		url.startsWith(PUBLIC_INTERNAL_URL.slice(0, -3)) ||
		url.startsWith(PUBLIC_EXTERNAL_URL.slice(0, -5))
	);
}
