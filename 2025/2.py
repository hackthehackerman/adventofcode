from util import tolines

def partone():
    ranges = tolines("input/day2")[0]
    ranges = ranges.split(",")

    
    def isValid(int_value):
        s = str(int_value)
        if len(s) % 2 != 0:
            return True
        half = int(len(s) / 2)
        left, right = s[:half], s[half:]
        if left == right:
            return False
        else:
            return True
    
    ret = 0
    for r in ranges:
        split = r.split("-")
        left = int(split[0])
        right = int(split[1])
        for i in range(left, right+1):
            if not isValid(i):
                # print(i)
                ret += i
    return ret

def parttwo():
    ranges = tolines("input/day2")[0]
    ranges = ranges.split(",")

    
    def isValid(int_value):
        s = str(int_value)
        
        for i in range(1, int(len(s) / 2) + 1):
            part = s[:i]
            tmp = part
            while len(tmp) < len(s):
                tmp = tmp + part
                if tmp == s:
                    return False
            
        return True
    
    ret = 0
    for r in ranges:
        split = r.split("-")
        left = int(split[0])
        right = int(split[1])
        for i in range(left, right+1):
            if not isValid(i):
                # print(i)
                ret += i
    return ret
    

print(partone())
print(parttwo())
