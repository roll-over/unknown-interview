<script lang="ts">
	import MaterialSymbolsLaptopMacOutline from '~icons/material-symbols/laptop-mac-outline';
	import IcOutlineGroups from '~icons/ic/outline-groups';
	import { route } from '$lib/utils/route';
</script>

<div class="bg-light-background dark:bg-dark-background flex h-full justify-center dark:text-white">
	<div class="grid h-full w-full max-w-xs md:max-w-lg xl:max-w-7xl">
		<h1 class="m-auto text-center md:text-7xl text-3xl">Visit purpose</h1>
		<div class="xl:gap-80 flex flex-col items-start justify-around gap-2 xl:flex-row md:p-10">
			<a
				class="current:scale-105 flex w-full flex-col items-center md:gap-4 gap-1 transition-transform"
				href={route('/vacancy/create')}
			>
				<span
					class="bg-white dark:bg-app-dark-blue dark:hover:bg-app-dark-light w-full rounded-xl md:px-16 px-6 py-3 md:py-6 text-center md:text-3xl text-large transition-colors hover:bg-sky-400"
					>Employees search</span
				>
				<MaterialSymbolsLaptopMacOutline
					class="text-app-blue-500 dark:text-app-dark-gray h-40 w-40"
				/>
			</a>
			<a
				class="current:scale-105 flex w-full flex-col items-center md:gap-4 gap-0 transition-transform"
				href={route('/cv/create')}
			>
				<span
					class="bg-white dark:bg-app-dark-blue dark:hover:bg-app-dark-light w-full rounded-xl md:px-16 px-6 py-3 md:py-6 text-center md:text-3xl text-large transition-colors hover:bg-sky-400"
					>Job search</span
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
