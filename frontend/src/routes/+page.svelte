<script lang="ts">
	import { testQuery } from '$lib/api';
	import { route } from '$lib/utils/route';
	import { createQuery } from '@tanstack/svelte-query';
	import IcOutlineArrowForwardIos from '~icons/ic/outline-arrow-forward-ios';
	import Background from '~icons/main/background';
	import Diversity from '~icons/main/diversity';

	let id = 1;
	$: test = createQuery({ ...testQuery(id) });
</script>

<div class="flex h-full flex-col items-center justify-center bg-white">
	<div class="relative z-0 mb-12 flex w-full flex-col items-center font-title">
		<Background class="absolute bottom-0 -z-10 h-[95%] w-[9999px] px-5" />
		<Diversity class="h-52 w-full text-app-blue-500" />
		<h1 class="pb-2 text-6xl text-gray-900">Hello!</h1>
		<p class="text-2xl text-black">Fill out a short form to get started!</p>
	</div>
	<a
		href={route('/create')}
		class="group flex items-center justify-end gap-6 rounded-lg bg-app-blue-100 px-14 py-2.5 text-2xl text-black transition-colors current:bg-app-blue-400"
	>
		go to survey!
		<IcOutlineArrowForwardIos
			class="text-3xl text-app-blue-500 transition-colors group-current:text-app-blue-100"
		/>
	</a>
	<input
		bind:value={id}
		placeholder="id"
	/>
	<div>{$test.data?.data?.email}</div>
</div>
