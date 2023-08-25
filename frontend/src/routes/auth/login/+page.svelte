<script lang="ts">
	import { browser } from '$app/environment';
	import Input from '$lib/components/Input.svelte';
</script>

<div class="flex min-h-screen items-center justify-center">
	<div class="flex flex-col gap-2 rounded-lg bg-slate-600 p-4">
		<p class="bg-gradient-to-r from-white to-slate-400 bg-clip-text font-bold text-transparent">
			Login with provider
		</p>
		<button
			class="current:tracking-widest w-full rounded-lg bg-white p-2 text-lg font-bold text-slate-900 transition-[letter-spacing]"
			on:click={() => {
				console.log('Google OAuth2');
			}}
		>
			<span class="text-blue-500">G</span><span class="text-red-500">o</span><span
				class="text-yellow-500">o</span
			><span class="text-blue-500">g</span><span class="text-green-600">l</span><span
				class="text-red-500">e</span
			>
		</button>
		<div
			class="h-1 w-[105%] self-center rounded-full bg-gradient-to-r from-slate-300 to-slate-500"
		/>
		<form
			class="flex flex-col gap-2"
			on:submit={(e) => {
				new FormData(e.currentTarget).forEach((value, key) => {
					console.log({ [key]: value });
				});
			}}
		>
			<p class="bg-gradient-to-r from-white to-slate-400 bg-clip-text font-bold text-transparent">
				Login with email
			</p>
			<Input
				attrs={{
					placeholder: 'Email',
					type: 'email',
					autocomplete: 'username',
					required: true,
					name: 'email'
				}}
				class="text-lg text-black"
			/>
			<button
				disabled={!browser}
				class="rounded-lg bg-slate-500 p-2 shadow-sm transition-shadow hover:shadow-lg disabled:bg-slate-300"
			>
				Log-in
			</button>
		</form>
	</div>
</div>
