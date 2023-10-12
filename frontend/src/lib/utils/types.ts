import type { components } from '$lib/openapi';

export type StrictOmit<T, K extends keyof T> = Pick<T, Exclude<keyof T, K>>;
export type Cv = components['schemas']['CVResponseSchema'];
export type Vacancy = components['schemas']['VacancyResponseSchema'];
