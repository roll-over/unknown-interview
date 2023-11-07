import type { components } from '$lib/openapi';

export type StrictOmit<T, K extends keyof T> = Omit<T, K>;
export type StrictPick<T, K extends keyof T> = Pick<T, K>;

export type CvRequest = components['schemas']['CVRequestSchema'];
export type VacancyRequest = components['schemas']['VacancyRequestSchema'];

export type CvResponse = components['schemas']['CVResponseSchema'];
export type VacancyResponse = components['schemas']['VacancyResponseSchema'];
