from util import toLines


def one(filename: str):
    lines = toLines(filename)
    bots = [[] for _ in range(250)]
    give = [[] for _ in range(250)]
    for l in lines:
        if l.startswith("value"):
            value = int(l.split(" ")[1])
            bot = int(l.split(" ")[5])
            bots[bot].append(value)
            bots[bot].sort()
        else:
            bot = int(l.split(" ")[1])
            low = int(l.split(" ")[6])
            high = int(l.split(" ")[11])
            give[bot] = [low, high]

    while True:
        for i in range(250):
            if len(bots[i]) == 2:
                if bots[i] == [17, 61]:
                    return i
                low, high = bots[i]
                gl, gh = give[i]
                bots[gl].append(low)
                bots[gh].append(high)
                bots[gl].sort()
                bots[gh].sort()

                bots[i] = []
                break

    return -1


def two(filename: str):
    lines = toLines(filename)
    bots = [[] for _ in range(250)]
    output = [None for _ in range(21)]
    give = [[] for _ in range(250)]
    for l in lines:
        if l.startswith("value"):
            value = int(l.split(" ")[1])
            bot = int(l.split(" ")[5])
            bots[bot].append(value)
            bots[bot].sort()
        else:
            bot = int(l.split(" ")[1])
            low = [l.split(" ")[5], int(l.split(" ")[6])]
            high = [l.split(" ")[10], int(l.split(" ")[11])]
            give[bot] = [low, high]

    while True:
        if output[0] is not None and output[1] is not None and output[2] is not None:
            return output[0] * output[1] * output[2]
        for i in range(250):
            if len(bots[i]) == 2:
                low, high = bots[i]
                gl, gh = give[i]
                if gl[0] == "output":
                    output[gl[1]] = low
                else:
                    bots[gl[1]].append(low)
                    bots[gl[1]].sort()
                if gh[0] == "output":
                    output[gh[1]] = high
                else:
                    bots[gh[1]].append(high)
                    bots[gh[1]].sort()

                bots[i] = []
                break


print("part one:", one("input/day10"))
print("part two:", two("input/day10"))
