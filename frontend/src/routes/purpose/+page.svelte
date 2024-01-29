<script lang="ts">
	import MaterialSymbolsLaptopMacOutline from '~icons/material-symbols/laptop-mac-outline';
	import IcOutlineGroups from '~icons/ic/outline-groups';
	import { route } from '$lib/utils/route';
</script>

<div class="flex h-full justify-center bg-light-background dark:bg-dark-background dark:text-white">
	<div class="grid content-between md:content-center h-full w-auto md:w-full max-w-none md:max-w-lg xl:max-w-7xl">
		<h1 class="m-auto mb-0 md:mb-20 md:mt-2 mt-36 text-center text-2xl md:text-7xl">Visit purpose</h1>
		<div
			class="flex mb-16 xl:mb-0 flex-col items-start justify-center gap-5 md:justify-around md:gap-20 md:p-10 xl:flex-row xl:gap-80"
		>
			<a
				class="flex w-full flex-col items-center gap-1 transition-transform current:scale-105 md:gap-4"
				href={route('/vacancy/create')}
			>
				<span
					class="md:text-large w-full rounded-lg bg-white md:pt-6 md:pb-6 pt-3.5 pb-3.5 pl-20 pr-20 text-center text-xs transition-colors hover:bg-sky-400 dark:bg-app-dark-blue dark:hover:bg-app-dark-light md:text-3xl"
					>Employees search</span
				>
				<MaterialSymbolsLaptopMacOutline
					class="hidden h-40 w-40 text-app-blue-500 dark:text-app-dark-gray md:inline"
				/>
			</a>
			<a
				class="flex w-full flex-col items-center gap-0 transition-transform current:scale-105 md:gap-4"
				href={route('/cv/create')}
			>
				<span
					class="md:text-large w-full rounded-lg bg-white md:pt-6 md:pb-6 pt-3.5 pb-3.5 pl-20 pr-20 text-center text-xs transition-colors hover:bg-sky-400 dark:bg-app-dark-blue dark:hover:bg-app-dark-light md:text-3xl"
					>Job search</span
				>
				<IcOutlineGroups
					class="hidden h-40 w-40 text-app-blue-500 dark:text-app-dark-gray md:inline"
				/>
			</a>
		</div>
	</div>
</div>
