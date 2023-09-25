<script lang="ts">
	import MaterialSymbolsLaptopMacOutline from '~icons/material-symbols/laptop-mac-outline';
	import IcOutlineGroups from '~icons/ic/outline-groups';
	import { route } from '$lib/utils/route';
</script>

<div class="flex h-full justify-center">
	<div class="grid h-full w-full max-w-5xl grid-rows-2">
		<h1 class="m-auto text-center font-title text-6xl">Visit Purpose</h1>
		<div class="flex flex-wrap items-start justify-around">
			<a
				class="flex flex-col items-center gap-4 transition-transform current:scale-105"
				href={route('/create/offer')}
			>
				<span class="rounded-xl bg-app-blue-100 px-16 py-6 text-3xl">Post a job offer</span>
				<MaterialSymbolsLaptopMacOutline class="h-40 w-40 text-app-blue-500" />
			</a>
			<a
				class="flex flex-col items-center gap-4 transition-transform current:scale-105"
				href={route('/create/cv')}
			>
				<span class="rounded-xl bg-app-blue-100 px-16 py-6 text-3xl">Post your resume</span>
				<IcOutlineGroups class="h-40 w-40 text-app-blue-500" />
			</a>
		</div>
	</div>
</div>
