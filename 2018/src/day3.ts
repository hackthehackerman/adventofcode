import { readFile, splitLines } from "./utils";

const CLAIM_REGEX = /(\d+) @ (\d+),(\d+): (\d+)x(\d+)/;

const solvePart1 = (input: string): number => {
  const lines = splitLines(input);

  var claimsCount = new Map<string, number>();
  for (const line of lines) {
    const match = CLAIM_REGEX.exec(line);
    const [, id, left, top, width, height] = match || [];

    for (let i = parseInt(left); i < parseInt(left) + parseInt(width); i++) {
      for (let j = parseInt(top); j < parseInt(top) + parseInt(height); j++) {
        const key = `${i},${j}`;
        claimsCount.set(key, (claimsCount.get(key) || 0) + 1);
      }
    }
  }
  var overlaps = 0;
  claimsCount.forEach((count) => {
    if (count > 1) overlaps++;
  });

  return overlaps;
};

const solvePart2 = (input: string): string => {
  const lines = splitLines(input);

  var fabric = new Map<string, Set<string>>();
  for (const line of lines) {
    const match = CLAIM_REGEX.exec(line);
    const [, id, left, top, width, height] = match || [];

    for (let i = parseInt(left); i < parseInt(left) + parseInt(width); i++) {
      for (let j = parseInt(top); j < parseInt(top) + parseInt(height); j++) {
        const key = `${i},${j}`;
        fabric.set(key, (fabric.get(key) || new Set()).add(id));
      }
    }
  }

  for (const line of lines) {
    const match = CLAIM_REGEX.exec(line);
    const [, id, left, top, width, height] = match || [];

    var overlaps = false;
    for (let i = parseInt(left); i < parseInt(left) + parseInt(width); i++) {
      for (let j = parseInt(top); j < parseInt(top) + parseInt(height); j++) {
        const key = `${i},${j}`;
        if ((fabric.get(key)?.size || 0) > 1) {
          overlaps = true;
          break;
        }
      }
    }
    if (!overlaps) {
      return id;
    }
  }
  return "";
};

// Read input and solve
const input = readFile("./input/day3.txt");
console.log("Part 1:", solvePart1(input));
console.log("Part 2:", solvePart2(input));
