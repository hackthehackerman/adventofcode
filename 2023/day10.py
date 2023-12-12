from util import tolines


def partone():
    lines = tolines("input/day10")
    m = [[c for c in line] for line in lines]
    si, sj = 0,0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "S":
                si,sj = i,j
    
    # find loop
    pipes = ["-","|","L","J","7","F"]
    mapping = {
        "-": [(0,-1), (0,1)],
        "|": [(-1,0), (1,0)],
        "L": [(-1,0), (0,1)],
        "J": [(0,-1), (-1,0)],
        "7": [(0,-1), (1,0)],
        "F": [(0,1), (1,0)],
    }
    big_loop = []
    for c in pipes:
        m[si][sj] = c
        loop = [(si,sj)]
        visited = set((si,sj))
        found = False
        while True:
            last = loop[-1]
            last_char = m[last[0]][last[1]]
            lastlast = (-10,-10) if len(loop) == 1 else loop[-2]
            last_delta = (lastlast[0] - last[0], lastlast[1] - last[1])
            next_delta = mapping[last_char][1-mapping[last_char].index(last_delta)] if last_delta in mapping[last_char] else mapping[last_char][0]
            next = (last[0] + next_delta[0], last[1] + next_delta[1])
            # determine if the pipe can continue
            if next[0] < 0 or next[0] >= len(m) or next[1] < 0 or next[1] >= len(m[0]):
                # invalid pipe
                break
            next_char = m[next[0]][next[1]]
            if next_char not in pipes:
                break
            if (-next_delta[0], -next_delta[1]) not in mapping[next_char]:
                # invalid pipe
                break
            if next == (si, sj):
                found = True
                break
            if next in visited:
                break
            loop.append(next)
            visited.add(next)
        if found:
            big_loop = loop
            break
    return int(len(big_loop) / 2)

def parttwo():
    lines = tolines("input/day10")
    m = [[c for c in line] for line in lines]
    si, sj = 0,0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "S":
                si,sj = i,j
    
    # find loop
    pipes = ["-","|","L","J","7","F"]
    mapping = {
        "-": [(0,-1), (0,1)],
        "|": [(-1,0), (1,0)],
        "L": [(-1,0), (0,1)],
        "J": [(0,-1), (-1,0)],
        "7": [(0,-1), (1,0)],
        "F": [(0,1), (1,0)],
        ".": []
    }
    big_loop = []
    for c in pipes:
        m[si][sj] = c
        loop = [(si,sj)]
        visited = set((si,sj))
        found = False
        while True:
            last = loop[-1]
            last_char = m[last[0]][last[1]]
            lastlast = (-10,-10) if len(loop) == 1 else loop[-2]
            last_delta = (lastlast[0] - last[0], lastlast[1] - last[1])
            next_delta = mapping[last_char][1-mapping[last_char].index(last_delta)] if last_delta in mapping[last_char] else mapping[last_char][0]
            next = (last[0] + next_delta[0], last[1] + next_delta[1])
            # determine if the pipe can continue
            if next[0] < 0 or next[0] >= len(m) or next[1] < 0 or next[1] >= len(m[0]):
                # invalid pipe
                break
            next_char = m[next[0]][next[1]]
            if next_char not in pipes:
                break
            if (-next_delta[0], -next_delta[1]) not in mapping[next_char]:
                # invalid pipe
                break
            if next == (si, sj):
                found = True
                break
            if next in visited:
                break
            loop.append(next)
            visited.add(next)
        if found:
            big_loop = loop
            break
        
    for i in range(len(m)):
        for j in range(len(m[0])):
            if (i,j) not in big_loop:
                m[i][j] = "."
    def connected(coordinate1, coordinate2):
        x1,y1 = coordinate1
        x2, y2 = coordinate2
        if x1 < 0 or x1 >= len(m) or x2 < 0 or x2 >= len(m):
            return False
        if y1 < 0 or y1 >= len(m[0]) or y2 < 0 or y2 >= len(m[0]):
            return False
        
        c1 = m[x1][y1]
        c2 = m[x2][y2]
        if (x2,y2) in [(x1+delta[0], y1+delta[1]) for delta in mapping[c1]] and (x1,y1) in [(x2+delta[0], y2+delta[1]) for delta in mapping[c2]]:
            return True
    
    expanded = [["." for _ in range(len(m[0]) *2 - 1)] for _ in range(len(m) * 2 - 1)]
    for i in range(len(m) * 2 - 1):
        for j in range(len(m[0])*2 - 1):
            if i%2 == 0 and j%2 == 0:
                expanded[i][j] = m[int(i/2)][int(j/2)]
            if i%2 != 0 and j%2 == 0:
                # squeeze through horizontally
                if connected((int(i/2), int(j/2)),(int(i/2)+1, int(j/2))):
                    expanded[i][j] = "X"
            if i%2 == 0 and j%2 != 0:
                # squeeze through vertically
                if connected((int(i/2), int(j/2)),(int(i/2), int(j/2)+1)):
                    expanded[i][j] = "X"
                    
    
    outside = set()
    for i in range(len(expanded)):
        for j in range(len(expanded[0])):
            if (i in [0, len(expanded)-1] or j in [0, len(expanded[0])-1]) and expanded[i][j]==".":
                expanded[i][j] = "O"
                outside.add((i,j))
    
    while True:
        next = set()
        for i,j in outside:
            toFill = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
            for ii, jj in toFill:
                if 0 <= ii < len(expanded) and 0 <= jj < len(expanded[0]) and (ii,jj) not in outside and expanded[ii][jj] in ["O","."]:
                    expanded[ii][jj] = "O"
                    next.add((ii,jj))
        outside.update(next)
        if len(next) == 0:
            break
    
    ret = 0
    for i in range(len(expanded)):
        for j in range(len(expanded[0])):
            if i%2 == 0 and j%2 ==0 and expanded[i][j] == ".":
                ret += 1
                
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = expanded[i*2][j*2]

    return ret
                    
    
        

print(partone())
print(parttwo())