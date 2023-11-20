<script lang="ts">
	import { createGetQuery } from '$lib/api';
	import { route } from '$lib/utils/route';
	import { getModalStore, popup, type PopupSettings } from '@skeletonlabs/skeleton';
	import { createQuery } from '@tanstack/svelte-query';
	import { showLogoutModal } from './LogoutModal.svelte';
	import LightSwitch from '../../utils/LightSwitch/LightSwitch.svelte';

	$: userInfoGet = createGetQuery('/api/v1/auth/user_info');
	$: userInfo = createQuery({
		queryKey: userInfoGet.key,
		queryFn: () => userInfoGet.runQuery()
	});

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
	const modalStore = getModalStore();
</script>

<header class="p-2">
	<nav class="flex items-center justify-between gap-3">
		<a href={route('/')}>
			<img
				src="/favicon.png"
				alt=""
				class="max-w-10 max-h-10"
			/>
		</a>
		<div class="flex items-center gap-3">
			<a href={route('/profile/chat')}>Chats</a>
			<button use:popup={navProfilePopup}>
				Match
				<div
					data-popup={navProfilePopup.target}
					class="bg-app-blue-50 px-4 py-2 text-black drop-shadow-md"
				>
					<div class="flex flex-col gap-2">
						<a href={route('/cv/match')}>CV</a>
						<hr />
						<a href={route('/vacancy/match')}>Vacancy</a>
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
						<a href={route('/cv/create')}>CV</a>
						<hr />
						<a href={route('/vacancy/create')}>Vacancy</a>
					</div>
					<div class="arrow bg-app-blue-50"></div>
				</div>
			</button>
			<a
				href={route('/integrations')}
				class="hidden sm:block">Api</a
			>
			<a
				href={route('/documents')}
				class="hidden sm:block">Documents</a
			>
			<a
				href={route('/about')}
				class="hidden sm:block">About</a
			>
			{#if $userInfo.isPending}
				<div>loading...</div>
			{:else if $userInfo.isError}
				<div>error</div>
			{:else if $userInfo.data.error}
				<LightSwitch rounded="rounded-full" />
				<a href={route('/auth/login')}>Log-in</a>
			{:else}
				{@const { email, picture } = $userInfo.data.data}
				<button
					on:click={() => showLogoutModal(modalStore, { email, image: picture })}
					aria-label="Logout"
				>
					<img
						src={picture}
						alt=""
						class="h-10 w-10 rounded-full"
					/>
				</button>
			{/if}
		</div>
	</nav>
</header>
