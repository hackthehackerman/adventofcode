import re
from util import toLines
from collections import Counter


def extract_parts(s):
    # Regex pattern to match the string format
    pattern = r"([a-z-]+)-(\d+)\[([a-z]+)\]"

    # Search the string for matches
    match = re.search(pattern, s)

    if match:
        # Extracting the parts
        letters = match.group(1)
        number = match.group(2)
        bracket_letters = match.group(3)
        return letters, number, bracket_letters
    else:
        return None


def one(filename: str):
    lines = toLines(filename)
    ret = 0
    for line in lines:
        letters, number, bracket_letters = extract_parts(line)
        letters = letters.replace("-", "")
        c = Counter(letters)
        most_common_c = sorted(c.most_common(), key=lambda x: (-x[1], x[0]))[:5]
        most_common = "".join([x[0] for x in most_common_c])

        if most_common == bracket_letters:
            ret += int(number)

    return ret


def two(filename: str):
    lines = toLines(filename)
    for line in lines:
        decrypted = ""
        letters, number, bracket_letters = extract_parts(line)
        letters = letters.replace("-", " ")

        for l in letters:
            if l == " ":
                decrypted += " "
            else:
                decrypted += chr((ord(l) - ord("a") + int(number)) % 26 + ord("a"))
        if decrypted == "northpole object storage":
            return number

    return -1


print("part one:", one("input/day4"))
print("part two:", two("input/day4"))
