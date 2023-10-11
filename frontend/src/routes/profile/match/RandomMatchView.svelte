<!-- #region -->
<script
	context="module"
	land="ts"
>
	const cvContent = `Carrying  out testing of customized / developed software, analysis of the results, formalization of comments and their discussion with the project team.
	
	Requirements:
 -Strong knowledge of C++, STL libraries (basic algorithms and containers). 
 -Understanding of simple data structures, knowledge of object-oriented programming principles, and good problem-solving skills.
 - Familiarity with version control systems such as Git.
 - Experience with software development tools, including integrated development environments (IDEs), compilers, and debuggers.
 - A solid foundation in computer science concepts such as algorithms, data structures, and computer architecture.
 - Effective communication skills, both written and verbal, as you'll be collaborating with team members and possibly communicating with non-technical stakeholders.
 - The ability to work both independently and as part of a team, as software development often involves both individual tasks and collaborative efforts.
 - Attention to detail and a commitment to writing clean, maintainable, and well-documented code.
 - Knowledge of software development best practices, including unit testing, code reviews, and continuous integration.
 - Experience with software design patterns and the ability to apply them appropriately to solve complex problems.
 `;
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
	const vacancyContent = `We are looking for C++ developers to join our team, both talented Juniors and experienced Middle and Senior.`;
	const randomVacancy = {
		title: 'С++ programmer',
		description: `C++ programmers are required for the design and development of highly loaded information systems.
		
		We are looking for C++ developers to join our team, both talented Juniors and experienced Middle and Senior.

Requirements:

- Strong knowledge of C++, including a deep understanding of the C++ Standard Template Library (STL), encompassing proficiency in basic algorithms and various containers such as vectors, lists, and maps.
- An understanding of simple data structures, combined with the ability to code in C at a fundamental level, enabling you to appreciate the core principles of programming.
- A strong curiosity and desire to delve into the inner workings of the technology you work with, allowing you to comprehend how software and hardware components interact and how systems are architected.
- Proficiency in working with memory, including memory management and allocation, an essential skill for optimizing resource utilization and preventing memory leaks in your code.
- Hands-on experience in software development under the Linux operating system, particularly in an environment following Object-Centric (OC) practices, which is crucial for developing robust and efficient software solutions on the Linux platform.
- A solid foundation in Structured Query Language (SQL), with the ability to design and interact with databases effectively. This skill is valuable for data-driven applications and database management, ensuring your software can store, retrieve, and manipulate data efficiently.
`
	};
</script>

<!-- #endregion -->

<script lang="ts">
	import api from '$lib/api';
	import { route } from '$lib/utils/route';
	import { createQuery } from '@tanstack/svelte-query';
	import DeleteIcon from '~icons/material-symbols/delete-outline';
	import EditIcon from '~icons/material-symbols/edit-outline';
	import ThumbsUpIcon from '~icons/material-symbols/thumb-up-outline';
	import Chip from './Chip.svelte';

	export let profileMeta: { id: string; type: 'cv' | 'vacancy' };
	$: isVacancy = profileMeta.type === 'vacancy';
	$: profileContent = isVacancy ? vacancyContent : cvContent;
	$: matchData = isVacancy ? randomCv : randomVacancy;

	$: userFormQuery = createQuery({
		queryFn: () =>
			isVacancy
				? api.GET('/api/v1/vacancies/{vacancy_id}', {
						params: { path: { vacancy_id: profileMeta.id } }
				  })
				: api.GET('/api/v1/cvs/{cv_id}', { params: { path: { cv_id: profileMeta.id } } })
	});
	$: userFormData = $userFormQuery.data?.data;
</script>

<div class="grid h-full grid-cols-2 grid-rows-[minmax(0,1fr),4rem] gap-x-5 px-12 py-5 text-2xl">
	<div class="flex flex-col gap-3 overflow-y-auto rounded-lg bg-app-blue-50 p-4">
		<div class="flex gap-1">
			<h2 class="font-title text-3xl">{isVacancy ? 'Vacancy' : 'CV'}</h2>
			<a
				class="ml-auto"
				href={isVacancy ? route('/create/vacancy') : route('/create/cv')}
			>
				<EditIcon
					class="h-8 w-8 rounded-full bg-app-blue-600 p-1 text-white duration-500 hover:bg-white hover:text-app-blue-500"
				/>
			</a>
			<a href="placeholder">
				<DeleteIcon
					class="h-8 w-8 rounded-full bg-red-600 p-1 text-white duration-500 hover:bg-white hover:text-red-600"
				/>
			</a>
		</div>
		<p>
			Profession:
			<Chip>{userFormData?.profession.name}</Chip>
		</p>
		<p>
			Grade:
			<Chip>{userFormData?.grade}</Chip>
		</p>
		<p>
			Title:
			<Chip>{userFormData?.title}</Chip>
		</p>
		{#if userFormData?.skillset}
			<div>
				<div class="flex flex-wrap items-center gap-1">
					Skills:
					{#each userFormData?.skillset.map((x) => x.name) as skill}
						<Chip>{skill}</Chip>
					{/each}
				</div>
			</div>{/if}
		<p>
			Salary from
			<Chip>
				{userFormData?.salary?.min_level}{userFormData?.salary?.currency}
			</Chip>
			to
			<Chip>
				{userFormData?.salary?.max_level}{userFormData?.salary?.currency}
			</Chip>
		</p>
		<p class="whitespace-pre-wrap">{profileContent}</p>
	</div>
	<div class="h-full overflow-y-auto rounded-lg bg-app-blue-50 p-4 pb-16">
		<h2 class="mx-auto w-fit font-title text-3xl font-medium">
			{matchData.title}
		</h2>
		<p class="whitespace-pre-wrap text-center">{matchData.description}</p>
	</div>
	<div class="flex gap-12 pt-4 text-base">
		<span>Views: 16</span>
		<span>Match: 7</span>
	</div>
	<div class="flex justify-between text-white">
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
