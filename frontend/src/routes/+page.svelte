<script lang="ts">
	import { route } from '$lib/utils/route';
	import IcOutlineArrowForwardIos from '~icons/ic/outline-arrow-forward-ios';
	import Logo from '~icons/main/logo';
	import LogoDark from '~icons/main/logo-dark';
	import { modeCurrent } from '../lib/utils/LightSwitch/index';
	
</script>

<div class="bg-light-background dark:bg-dark-background h-full flex flex-col items-center justify-center">
	<div class="font-title gap-6 md:h-80 h-52 relative z-0 md:mb-28 mb-52 flex w-full flex-col items-center">
    {#if $modeCurrent}
      <Logo/>
    {:else}
      <LogoDark/>
    {/if}
		<h1 class="text-center md:text-3xl text-lg uppercase dark:text-white">Skills first. Unbiased Hiring.</h1>
	</div>
	<a
		href={route('/purpose')}
		class="current:bg-app-blue-400 dark:bg-app-dark-blue dark:hover:bg-app-dark-light group flex items-center justify-end md:gap-16 gap-6 rounded-lg bg-white py-3 pr-16 pl-16 md:pl-24 md:text-2xl text-lg text-black transition-colors dark:text-white"
	>
		go to survey
		<IcOutlineArrowForwardIos
			class="text-app-blue-500 group-current:text-app-blue-100 md:text-6xl text-2xl transition-colors dark:text-white"
		/>
	</a>
</div>
