from util import tolines

def find_horizontal(m):
    ret = []
    for i in range(1,len(m)):
        lptr = i-1
        rptr = i
        same = True
        while lptr >= 0 and rptr <len(m):
            same = same and m[lptr] == m[rptr]
            lptr -= 1
            rptr += 1
        if (lptr == -1 or rptr == len(m)) and same:
            ret.append(i)
    return ret

def find_vertical(m):
    ret = []
    for i in range(1,len(m[0])):
        lptr = i-1
        rptr = i
        same = True
        while lptr >= 0 and rptr <len(m[0]):
            lcol = [r[lptr] for r in m]
            rcol = [r[rptr] for r in m]
            
            same = same and lcol == rcol
            lptr -= 1
            rptr += 1
        if (lptr == -1 or rptr == len(m[0])) and same:
            ret.append(i)
    return ret

def partone():
    lines = tolines("input/day13")
    m = []
    ret = 0
    for i, line in enumerate(lines):
        m.append([c for c in line])
        if line == "":
            m = m[:-1]
        elif i != len(lines)-1:
            continue
        
        h = find_horizontal(m)
        v = find_vertical(m)
        if len(h) != 0:
            ret += (h[0] * 100)
        if len(v) != 0:
            ret += v[0]
        m = []
    return ret

def parttwo():
    lines = tolines("input/day13")
    m = []
    ret = 0
    for i, line in enumerate(lines):
        m.append([c for c in line])
        if line == "":
            m = m[:-1]
        elif i != len(lines)-1:
            continue
        
        h = find_horizontal(m)
        v = find_vertical(m)
        
        found = False
        for ii in range(len(m)):
            if found:
                break
            for jj in range(len(m[0])):
                if found:
                    break
                m[ii][jj] = "#" if m[ii][jj] == "." else "."
                hh = find_horizontal(m)
                vv = find_vertical(m)
                if len(hh) != 0 or len(vv) != 0:
                    if len(hh) != 0 and len(set(hh) - set(h))!= 0:
                        found = True
                        hh = list(set(hh) - set(h))[0]
                        ret += (hh * 100)
                    if len(vv) != 0 and len(set(vv) - set(v))!= 0:
                        found = True
                        vv = list(set(vv) - set(v))[0]
                        ret += vv
                
                m[ii][jj] = "#" if m[ii][jj] == "." else "."
            
        m = []
    return ret


print(partone())
print(parttwo())
       