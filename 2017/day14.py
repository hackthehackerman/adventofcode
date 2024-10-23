from util import toString
from collections import Counter

def get_knot_hash(s):
    lengths = [ord(c) for c in s]
    lengths += [17, 31, 73, 47, 23]
    nums = [i for i in range(256)]
    
    cur_position = 0
    skip_size = 0
    for i in range(64):
        for length in lengths:
            ptrl = cur_position
            ptrr = cur_position + length
            
            if ptrr >= len(nums):
                # wrap around
                sub_list = nums[ptrl:] + nums[:ptrr - len(nums)]
                sub_list = list(reversed(sub_list))
                nums = sub_list[(len(nums) - ptrl):] + nums[ptrr - len(nums):ptrl] + sub_list[:(len(nums) - ptrl)]
                
            else:
                sub_list = nums[ptrl:ptrr]
                sub_list = list(reversed(sub_list))
                nums = nums[:ptrl] + sub_list + nums[ptrr:]

            cur_position = (cur_position + length + skip_size) % len(nums)
            skip_size += 1
    
    dense_hash = []
    for i in range(0, 256, 16):
        block = nums[i:i+16]
        xor_result = 0
        for num in block:
            xor_result ^= num
        dense_hash.append(xor_result)
            
    hex_string = ''.join([format(num, '02x') for num in dense_hash])
    return hex_string

def hex_to_bin(hex_char):
    # Convert a single hex character to 4 binary digits
    return format(int(hex_char, 16), '04b')

def part1():
    s = toString("input/day14")
    
    ret = 0
    for i in range(128):
        row = f"{s}-{i}"
        
        hash = get_knot_hash(row)
        
        row_str = "".join([bin(int(char, 16))[2:].zfill(4) for char in hash])
        c = Counter(row_str)
        ret += c["1"]
    print(ret)
    
def part2():
    s = toString("input/day14")
    
    m = []
    c = Counter()
    for i in range(128):
        row = f"{s}-{i}"
        
        hash = get_knot_hash(row)
        
        row_str = "".join([bin(int(char, 16))[2:].zfill(4) for char in hash])
        row_sign = ["#" if c == "1" else "." for c in row_str ]
        c.update(row_sign)
        m.append(row_sign)
    
    def traverse(m, i, j, idx):
        if i < 0 or i >= len(m):
            return
        if j < 0 or j >= len(m[0]):
            return
        if m[i][j] == "#":
            m[i][j] = idx
            traverse(m, i-1, j, idx)
            traverse(m, i+1, j, idx)
            traverse(m, i, j-1, idx)
            traverse(m, i, j+1, idx)
        
    
    idx = 1
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == "#":
                traverse(m,i,j,idx)
                idx += 1
    print(idx-1)
                
                
    
        
part1()
part2()
        