def part1():
    n = 277678
    i = 1
    layer = 1
    while i * i < n:
        i += 2
        layer += 1
    # calculate the four corner of the layer
    c1, c2, c3, c4 = i*i, i*i - (i-1), i*i - 2*(i-1), i*i - 3*(i-1)
    # calculate the four center of the layer
    c1, c2, c3, c4 = i*i - (i//2), i*i - (i//2) - (i-1), i*i - (i//2) - 2*(i-1), i*i - (i//2) - 3*(i-1)
    
    min_dist = min(abs(n-c1), abs(n-c2), abs(n-c3), abs(n-c4))
    print(min_dist + layer - 1)
    
    
def part2():
    n = 277678
    m = [[0 for _ in range(100)] for _ in range(100)]
    x, y = 50, 50
    m[x][y] = 1
    i = 1
    layer = 1
    step = 1
    x += 1
    step += 1
    while True:
        i += 2
        layer += 1
        # calculate the four corner of the layer
        c1, c2, c3, c4 = i*i, i*i - (i-1), i*i - 2*(i-1), i*i - 3*(i-1)
        # x += 1
        # step += 1
        while step <= c1:
            m[x][y] = m[x-1][y-1] + m[x-1][y] + m[x-1][y+1] + m[x][y-1] + m[x][y+1] + m[x+1][y-1] + m[x+1][y] + m[x+1][y+1]
            if m[x][y] > n:
                print(m[x][y])
                exit()
            if step < c4:
                y += 1
            elif step < c3:
                x -= 1
            elif step < c2:
                y -= 1
            else:
                x += 1
            step += 1

part1()
part2()