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
	const apiUrl = process.env.INTERNAL_URL;
	// todo - this needs a more robust check if fetch request we're making is to our backend to pass along our cookie
	if (apiUrl && request.url.startsWith(apiUrl.slice(0, -3))) {
		request.headers.set('cookie', `session=${event.cookies.get('session')}`);
	}

	return fetch(request);
};
