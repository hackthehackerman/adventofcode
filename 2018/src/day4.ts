import { readFile, splitLines } from "./utils";

const CLAIM_REGEX = /\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (.*)/;

const solvePart1 = (input: string): number => {
  const lines = splitLines(input);

  const sortedLines: { date: string; line: string }[] = [];

  for (const line of lines) {
    const match = CLAIM_REGEX.exec(line);
    const [, year, month, day, hour, minute, action] = match || [];
    const key = `${year}-${month}-${day}-${hour}-${minute}`;
    sortedLines.push({ date: key, line: line });
  }
  sortedLines.sort((a, b) => a.date.localeCompare(b.date));

  var currentGuard = 0;
  var lastSleep = 0;
  var guardSleepRecord = new Map<string, Map<number, boolean>>();
  var guardSleepTime = new Map<string, number>();
  var dayGuard = new Map<string, number>();

  for (const line of sortedLines) {
    const [, year, month, day, hour, minute, action] =
      CLAIM_REGEX.exec(line.line) || [];

    if (action.startsWith("Guard")) {
      const guardId = action.split(" ")[1].slice(1);
      currentGuard = parseInt(guardId);
      if (hour === "00") {
        dayGuard.set(`${year}-${month}-${day}`, currentGuard);
      } else {
        const nextDayKey = `${year}-${month}-${parseInt(day) + 1}`;
        dayGuard.set(nextDayKey, currentGuard);
      }
    }
    if (action.startsWith("falls")) {
      lastSleep = parseInt(minute);
    }
    if (action.startsWith("wakes")) {
      const sleepTime = parseInt(minute) - lastSleep;
      guardSleepTime.set(`${year}-${month}-${day}`, sleepTime);

    }
  }
  

  return 0;
};

const solvePart2 = (input: string): string => {
  return "";
};

// Read input and solve
const input = readFile("./input/day4.txt");
console.log("Part 1:", solvePart1(input));
console.log("Part 2:", solvePart2(input));
