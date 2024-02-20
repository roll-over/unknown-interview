<script>
	import { SlideToggle } from '@skeletonlabs/skeleton';
	let showFirstDiv = true;

	const toggleDiv = () => {
		showFirstDiv = !showFirstDiv;
		const divs = document.querySelectorAll('.text-md > div');

		divs.forEach((div, index) => {
			div.style.display = showFirstDiv || index % 2 === 0 ? 'block' : 'none';
		});
	};
</script>

<SlideToggle
	class="ml-auto mr-2 flex pb-0 pl-1 pt-2 md:pl-12 xl:hidden"
	size="sm"
	active="bg-app-blue-400"
	background="bg-app-dark-gray"
	name="slider-small"
	bind:checked={showFirstDiv}
	on:click={toggleDiv}
>
	<span class="inline-block text-left dark:text-white">{showFirstDiv ? 'Offer' : 'My profile'}</span
	>
</SlideToggle>

<div
	class="text-md sm: md: lg: xl: grid h-full grid-cols-[1fr] grid-rows-[1fr] gap-1 px-1 py-1 dark:text-white md:max-h-none md:gap-x-5 md:px-12 md:py-5 md:text-2xl xl:grid-cols-[2fr,3fr]"
>
	<slot />
</div>
