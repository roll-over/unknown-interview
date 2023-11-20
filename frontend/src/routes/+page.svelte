<script lang="ts">
	import { route } from '$lib/utils/route';
	import IcOutlineArrowForwardIos from '~icons/ic/outline-arrow-forward-ios';
	import Logo from '~icons/main/logo';
</script>

<div
	class="flex h-full flex-col items-center justify-center bg-light-background dark:bg-dark-background"
>
	<div class="relative z-0 mb-12 flex w-full flex-col items-center font-title">
		<Logo class="h-52 w-full dark:fill-white" />
		<h1 class="text-2xl uppercase dark:text-white">Skills first. Unbiased Hiring.</h1>
	</div>
	<a
		href={route('/purpose')}
		class="group flex items-center justify-end gap-6 rounded-lg bg-white px-14 py-2.5 text-2xl text-black transition-colors current:bg-app-blue-400 dark:bg-app-dark-blue dark:text-white"
	>
		go to survey!
		<IcOutlineArrowForwardIos
			class="text-3xl text-app-blue-500 transition-colors group-current:text-app-blue-100 dark:text-white"
		/>
	</a>
</div>
