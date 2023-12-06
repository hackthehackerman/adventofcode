def partone():
    state = "01111001100111011"
    target_length = 272

    while len(state) < target_length:
        copy = state[::-1]
        copy = ["1" if c == "0" else "0" for c in copy]
        state = state + "0" + "".join(copy)
        state = state[:target_length]

    checksum = state
    started = False
    while len(checksum) % 2 == 0 or not started:
        started = True
        checksum = "".join(
            [
                "1" if checksum[i] == checksum[i + 1] else "0"
                for i in range(0, len(checksum), 2)
            ]
        )
    return checksum


def parttwo():
    state = "01111001100111011"
    target_length = 35651584

    while len(state) < target_length:
        copy = state[::-1]
        copy = ["1" if c == "0" else "0" for c in copy]
        state = state + "0" + "".join(copy)
        state = state[:target_length]

    checksum = state
    started = False
    while len(checksum) % 2 == 0 or not started:
        started = True
        checksum = "".join(
            [
                "1" if checksum[i] == checksum[i + 1] else "0"
                for i in range(0, len(checksum), 2)
            ]
        )
    return checksum


print("partone", partone())
print("parttwo", parttwo())
