<!-- #region -->
<script
	context="module"
	land="ts"
>
	const cvContent = `Carrying  out testing of customized / developed software, analysis of the results, formalization of comments and their discussion with the project team.
	
Requirements:
 -Strong knowledge of C++, STL libraries (basic algorithms and containers). 
 -Understanding of simple data structures, knowledge`;
	const randomCv = {
		title: 'С++ programmer',
		description: `Professional skills:
- Experience with HTML5, CSS3, JS;
- knowledge of JavaScript/JQuery;
- experience of adaptive layout;
- experience in creating HTML website pages based on design layouts;
- experience in website layout and templates for CMS;
- skills in linking scripts to the user interface that provide visualization and animation of site pages;
- skills to provide the required level of user interface (UI 
- User Interface) and interaction experience (UX 
- User Experience);
- knowledge of CSS frameworks;
- knowledge of cross
-browser layout;
- knowledge of Photoshop;
- knowledge of other programming languages.

Additional information:The ability to work in multitasking mode and high analytical skills allow me to work effectively with large amounts of information, quickly find high-quality solutions to complex problems.`
	};
	const offerContent = `We are looking for C++ developers to join our team, both talented Juniors and experienced Middle and Senior.`;
	const randomOffer = {
		title: 'С++ programmer',
		description: `C++ programmers are required for the design and development of highly loaded information systems.
		
		We are looking for C++ developers to join our team, both talented Juniors and experienced Middle and Senior.

Requirements:

-Strong knowledge of C++, STL libraries (basic algorithms and containers).
-Understanding of simple data structures, knowledge of C at a basic level.
-The desire to understand how the technology used is arranged inside.
-Ability to work with memory.
-Experience in software development under OC Linux.Knowledge of SQL.
-Understanding what XML and JSON are.
-High analytical skills, ability to work in a team, read and understand other people's code, initiative, communication skills and goodwill
-Knowledge of Oracle, Postgresql and English will be a plus.`
	};
</script>

<!-- #endregion -->

<script lang="ts">
	import api from '$lib/api';
	import { route } from '$lib/utils/route';
	import { createQuery } from '@tanstack/svelte-query';
	import { scale } from 'svelte/transition';
	import MaterialSymbolsArrowDropDown from '~icons/material-symbols/arrow-drop-down';
	import MaterialSymbolsEditOutline from '~icons/material-symbols/edit-outline';
	import MaterialSymbolsThumbDownOutline from '~icons/material-symbols/thumb-down-outline';
	import MaterialSymbolsThumbUpOutline from '~icons/material-symbols/thumb-up-outline';

	$: userQuery = createQuery({
		queryKey: ['userInfo'],
		queryFn: () => api.GET('/api/v1/auth/user_info', {})
	});

	export let profileMeta: { id: string; type: 'cv' | 'offer' };
	$: profileContent = profileMeta.type === 'cv' ? cvContent : offerContent;
	$: matchData = profileMeta.type === 'cv' ? randomOffer : randomCv;

	let isOpen = false;
</script>

<div class="flex gap-5 px-12 pt-5">
	<div class="flex shrink-0 basis-2/5 flex-col pt-7">
		<img
			alt="your profile avatar"
			src={$userQuery.data?.data?.picture}
			class="mb-14 h-52 w-52 self-center rounded-full bg-app-blue-50 ring-1 ring-app-blue-600"
			referrerpolicy="no-referrer"
		/>
		<div class="flex flex-col gap-7 rounded-lg bg-app-blue-50 px-11 py-10">
			<div class="flex justify-between">
				<h2 class="font-title text-3xl">Resume</h2>
				<a href={route('/create/cv')}>
					<MaterialSymbolsEditOutline
						class="h-8 w-8 rounded-full bg-app-blue-600 p-1 text-white duration-500 hover:bg-white hover:text-app-blue-500"
					/>
				</a>
			</div>
			<div
				class="grid justify-items-start transition-[grid-template-rows] {isOpen
					? 'grid-rows-[1fr]'
					: 'grid-rows-[0fr]'}"
			>
				<span class="min-h-[4.5rem] overflow-hidden whitespace-pre-wrap">
					{profileContent}
				</span>
				<!-- how do I hide you when text isn't overflowing? 😟 -->
				<button
					on:click={() => (isOpen = !isOpen)}
					class="btn p-0"
					transition:scale
				>
					{isOpen ? 'Collapse' : 'Expand'}
					<MaterialSymbolsArrowDropDown class="-rotate-90" />
				</button>
			</div>
		</div>
		<div class="flex gap-12 pt-3">
			<span>Views: 16</span>
			<span>Match: 7</span>
		</div>
	</div>
	<div class="relative h-fit grow font-medium text-white">
		<div class="rounded-lg bg-app-blue-600 py-10">
			<div class="flex flex-col items-center gap-5 px-11">
				<h2
					class="rounded-full border-2 border-app-blue-100 px-12 py-3 font-title text-3xl font-bold"
				>
					{matchData.title}
				</h2>
				<p class="whitespace-pre-wrap text-center text-2xl">{matchData.description}</p>
			</div>
		</div>
		<div class="flex w-full -translate-y-10 justify-between">
			<button
				type="button"
				class="h-32 w-32 rounded-full bg-app-blue-100 p-3 duration-500 current:bg-red-400 current:text-app-blue-50"
			>
				<MaterialSymbolsThumbDownOutline class="h-full w-full" />
			</button>
			<button
				type="button"
				class="h-32 w-32 rounded-full bg-app-blue-100 p-3 duration-500 current:bg-green-400 current:text-app-blue-50"
			>
				<MaterialSymbolsThumbUpOutline class="h-full w-full" />
			</button>
		</div>
	</div>
</div>
