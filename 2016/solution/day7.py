from util import toLines
import re, itertools


def abba(s):
    for i in range(len(s) - 3):
        if s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1]:
            return True
    return False


def aba(s) -> list:
    ret = []
    for i in range(len(s) - 2):
        if s[i] == s[i + 2] and s[i] != s[i + 1]:
            ret.append(s[i : i + 3])
    return ret


def one(filename: str):
    lines = toLines(filename)
    ret = 0
    for line in lines:
        inside_brackets = re.findall(r"\[([^\]]+)\]", line)
        outside_brackets = re.sub(r"\[[^\]]+\]", "|", line).split("|")
        inside = all([not abba(s) for s in inside_brackets])
        outside = any([abba(s) for s in outside_brackets])
        if inside and outside:
            ret += 1

    return ret


def two(filename: str):
    lines = toLines(filename)
    ret = 0
    for line in lines:
        inside_brackets = re.findall(r"\[([^\]]+)\]", line)
        outside_brackets = re.sub(r"\[[^\]]+\]", "|", line).split("|")
        outside_abas = [result for s in outside_brackets for result in aba(s)]
        inside_abas = [result for s in inside_brackets for result in aba(s)]
        for a, b in itertools.product(outside_abas, inside_abas):
            if a[0] == b[1] and a[1] == b[0]:
                ret += 1
                break

    return ret


print("part one:", one("input/day7"))
print("part two:", two("input/day7"))
