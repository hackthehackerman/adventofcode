from util import tolines
import re


def partone():
    lines = tolines("input/day3")
    matches = []
    for line in lines:
        numbers = re.finditer(r"\d+", line)
        symbols = re.finditer(r"[^\d.]", line)
        matches.append((list(numbers), list(symbols)))

    part_numbers = []
    for i in range(len(matches)):
        numbers = matches[i][0]

        for number in numbers:
            adjacent = False

            for j in [i - 1, i, i + 1]:
                if j < 0 or j >= len(matches):
                    continue
                symbols = matches[j][1]

                for symbol in symbols:
                    if number.start() - 1 <= symbol.start() <= number.end():
                        adjacent = True
                        break

            if adjacent:
                part_numbers.append(int(number.group()))

    return sum(part_numbers)


def parttwo():
    lines = tolines("input/day3")
    matches = []
    for line in lines:
        numbers = re.finditer(r"\d+", line)
        symbols = re.finditer(r"[^\d.]", line)
        matches.append((list(numbers), list(symbols)))

    gear_ratio = []
    for i in range(len(matches)):
        symbols = matches[i][1]

        for symbol in symbols:
            adjacent = []

            for j in [i - 1, i, i + 1]:
                if j < 0 or j >= len(matches):
                    continue
                numbers = matches[j][0]

                for number in numbers:
                    if number.start() - 1 <= symbol.start() <= number.end():
                        adjacent.append(int(number.group()))

            if len(adjacent) == 2:
                gear_ratio.append(adjacent[0] * adjacent[1])

    return sum(gear_ratio)


print("part one:", partone())
print("part two:", parttwo())
