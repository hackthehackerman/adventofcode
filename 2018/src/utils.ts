/**
 * Reads a file and returns its contents as a string
 */
export const readFile = (path: string): string => {
  return require("fs").readFileSync(path, "utf8");
};

/**
 * Splits a string into lines and returns an array of strings
 */
export const splitLines = (input: string): string[] => {
  return input.split("\n").filter((line) => line.length > 0);
};

/**
 * Converts a string array to a number array
 */
export const toNumbers = (input: string[]): number[] => {
  return input.map(Number);
};

/**
 * Creates a 2D array filled with a value
 */
export const create2DArray = <T>(
  width: number,
  height: number,
  fillValue: T
): T[][] => {
  return Array(height)
    .fill(null)
    .map(() => Array(width).fill(fillValue));
};

/**
 * Prints a 2D array in a readable format
 */
export const print2DArray = <T>(array: T[][]): void => {
  console.log(array.map((row) => row.join("")).join("\n"));
};

/**
 * Counts occurrences of each element in an array and returns a Map
 */
export const count = <T>(array: T[]): Map<T, number> => {
  return array.reduce((acc, item) => {
    acc.set(item, (acc.get(item) || 0) + 1);
    return acc;
  }, new Map<T, number>());
};

/**
 * Calculates the edit distance between two strings
 */
export const editDistance = (a: string, b: string): number => {
  return a.split("").filter((char, index) => char !== b[index]).length;
};
