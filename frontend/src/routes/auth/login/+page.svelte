<script lang="ts">
	import GoogleLogo from '~icons/logos/google-icon';
</script>

<div class="flex min-h-full items-center justify-center dark:text-white">
	<div class="flex flex-col gap-48 rounded-lg p-4">
		<div class="flex flex-col items-center gap-10">
			<h1 class="font-title text-5xl ">WELCOME!</h1>
			<p class="text-3xl ">You need to be logged in to use the service</p>
		</div>
		<a
			class="group dark:hover:bg-app-dark-light flex items-center justify-between rounded-2xl bg-app-blue-100 px-4 py-3 dark:bg-app-dark-gray transition-colors current:bg-app-blue-400"
			href="/api/v1/auth/login/google"
		>
			<GoogleLogo class="h-full w-16" />
			<span
				class="shrink-0 grow px-10 text-center text-4xl transition-colors group-current:text-white"
			>
				continue with google
			</span>
		</a>
	</div>
</div>
