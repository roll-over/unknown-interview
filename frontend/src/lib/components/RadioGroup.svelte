<script
	lang="ts"
	context="module"
>
	type V = unknown;
</script>

<script
	lang="ts"
	generics="V"
>
	export let options: V[];
	export let value: V;
	export let name: string;
</script>

<div class="flex gap-2">
	{#each options as option (option)}
		<label
			class="cursor-pointer rounded-md bg-app-blue-100 px-2 hover:bg-app-blue-50 transition-colors {value === option
				? 'outline outline-2 outline-app-blue-400'
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
