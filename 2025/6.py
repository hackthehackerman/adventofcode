from util import tolines

def partone():
    lines = tolines("input/day6")
    lines = [[item for item in line.split(" ") if item != ""] for line in lines]
    
    results = []
    
    for i in range(len(lines[0])):
        symbol = lines[-1][i]
        ret = 0

        for j in range(len(lines) - 1):
            number = int(lines[j][i])
            if j == 0:
                ret = number
            else:
                if symbol == "+":
                    ret += number
                elif symbol == "*":
                    ret *= number
        results.append(ret)   
    return sum(results)

        

from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Problem:
    numbers: List[int] = field(default_factory=list)
    symbol: Optional[str] = None

from math import prod

def parttwo():
    lines = tolines("input/day6")
    
    problems = [Problem()]
    for col in range(len(lines[0])):
        number = 0
        is_separator = True
        for row in range(len(lines)):
            char = lines[row][col]
            if char in "+*":
                problems[-1].symbol = char
            elif char.isdigit():
                number = number * 10 + int(char)
                is_separator = False
        
        if is_separator:
            problems.append(Problem())
        else:
            problems[-1].numbers.append(number)
    
    return sum(
        sum(p.numbers) if p.symbol == "+" else prod(p.numbers)
        for p in problems if p.numbers
    )
    
    

print(partone())
print(parttwo())
