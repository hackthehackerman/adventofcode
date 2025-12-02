def part1(a,b):
    ret = 0
    for i in range(40000000):
        
        a = a * 16807 % 2147483647
        b = b * 48271 % 2147483647
        bi_a = bin(a)[2:][-16:]
        bi_b = bin(b)[2:][-16:]
        if bi_a == bi_b:
            ret += 1

    print(ret)
    
def part2(a,b):
    ret = 0
    for i in range(5000000):
        a = a * 16807 % 2147483647
        while a % 4 != 0:
            a = a * 16807 % 2147483647
        
        b = b * 48271 % 2147483647
        while b % 8 != 0:
            b = b * 48271 % 2147483647
            
        bi_a = bin(a)[2:][-16:]
        bi_b = bin(b)[2:][-16:]
        if bi_a == bi_b:
            ret += 1

    print(ret)

part1(618,814)
part2(618,814)