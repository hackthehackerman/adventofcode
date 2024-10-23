from util import tolines

def part1():
    lines = tolines("input/day13")
    firewall = {}
    for line in lines:
        layer, range = line.split(": ")
        firewall[int(layer)] = int(range)
    
    severity = 0
    for layer, range in firewall.items():
        if layer % ((range - 1) * 2) == 0:
            severity += layer * range
    print(severity)
    
def part2():
    lines = tolines("input/day13")
    firewall = {}
    for line in lines:
        layer, range = line.split(": ")
        firewall[int(layer)] = int(range)
    
    delay = 0
    while True:
        caught = False
        for layer, range in firewall.items():
            if (layer + delay) % ((range - 1) * 2) == 0:
                caught = True
                break
        if not caught:
            print(delay)
            break
        delay += 1
part1()
part2()