from util import tolines
from itertools import combinations


def partone():
    lines = tolines("input/day11")
    rStar = set()
    cStar = set()
    m = []
    for i, line in enumerate(lines):
        row = []
        for j, c in enumerate(line):
            row.append(c)
            if c == "#":
                rStar.add(i)
                cStar.add(j)
        m.append(row)
    rNoStar = [i for i in range(len(m)) if i not in rStar]
    cNoStar = [i for i in range(len(m[0])) if i not in cStar]
    
    for j in sorted(cNoStar, reverse=True):
        for row in m:
            row.insert(j, ".")
    for i in sorted(rNoStar, reverse=True):
        m.insert(i, ["." for i in range(len(m[0]))])

    stars = [(i,j) for i in range(len(m)) for j in range(len(m[0])) if m[i][j] == "#"]
    
    ret = 0
    for star1, star2 in combinations(stars,2):
        ret += abs(star2[0] - star1[0]) + abs(star2[1] - star1[1])
    return ret

def parttwo():
    lines = tolines("input/day11")
    rStar = set()
    cStar = set()
    m = []
    for i, line in enumerate(lines):
        row = []
        for j, c in enumerate(line):
            row.append(c)
            if c == "#":
                rStar.add(i)
                cStar.add(j)
        m.append(row)

    stars = [[i,j] for i in range(len(m)) for j in range(len(m[0])) if m[i][j] == "#"]
    rNoStar = [i for i in range(len(m)) if i not in rStar]
    cNoStar = [i for i in range(len(m[0])) if i not in cStar]
    
    for j in sorted(cNoStar, reverse=True):
        for star in stars:
            if star[1] > j:
                star[1] += 999999
    for i in sorted(rNoStar, reverse=True):
        for star in stars:
            if star[0] > i:
                star[0] += 999999    
    ret = 0
    for star1, star2 in combinations(stars,2):
        ret += abs(star2[0] - star1[0]) + abs(star2[1] - star1[1])
    return ret
    
    
        
print(partone())
print(parttwo())