<script lang="ts">
	import api from '$lib/api';
	import { route } from '$lib/utils/route';
	import { createQuery } from '@tanstack/svelte-query';
	import MaterialSymbolsEditOutline from '~icons/material-symbols/edit-outline';
	import MaterialSymbolsThumbDownOutline from '~icons/material-symbols/thumb-down-outline';
	import MaterialSymbolsThumbUpOutline from '~icons/material-symbols/thumb-up-outline';
	import MaterialSymbolsArrowDropDown from '~icons/material-symbols/arrow-drop-down';

	$: userQuery = createQuery({
		queryKey: ['userInfo'],
		queryFn: () => api.GET('/api/v1/auth/user_info', {})
	});

	const textContent = `Carrying  out testing of customized / developed software, analysis of the results, formalization of comments and their discussion with the project team Requirements: -Strong knowledge of C++, STL libraries (basic algorithms and containers). -Understanding of simple data structures, knowledge`;

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
				<a href={route("/create/cv")}>
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
				<span class="min-h-[4.5rem] overflow-hidden">{textContent}</span>
				<button
					on:click={() => (isOpen = !isOpen)}
					class="btn p-0"
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

	<div class="h-fit grow rounded-lg bg-app-blue-600 pt-10 font-medium text-white">
		<div class="flex flex-col items-center gap-5 px-11">
			<h2 class="rounded-full border-2 border-app-blue-100 px-12 py-3 font-title text-3xl">
				С++ programmer
			</h2>
			<h3 class="px-12 text-2xl">Professional skills:</h3>
			<ul class="flex list-disc flex-col items-center">
				<li>experience with HTML5, CSS3, JS;</li>
				<li>knowledge of JavaScript/JQuery;</li>
				<li>experience of adaptive layout</li>
				<li>experience in creating HTML website pages based on design layouts</li>
				<li>experience in website layout and templates for CMS</li>
				<li>
					skills in linking scripts to the user interface that provide visualization and animation
					of site pages
				</li>
				<li>
					skills to provide the required level of user interface (UI - User Interface) and
					interaction experience (UX - User Experience)
				</li>
				<li>knowledge of CSS frameworks</li>
				<li>knowledge of cross-browser layout</li>
				<li>knowledge of Photoshop</li>
				<li>knowledge of other programming languages</li>
			</ul>
			<h3 class="px-12 text-2xl">Additional information:</h3>
			<p class="text-center">
				The ability to work in multitasking mode and high analytical skills allow me to work
				effectively with large amounts of information, quickly find high-quality solutions to
				complex problems.
			</p>
		</div>
		<div class="flex justify-between">
			<button
				type="button"
				class="h-32 w-32 translate-y-2/3 rounded-full bg-app-blue-100 p-3 duration-500 current:bg-red-400 current:text-app-blue-50"
			>
				<MaterialSymbolsThumbDownOutline class="h-full w-full" />
			</button>
			<button
				type="button"
				class="h-32 w-32 translate-y-2/3 rounded-full bg-app-blue-100 p-3 duration-500 current:bg-green-400 current:text-app-blue-50"
			>
				<MaterialSymbolsThumbUpOutline class="h-full w-full" />
			</button>
		</div>
	</div>
</div>
