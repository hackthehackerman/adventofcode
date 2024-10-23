from util import tolines
from collections import defaultdict

def part1():
    lines = tolines("input/day12")
    graph = defaultdict(set)
    for line in lines:
        left, right = line.split(" <-> ")
        left = int(left)
        right = list(map(int, right.split(", ")))
        graph[left].update(right)
        
    
    group = set()
    toVisit = [0]
    while toVisit:
        current = toVisit.pop()
        group.add(current)
        for neighbor in graph[current]:
            if neighbor not in group:
                toVisit.append(neighbor)
    print(len(group))
    
    
def part2():
    lines = tolines("input/day12")
    graph = defaultdict(set)
    for line in lines:
        left, right = line.split(" <-> ")
        left = int(left)
        right = list(map(int, right.split(", ")))
        graph[left].update(right)
        
    all_nodes = set(graph.keys())
    groups = 0
    while all_nodes:
        group = set()
        toVisit = [all_nodes.pop()]
        while toVisit:
            current = toVisit.pop()
            group.add(current)
            for neighbor in graph[current]:
                if neighbor not in group:
                    toVisit.append(neighbor)
        all_nodes -= group
        groups += 1
    print(groups)
    
part1()
part2()