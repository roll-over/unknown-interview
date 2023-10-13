import { describe, expect, test } from 'vitest';
import { isRangeOverlap, mapWithFilter } from '.';

test('Map with filter', () => {
	const array = Array.from({ length: 10 }, (_, i) => i);

	expect(
		mapWithFilter(
			array,
			(x) => x * 2,
			(x) => !!(x % 2)
		)
	).toEqual([]);

	expect(
		mapWithFilter(
			array,
			(x) => x * 3,
			(x) => !!(x % 2)
		)
	).toEqual([3, 9, 15, 21, 27]);

	expect(
		mapWithFilter(
			array,
			(x) => x,
			() => true
		)
	).toEqual(array);
});

describe('Range overlap works for', () => {
	test('partial overlap', () => {
		expect(isRangeOverlap(0, 10, 3, 15)).toEqual(true);
		expect(isRangeOverlap(27, 34, 12, 28)).toEqual(true);
	});
	test('full overlap', () => {
		expect(isRangeOverlap(0, 10, 2, 8)).toEqual(true);
		expect(isRangeOverlap(3, 50, 2, 80)).toEqual(true);
	});
	test('edge overlap', () => {
		expect(isRangeOverlap(0, 10, 10, 15)).toEqual(true);
		expect(isRangeOverlap(5, 10, 0, 5)).toEqual(true);
		expect(isRangeOverlap(0, 10, 5, 10)).toEqual(true);
		expect(isRangeOverlap(0, 10, 0, 15)).toEqual(true);
	});
	test('no overlap', () => {
		expect(isRangeOverlap(0, 10, 11, 15)).toEqual(false);
		expect(isRangeOverlap(20, 25, -11, 15)).toEqual(false);
	});
	test('invalid range', () => {
		expect(isRangeOverlap(20, 10, 3, 15)).toEqual(false);
		expect(isRangeOverlap(10, 20, 15, 3)).toEqual(false);
		expect(isRangeOverlap(20, 10, 15, 3)).toEqual(false);
	});
});
