from util import toMatrix

def partone():
    m = toMatrix("input/day4")
    counts = [[0 for i in range(len(m[0]))] for j in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == ".":
                continue
            for ii in [i-1, i, i+1]:
                for jj in [j-1, j, j+1]:
                    if ii == i and jj == j:
                        continue
                    if ii < 0 or ii >= len(m):
                        continue
                    if jj < 0 or jj >= len(m[0]):
                        continue
                    counts[ii][jj] += 1
    ret = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            count = counts[i][j]
            if count < 4 and m[i][j] == "@":
                ret += 1
    return ret
    
            
def parttwo():
    
    def remove_paper(m):
        counts = [[0 for i in range(len(m[0]))] for j in range(len(m))]
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == ".":
                    continue
                for ii in [i-1, i, i+1]:
                    for jj in [j-1, j, j+1]:
                        if ii == i and jj == j:
                            continue
                        if ii < 0 or ii >= len(m):
                            continue
                        if jj < 0 or jj >= len(m[0]):
                            continue
                        counts[ii][jj] += 1
        for i in range(len(m)):
            for j in range(len(m[0])):
                count = counts[i][j]
                if count < 4 and m[i][j] == "@":
                    m[i][j] = "."
        return m
    
    def count_paper(m):
        ret = 0
        for row in m:
            for item in row:
                if item == "@":
                    ret += 1
        return ret
    
    m = toMatrix("input/day4")
    initial_cnt = count_paper(m)
    prev_cnt = initial_cnt
    while True:
        m = remove_paper(m)
        new_cnt = count_paper(m)
        
        if new_cnt == prev_cnt:
            break
        prev_cnt = new_cnt
    final_cnt = count_paper(m)
    return initial_cnt - final_cnt


    
    return 0
            
    
    

print(partone())
print(parttwo())
