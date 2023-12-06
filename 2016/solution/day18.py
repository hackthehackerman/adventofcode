from util import toLines


def partone():
    lines = toLines("input/day18")
    for i in range(39):
        line = lines[-1]
        newline = ""
        for j in range(len(line)):
            left = line[j - 1] if j > 0 else "."
            center = line[j]
            right = line[j + 1] if j < len(line) - 1 else "."
            combination = left + center + right
            if combination == "^^.":
                newline += "^"
            elif combination == ".^^":
                newline += "^"
            elif combination == "^..":
                newline += "^"
            elif combination == "..^":
                newline += "^"
            else:
                newline += "."
        lines.append(newline)
    safe = 0
    for line in lines:
        safe += line.count(".")
    return safe


def parttwo():
    lines = toLines("input/day18")
    for i in range(400000 - 1):
        line = lines[-1]
        newline = ""
        for j in range(len(line)):
            left = line[j - 1] if j > 0 else "."
            center = line[j]
            right = line[j + 1] if j < len(line) - 1 else "."
            combination = left + center + right
            if combination == "^^.":
                newline += "^"
            elif combination == ".^^":
                newline += "^"
            elif combination == "^..":
                newline += "^"
            elif combination == "..^":
                newline += "^"
            else:
                newline += "."
        lines.append(newline)
    safe = 0
    for line in lines:
        safe += line.count(".")
    return safe


print("partone", partone())
print("parttwo", parttwo())
