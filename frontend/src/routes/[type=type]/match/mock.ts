import type { CvResponse, VacancyResponse } from '$lib/utils/types';
import { faker } from '@faker-js/faker';
type Match = CvResponse | VacancyResponse;
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
export const getRandomCv = (): CvResponse => {
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
export const getRandomVacancy: () => VacancyResponse = getRandomCv;
