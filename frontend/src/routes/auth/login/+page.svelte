<script lang="ts">
</script>

<div class="flex min-h-full items-center justify-center">
	<div class="flex flex-col gap-48 rounded-lg p-4">
		<div class="flex flex-col items-center gap-10">
			<h1 class="text-2xl">WELCOME!</h1>
			<p class="bg-clip-text text-slate-800 text-transparent">
				You need to be logged in to use the service
			</p>
		</div>
		<a
			class="flex w-full flex-row justify-between rounded-lg border-2 bg-cyan-200 p-2 text-lg text-slate-900 transition-[letter-spacing] current:tracking-widest"
			href="/api/v1/auth/login/google"
		>
			Continue with:
			<p class=" font-bold">
				<span class="text-blue-500">G</span><span class="text-red-500">o</span><span
					class="text-yellow-500">o</span
				><span class="text-blue-500">g</span><span class="text-green-600">l</span><span
					class="text-red-500">e</span
				>
			</p>
		</a>
	</div>
</div>
