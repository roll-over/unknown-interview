import { expect, test } from 'vitest';
import { divide } from '$lib/utils/types';

test('basic for divide function test', () => {
	expect(divide(3, 5)).toEqual(3 / 5);
	expect(divide(3, 0)).toEqual(Infinity);

	expect(() => divide(0, 0)).toThrow('divide');
});
