<script lang="ts">
	import { route } from '$lib/utils/route';
	import IcOutlineArrowForwardIos from '~icons/ic/outline-arrow-forward-ios';
	import { modeCurrent } from '../lib/utils/LightSwitch/index';
</script>

<div
	class="flex h-full flex-col items-center justify-between bg-light-background dark:bg-dark-background md:justify-center"
>
	<div
		class="relative z-0 mt-36 flex h-48 w-full select-none flex-col items-center gap-6 md:mb-28 md:mt-0 md:h-80 md:gap-3"
	>
		{#if $modeCurrent}
			<img
				class="pointer-events-none h-32 md:h-80"
				src="logo.svg"
				alt="logotype"
			/>
		{:else}
			<img
				class="pointer-events-none h-32 md:h-80"
				src="logo-dark.svg"
				alt="logotype dark"
			/>
		{/if}
		<h1 class="block text-center font-body uppercase dark:text-white md:font-title">
			<span class="text-m32 md:text-3xl">Skills first.</span>
			<br class="inline md:hidden" />
			<span class="text-xl md:text-3xl">Unbiased Hiring.</span>
		</h1>
	</div>
	<a
		href={route('/purpose')}
		class="group mb-16 flex items-center justify-end gap-1 rounded-lg bg-white py-3 pl-20 pr-20 text-xs text-black transition-colors current:bg-app-blue-400 dark:bg-app-dark-blue dark:text-white dark:hover:bg-app-dark-light md:gap-14 md:pl-28 md:pr-16 md:text-2xl"
	>
		Go to survey
		<IcOutlineArrowForwardIos
			class="text-xl text-app-blue-500 transition-colors group-current:text-app-blue-100 dark:text-white md:text-6xl"
		/>
	</a>
</div>
