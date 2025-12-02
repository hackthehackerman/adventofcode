from itertools import cycle
from util import toString
from collections import defaultdict


def dance(line, moves):
    for m in moves:
        if m.startswith("s"):
            dist = int(m[1:]) % len(line)
            line = line[-dist:] + line[:len(line)-dist]
        elif m.startswith("x"):
            pos_1, pos_2 = m[1:].split("/")
            pos_1, pos_2 = int(pos_1), int(pos_2)
            
            tmp = line[pos_1]
            line[pos_1] = line[pos_2]
            line[pos_2] = tmp
        else:
            letter_1, letter_2 = m[1:].split("/")
            idx_1, idx_2 = line.index(letter_1), line.index(letter_2)
            line[idx_1] = letter_2
            line[idx_2] = letter_1
    return line


def part1():
    s = toString("input/day16")
    moves = s.split(",")
    
    num_program = 16
    line = [chr(ord('a')+ i) for i in range(num_program)]
    line = dance(line,moves)
            
    print("".join(line))    
    
def part2():
    s = toString("input/day16")
    moves = s.split(",")
    
    num_program = 16
    line = [chr(ord('a')+ i) for i in range(num_program)]
    mapping = {}
    cycle_length = 0
    step = 0
    while step < 1000000000:
        print(step)
        if cycle_length == 0:
            line = dance(line,moves)
            s = "".join(line)
            step += 1
            if s in mapping:
                print("yoo", step, cycle_length, mapping[s])
                cycle_length = step - mapping[s]
                step += (cycle_length * (((1000000000 - mapping[s]) // cycle_length)-1) -1)
                print("yoo after", step, cycle_length)

                continue
            mapping[s] = step
        else:
            line = dance(line,moves)
            step += 1                    
    print("".join(line)) 
    
"""

after step1: abc
step2: bbb
step3: abc ---> cycle_length = 
step4 : bbb
step5: abc


"""

part1()
part2()
