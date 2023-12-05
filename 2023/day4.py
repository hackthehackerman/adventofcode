from util import tolines
import re


def partone():
    lines = tolines("input/day4")
    scores = []
    for line in lines:
        numbers = re.findall(r"\d+", line)
        numbers = [int(number) for number in numbers]
        winning = numbers[1:11]
        ticket = numbers[11:]
        score = 0
        for n in ticket:
            if n in winning:
                if score == 0:
                    score += 1
                else:
                    score *= 2
        scores.append(score)

    return sum(scores)


def parttwo():
    lines = tolines("input/day4")
    scores = [1] * len(lines)
    for i, line in enumerate(lines):
        numbers = re.findall(r"\d+", line)
        numbers = [int(number) for number in numbers]
        winning = numbers[1:11]
        ticket = numbers[11:]
        score = 0
        for n in ticket:
            if n in winning:
                score += 1

        for j in range(i + 1, i + score + 1):
            scores[j] += scores[i]

    return sum(scores)


print("part one:", partone())
print("part two:", parttwo())
