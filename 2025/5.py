from util import tolines

def partone():
    lines = tolines("input/day5")
    ranges = []
    ingredients = []
    
    for line in lines:
        if len(line) == 0:
            continue
        if "-" in line:
            parts = line.split("-")
            parts = [int(p) for p in parts]
            ranges.append(parts)
        else:
            ingredients.append(int(line))
            
    def isFresh(ranges, ingredient):
        for range in ranges:
            left,right = range
            if ingredient >= left and ingredient <= right:
                return True
        return False
    
    ret = 0
    for ingredient in ingredients:
        if isFresh(ranges, ingredient):
            ret += 1
        
   
    return ret


class Node:
    def __init__(self, prev, next, left, right):
        self.prev = prev
        self.next = next
        self.left = left
        self.right = right
    
        
            
def parttwo():
    lines = tolines("input/day5")
    ranges = []
    
    for line in lines:
        if len(line) == 0:
            break
        parts = line.split("-")
        parts = [int(p) for p in parts]
        ranges.append(parts) 

    def overlap(left1, right1, left2, right2):
        overlap_left = max(left1, left2)
        overlap_right = min(right1, right2)
        if overlap_left > overlap_right:
            return None, None
        return overlap_left, overlap_right

    placed = []

    for left, right in ranges:
        new_segments = [[left, right]]
        next_placed = []
        for seg_left, seg_right in new_segments:
            temp_segments = [[seg_left, seg_right]]
            for old_left, old_right in placed:
                i = 0
                while i < len(temp_segments):
                    nl, nr = temp_segments[i]
                    ov_left, ov_right = overlap(nl, nr, old_left, old_right)
                    if ov_left is None:
                        i += 1
                        continue
                    new_parts = []
                    if nl < ov_left:
                        new_parts.append([nl, ov_left - 1])
                    if ov_right < nr:
                        new_parts.append([ov_right + 1, nr])
                    temp_segments.pop(i)
                    for part in new_parts:
                        temp_segments.insert(i, part)
                        i += 1
            next_placed.extend(temp_segments)
        placed.extend(next_placed)

    total = 0
    for left, right in placed:
        total += right - left + 1

    return total
            
    
    

print(partone())
print(parttwo())
