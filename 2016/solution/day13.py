from collections import Counter


def value(x, y, fnum):
    num = x * x + 3 * x + 2 * x * y + y + y * y + fnum
    binary = bin(num)
    open = Counter(binary)["1"] % 2 == 0
    return 0 if open else 1


def partone():
    fnum = 1362
    destination = [31, 39]
    visited = set()
    queue = [tuple([1, 1])]
    step = 0
    # bfs
    while True:
        step += 1
        newQueue = []
        for x, y in queue:
            for xx in [x - 1, x, x + 1]:
                for yy in [y - 1, y, y + 1]:
                    if abs(x - xx) + abs(y - yy) == 2:
                        continue
                    if xx == x and yy == y:
                        continue
                    if xx < 0 or yy < 0:
                        continue
                    if tuple([xx, yy]) in visited:
                        continue
                    if value(xx, yy, fnum) == 1:
                        visited.add(tuple([xx, yy]))
                        continue
                    if [xx, yy] == destination:
                        return step
                    visited.add(tuple([xx, yy]))
                    newQueue.append(tuple([xx, yy]))
        queue = newQueue
    return -1


def parttwo():
    fnum = 1362
    destination = [31, 39]
    visited = set([tuple([1, 1])])
    queue = [tuple([1, 1])]
    # bfs
    for i in range(50):
        newQueue = []
        for x, y in queue:
            for xx in [x - 1, x, x + 1]:
                for yy in [y - 1, y, y + 1]:
                    if abs(x - xx) + abs(y - yy) == 2:
                        continue
                    if xx == x and yy == y:
                        continue
                    if xx < 0 or yy < 0:
                        continue
                    if tuple([xx, yy]) in visited:
                        continue
                    if value(xx, yy, fnum) == 1:
                        continue
                    visited.add(tuple([xx, yy]))
                    newQueue.append(tuple([xx, yy]))
        queue = newQueue
    return len(visited)


print("part one", partone())
print("part two", parttwo())
