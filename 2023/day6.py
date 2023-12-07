from util import tolines
import re


def partone():
    lines = tolines("input/day6")
    time = re.findall(r'\d+',lines[0])
    distance = re.findall(r'\d+',lines[1])
    time = [int(x) for x in time]
    distance = [int(x) for x in distance]
    
    ret = 1
    for i in range(len(time)):
        t = time[i]
        d = distance[i]
        ways = 0
        for j in range(t + 1):
            speed = j
            new_distance = speed * (t-j)
            if new_distance > d:
                ways += 1
        ret *= ways
    return ret

def parttwo():
    lines = tolines("input/day6")
    time = re.findall(r'\d+',lines[0])
    distance = re.findall(r'\d+',lines[1])
    time = int("".join(time))
    distance = int("".join(distance))
        
    ways = 0
    for i in range(time):
        speed = i
        new_distance = speed * (time-i)
        if new_distance > distance:
            ways += 1
        
    return ways
                
            
    
    
print("partone", partone())
print("parttwo", parttwo())