<script lang="ts">
	import api from '$lib/api';
	import { createQuery } from '@tanstack/svelte-query';
	import MaterialSymbolsEditOutline from '~icons/material-symbols/edit-outline';
	import MaterialSymbolsThumbDownOutline from '~icons/material-symbols/thumb-down-outline';
	import MaterialSymbolsThumbUpOutline from '~icons/material-symbols/thumb-up-outline';

	$: userQuery = createQuery({
		queryKey: ['userInfo'],
		queryFn: () => api.GET('/api/v1/auth/user_info', {})
	});
</script>

<div class="flex gap-5 px-12 pt-5">
	<div class="flex shrink-0 basis-2/5 flex-col pt-7">
		<img
			alt="your profile avatar"
			src={$userQuery.data?.data?.picture}
			class="bg-app-blue-50 ring-app-blue-600 mb-14 h-52 w-52 self-center rounded-full ring-1"
			referrerpolicy="no-referrer"
		/>
		<div class="bg-app-blue-50 flex flex-col gap-7 rounded-lg px-11 py-10">
			<div class="flex justify-between">
				<h2 class="font-title text-3xl">Resume</h2>
				<a href="/create/cv">
					<MaterialSymbolsEditOutline
						class="bg-app-blue-600  hover:text-app-blue-500 h-8 w-8 rounded-full p-1 text-white duration-500 hover:bg-white"
					/>
				</a>
			</div>
			<p>Fill out a resume</p>
		</div>
		<div class="flex gap-12 pt-3">
			<span>Views: 16</span>
			<span>Match: 7</span>
		</div>
	</div>

	<div class="bg-app-blue-600 h-fit grow rounded-lg pt-10 text-white">
		<div class="flex flex-col items-center gap-5 px-11">
			<h2 class="font-title border-app-blue-100 rounded-full border-2 px-12 py-3 text-3xl">
				С++ programmer
			</h2>
			<p>
				Professional skills: - Experience with HTML5, CSS3, JS;- knowledge of JavaScript/JQuery;-
				experience of adaptive layout;- experience in creating HTML website pages based on design
				layouts;- experience in website layout and templates for CMS;- skills in linking scripts to
				the user interface that provide visualization and animation of site pages;- skills to
				provide the required level of user interface (UI - User Interface) and interaction
				experience (UX - User Experience);- knowledge of CSS frameworks;- knowledge of cross-browser
				layout;- knowledge of Photoshop;- knowledge of other programming languages. Additional
				information:The ability to work in multitasking mode and high analytical skills allow me to
				work effectively with large amounts of information, quickly find high-quality solutions to
				complex problems.
			</p>
		</div>
		<div class="flex justify-between">
			<button
				type="button"
				class="current:text-app-blue-50 bg-app-blue-100 current:bg-red-400 h-32 w-32 translate-y-2/3 rounded-full p-3 duration-500"
			>
				<MaterialSymbolsThumbDownOutline class="h-full w-full" />
			</button>
			<button
				type="button"
				class="current:text-app-blue-50 bg-app-blue-100 current:bg-green-400 h-32 w-32 translate-y-2/3 rounded-full p-3 duration-500"
			>
				<MaterialSymbolsThumbUpOutline class="h-full w-full" />
			</button>
		</div>
	</div>
</div>
