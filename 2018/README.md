# Advent of Code 2018 - TypeScript Solutions

This project contains my solutions for Advent of Code 2018, written in TypeScript.

## Project Structure

```
2018/
├── src/
│   ├── day1.ts
│   ├── day2.ts
│   └── utils.ts
├── input/
│   ├── day1.txt
│   └── day2.txt
├── package.json
└── tsconfig.json
```

## Setup

1. Install dependencies:

```bash
npm install
```

2. Create your input files in the `input` directory (e.g., `input/day1.txt`)

3. Run a solution:

```bash
npx ts-node src/day1.ts
```

## Development

- Each day's solution is in its own file (e.g., `day1.ts`)
- Common utilities are in `utils.ts`
- Input files should be placed in the `input` directory
- Use `npm run build` to compile TypeScript to JavaScript
