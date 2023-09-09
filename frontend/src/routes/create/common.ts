import type { components } from '../../openapi';

export const positions: components['schemas']['CVRequestSchema']['title'][] = [
	'member',
	'lead',
	'teamlead',
	'manager',
	'director'
];
export const grades: components['schemas']['CVRequestSchema']['grade'][] = [
	'junior',
	'middle',
	'senior',
	'lead',
	'principal'
];

export const professions = [
	'programmer',
	'designer',
	'project manager',
	'engineer',
	'devops',
	'full-stack',
	'frontend',
	'backend'
];
export const skills = ['java', 'javascript', 'python', 'c#', 'c++', 'php', 'swift'];
export const currencies = ['USD', 'EUR'];

export type CVState = {
	position: (typeof positions)[number] | '';
	grade: (typeof grades)[number] | '';
	salaryFork: {
		min: number;
		max: number;
		currency: (typeof currencies)[number];
	};
	profession: (typeof professions)[number];
	skills: string[];
};

export const defaultCVState: CVState = {
	position: '',
	grade: '',
	salaryFork: {
		min: 0,
		max: 0,
		currency: 'USD'
	},
	profession: '',
	skills: []
};

export type JobOfferState = CVState;
export const defaultJobOfferState: JobOfferState = defaultCVState;
