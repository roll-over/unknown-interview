import type { StrictOmit } from '$lib/utils/types';
import type { components } from '$lib/openapi';

export type CVState = StrictOmit<components['schemas']['CVRequestSchema'], 'skillset'> & {
	skillset: string[];
};

export const titles: CVState['title'][] = ['member', 'lead', 'teamlead', 'manager', 'director'];
export const grades: CVState['grade'][] = ['junior', 'middle', 'senior', 'lead', 'principal'];

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

export const defaultCVState = {
	title: 'member',
	grade: 'junior',
	salary: {
		min_level: 0,
		max_level: 0,
		currency: 'USD'
	},
	profession: { name: '' },
	skillset: [] as string[],
	extra_info: null
} satisfies CVState;

export type JobOfferState = CVState;
export const defaultJobOfferState = defaultCVState satisfies JobOfferState;
