<script lang="ts">
	import { route } from '$lib/utils/route';
	import IcOutlineArrowForwardIos from '~icons/ic/outline-arrow-forward-ios';
	import Logo from '~icons/main/logo';
</script>

<div class="bg-light-background dark:bg-dark-background flex flex-col items-center justify-center">
	<div class="font-title relative z-0 mb-12 flex w-full flex-col items-center">
		<Logo class="h-52 w-full dark:fill-white" />
		<h1 class="text-center text-2xl uppercase dark:text-white">Skills first. Unbiased Hiring.</h1>
	</div>
	<a
		href={route('/purpose')}
		class="current:bg-app-blue-400 dark:bg-app-dark-blue dark:hover:bg-app-dark-light group flex items-center justify-end gap-6 rounded-lg bg-white px-14 py-2.5 text-2xl text-black transition-colors dark:text-white"
	>
		go to survey!
		<IcOutlineArrowForwardIos
			class="text-app-blue-500 group-current:text-app-blue-100 text-3xl transition-colors dark:text-white"
		/>
	</a>
</div>
