from util import toLines
import re


def partone():
    lines = toLines("input/day15")
    discs = []

    for line in lines:
        matches = re.findall(
            r"has (\d+) positions; at time=\d+, it is at position (\d+)", line
        )
        pos_total, pos_now = matches[0]
        discs.append([int(pos_total), int(pos_now)])

    time = 0
    while True:
        positions = []
        for i in range(len(discs)):
            pos_total, pos_now = discs[i]
            positions.append((pos_now + time + 1 + i) % pos_total)
        if sum(positions) == 0:
            return time
        time += 1


def parttwo():
    lines = toLines("input/day15")
    discs = []

    for line in lines:
        matches = re.findall(
            r"has (\d+) positions; at time=\d+, it is at position (\d+)", line
        )
        pos_total, pos_now = matches[0]
        discs.append([int(pos_total), int(pos_now)])
    discs.append([11, 0])

    time = 0
    while True:
        positions = []
        for i in range(len(discs)):
            pos_total, pos_now = discs[i]
            positions.append((pos_now + time + 1 + i) % pos_total)
        if sum(positions) == 0:
            return time
        time += 1


print("partone", partone())
print("parttwo", parttwo())
