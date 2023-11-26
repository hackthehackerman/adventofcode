from util import toLines


def one(filename: str):
    pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    start = [1, 1]
    ret = ""

    content = toLines(filename)
    for l in content:
        l = l.strip()
        for c in l:
            if c == "U":
                start[1] = max(0, start[1] - 1)
            elif c == "D":
                start[1] = min(2, start[1] + 1)
            elif c == "L":
                start[0] = max(0, start[0] - 1)
            elif c == "R":
                start[0] = min(2, start[0] + 1)
        ret += str(pad[start[1]][start[0]])
    return ret


def two(filename: str):
    pad = [
        [None, None, "1", None, None],
        [None, "2", "3", "4", None],
        ["5", "6", "7", "8", "9"],
        [None, "A", "B", "C", None],
        [None, None, "D", None, None],
    ]

    start = [2, 0]
    ret = ""

    content = toLines(filename)
    for l in content:
        l = l.strip()

        for c in l:
            next = start.copy()
            if c == "U":
                next[0] = max(next[0] - 1, 0)
            elif c == "D":
                next[0] = min(next[0] + 1, 4)
            elif c == "L":
                next[1] = max(0, start[1] - 1)
            elif c == "R":
                next[1] = min(4, start[1] + 1)

            if pad[next[0]][next[1]] is not None:
                start = next.copy()
        ret += pad[start[0]][start[1]]
    return ret


print("part one:", one("input/day2"))
print("part two:", two("input/day2"))
