from util import toString

def part1():
    s = toString("input/day9")
    cleaned = ""
    ignored = False
    for c in s:
        if c == "!" and not ignored:
            ignored = True
            cleaned += "."
        elif ignored:
            ignored = False
            cleaned += "."
        else:
            cleaned += c
            
    idx = -1
    for i, c in enumerate(cleaned):
        if c == "<" and idx == -1:
            idx = i
        elif c == ">":
            cleaned = cleaned[:idx] + "." * (i - idx + 1) + cleaned[i+1:]
            idx = -1
    
    cnt = 0
    sum_score = 0
    for c in cleaned:
        if c == "{":
            cnt += 1
        elif c== "}":
            sum_score += cnt
            cnt -= 1
    print(sum_score)
    
def part2():
    s = toString("input/day9")
    cleaned = ""
    ignored = False
    for c in s:
        if c == "!" and not ignored:
            ignored = True
            cleaned += "."
        elif ignored:
            ignored = False
            cleaned += "."
        else:
            cleaned += c
    
    ret = 0
    idx = -1
    for i, c in enumerate(cleaned):
        if c == "<" and idx == -1:
            idx = i
        elif c == ">":
            for char in cleaned[idx+1: i]:
                if char != ".":
                    ret += 1
            
            idx = -1
    print(ret)
    
    
part1()
part2()