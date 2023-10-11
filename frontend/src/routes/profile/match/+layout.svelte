<!-- #region -->
<script
	context="module"
	lang="ts"
>
	import type { components } from '$lib/openapi';
	const randomCv: components['schemas']['CVResponseSchema'] = {
		profession: { name: 'C++ programmer' },
		title: 'manager',
		grade: 'principal',
		skillset: [{ name: 'CSS' }, { name: 'HTML5' }, { name: 'JS/TS' }],
		salary: { currency: 'USD', max_level: 3500, min_level: 3000 },
		extra_info: `Professional skills:
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

Additional information:The ability to work in multitasking mode and high analytical skills allow me to work effectively with large amounts of information, quickly find high-quality solutions to complex problems.`,
		owner_id: '',
		custom_id: ''
	};

	const randomVacancy: components['schemas']['VacancyResponseSchema'] = {
		profession: { name: 'С++ programmer' },
		title: 'lead',
		grade: 'junior',
		skillset: [{ name: 'C++' }, { name: 'SQL' }, { name: 'Rust' }],
		salary: { currency: 'EUR', min_level: 300, max_level: 700 },
		extra_info: `C++ programmers are required for the design and development of highly loaded information systems.
		
We are looking for C++ developers to join our team, both talented Juniors and experienced Middle and Senior.

Requirements:

- Strong knowledge of C++, including a deep understanding of the C++ Standard Template Library (STL), encompassing proficiency in basic algorithms and various containers such as vectors, lists, and maps.
- An understanding of simple data structures, combined with the ability to code in C at a fundamental level, enabling you to appreciate the core principles of programming.
- A strong curiosity and desire to delve into the inner workings of the technology you work with, allowing you to comprehend how software and hardware components interact and how systems are architected.
- Proficiency in working with memory, including memory management and allocation, an essential skill for optimizing resource utilization and preventing memory leaks in your code.
- Hands-on experience in software development under the Linux operating system, particularly in an environment following Object-Centric (OC) practices, which is crucial for developing robust and efficient software solutions on the Linux platform.
- A solid foundation in Structured Query Language (SQL), with the ability to design and interact with databases effectively. This skill is valuable for data-driven applications and database management, ensuring your software can store, retrieve, and manipulate data efficiently.
`,
		custom_id: '',
		owner_id: ''
	};
</script>

<!-- #endregion -->

<script lang="ts">
	import { page } from '$app/stores';
	import ThumbsUpIcon from '~icons/material-symbols/thumb-up-outline';
	import Chip from './Chip.svelte';

	$: matchData = $page.route.id?.includes('cv') ? randomVacancy : randomCv;
</script>

<div class="grid h-full grid-cols-2 p-5 text-2xl">
	<div>
		<slot />
	</div>
	<div class="flex min-h-0 flex-col">
		<div class="flex flex-col gap-y-5 overflow-y-auto rounded-lg bg-app-blue-50 p-4 pb-16">
			<h2 class="mx-auto w-fit font-title text-3xl font-medium capitalize">
				{matchData.grade}
				{matchData.profession.name}
			</h2>
			<p>
				Profession:
				<Chip>{matchData.profession.name}</Chip>
			</p>
			<p>
				Grade:
				<Chip>{matchData.grade}</Chip>
			</p>
			<p>
				Title:
				<Chip>{matchData.title}</Chip>
			</p>
			{#if matchData.skillset}
				<div>
					<div class="flex flex-wrap items-center gap-1">
						Skills:
						{#each matchData.skillset.map((x) => x.name) as skill}
							<Chip>{skill}</Chip>
						{/each}
					</div>
				</div>{/if}
			<p>
				Salary from
				<Chip>
					{matchData.salary?.min_level}{matchData.salary?.currency}
				</Chip>
				to
				<Chip>
					{matchData.salary?.max_level}{matchData.salary?.currency}
				</Chip>
			</p>
			<p class="whitespace-pre-wrap">{matchData.extra_info}</p>
		</div>
		<div class="flex h-16 justify-between text-white">
			<button
				type="button"
				class="h-32 w-32 -translate-y-1/2 rounded-full bg-app-blue-600 p-3 duration-500 current:bg-red-400 current:text-app-blue-50"
			>
				<ThumbsUpIcon class="h-full w-full -scale-x-100 -scale-y-100" />
			</button>
			<button
				type="button"
				class="h-32 w-32 -translate-y-1/2 rounded-full bg-app-blue-600 p-3 duration-500 current:bg-green-400 current:text-app-blue-50"
			>
				<ThumbsUpIcon class="h-full w-full" />
			</button>
		</div>
	</div>
</div>
