from typing import List
from util import tolines
from collections import Counter

def countwithstop(s,c,stops):
    ret = []
    cur = 0
    for i in range(len(s)):
        if s[i] == c:
            cur += 1
        elif cur > 0:
            ret.append(cur)
            cur = 0
        if s[i] in stops:
            break
    if cur > 0:
        ret.append(cur)
    return ret

        
def arrangement(records: str, numbers: List[int], memo) -> int:
    key = records+(",".join([str(num) for num in numbers]))
    if key in memo:
        return memo[key]
    
    # print("eval", records, numbers)
    if sum(numbers) + len(numbers) - 1 > len(records):
        result = 0
        memo[key] = result
        return result
    counter = Counter(records)
    if len(numbers) == 0:
        result = 1 if counter["#"] == 0 else 0
        memo[key] = result
        return result
    if sum(numbers) > counter["#"] + counter["?"]:
        result = 0
        memo[key] = result
        return result
    if sum(numbers) < counter["#"]:
        result = 0
        memo[key] = result
        return result
    
    if "?" not in records:
        result = 1 if countwithstop(records, "#", "") == numbers else 0
        memo[key] = result
        return result
    
    first_chunk = [chunk for chunk in records.split(".") if len(chunk) > 0][0]
    if "?" not in first_chunk:
        result = arrangement(records[records.index(first_chunk)+len(first_chunk):], numbers[1:], memo) if len(first_chunk) == numbers[0] else 0
        memo[key] = result
        return result
    
    
    q_index = records.index("?")
    ret = 0
    candidate1 = records[:q_index] + "#" + records[q_index+1:]
    candidate2 = records[:q_index] + "." + records[q_index+1:]
    
    c = countwithstop(candidate1, "#", ".?")
    if len(c) > 0 and c[0] > numbers[0]:
        pass
    else:
        ret += arrangement(candidate1, numbers, memo)
    c = countwithstop(candidate2, "#", ".?")
    if len(c) > 0 and c[0] > numbers[0]:
        pass
    else:
        ret += arrangement(candidate2, numbers, memo)
    memo[key] = ret
    return ret
    
def partone():
    lines = tolines("input/day12")
    ret = 0
    for line in lines:
        left,right = line.split(" ")
        numbers = [int(n) for n in right.split(",")]
        memo = {}
        ret += arrangement(left, numbers, memo)
        
    return ret     
  
def parttwo():
    lines = tolines("input/day12")
    ret = 0
    for line in lines:
        left,right = line.split(" ")
        numbers = [int(n) for n in right.split(",")]
        left = ((left + "?") * 5)[:-1]
        numbers = numbers * 5
        # print(left)
        memo = {}
        ret += arrangement(left, numbers, memo)
        
    return ret     
            
        
        
print(partone())
print(parttwo())
