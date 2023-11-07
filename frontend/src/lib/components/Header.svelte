<script lang="ts">
	import { createGetQuery } from '$lib/api';
	import { route } from '$lib/utils/route';
	import { popup, type PopupSettings } from '@skeletonlabs/skeleton';
	import { createQuery } from '@tanstack/svelte-query';
	$: showModal = false;

	let dialog; // HTMLDialogElement

	$: if (dialog && showModal) dialog.showModal();
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

<header class="p-2">
	<nav class="flex items-center justify-between gap-3">
		<a href={route('/')}
			><img
				src="/favicon.png"
				alt="logo"
				class="max-w-10 max-h-10"
			/></a
		>
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
			{#if $userInfo.status === 'pending'}
				<div>loading...</div>
			{:else if $userInfo.status === 'error'}
				<div>error</div>
			{:else if data}
				<button on:click={() => (showModal = true)}>
					<img
						src={data.picture}
						alt="avatar"
						class="max-w-10 max-h-10 rounded-full"
					/>
				</button>
			{:else}
				<a href={route('/auth/login')}>Log-in</a>
			{/if}
		</div>
	</nav>

	<dialog
		bind:this={dialog}
		class="rounded-md bg-white p-10 shadow-md"
		on:close={() => (showModal = false)}
		on:click|self={() => dialog.close()}
	>
		<div class="flex flex-col items-start gap-4">
			<h1 class="text-xl">Are you sure you want to logout?</h1>
			{data?.email}
			<img
				src={data?.picture}
				alt="avatar"
				class="max-w-20 max-h-20 rounded-full"
			/>
			<div class="flex w-full flex-row justify-between">
				<a href="/api/v1/auth/logout">Logout</a>
				<button on:click={() => (showModal = false)}>Close</button>
			</div>
		</div>
	</dialog>
</header>
