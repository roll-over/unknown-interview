import { describe, expect, test } from 'vitest';
import {
	templateParam as Param,
	parsePath,
	stringifyRoute,
	templateRest as Rest
} from './router-gen';

function parseType(path: string[]) {
	return stringifyRoute(parsePath(path)).join(' | ');
}

function construcUnion(types: string[]) {
	return types.map((type) => '`' + type + '`').join(' | ');
}

describe('Test that router codegen parses', () => {
	test('static paths', () => {
		expect(parseType(['x', 'y', 'z'])).toEqual(construcUnion(['/x/y/z']));
		expect(parseType([])).toEqual(construcUnion(['/']));
		expect(parseType(['a'])).toEqual(construcUnion(['/a']));
	});

	test('params', () => {
		expect(parseType(['x', '[y]', 'z'])).toEqual(construcUnion([`/x/${Param}/z`]));
		expect(parseType(['[x]'])).toEqual(construcUnion([`/${Param}`]));
		expect(parseType(['[x]', 'y'])).toEqual(construcUnion([`/${Param}/y`]));
		expect(parseType(['x', '[y]'])).toEqual(construcUnion([`/x/${Param}`]));
	});

	test('optional params', () => {
		expect(parseType(['x', '[[y]]', 'z'])).toEqual(construcUnion([`/x/${Param}/z`, `/x/z`]));
		expect(parseType(['[[x]]'])).toEqual(construcUnion([`/${Param}`, `/`]));
		expect(parseType(['[[x]]', 'y'])).toEqual(construcUnion([`/${Param}/y`, `/y`]));
		expect(parseType(['x', '[[y]]'])).toEqual(construcUnion([`/x/${Param}`, `/x`]));
	});

	test('rest params', () => {
		expect(parseType(['x', '[...y]', 'z'])).toEqual(construcUnion([`/x/${Rest}/z`, `/x/z`]));
		expect(parseType(['[...x]'])).toEqual(construcUnion([`/${Rest}`, `/`]));
		expect(parseType(['[...x]', 'y'])).toEqual(construcUnion([`/${Rest}/y`, `/y`]));
		expect(parseType(['x', '[...y]'])).toEqual(construcUnion([`/x/${Rest}`, `/x`]));
	});

	test('groups', () => {
		expect(parseType(['x', '(y)', 'z'])).toEqual(construcUnion([`/x/z`]));
		expect(parseType(['(x)'])).toEqual(construcUnion([`/`]));
		expect(parseType(['(x)', 'y'])).toEqual(construcUnion([`/y`]));
		expect(parseType(['x', '(y)'])).toEqual(construcUnion([`/x`]));
	});
});
