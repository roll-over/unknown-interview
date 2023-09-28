<script lang="ts">
	import api from '$lib/api';
	import { createQuery } from '@tanstack/svelte-query';

	$: userInfo = createQuery({
		queryKey: ['userInfo'],
		queryFn: () => api.GET('/api/v1/auth/user_info', {})
	});
</script>

<header class="bg-slate-400">
	<nav class="flex gap-3">
		<a href="/">Home</a>

		<a href="/profile/matches">Matches</a>

		{#if $userInfo.status === 'pending'}
			<div>loading...</div>
		{:else if $userInfo.status === 'error'}
			<div>error</div>
		{:else if $userInfo.isSuccess && $userInfo.data?.data?.email}
			{$userInfo.data?.data?.email}
			<a href="/api/v1/auth/logout">Logout</a>
		{:else}
			<a href="/auth/login">Log-in</a>
		{/if}

		<a href="/api/service">Api</a>
	</nav>
</header>
