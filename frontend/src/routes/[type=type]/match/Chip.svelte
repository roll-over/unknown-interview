<script lang="ts">
	export let highlight = false;
</script>

<span
	class="rounded-lg bg-app-blue-100 px-4 py-1 outline-2 outline-app-blue-600 dark:bg-app-dark-light dark:outline-white"
	class:outline={highlight}
>
	<slot />
</span>
