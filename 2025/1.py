from util import tolines

def partone():
    lines = tolines("input/day1")
    cur = 50 
    cnt = 0

    for line in lines:
        lr = line[0]
        dist = int(line[1:])
        
        if lr == "L":
            cur -= dist
        else:
            cur += dist
        
        while cur < 0 or cur > 99:
            if cur < 0:
                cur += 100
            elif cur > 99:
                cur -= 100
        # print(cur)
        if cur == 0:
            cnt += 1
    return cnt

def parttwo():
    lines = tolines("input/day1")
    cur = 50 
    cnt = 0

    for line in lines:
        lr = line[0]
        dist = int(line[1:])
        click = 0
            
        while dist > 0:
            if lr == "L":
                # L
                if cur > 0 :
                    dist_to_rotate = min(cur, dist)
                    dist -= dist_to_rotate
                    cur -= dist_to_rotate
                    if cur == 0:
                        click += 1
                else:
                    # cur == 0
                    dist_to_rotate = min(100, dist)
                    dist -= dist_to_rotate
                    cur = cur - dist_to_rotate + 100
                    if cur == 0:
                        click += 1
            else:
                # R
                if cur > 0 :
                    dist_to_rotate = min(100 - cur, dist)
                    dist -= dist_to_rotate
                    cur += dist_to_rotate
                    if cur == 100:
                        click += 1
                        cur = 0
                else:
                    # cur == 0
                    dist_to_rotate = min(100, dist)
                    dist -= dist_to_rotate
                    cur += dist_to_rotate
                    if cur == 100:
                        click += 1
                        cur = 0
        cnt += click

        
        
        
    return cnt

print(partone())
print(parttwo())