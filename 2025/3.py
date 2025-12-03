from util import tolines

def partone():
    batteries = tolines("input/day3")
    ret = 0
    
    for battery in batteries:
        digits = [int(c) for c in battery]
        first = -1
        firstIdx = -1
        for idx, num in enumerate(digits[:-1]):
            if num > first:
                first = num
                firstIdx =  idx
        
        second = -1
        for num in digits[firstIdx+1:]:
            if num > second:
                second = num

        joltage = first * 10 + second
        ret += joltage
    return ret
        
    


def parttwo():
    batteries = tolines("input/day3")
    ret = 0
    num_digits_in_joltage = 12
    
    for battery in batteries:
        digits = [int(c) for c in battery]
        chosen = []
        cur_idx = 0
        
        for i in range(num_digits_in_joltage):
            candidate = -1
            candidate_idx = -1
            remaining_num_digits = num_digits_in_joltage - i - 1
            for idx in range(cur_idx, len(digits) - remaining_num_digits):
                num = digits[idx]
                if num > candidate:
                    candidate = num
                    candidate_idx = idx
            chosen.append(candidate)
            cur_idx = candidate_idx + 1
        joltage = 0
        for digit in chosen:
            joltage *= 10
            joltage += digit
        ret += joltage
    return ret
            
    
    

print(partone())
print(parttwo())
