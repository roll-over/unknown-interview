<script lang="ts">
	import { createGetQuery } from '$lib/api';
	import { route } from '$lib/utils/route';
	import { popup, type PopupSettings } from '@skeletonlabs/skeleton';
	import { createQuery } from '@tanstack/svelte-query';

	$: userInfoGet = createGetQuery('/api/v1/auth/user_info');
	$: userInfo = createQuery({
		queryKey: userInfoGet.key,
		queryFn: () => userInfoGet.runQuery()
	});
	$: data = $userInfo.isSuccess && $userInfo.data.data ? $userInfo.data.data : null;

	const navCreatePopup: PopupSettings = {
		event: 'click',
		target: 'nav-create-popup',
		placement: 'bottom'
	};
	const navProfilePopup: PopupSettings = {
		event: 'click',
		target: 'nav-profile-popup',
		placement: 'bottom'
	};
</script>

<header class="bg-app-blue-50 px-2">
	<nav class="flex gap-3">
		<a href={route('/')}>Home</a>
		<a href={route('/profile/chat')}>Chats</a>
		<button use:popup={navProfilePopup}>
			Match
			<div
				data-popup={navProfilePopup.target}
				class="bg-app-blue-50 px-4 py-2 text-black drop-shadow-md"
			>
				<div class="flex flex-col gap-2">
					<a href={route('/profile/match/cv')}>CV</a>
					<hr />
					<a href={route('/profile/match/vacancy')}>Vacancy</a>
				</div>
				<div class="arrow bg-app-blue-50"></div>
			</div>
		</button>
		<button use:popup={navCreatePopup}>
			Create
			<div
				data-popup={navCreatePopup.target}
				class="bg-app-blue-50 px-4 py-2 text-black drop-shadow-md"
			>
				<div class="flex flex-col gap-2">
					<a href={route('/create/cv')}>CV</a>
					<hr />
					<a href={route('/create/vacancy')}>Vacancy</a>
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
		<a href={route('/documents')}>Documents</a>
		<a href={route('/about')}>About</a>
	</nav>
</header>
