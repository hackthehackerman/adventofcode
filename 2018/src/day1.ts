import { readFile, splitLines, toNumbers } from "./utils";

const solvePart1 = (input: string): number => {
  const numbers = toNumbers(splitLines(input));
  return numbers.reduce((sum, num) => sum + num, 0);
};

const solvePart2 = (input: string): number => {
  const numbers = toNumbers(splitLines(input));
  var seen = new Set<number>();
  var current = 0;
  while (true) {
    for (const num of numbers) {
      current += num;
      if (seen.has(current)) {
        return current;
      }
      seen.add(current);
    }
  }
};

// Read input and solve
const input = readFile("./input/day1.txt");
console.log("Part 1:", solvePart1(input));
console.log("Part 2:", solvePart2(input));
