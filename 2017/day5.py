from util import tolines

def part1():
    jumps = [int(line) for line in tolines("input/day5")]
        
    idx = 0
    count = 0
    while idx < len(jumps):
        tmp = jumps[idx]
        jumps[idx] += 1
        idx += tmp
        count += 1
    print(count)
    
def part2():
    jumps = [int(line) for line in tolines("input/day5")]
        
    idx = 0
    count = 0
    while idx < len(jumps):
        tmp = jumps[idx]
        if tmp >= 3:
            jumps[idx] -= 1
        else:
            jumps[idx] += 1
        idx += tmp
        count += 1
    print(count)
        
        
part1()
part2()