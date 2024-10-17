from util import toString

def part1():
    s = toString("input/day1")
    ret = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            ret += int(s[i])
    if s[0] == s[-1]:
        ret += int(s[0])
    print(ret)
    
    
def part2():
    s = toString("input/day1")
    arr = [int(i) for i in s]
    ret = 0
    for i in range(len(arr)):
        if arr[i] == arr[(i+len(arr)//2) % len(arr)]:
            ret += arr[i]
    print(ret)

part1()
part2()