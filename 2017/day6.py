from util import tolines

def part1():
    banks = [int(x) for x in tolines("input/day6")[0].split()]
    seen = set()
    count = 0
    while tuple(banks) not in seen:
        seen.add(tuple(banks))
        max_val = max(banks)
        max_idx = banks.index(max_val)
        banks[max_idx] = 0
        for i in range(max_val):
            banks[(max_idx + i + 1) % len(banks)] += 1
        count += 1
    print(count)
    
def part2():
    banks = [int(x) for x in tolines("input/day6")[0].split()]
    seen = set()
    cycle_start = None
    count = 0
    while tuple(banks) not in seen:
        seen.add(tuple(banks))
        max_val = max(banks)
        max_idx = banks.index(max_val)
        banks[max_idx] = 0
        for i in range(max_val):
            banks[(max_idx + i + 1) % len(banks)] += 1
        count += 1
        if tuple(banks) in seen:
            cycle_start = tuple(banks)
    
    count = 0
    while tuple(banks) != cycle_start or count == 0:
        max_val = max(banks)
        max_idx = banks.index(max_val)
        banks[max_idx] = 0
        for i in range(max_val):
            banks[(max_idx + i + 1) % len(banks)] += 1
        count += 1
        
    print(count)
    
part1()
part2()