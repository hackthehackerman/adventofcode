import { readFile, splitLines, count, editDistance } from "./utils";

const solvePart1 = (input: string): number => {
  const lines = splitLines(input).map((line) => line.split("").sort());
  var twos = 0;
  var threes = 0;

  for (const line of lines) {
    const counts = count(line);
    var two = false;
    var three = false;
    for (const [char, count] of counts) {
      if (count === 2) {
        two = true;
      }
      if (count === 3) {
        three = true;
      }
    }
    twos += two ? 1 : 0;
    threes += three ? 1 : 0;
  }
  return twos * threes;
};

const solvePart2 = (input: string): string => {
  const lines = splitLines(input);

  for (const line of lines) {
    for (const otherLine of lines) {
      if (editDistance(line, otherLine) === 1) {
        return line
          .split("")
          .filter((char, index) => char === otherLine[index])
          .join("");
      }
    }
  }
  return "";
};

// Read input and solve
const input = readFile("./input/day2.txt");
console.log("Part 1:", solvePart1(input));
console.log("Part 2:", solvePart2(input));
