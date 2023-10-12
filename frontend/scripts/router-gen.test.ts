import { describe, expect, test } from 'vitest';
import {
	templateParam as Param,
	templateRest as Rest,
	parsePath,
	stringifyRoute
} from './router-gen';

function parseType(path: string[]) {
	return stringifyRoute(parsePath(path));
}

function constructUnion(types: string[]) {
	return types.map((type) => '`' + type + '`');
}

describe('Router codegen parses', () => {
	test('static paths', () => {
		expect(parseType(['x', 'y', 'z'])).toEqual(constructUnion(['/x/y/z']));
		expect(parseType([])).toEqual(constructUnion(['/']));
		expect(parseType(['a'])).toEqual(constructUnion(['/a']));
	});

	test('params', () => {
		expect(parseType(['x', '[y]', 'z'])).toEqual(constructUnion([`/x/${Param}/z`]));
		expect(parseType(['[x]'])).toEqual(constructUnion([`/${Param}`]));
		expect(parseType(['[x]', 'y'])).toEqual(constructUnion([`/${Param}/y`]));
		expect(parseType(['x', '[y]'])).toEqual(constructUnion([`/x/${Param}`]));
	});

	test('optional params', () => {
		expect(parseType(['x', '[[y]]', 'z'])).toEqual(constructUnion([`/x/${Param}/z`, `/x/z`]));
		expect(parseType(['[[x]]'])).toEqual(constructUnion([`/${Param}`, `/`]));
		expect(parseType(['[[x]]', 'y'])).toEqual(constructUnion([`/${Param}/y`, `/y`]));
		expect(parseType(['x', '[[y]]'])).toEqual(constructUnion([`/x/${Param}`, `/x`]));
	});

	test('rest params', () => {
		expect(parseType(['x', '[...y]', 'z'])).toEqual(constructUnion([`/x/${Rest}/z`, `/x/z`]));
		expect(parseType(['[...x]'])).toEqual(constructUnion([`/${Rest}`, `/`]));
		expect(parseType(['[...x]', 'y'])).toEqual(constructUnion([`/${Rest}/y`, `/y`]));
		expect(parseType(['x', '[...y]'])).toEqual(constructUnion([`/x/${Rest}`, `/x`]));
	});

	test('groups', () => {
		expect(parseType(['x', '(y)', 'z'])).toEqual(constructUnion([`/x/z`]));
		expect(parseType(['(x)'])).toEqual(constructUnion([`/`]));
		expect(parseType(['(x)', 'y'])).toEqual(constructUnion([`/y`]));
		expect(parseType(['x', '(y)'])).toEqual(constructUnion([`/x`]));
	});

	test('multiple params', () => {
		expect(parseType(['x', 'a-[x]-[[x]]-y', 'z'])).toEqual(
			constructUnion([`/x/a-${Param}-${Param}-y/z`, `/x/a-${Param}--y/z`])
		);
		expect(parseType(['[x]-[[x]]'])).toEqual(constructUnion([`/${Param}-${Param}`, `/${Param}-`]));
		expect(parseType(['[x]-[[x]]-y', 'y'])).toEqual(
			constructUnion([`/${Param}-${Param}-y/y`, `/${Param}--y/y`])
		);
		expect(parseType(['x', 'a-[x]-[[x]]'])).toEqual(
			constructUnion([`/x/a-${Param}-${Param}`, `/x/a-${Param}-`])
		);
	});

	test('some complicated route', () => {
		expect(parseType(['(x)', '[[x]]-a-[...x]', '[x]-y', '(x)', 'y', '[x]-[[x]]', 'x'])).toEqual(
			constructUnion([
				`/${Param}-a-${Rest}/${Param}-y/y/${Param}-${Param}/x`,
				`/-a-${Rest}/${Param}-y/y/${Param}-${Param}/x`,
				`/${Param}-a-/${Param}-y/y/${Param}-${Param}/x`,
				`/-a-/${Param}-y/y/${Param}-${Param}/x`,
				`/${Param}-a-${Rest}/${Param}-y/y/${Param}-/x`,
				`/-a-${Rest}/${Param}-y/y/${Param}-/x`,
				`/${Param}-a-/${Param}-y/y/${Param}-/x`,
				`/-a-/${Param}-y/y/${Param}-/x`
			])
		);
	});
});
