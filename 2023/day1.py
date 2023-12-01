import re

from util import tolines


def partone():
    lines = tolines("input/day1")
    ret = 0
    for l in lines:
        numbers = re.findall("[0-9]", l)
        if len(numbers) == 1:
            ret += int(numbers[0]) * 11
        else:
            ret += int(f"{numbers[0]}{numbers[-1]}")
    return ret


def parttwo():
    lookups = [
        "[0-9]",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    regex = f"(?=({'|'.join(lookups)}))"

    lines = tolines("input/day1")
    ret = 0
    for l in lines:
        numbers = re.findall(regex, l)
        first = numbers[0] if numbers[0].isdigit() else lookups.index(numbers[0])
        second = (
            numbers[len(numbers) - 1]
            if numbers[len(numbers) - 1].isdigit()
            else lookups.index(numbers[len(numbers) - 1])
        )

        ret += int(f"{first}{second}")

    return ret


print("partone:", partone())
print("parttwo:", parttwo())
