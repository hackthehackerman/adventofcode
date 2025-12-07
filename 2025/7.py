from util import tolines, toMatrix

def partone():
    m = toMatrix("input/day7")
    
    split = 0
    for i in range(len(m)-1):
        for j in range(len(m[0])):
            char = m[i][j]
            if char == "S":
                m[i+1][j] = "|"
            elif char == "|" and m[i+1][j] == "^":
                split += 1
                if j-1 >= 0:
                    m[i+1][j-1] = "|"
                if j+1 < len(m[0]):
                    m[i+1][j+1] = "|"
            elif char == "|":
                m[i+1][j] = "|"
    
    return split

    
def parttwo():
    m = toMatrix("input/day7")
    
    for i in range(len(m)-1):
        for j in range(len(m[0])):
            char = m[i][j]
            if char == "S":
                m[i+1][j] = "|"
            elif char == "|" and m[i+1][j] == "^":
                if j-1 >= 0:
                    m[i+1][j-1] = "|"
                if j+1 < len(m[0]):
                    m[i+1][j+1] = "|"
            elif char == "|":
                m[i+1][j] = "|"
        
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == "|":
                if i == len(m)-1:
                    m[i][j] = 1
                else:
                    m[i][j] = 0
        
        
    for i in reversed(range(1, len(m))):
        for j in range(len(m[0])):
            item = m[i][j]
            if str(item).isdigit():
                if j-1 >= 0 and m[i][j-1] == "^" and str(m[i-1][j-1]).isdigit():
                    m[i-1][j-1] += item
                if j+1 < len(m[0]) and m[i][j+1] == "^" and str(m[i-1][j+1]).isdigit():
                    m[i-1][j+1] += item
                if str(m[i-1][j]).isdigit():
                    m[i-1][j] = item
        
    for j in range(len(m[0])):
        if m[0][j] == "S":
            return m[1][j]
                    
                    
            

    return 0
    
    

print(partone())
print(parttwo())
