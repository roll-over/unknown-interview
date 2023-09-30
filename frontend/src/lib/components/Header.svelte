<script lang="ts">
	import api from '$lib/api';
	import { route } from '$lib/utils/route';
	import { popup, type PopupSettings } from '@skeletonlabs/skeleton';
	import { createQuery } from '@tanstack/svelte-query';

	$: userInfo = createQuery({
		queryKey: ['userInfo'],
		queryFn: () => api.GET('/api/v1/auth/user_info', {})
	});
	$: data = $userInfo.isSuccess && $userInfo.data.data ? $userInfo.data.data : null;

	const navPopup: PopupSettings = {
		event: 'click',
		target: 'nav-anchor-popup',
		placement: 'bottom'
	};
</script>

<header class="bg-app-blue-50 px-2">
	<nav class="flex gap-3">
		<a href={route('/')}>Home</a>
		<a href={route('/profile/matches')}>Matches</a>
		<a href={route('/user')}>User</a>
		<button use:popup={navPopup}>
			Create
			<div
				data-popup={navPopup.target}
				class="bg-app-blue-50 px-4 py-2 text-black drop-shadow-md"
			>
				<div class="flex flex-col gap-2">
					<a href={route('/create/cv')}>CV</a>
					<hr />
					<a href={route('/create/offer')}>Offer</a>
				</div>
				<div class="arrow bg-app-blue-50"></div>
			</div>
		</button>
		{#if $userInfo.status === 'pending'}
			<div>loading...</div>
		{:else if $userInfo.status === 'error'}
			<div>error</div>
		{:else if data}
			{data.email}
			<a href="/api/v1/auth/logout">Logout</a>
		{:else}
			<a href={route('/auth/login')}>Log-in</a>
		{/if}
		<a href={route('/integrations')}>Api</a>
	</nav>
</header>
