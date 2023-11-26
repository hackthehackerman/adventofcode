from util import toLines
from collections import Counter


def one(filename: str):
    lines = toLines(filename)
    counters = [Counter() for _ in range(len(lines[0]))]

    for line in lines:
        for i, c in enumerate(line):
            counters[i][c] += 1
    return "".join([c.most_common(1)[0][0] for c in counters])


def two(filename: str):
    lines = toLines(filename)
    counters = [Counter() for _ in range(len(lines[0]))]

    for line in lines:
        for i, c in enumerate(line):
            counters[i][c] += 1
    return "".join([c.most_common()[-1][0] for c in counters])


print("part one:", one("input/day6"))
print("part two:", two("input/day6"))
