from util import tolines
import math

def partone():
    lines = tolines("input/day8")
    instruction = lines[0]
    m = {}
    
    for i in range(2, len(lines)):
        # DBQ = (RTP, NBX)
        parts = lines[i].split(" ")
        start = parts[0]
        left = parts[2][1:-1]
        right = parts[-1][:-1]
        m[start] = (left, right)
    
    ptr = 0
    steps = 0
    cur = "AAA"
    while True:
        if cur == "ZZZ":
            return steps
        lr = instruction[ptr]
        if lr == "L":
            cur = m[cur][0]
        else:
            cur = m[cur][1]
        steps += 1
        
        ptr += 1
        if ptr >= len(instruction):
            ptr = 0
    return -1

def find_lcm(a, b):
    return (a * b) // math.gcd(a, b)

def lcm_array(arr):
    lcm = arr[0]
    for i in range(1, len(arr)):
        lcm = find_lcm(lcm, arr[i])
    return lcm
    
def parttwo():
    lines = tolines("input/day8")
    instruction = lines[0]
    m = {}
    heads = []
    
    for i in range(2, len(lines)):
        # DBQ = (RTP, NBX)
        parts = lines[i].split(" ")
        start = parts[0]
        left = parts[2][1:-1]
        right = parts[-1][:-1]
        m[start] = (left, right)
        if start.endswith("A"):
            heads.append(start)
    

    diffs = []
    for i, head in enumerate(heads):
        ptr = 0
        steps = 0
        prev_z = 0
        cur = head
        while True:
            if cur.endswith("Z") and prev_z != 0:
               diffs.append(steps - prev_z)
               break
            elif cur.endswith("Z"):
                prev_z = steps
            lr = instruction[ptr]
            if lr == "L":
                cur = m[cur][0]
            else:
                cur = m[cur][1]
            steps += 1
            ptr += 1
            if ptr >= len(instruction):
                ptr = 0

    return lcm_array(diffs)
        
        
print("partone", partone())
print("parttwo", parttwo())