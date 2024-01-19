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
		class="relative z-0 mb-52 flex h-52 w-full flex-col items-center gap-6 font-title md:mb-28 md:h-80"
	>
		{#if $modeCurrent}
			<Logo />
		{:else}
			<LogoDark />
		{/if}
		<h1 class="text-center text-lg uppercase dark:text-white md:text-3xl">
			Skills first. Unbiased Hiring.
		</h1>
	</div>
	<a
		href={route('/purpose')}
		class="group flex items-center justify-end gap-6 rounded-lg bg-white py-3 pl-16 pr-16 text-lg text-black transition-colors current:bg-app-blue-400 dark:bg-app-dark-blue dark:text-white dark:hover:bg-app-dark-light md:gap-16 md:pl-24 md:text-2xl"
	>
		go to survey
		<IcOutlineArrowForwardIos
			class="text-2xl text-app-blue-500 transition-colors group-current:text-app-blue-100 dark:text-white md:text-6xl"
		/>
	</a>
</div>
