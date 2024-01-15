<script lang="ts">
	import { createGetQuery } from '$lib/api';
	import { route } from '$lib/utils/route';
	import { getModalStore, popup, type PopupSettings } from '@skeletonlabs/skeleton';
	import { createQuery } from '@tanstack/svelte-query';
	import { showLogoutModal } from './LogoutModal.svelte';
	import LightSwitch from '../../utils/LightSwitch/LightSwitch.svelte';
	// import { page } from '$app/stores';

	$: userInfoGet = createGetQuery('/api/v1/auth/user_info');
	$: userInfo = createQuery({
		queryKey: userInfoGet.key,
		queryFn: () => userInfoGet.runQuery()
	});

	$: userRecordsGet = createGetQuery('/api/v1/users/records');
	$: userRecordsQuery = createQuery({
		queryKey: userRecordsGet.key,
		queryFn() {
			return userRecordsGet.runQuery();
		},
		select(res) {
			return res.data || null;
		}
	});

	const navCreatePopup: PopupSettings = {
		event: 'click',
		target: 'nav-create-popup',
		placement: 'bottom'
	};

	const modalStore = getModalStore();

	// $: recordId = $page.params.id || '';
	// $: isCV = ($userRecordsQuery.data?.cv_ids || []).includes(recordId) || false;
	$: chatPickerPopup = {
		event: 'click',
		target: 'chat-picker-popup',
		placement: 'bottom'
	};

	$: matchPickerPopup = {
		event: 'click',
		target: 'match-picker-popup',
		placement: 'bottom'
	};
</script>

<header class="p-2 text-black dark:text-white">
	<nav class="flex items-center justify-between gap-3">
		<a href={route('/')}>
			<img
				src="/favicon.png"
				alt=""
				class="max-w-10 max-h-10"
			/>
		</a>
		<div class="flex items-center gap-3">
			{#if $userRecordsQuery.data?.cv_ids || $userRecordsQuery.data?.vacancy_ids}
				<button use:popup={matchPickerPopup}> Match </button>
				<div
					data-popup={matchPickerPopup.target}
					class="drop-shado w-md bg-app-blue-50 px-4 py-2 text-black dark:bg-app-dark-gray dark:text-white"
				>
					<div class="arrow bg-app-blue-50 dark:bg-app-dark-gray"></div>
					{#if $userRecordsQuery.data?.cv_ids}
						<h3>CV:</h3>
						<ul class="list pl-2">
							{#each $userRecordsQuery.data.cv_ids as id}
								<li>
									<a href={route('/cv/match/' + id)}> {id} </a>
								</li>
							{/each}
						</ul>
					{/if}
					{#if $userRecordsQuery.data?.vacancy_ids}
						<h3>Vacancy:</h3>
						<ul class="list pl-2">
							{#each $userRecordsQuery.data.vacancy_ids as id}
								<li>
									<a href={route('/vacancy/match/' + id)}> {id} </a>
								</li>
							{/each}
						</ul>
					{/if}
				</div>
			{/if}

			{#if $userRecordsQuery.data?.cv_ids || $userRecordsQuery.data?.vacancy_ids}
				<button use:popup={chatPickerPopup}> Chats </button>
				<div
					data-popup={chatPickerPopup.target}
					class="bg-app-blue-50 px-4 py-2 text-black drop-shadow-md dark:bg-app-dark-gray dark:text-white"
				>
					<div class="arrow bg-app-blue-50 dark:bg-app-dark-gray"></div>
					{#if $userRecordsQuery.data?.cv_ids}
						<h3>CV:</h3>
						<ul class="list pl-2">
							{#each $userRecordsQuery.data.cv_ids as id}
								<li>
									<a href={route('/profile/chat/' + id)}> {id} </a>
								</li>
							{/each}
						</ul>
					{/if}
					{#if $userRecordsQuery.data?.vacancy_ids}
						<h3>Vacancy:</h3>
						<ul class="list pl-2">
							{#each $userRecordsQuery.data.vacancy_ids as id}
								<li>
									<a href={route('/profile/chat/' + id)}> {id} </a>
								</li>
							{/each}
						</ul>
					{/if}
				</div>
			{/if}

			<button use:popup={navCreatePopup}> Create </button>
			<div
				data-popup={navCreatePopup.target}
				class="bg-app-blue-50 px-4 py-2 text-black drop-shadow-md dark:bg-app-dark-gray dark:text-white"
			>
				<div class="flex flex-col gap-2">
					<a href={route('/cv/create')}>CV</a>
					<hr />
					<a href={route('/vacancy/create')}>Vacancy</a>
				</div>
				<div class="arrow bg-app-blue-50 dark:bg-app-dark-gray"></div>
			</div>
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
			<LightSwitch rounded="rounded-full" />
			{#if $userInfo.isPending}
				<div>loading...</div>
			{:else if $userInfo.isError}
				<div>error</div>
			{:else if $userInfo.data.error}
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
