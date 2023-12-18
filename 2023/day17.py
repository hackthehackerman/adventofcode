from util import toMatrix
import sys
import heapq


def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def inbound(m, x, y):
    return 0 <= x < len(m) and 0 <=y<len(m[0])

def partone():
    m = toMatrix("input/day17")
    m = [[int(j) for j in row] for row in m]
    up, down, left, right = (-1,0), (1,0), (0,-1), (0,1)
    next = {
        up: [up, left, right],
        down: [down, left, right],
        left: [left, up, down],
        right: [right, up, down]
    }
    ret = sys.maxsize
    visited = {
    }
    queue = []
    heapq.heappush(queue, ( 0, (0,0), ()))
    while len(queue) > 0:
        loss, coord, direction_history = heapq.heappop(queue)
        if (coord, direction_history) in visited:
            continue
        else:
            visited[(coord, direction_history)] = loss
        if coord == (len(m)-1, len(m[0])-1):
            ret = min(ret, loss)
            break
        nextDirections = [up, down, left, right] if len(direction_history)== 0 else next[direction_history[-1]]
        for nextDirection in nextDirections:
            newDirectionHistory = list(direction_history)[-3:] + [nextDirection]
            if len(newDirectionHistory) >= 4 and len(set(newDirectionHistory)) == 1:
                continue
            newCoord = add(coord, nextDirection)
            if not inbound(m, *newCoord):
                continue
            newLoss = loss+m[newCoord[0]][newCoord[1]]
            heapq.heappush(queue, (newLoss, newCoord, tuple(newDirectionHistory[-3:])))
        
    return ret

def parttwo():
    m = toMatrix("input/day17")
    m = [[int(j) for j in row] for row in m]
    up, down, left, right = (-1,0), (1,0), (0,-1), (0,1)
    next = {
        up: [up, left, right],
        down: [down, left, right],
        left: [left, up, down],
        right: [right, up, down]
    }
    # def validPath(directions):
    #     if len(directions) == 0:
    #         return True
    #     lastDirection, count = directions[0], 1
    #     for i in range(1, len(directions)):
    #         if directions[i] == lastDirection:
    #             count +=1
    #             if count > 10:
    #                 return False
    #         elif count < 4:
    #             return False
    #         elif directions[i] not in next[lastDirection]:
    #             return False
    #         else:
    #             lastDirection = directions[i]
    #             count = 1
    #     return True
    
    def countConsecutiveLastElement(directions):
        if len(directions) == 0:
            return 0
        ret = 0
        last = directions[-1]
        for i in range(len(directions)):
            if directions[len(directions) - i -1] == last:
                ret +=1
            else:
                break
        return ret
    
    
    ret = sys.maxsize
    visited = {
    }
    queue = []
    heapq.heappush(queue, (0, (0,0), ()))
    while len(queue) > 0:
        loss, coord, direction_history = heapq.heappop(queue)
        if (coord, direction_history) in visited:
            continue
        else:
            visited[(coord, direction_history)] = loss
            
        if coord == (len(m)-1, len(m[0])-1) and len(set(direction_history[-4:]))==1:
            ret = min(ret, loss)
            break
            
        nextDirections = [up, down, left, right] if len(direction_history)== 0 else next[direction_history[-1]]
        for nextDirection in nextDirections:
            newDirectionHistory = list(direction_history) + [nextDirection]
            if countConsecutiveLastElement(newDirectionHistory) > 10:
                continue
            if 1 <= countConsecutiveLastElement(list(direction_history)) <= 3 and nextDirection != direction_history[-1]:
                continue
            
  
            newCoord = add(coord, nextDirection)
            if not inbound(m, *newCoord):
                continue
            newLoss = loss+m[newCoord[0]][newCoord[1]]
            heapq.heappush(queue, (newLoss, newCoord, tuple(newDirectionHistory[-10:])))
    return ret
          
print(partone())
print(parttwo())