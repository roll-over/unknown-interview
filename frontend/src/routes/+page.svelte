<script lang="ts">
	import IcOutlineArrowForwardIos from '~icons/ic/outline-arrow-forward-ios';
	import Diversity from '~icons/main/diversity';
	import Background from '~icons/main/background';
</script>

<div class="flex h-full flex-col items-center justify-center bg-white">
	<div class="font-title relative z-0 mb-12 flex w-full flex-col items-center">
		<Background class="absolute bottom-0 -z-10 h-[95%] w-[9999px] px-5" />
		<Diversity class="text-app-blue-500 h-52 w-full" />
		<h1 class="pb-2 text-6xl text-gray-900">Hello!</h1>
		<p class="text-2xl text-black">Fill out a short form to get started!</p>
	</div>
	<a
		href="/create"
		class="bg-app-blue-100 current:bg-app-blue-400 group flex items-center justify-end gap-6 rounded-lg px-14 py-2.5 text-2xl text-black focus:outline-none focus:ring-4"
	>
		go to survey!
		<IcOutlineArrowForwardIos class="text-app-blue-500 group-current:text-app-blue-100 text-3xl" />
	</a>
</div>
