from util import toLines


def one(filename: str):
    lines = toLines(filename)

    ret = 0
    for line in lines:
        lengths = line.split()
        lengths = [int(length) for length in lengths]
        lengths = sorted(lengths)
        if lengths[0] + lengths[1] > lengths[2]:
            ret += 1
    return ret


def two(filename: str):
    lines = toLines(filename)
    lines = [line.split() for line in lines]
    ret = 0
    for i in range(0, len(lines), 3):
        for j in range(3):
            lengths = sorted([int(lines[i + k][j]) for k in range(3)])
            if lengths[0] + lengths[1] > lengths[2]:
                ret += 1
    return ret


print("part one:", one("input/day3"))
print("part two:", two("input/day3"))
