<script lang="ts">
	import MaterialSymbolsLaptopMacOutline from '~icons/material-symbols/laptop-mac-outline';
	import IcOutlineGroups from '~icons/ic/outline-groups';
	import { route } from '$lib/utils/route';
</script>

<div class="flex h-full justify-center bg-light-background dark:bg-dark-background dark:text-white">
	<div class="grid h-full w-full max-w-xs md:max-w-lg xl:max-w-7xl">
		<h1 class="m-auto text-center text-2xl md:text-7xl">Visit purpose</h1>
		<div
			class="flex flex-col items-start justify-center gap-5 md:justify-around md:gap-2 md:p-10 xl:flex-row xl:gap-80"
		>
			<a
				class="flex w-full flex-col items-center gap-1 transition-transform current:scale-105 md:gap-4"
				href={route('/vacancy/create')}
			>
				<span
					class="md:text-large w-full rounded-xl bg-white px-6 py-3 pl-20 pr-20 text-center text-xs transition-colors hover:bg-sky-400 dark:bg-app-dark-blue dark:hover:bg-app-dark-light md:px-16 md:py-6 md:text-3xl"
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
					class="md:text-large w-full rounded-xl bg-white px-6 py-3 pl-20 pr-20 text-center text-xs transition-colors hover:bg-sky-400 dark:bg-app-dark-blue dark:hover:bg-app-dark-light md:px-16 md:pl-6 md:pr-6 md:text-3xl"
					>Job search</span
				>
				<IcOutlineGroups
					class="hidden h-40 w-40 text-app-blue-500 dark:text-app-dark-gray md:inline"
				/>
			</a>
		</div>
	</div>
</div>
