from util import tolines
from collections import defaultdict

def part1():
    lines = tolines("input/day8")
    instructions = []
    regs = defaultdict(int)
    for line in lines:
        reg, op, val, _, reg2, comp, val2 = line.split()
        instructions.append([reg,op,val, reg2, comp, val2])
        
    def isTrue(reg, comp, val):
        val = int(val)
        if comp == ">":
            if regs[reg] > val:
                return True
        elif comp == ">=":
            if regs[reg] >= val:
                return True
        elif comp == "<":
            if regs[reg] < val:
                return True
        elif comp == "<=":
            if regs[reg] <= val:
                return True
        elif comp == "==":
            if regs[reg] == val:
                return True
        elif comp == "!=":
            if regs[reg] != val:
                return True
        else:
            print("wrong comparator:", comp)
            exit(1)
        return False
        
    for reg,op,val, reg2, comp, val2 in instructions:
        if isTrue(reg2, comp, val2):
            if op == "inc":
                regs[reg] += int(val)
            else:
                regs[reg] -= int(val)
                
    max_key = max(regs, key=regs.get)
    print(regs[max_key])

def part2():
    lines = tolines("input/day8")
    instructions = []
    regs = defaultdict(int)
    for line in lines:
        reg, op, val, _, reg2, comp, val2 = line.split()
        instructions.append([reg,op,val, reg2, comp, val2])
        
    def isTrue(reg, comp, val):
        val = int(val)
        if comp == ">":
            if regs[reg] > val:
                return True
        elif comp == ">=":
            if regs[reg] >= val:
                return True
        elif comp == "<":
            if regs[reg] < val:
                return True
        elif comp == "<=":
            if regs[reg] <= val:
                return True
        elif comp == "==":
            if regs[reg] == val:
                return True
        elif comp == "!=":
            if regs[reg] != val:
                return True
        else:
            print("wrong comparator:", comp)
            exit(1)
        return False
        
    max_val = 0
    for reg,op,val, reg2, comp, val2 in instructions:
        if isTrue(reg2, comp, val2):
            if op == "inc":
                regs[reg] += int(val)
            else:
                regs[reg] -= int(val)
        max_key = max(regs, key=regs.get)
        max_val = max(max_val, regs[max_key])
    print(max_val)
                

    
    
part1()
part2()