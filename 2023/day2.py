from util import tolines
import re


def partone():
    lines = tolines("input/day2")
    total = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    ret = 0
    for idx, l in enumerate(lines):
        sets = l.split(":")[1].split(";")
        possible = True
        for set in sets:
            matches = re.findall("(\d+)\s+(blue|green|red)", set)
            for match in matches:
                if int(match[0]) > total[match[1]]:
                    possible = False

        if possible:
            ret += idx + 1

    return ret


def parttwo():
    lines = tolines("input/day2")

    ret = 0
    for idx, l in enumerate(lines):
        sets = l.split(":")[1].split(";")
        total = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for set in sets:
            matches = re.findall("(\d+)\s+(blue|green|red)", set)
            for match in matches:
                total[match[1]] = max(total[match[1]], int(match[0]))

        multiplier = 1
        for color in total:
            multiplier *= total[color]
        ret += multiplier

    return ret


print("part one:", partone())
print("part two:", parttwo())
