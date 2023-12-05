from util import toLines


def partone():
    lines = toLines("input/day12")
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}

    ptr = 0
    while ptr < len(lines):
        line = lines[ptr]
        if line.startswith("cpy"):
            _, x, y = line.split()
            if x in registers:
                registers[y] = registers[x]
            else:
                registers[y] = int(x)
        elif line.startswith("inc"):
            _, x = line.split()
            registers[x] += 1
        elif line.startswith("dec"):
            _, x = line.split()
            registers[x] -= 1
        elif line.startswith("jnz"):
            _, x, y = line.split()
            if x in registers:
                if registers[x] != 0:
                    ptr += int(y)
                    continue
            else:
                if int(x) != 0:
                    ptr += int(y)
                    continue
        ptr += 1
    return registers["a"]


def parttwo():
    lines = toLines("input/day12")
    registers = {"a": 0, "b": 0, "c": 1, "d": 0}

    ptr = 0
    while ptr < len(lines):
        line = lines[ptr]
        if line.startswith("cpy"):
            _, x, y = line.split()
            if x in registers:
                registers[y] = registers[x]
            else:
                registers[y] = int(x)
        elif line.startswith("inc"):
            _, x = line.split()
            registers[x] += 1
        elif line.startswith("dec"):
            _, x = line.split()
            registers[x] -= 1
        elif line.startswith("jnz"):
            _, x, y = line.split()
            if x in registers:
                if registers[x] != 0:
                    ptr += int(y)
                    continue
            else:
                if int(x) != 0:
                    ptr += int(y)
                    continue
        ptr += 1
    return registers["a"]


print("part one", partone())
print("part two", parttwo())
