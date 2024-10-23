from util import toString

def get_direction_vectors():
    return {
        'n': (0, 1, -1),
        'ne': (1, 0, -1),
        'se': (1, -1, 0),
        's': (0, -1, 1),
        'sw': (-1, 0, 1),
        'nw': (-1, 1, 0)
    }

def cube_distance(x, y, z):
    return max(abs(x), abs(y), abs(z))

def part1():
    steps = toString("input/day11").split(",")
    directions = get_direction_vectors()
    
    x, y, z = 0, 0, 0
    
    for step in steps:
        dx, dy, dz = directions[step]
        x += dx
        y += dy
        z += dz
    
    distance = cube_distance(x, y, z)
    print(distance)
    
def part2():
    steps = toString("input/day11").split(",")
    directions = get_direction_vectors()
    
    x, y, z = 0, 0, 0
    max_distance = 0
    for step in steps:
        dx, dy, dz = directions[step]
        x += dx
        y += dy
        z += dz
        max_distance = max(max_distance, cube_distance(x, y, z))
    print(max_distance)

part1()
part2()