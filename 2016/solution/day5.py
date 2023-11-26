from util import toString
from collections import Counter
import hashlib


def one(filename: str):
    string = toString(filename)
    i = 0
    ret = ""
    while True:
        hex = hashlib.md5((string + str(i)).encode("utf-8")).hexdigest()
        if hex.startswith("00000"):
            ret += hex[5]
            if len(ret) == 8:
                break
        i += 1

    return ret


def two(filename: str):
    string = toString(filename)
    i = 0
    ret = ["" for _ in range(8)]
    while True:
        hex = hashlib.md5((string + str(i)).encode("utf-8")).hexdigest()
        if (
            hex.startswith("00000")
            and hex[5].isdigit()
            and int(hex[5]) < 8
            and ret[int(hex[5])] == ""
        ):
            ret[int(hex[5])] = hex[6]
            if Counter(ret)[""] == 0:
                break
        i += 1

    return "".join(ret)


print("part one:", one("input/day5"))
print("part two:", two("input/day5"))
