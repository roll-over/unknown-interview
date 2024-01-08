import type { components } from '$lib/openapi';

export type StrictOmit<T, K extends keyof T> = Omit<T, K>;
export type StrictPick<T, K extends keyof T> = Pick<T, K>;

export type CvRequest = components['schemas']['CVRequestSchema'];
export type VacancyRequest = components['schemas']['VacancyRequestSchema'];

export type CvResponse = components['schemas']['CVResponseSchema'];
export type VacancyResponse = components['schemas']['VacancyResponseSchema'];

export type MessageRequestSchema = components['schemas']['MessageRequestSchema'];
export type MessageResponseSchema = components['schemas']['MessageResponseSchema'];

export type ChatResponseSchema = components['schemas']['ChatResponseSchema'];
export type ChatsResponseSchema = components['schemas']['ChatsResponseSchema'];
