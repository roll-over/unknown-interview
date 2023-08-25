<script lang="ts">
	import type { StrictOmit } from '$lib/utils/types';
	import type { HTMLInputAttributes } from 'svelte/elements';

	export { className as class };
	export let attrs: StrictOmit<HTMLInputAttributes, 'class'> = {};

	let className: string = '';
</script>

<input
	class="{className} rounded-lg p-2"
	{...attrs}
/>
