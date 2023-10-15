/**
 * Apply map and filter in one go
 * @param array initial array
 * @param map transform function
 * @param filter filter function based on value returned from map
 * @returns filtered transformed array
 */
export function mapWithFilter<T, U>(
	array: T[],
	map: (value: T) => U,
	filter: (value: U) => boolean
) {
	return array.reduce<U[]>((agg, value) => {
		const x = map(value);
		if (filter(x)) agg.push(x);
		return agg;
	}, []);
}

/**
 * Checks if two ranges overlap
 * @param x1 start of first range
 * @param x2 end of first range
 * @param y1 start of second range
 * @param y2 end of second range
 */
export function isRangeOverlap(x1: number, x2: number, y1: number, y2: number) {
	return Math.max(x1, y1) <= Math.min(x2, y2);
}
