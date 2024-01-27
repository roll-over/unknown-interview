<script
	lang="ts"
	generics="V"
>
	export let options: V[];
	export let value: V;
	export let name: string;
</script>

<div class="flex flex-wrap gap-2">
	{#each options as option (option)}
		<label
			class="cursor-pointer rounded-md bg-app-blue-100 px-4 py-0.5 transition-colors hover:bg-app-blue-50 dark:bg-app-dark-light dark:hover:bg-app-dark-gray {value ===
			option
				? 'outline outline-2 outline-app-blue-400 dark:outline-white'
				: ''}"
		>
			{option}
			<input
				type="radio"
				{name}
				bind:group={value}
				value={option}
				class="absolute w-0 opacity-0"
			/>
		</label>
	{/each}
</div>
