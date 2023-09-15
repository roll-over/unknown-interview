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
			class="bg-app-blue-100 cursor-pointer rounded-md px-2 {value === option
				? 'outline-app-blue-400 outline outline-1'
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
