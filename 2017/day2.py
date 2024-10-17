from util import tolines

def part1():
    lines = tolines("input/day2")
    m = []
    for line in lines:
        m.append([int(c) for c in line.split()])
    
    ret = sum(max(line) - min(line) for line in m)
    print(ret)
    
def part2():
    lines = tolines("input/day2")
    m = []
    for line in lines:
        m.append(sorted([int(c) for c in line.split()]))
    
    ret = 0
    for line in m:
        for i in range(len(line)):
            for j in range(i+1, len(line)):
                if line[j] % line[i] == 0:
                    ret += line[j] // line[i]
    print(ret)
    

part1()
part2()