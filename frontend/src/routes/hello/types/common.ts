const positions = [
	'member',
	'leader',
	'team',
	'leader',
	'manager',
	'director',
	'vp',
	'c-level'
] as const;

const grades = ['junior', 'middle', 'senior', 'presenter', 'director'] as const;

const professions = ['programmer', 'designer', 'Project manager'] as const;

const skills = {
	programmer: ['java', 'javascript', 'python', 'c#', 'c++', 'php', 'swift']
} as const;

const currencies = ['USD', 'EUR'] as const;

type NewJobState = {
	position?: (typeof positions)[number];
	grade?: (typeof grades)[number];
	salaryFork?: {
		min?: number;
		max?: number;
		currency: (typeof currencies)[number];
		applied: boolean;
	};
	profession?: (typeof professions)[number];
	skills?: string[];
};

type NewEmployeState = {
	position?: (typeof positions)[number];
	grade?: (typeof grades)[number];
	salaryFork?: {
		min?: number;
		max?: number;
		currency: (typeof currencies)[number];
		applied: boolean;
	};
	profession?: (typeof professions)[number];
	skills?: string[];
};

const defaultNewJobState: NewJobState = {
	position: undefined,
	grade: undefined,
	salaryFork: {
		min: undefined,
		max: undefined,
		currency: 'USD',
		applied: false
	},
	profession: undefined,
	skills: []
};

const defaultNewEmployeState: NewEmployeState = {
	position: undefined,
	grade: undefined,
	salaryFork: {
		min: undefined,
		max: undefined,
		currency: 'USD',
		applied: false
	},
	profession: undefined,
	skills: []
};

export {
	positions,
	grades,
	professions,
	skills,
	currencies,
	defaultNewJobState,
	defaultNewEmployeState,
	type NewJobState,
	type NewEmployeState
};
