from util import tolines


def partone():
    lines = tolines("input/day9")
    nums = [line.split(" ") for line in lines]
    nums = [[int(n) for n in num] for num in nums]
    
    def find_next(nums):
        temp = [nums]
        next = nums
        while True:
            tmp = []
            
            if next[0] == 0 and len(set(next)) == 1:
                break
            for i in range(len(next)-1):
                tmp.append( next[i+1] - next[i])
            temp.append(tmp)
            next = tmp
        for i in range(len(temp)-1):
             temp[-(i+2)].append(temp[-(i+1)][-1] + temp[-(i+2)][-1])
        return temp[0][-1]
    
    return sum([find_next(num) for num in nums])

def parttwo():
    lines = tolines("input/day9")
    nums = [line.split(" ") for line in lines]
    nums = [[int(n) for n in num] for num in nums]
    
    def find_next(nums):
        temp = [nums]
        next = nums
        while True:
            tmp = []
            
            if next[0] == 0 and len(set(next)) == 1:
                break
            for i in range(len(next)-1):
                tmp.append(next[i+1] - next[i])
            temp.append(tmp)
            next = tmp
        for i in range(len(temp)-1):
             temp[-(i+2)].insert(0,temp[-(i+2)][0]-temp[-(i+1)][0] )
        return temp[0][0]
    
    return sum([find_next(num) for num in nums])
    
print("partone",partone())
print("parttwo",parttwo())
