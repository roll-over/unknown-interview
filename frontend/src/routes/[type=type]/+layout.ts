export function load({ params }) {
	return { isCvRoute: params.type === 'cv' };
}
