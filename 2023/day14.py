from util import tolines
from collections import Counter

def spin(m, direction):
    map = {
        "N": [-1,0],
        "W": [0,-1],
        "S": [1, 0],
        "E": [0,1],
    }
    delta = map[direction]
    irange = list(range(len(m)))
    if direction == "S":
        irange = list(reversed(irange))
    jrange = list(range(len(m[0])))
    if direction == "E":
        jrange = list(reversed(jrange))
    for i in irange:
        for j in jrange:
            if m[i][j] != "O":
                continue
            ii, jj = i+delta[0], j + delta[1]
            lii, ljj = i, j
            while 0 <= ii < len(m) and 0<=jj < len(m[0]) and m[ii][jj] == ".":
                m[ii][jj] = "O"
                m[lii][ljj] = "."
                lii, ljj = ii, jj
                ii = ii + delta[0]
                jj = jj + delta[1]
    
    
def partone():
    lines = tolines("input/day14")
    m = []
    for line in lines:
        m.append([c for c in line])
    
    spin(m, "N")
    
    ret = 0
    for i, row in enumerate(m):
        c = Counter(row)["O"] 
        ret += c * (len(m) - i)
    return ret



def parttwo():
    lines = tolines("input/day14")
    m = []
    for line in lines:
        m.append([c for c in line])
    
    cache = {}
    ptr = 0
    target = 1000000000
    version = 0
    loop_low = 0
    loop_high = 0
    while ptr < target:
        spin(m,"N")
        spin(m,"W")
        spin(m,"S")
        spin(m,"E")
        key = "\n".join(["".join(row) for row in m])
        if key in cache:
            loop_low = cache[key]
            loop_high = version - 1
            delta = loop_high + 1 - loop_low
            while ptr + delta < target:
                ptr += delta
            ptr += 1
            while ptr < target:
                spin(m,"N")
                spin(m,"W")
                spin(m,"S")
                spin(m,"E")
                ptr += 1
        else:
            cache[key] = version
            version += 1
        ptr += 1
            
    
    ret = 0
    for i, row in enumerate(m):
        c = Counter(row)["O"] 
        ret += c * (len(m) - i)
    return ret

print(partone())
print(parttwo())