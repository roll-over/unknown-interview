<script lang="ts">
	import Chats from './Chats.svelte';
</script>

<div class="grid h-full grid-rows-4">
	<div class="row-span-4 grid grid-cols-4">
		<div class="flex col-span-1 flex-col border-l-0 overflow-y-hidden border-2 border-sky-900 bg-app-blue-50 p-5">
			<h1 class="pb-5 text-center font-title text-xl">Chats</h1>
			<Chats />
		</div>
		<div class="flex col-span-3 overflow-y-hidden justify-center">
			<slot />
		</div>
	</div>
</div>
