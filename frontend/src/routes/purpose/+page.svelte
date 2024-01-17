<script lang="ts">
	import MaterialSymbolsLaptopMacOutline from '~icons/material-symbols/laptop-mac-outline';
	import IcOutlineGroups from '~icons/ic/outline-groups';
	import { route } from '$lib/utils/route';
</script>

<div class="bg-light-background dark:bg-dark-background flex h-full justify-center dark:text-white">
	<div class="grid h-full w-full max-w-5xl grid-rows-2">
		<h1 class="font-title m-auto text-center text-6xl">Visit Purpose</h1>
		<div class="md:gap-15 flex flex-col items-start justify-around gap-5 md:flex-row md:p-10">
			<a
				class="current:scale-105 flex w-full flex-col items-center gap-4 transition-transform"
				href={route('/vacancy/create')}
			>
				<span
					class="bg-app-blue-100 dark:bg-app-dark-blue dark:hover:bg-app-dark-light w-full rounded-xl px-16 py-6 text-center text-3xl transition-colors hover:bg-sky-400"
					>Post your vacancy</span
				>
				<MaterialSymbolsLaptopMacOutline
					class="text-app-blue-500 dark:text-app-dark-gray h-40 w-40"
				/>
			</a>
			<a
				class="current:scale-105 flex w-full flex-col items-center gap-4 transition-transform"
				href={route('/cv/create')}
			>
				<span
					class="bg-app-blue-100 dark:bg-app-dark-blue dark:hover:bg-app-dark-light w-full rounded-xl px-16 py-6 text-center text-3xl transition-colors hover:bg-sky-400"
					>Post your CV</span
				>
				<IcOutlineGroups class="text-app-blue-500 dark:text-app-dark-gray h-40 w-40" />
			</a>
		</div>
	</div>
</div>

<style>
	.go-btn {
		max-width: 400px;
		width: 100%;
		min-width: 320px;
	}
</style>
