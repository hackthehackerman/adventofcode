def tolines(f):
    return open(f).read().splitlines()

def toString(f):
    return open(f).read()

def toMatrix(f):
    lines = tolines(f)
    ret = []
    for line in lines:
        ret.append([c for c in line])
    return ret