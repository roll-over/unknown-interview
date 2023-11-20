<script lang="ts">
	import MaterialSymbolsLaptopMacOutline from '~icons/material-symbols/laptop-mac-outline';
	import IcOutlineGroups from '~icons/ic/outline-groups';
	import { route } from '$lib/utils/route';
</script>

<div class="flex h-full justify-center bg-light-background dark:bg-dark-background dark:text-white">
	<div class="grid h-full w-full max-w-5xl grid-rows-2">
		<h1 class="m-auto text-center font-title text-6xl">Visit Purpose</h1>
		<div class="flex flex-wrap items-start justify-around">
			<a
				class="flex flex-col items-center gap-4 transition-transform current:scale-105"
				href={route('/vacancy/create')}
			>
				<span class="rounded-xl bg-app-blue-100 px-16 py-6 text-3xl dark:bg-app-dark-blue"
					>Post your vacancy</span
				>
				<MaterialSymbolsLaptopMacOutline
					class="h-40 w-40 text-app-blue-500 dark:text-app-dark-gray"
				/>
			</a>
			<a
				class="flex flex-col items-center gap-4 transition-transform current:scale-105"
				href={route('/cv/create')}
			>
				<span class="rounded-xl bg-app-blue-100 px-16 py-6 text-3xl dark:bg-app-dark-blue"
					>Post your CV</span
				>
				<IcOutlineGroups class="h-40 w-40 text-app-blue-500 dark:text-app-dark-gray" />
			</a>
		</div>
	</div>
</div>
