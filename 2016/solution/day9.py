from util import toString


def expand(str: str, index: int):
    if index >= len(str):
        return ""
    if str[index] == "(":
        end = str.find(")", index)
        marker = str[index + 1 : end]
        x, y = map(int, marker.split("x"))
        return str[end + 1 : end + 1 + x] * y + expand(str, end + 1 + x)
    else:
        return str[index] + expand(str, index + 1)


def expand2(str: str, index: int):
    if index >= len(str):
        return ""
    if str[index] == "(":
        end = str.find(")", index)
        marker = str[index + 1 : end]
        x, y = map(int, marker.split("x"))
        return expand2(str[end + 1 : end + 1 + x], 0) * y + expand2(str, end + 1 + x)

        # return str[end + 1 : end + 1 + x] * y + expand(str, end + 1 + x)
    else:
        return str[index] + expand2(str, index + 1)


def one(filename: str):
    str = toString(filename)
    str = expand(str, 0)
    return len(str)


def two(filename: str):
    str = toString(filename)
    str = expand2(str, 0)
    return len(str)


print("part one:", one("input/day9"))
print("part two:", two("input/day9"))
