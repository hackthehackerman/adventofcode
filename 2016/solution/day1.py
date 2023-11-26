from util import toString


def one(filename: str):
    directions = ["N", "E", "S", "W"]
    direction = directions[0]
    coordinates = [0, 0]

    content = toString(filename)
    instructions = content.split(",")
    for step in instructions:
        step = step.strip()
        if step[0] == "L":
            direction = directions[(directions.index(direction) - 1) % 4]
        else:
            direction = directions[(directions.index(direction) + 1) % 4]
        distance = int(step[1:])
        if direction == "N":
            coordinates[1] += distance
        elif direction == "E":
            coordinates[0] += distance
        elif direction == "S":
            coordinates[1] -= distance
        elif direction == "W":
            coordinates[0] -= distance

    return abs(coordinates[0]) + abs(coordinates[1])


def two(filename: str):
    directions = ["N", "E", "S", "W"]
    visited = set()
    direction = directions[0]
    coordinates = [0, 0]

    content = toString(filename)
    instructions = content.split(",")
    for step in instructions:
        step = step.strip()
        if step[0] == "L":
            direction = directions[(directions.index(direction) - 1) % 4]
        else:
            direction = directions[(directions.index(direction) + 1) % 4]
        distance = int(step[1:])

        for i in range(distance):
            if direction == "N":
                coordinates[1] += 1
            elif direction == "E":
                coordinates[0] += 1
            elif direction == "S":
                coordinates[1] -= 1
            elif direction == "W":
                coordinates[0] -= 1

            if tuple(coordinates) in visited:
                return abs(coordinates[0]) + abs(coordinates[1])
            else:
                visited.add(tuple(coordinates))

    return -1


print("part one:", one("input/day1"))
print("part two:", two("input/day1"))
