import type { Cv, Vacancy } from '$lib/utils/types';
import { faker } from '@faker-js/faker';
export const mockCvExtraInfo = `Carrying  out testing of customized / developed software, analysis of the results, formalization of comments and their discussion with the project team.
	
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
export const mockVacancyExtraInfo = `We are looking for C++ developers to join our team, both talented Juniors and experienced Middle and Senior`;

type Match = Cv | Vacancy;
const titles: Match['title'][] = ['director', 'lead', 'manager', 'member', 'teamlead'];
const grades: Match['grade'][] = ['junior', 'lead', 'middle', 'principal', 'senior'];
const skills = [
	'JavaScript',
	'Python',
	'Java',
	'C++',
	'Ruby',
	'Swift',
	'Go',
	'PHP',
	'C#',
	'Rust',
	'Kotlin',
	'TypeScript',
	'Dart',
	'Scala',
	'Haskell',
	'Perl',
	'Objective-C',
	'Lua',
	'Clojure',
	'Elixir',
	'Groovy',
	'F#',
	'R',
	'Assembly',
	'Swift',
	'Racket',
	'COBOL',
	'Lisp',
	'Ada',
	'Prolog',
	'SQL',
	'VHDL',
	'Verilog',
	'Fortran',
	'Pascal',
	'Rexx',
	'PL/I',
	'Smalltalk',
	'Erlang',
	'Ada',
	'ABAP',
	'Scheme',
	'Objective-C',
	'Tcl',
	'Julia'
];
export const getRandomCv = (): Cv => {
	const minSalary = faker.number.int({ min: 0, max: 50 });
	const maxSalary = faker.number.int({ min: 0, max: 50 });

	return {
		profession: { name: faker.person.jobTitle() },
		title: faker.helpers.arrayElement(titles),
		grade: faker.helpers.arrayElement(grades),
		skillset: faker.helpers
			.uniqueArray(skills, faker.number.int({ min: 0, max: 6 }))
			.map((name) => ({ name })),
		salary: {
			currency: faker.finance.currencyCode(),
			min_level: faker.helpers.maybe(() => minSalary * 10) ?? null,
			max_level: faker.helpers.maybe(() => maxSalary * 10) ?? null
		},
		extra_info: faker.lorem.paragraphs({ min: 1, max: 5 }),
		custom_id: '',
		owner_id: ''
	};
};
export const getRandomVacancy: () => Vacancy = getRandomCv;
