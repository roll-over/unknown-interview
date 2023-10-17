import type { components } from '$lib/openapi';

export type StrictOmit<T, K extends keyof T> = Omit<T, K>;
export type StrictPick<T, K extends keyof T> = Pick<T, K>;
export type Cv = components['schemas']['CVResponseSchema'];
export type Vacancy = components['schemas']['VacancyResponseSchema'];
