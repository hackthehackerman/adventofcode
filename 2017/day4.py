from util import tolines

def part1():
    lines = tolines("input/day4")
    count = 0
    for line in lines:
        words = line.split()
        if len(words) == len(set(words)):
            count += 1
    print(count)
    
def part2():
    lines = tolines("input/day4")
    count = 0
    for line in lines:
        words = line.split()
        words = [''.join(sorted(word)) for word in words]
        if len(words) == len(set(words)):
            count += 1
    print(count)

part1()
part2()