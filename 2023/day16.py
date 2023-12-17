from util import toMatrix

def inbound(m, x, y):
    return 0 <= x < len(m) and 0 <=y<len(m[0])

def partone():
    m = toMatrix("input/day16")
    visited = {}
    up, down, left, right = (-1,0), (1,0), (0,-1), (0,1)
    reaction = {
        "|": {
            left: [up, down],
            right: [up,down]
        },
        "-": {
            up: [left, right],
            down: [left, right]
        },
        "/": {
            right: [up],
            left: [down],
            up: [right],
            down: [left]
        },
        "\\": {
            right: [down],
            left: [up],
            up: [left],
            down: [right]
        }
    }
    beams  = [[(0,0-1), right]]
    while len(beams) > 0:
        coord, direction = beams.pop()
        if (coord,direction) in visited:
            continue
        visited[(coord,direction)] = True
        coord_next = (coord[0] + direction[0], coord[1] + direction[1])
        cnx, cny = coord_next
        if not inbound(m, cnx, cny):
            continue
        if m[cnx][cny] == ".":
            beams.append((coord_next, direction))
        else:
            if direction in reaction[m[cnx][cny]]:
                for new_direction in reaction[m[cnx][cny]][direction]:
                    beams.append((coord_next, new_direction))
            else:
                beams.append((coord_next, direction))
    return len(list(set([coord for coord, _ in visited.keys()]))) -1


def parttwo():
    m = toMatrix("input/day16")
    up, down, left, right = (-1,0), (1,0), (0,-1), (0,1)
    def charged(init_coord, init_direction):
        visited = {}
        reaction = {
            "|": {
                left: [up, down],
                right: [up,down]
            },
            "-": {
                up: [left, right],
                down: [left, right]
            },
            "/": {
                right: [up],
                left: [down],
                up: [right],
                down: [left]
            },
            "\\": {
                right: [down],
                left: [up],
                up: [left],
                down: [right]
            }
        }
        beams  = [[init_coord, init_direction]]
        while len(beams) > 0:
            coord, direction = beams.pop()
            if (coord,direction) in visited:
                continue
            visited[(coord,direction)] = True
            coord_next = (coord[0] + direction[0], coord[1] + direction[1])
            cnx, cny = coord_next
            if not inbound(m, cnx, cny):
                continue
            if m[cnx][cny] == ".":
                beams.append((coord_next, direction))
            else:
                if direction in reaction[m[cnx][cny]]:
                    for new_direction in reaction[m[cnx][cny]][direction]:
                        beams.append((coord_next, new_direction))
                else:
                    beams.append((coord_next, direction))
        return len(list(set([coord for coord, _ in visited.keys()]))) -1
    
    ret = 0
    for j in range(len(m[0])):
        ret = max(ret, charged((-1,j),down))
        ret = max(ret, charged((len(m),j),up))
    
    for i in range(len(m)):
        ret = max(ret, charged((i,-1),right))
        ret = max(ret, charged((i, len(m[0])),left))
    return ret
    
            
print(partone())
print(parttwo())
       