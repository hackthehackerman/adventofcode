from util import tolines, toMatrix
from math import sqrt
from collections import defaultdict
from functools import reduce
from operator import mul

def partone():
    num_pairs = 1000
    l = tolines("input/day8")
    coordinates = [tuple(map(int, line.split(','))) for line in l if line.strip()]
    distances = [] # each item is tuple of (distance, index1, index2) where index1 and index2 maps to the item in coordinates arr
    
    n = len(coordinates)
    for i in range(n):
        for j in range(i + 1, n):
            p1 = coordinates[i]
            p2 = coordinates[j]
            # Euclidean distance in 3D
            dist = sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))
            distances.append((dist, i, j))
    
    distances.sort()
    
    graph = defaultdict(set) # idx: [idx]
    
    for i in range(num_pairs):
        _, idx1, idx2 = distances[i]
        graph[idx1].add(idx2)
        graph[idx2].add(idx1)
    
    
    def dfs(start, visited):
        stack = [start]
        circuit = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                circuit.append(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return circuit

    visited = set()
    circuits = []

    for node in range(n):
        if node not in visited and node in graph:
            circuit = dfs(node, visited)
            circuits.append(circuit)
        elif node not in visited:
            circuits.append([node])
            visited.add(node)

    sizes = sorted([len(circuit) for circuit in circuits], reverse=True)
    top_three = sizes[:3]

    product = reduce(mul, top_three, 1)
    return product
    
def parttwo():
    lines = tolines("input/day8")
    coordinates = [tuple(map(int, line.split(','))) for line in lines if line.strip()]
    n = len(coordinates)

    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            p1 = coordinates[i]
            p2 = coordinates[j]
            dist = sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))
            distances.append((dist, i, j))
    distances.sort()

    # Union Find Structure
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        parent[py] = px
        return True

    sets = n
    last_pair = None
    for _, i, j in distances:
        if union(i, j):
            sets -= 1
            if sets == 1:
                last_pair = (i, j)
                break

    if last_pair is None:
        return -1


    x1 = coordinates[last_pair[0]][0]
    x2 = coordinates[last_pair[1]][0]
    return x1 * x2
    
    

print(partone())
print(parttwo())
