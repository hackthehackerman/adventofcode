from util import md5_str


def partone():
    point = tuple([0, 0])
    initial_code = "vkjiggvb"
    queue = [tuple([initial_code, 0, 0])]
    while len(queue) > 0:
        new_queue = []
        for state in queue:
            passcode, x, y = state
            if [x, y] == [3, 3]:
                return passcode[len(initial_code) :]
            hash = md5_str(passcode)[:4]
            hash = [c in ["b", "c", "d", "e", "f"] for c in hash]
            if hash[0] and y - 1 >= 0:
                new_queue.append(tuple([passcode + "U", x, y - 1]))
            if hash[1] and y + 1 <= 3:
                new_queue.append(tuple([passcode + "D", x, y + 1]))
            if hash[2] and x - 1 >= 0:
                new_queue.append(tuple([passcode + "L", x - 1, y]))
            if hash[3] and x + 1 <= 3:
                new_queue.append(tuple([passcode + "R", x + 1, y]))
        queue = new_queue

    return -1


def parttwo():
    point = tuple([0, 0])
    initial_code = "vkjiggvb"
    queue = [tuple([initial_code, 0, 0])]
    passcode_length = 0
    while len(queue) > 0:
        new_queue = []
        for state in queue:
            passcode, x, y = state
            if [x, y] == [3, 3]:
                passcode_length = max(
                    passcode_length, len(passcode) - len(initial_code)
                )
                continue
            hash = md5_str(passcode)[:4]
            hash = [c in ["b", "c", "d", "e", "f"] for c in hash]
            if hash[0] and y - 1 >= 0:
                new_queue.append(tuple([passcode + "U", x, y - 1]))
            if hash[1] and y + 1 <= 3:
                new_queue.append(tuple([passcode + "D", x, y + 1]))
            if hash[2] and x - 1 >= 0:
                new_queue.append(tuple([passcode + "L", x - 1, y]))
            if hash[3] and x + 1 <= 3:
                new_queue.append(tuple([passcode + "R", x + 1, y]))
        queue = new_queue

    return passcode_length


print("partone", partone())
print("parttwo", parttwo())
