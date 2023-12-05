import hashlib
from collections import Counter


def same(s, length):
    ret = []
    for i in range(len(s) - length + 1):
        if len(Counter(s[i : i + length]).keys()) == 1:
            ret.append(s[i : i + length])
    return ret


def md5_str(s):
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def findrepeat():
    memo = {}

    def f(s, length):
        if s in memo and length in memo[s]:
            return memo[s][length]
        else:
            result = same(s, length)
            if s not in memo:
                memo[s] = {}
            memo[s][length] = result
            return result

    return f


def partone():
    salt = "qzyelonm"
    keys = []
    ptr = 0
    find_repeat_memo = findrepeat()
    while True:
        s = md5_str(salt + str(ptr))
        threepeats = find_repeat_memo(s, 3)
        if len(threepeats) == 0:
            ptr += 1
            continue
        threepeat = threepeats[0]

        for i in range(ptr + 1, ptr + 1002):
            query = threepeat[0] * 5
            ss = md5_str(salt + str(i))
            if query in find_repeat_memo(ss, 5):
                keys.append(ptr)
                break
        if len(keys) == 64:
            break

        ptr += 1
    return keys[-1]


def superhash():
    memo = {}

    def superhash(s):
        if s in memo:
            return memo[s]
        hash = md5_str(s)
        for i in range(2016):
            hash = md5_str(hash)
        memo[s] = hash
        return hash

    return superhash


def parttwo():
    salt = "qzyelonm"
    keys = []
    ptr = 0
    find_repeat_memo = findrepeat()
    super_hash_memo = superhash()
    while True:
        s = super_hash_memo(salt + str(ptr))
        threepeats = find_repeat_memo(s, 3)
        if len(threepeats) == 0:
            ptr += 1
            continue
        threepeat = threepeats[0]

        for i in range(ptr + 1, ptr + 1002):
            query = threepeat[0] * 5
            ss = super_hash_memo(salt + str(i))
            if query in find_repeat_memo(ss, 5):
                keys.append(ptr)
                break
        if len(keys) == 64:
            break

        ptr += 1
    return keys[-1]


print("partone", partone())
print("parttwo", parttwo())
