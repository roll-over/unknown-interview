export type StrictOmit<T, K extends keyof T> = Pick<T, Exclude<keyof T, K>>;

/** Just a placeholder function to check that alias imports work with tests */
export function divide(x: number, y: number) {
	if (!(x || y)) throw Error("Can't divide 0 by 0");
	return x / y;
}
