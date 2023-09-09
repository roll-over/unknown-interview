<script lang="ts">
	export let options: unknown[];
	export let value: unknown;
</script>

<div class="flex gap-2">
	{#each options as option (option)}
		<label
			class="bg-app-blue-300 rounded-md px-2 {value === option
				? 'outline-app-blue-500 outline outline-1'
				: ''}"
		>
			{option}
			<input
				type="radio"
				name="position"
				bind:group={value}
				value={option}
				class="absolute w-0 opacity-0"
			/>
		</label>
	{/each}
</div>
