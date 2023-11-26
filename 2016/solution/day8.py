from util import toLines


def one(filename: str):
    lines = toLines(filename)
    matrix = [[0 for _ in range(50)] for _ in range(6)]
    for line in lines:
        if line.startswith("rect"):
            x, y = map(int, line.split(" ")[1].split("x"))
            for i in range(y):
                for j in range(x):
                    matrix[i][j] = 1
        elif line.startswith("rotate row"):
            row = int(line.split(" ")[2].split("=")[1])
            amount = int(line.split(" ")[4])
            matrix[row] = matrix[row][-amount:] + matrix[row][:-amount]
        elif line.startswith("rotate column"):
            col = int(line.split(" ")[2].split("=")[1])
            amount = int(line.split(" ")[4])
            column = [matrix[i][col] for i in range(len(matrix))]
            column = column[-amount:] + column[:-amount]
            for i in range(len(matrix)):
                matrix[i][col] = column[i]

    return sum([sum(row) for row in matrix])


def two(filename: str):
    lines = toLines(filename)
    matrix = [[0 for _ in range(50)] for _ in range(6)]
    for line in lines:
        if line.startswith("rect"):
            x, y = map(int, line.split(" ")[1].split("x"))
            for i in range(y):
                for j in range(x):
                    matrix[i][j] = 1
        elif line.startswith("rotate row"):
            row = int(line.split(" ")[2].split("=")[1])
            amount = int(line.split(" ")[4])
            matrix[row] = matrix[row][-amount:] + matrix[row][:-amount]
        elif line.startswith("rotate column"):
            col = int(line.split(" ")[2].split("=")[1])
            amount = int(line.split(" ")[4])
            column = [matrix[i][col] for i in range(len(matrix))]
            column = column[-amount:] + column[:-amount]
            for i in range(len(matrix)):
                matrix[i][col] = column[i]
    for row in matrix:
        print("".join(["#" if x == 1 else " " for x in row]))


print("part one:", one("input/day8"))
print("part two:")
two("input/day8")
