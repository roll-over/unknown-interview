export const positions = [
	'member',
	'leader',
	'team leader',
	'manager',
	'director',
	'vp',
	'c-level'
];

export const grades = ['junior', 'middle', 'senior', 'presenter', 'director'];

export const professions = ['programmer', 'designer', 'Project manager'];

export const skills = ['java', 'javascript', 'python', 'c#', 'c++', 'php', 'swift'];

export const currencies = ['USD', 'EUR'];

export type CVState = {
	position: (typeof positions)[number];
	grade: (typeof grades)[number];
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
