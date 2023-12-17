from util import toString
from collections import OrderedDict


def partone():
    s = toString("input/day15")
    seqs = s.split(',')
    ret = 0
    for seq in seqs:
        val = 0
        for c in seq:
            val += ord(c)
            val *= 17
            val = val % 256
        ret += val
    return ret

def hash(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val = val % 256
    return val

def parttwo():
    seqs=  toString("input/day15").split(',')
    boxes = {
        i: OrderedDict() for i in range(256)
    }
    for seq in seqs:
        if "=" in seq:
            label, val = seq.split("=")
            box = hash(label)
            boxes[box][label] = int(val)
        else:
            label = seq[:-1]
            box = hash(label)
            if label in boxes[box]:
                del boxes[box][label]
    
    ret = {}
    for i in range(256):
        for idx, (key, value) in enumerate(boxes[i].items()):
            ret[key] = (i+1) * (idx+1) * value
    return sum(ret.values())
            
        

print(partone())
print(parttwo())

            