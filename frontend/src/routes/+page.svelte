<script lang="ts">
	import { route } from '$lib/utils/route';
	import IcOutlineArrowForwardIos from '~icons/ic/outline-arrow-forward-ios';
	import Logo from '~icons/main/logo';
	import LogoDark from '~icons/main/logo-dark';
	import { modeCurrent } from '../lib/utils/LightSwitch/index';
</script>

<div
	class="flex h-full flex-col items-center justify-center bg-light-background dark:bg-dark-background"
>
	<div
		class="relative z-0 mb-60 mt-8 flex h-48 w-full flex-col items-center gap-6 md:mb-28 md:mt-0 md:h-80 md:gap-3"
	>
		{#if $modeCurrent}
			<Logo />
		{:else}
			<LogoDark />
		{/if}
		<h1 class="block text-center font-body uppercase dark:text-white md:font-title">
			<span class="text-m32 md:text-3xl">Skills first.</span>
			<br class="inline md:hidden" />
			<span class="text-xl md:text-3xl">Unbiased Hiring.</span>
		</h1>
	</div>
	<a
		href={route('/purpose')}
		class="group flex items-center justify-end gap-1 rounded-lg bg-white py-3 pl-20 pr-20 text-xs text-black transition-colors current:bg-app-blue-400 dark:bg-app-dark-blue dark:text-white dark:hover:bg-app-dark-light md:gap-16 md:pl-24 md:text-2xl"
	>
		Go to survey
		<IcOutlineArrowForwardIos
			class="text-xl text-app-blue-500 transition-colors group-current:text-app-blue-100 dark:text-white md:text-6xl"
		/>
	</a>
</div>
