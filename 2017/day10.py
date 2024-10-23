from util import toString

def part1():
    s = toString("input/day10")
    lengths = [int(c) for c in s.split(",")]
    
    nums = [i for i in range(256)]
    
    cur_position = 0
    skip_size = 0
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
            
        new_position = cur_position + length + skip_size
        if new_position >= len(nums):
            new_position  -= len(nums)
        cur_position = new_position
        skip_size += 1
    print(nums[0] * nums[1])

def part2():
    s = toString("input/day10")
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
    print(hex_string)

part1()
part2()
