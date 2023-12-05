from util import tolines
import re, sys


def partone():
    lines = tolines("input/day5")
    seeds = []
    table = {}
    source, destination = "", ""
    for idx, line in enumerate(lines):
        if idx == 0:
            numbers = re.findall(r"\d+", line)
            seeds = [int(number) for number in numbers]
        elif line.strip() == "":
            continue
        elif "map" in line:
            parts = line.split(" ")[0].split("-to-")
            source, destination = parts
        else:
            numbers = re.findall(r"\d+", line)
            numbers = [int(number) for number in numbers]
            dest_start, src_start, range_num = numbers
            if source not in table:
                table[source] = {}
                table[source][destination] = []
            table[source][destination].append([dest_start, src_start, range_num])

    ret = sys.maxsize
    for seed in seeds:
        start = "seed"
        next = list(table[start].keys())[0]
        value = seed
        while True:
            for dest_start, src_start, range_num in table[start][next]:
                if value >= src_start and value <= src_start + range_num:
                    value = dest_start + value - src_start
                    break
            value = value
            if next == "location":
                ret = min(ret, value)
                break
            start = next
            next = list(table[start].keys())[0]

    return ret


def segment(range1: list[int], range2: list[int]) -> list[int]:
    # given two range in the format of [start,end]
    # return overlapped segment between the two range
    start1, end1 = range1
    start2, end2 = range2
    if end1 < start2 or end2 < start1:
        return []
    elif start1 <= end2 <= end1:
        return [max(start2, start1), end2]
    elif start1 <= start2 <= end1:
        return [start2, min(end1, end2)]
    elif start2 <= start1 and end2 >= end1:
        return [start1, end1]
    else:
        print("something went wrong", range1, range2)
        exit("something went wrong")


def remaining_range(range1: list[int], range2: list[int]) -> list[list[int]]:
    # given two range, range2 is gauranteed to be an overlapped segment of range1
    # return the remaining range of range1 after removing range2

    start1, end1 = range1
    start2, end2 = range2
    if start1 <= start2 <= end1:
        if end2 < end1:
            return [[start1, start2], [end2, end1]]
        else:
            if start2 == start1:
                return []
            else:
                return [[start1, start2]]
    elif start1 <= end2 <= end1:
        if start2 > start1:
            return [[start1, start2], [end2, end1]]
        else:
            return [[end2, end1]]
    else:
        print("something went wrong ramining range", range1, range2)
        exit("something went wrong")


def parttwo():
    lines = tolines("input/day5")
    seeds = []
    table = {}
    source, destination = "", ""
    for idx, line in enumerate(lines):
        if idx == 0:
            numbers = re.findall(r"\d+", line)
            seeds = [int(number) for number in numbers]
        elif line.strip() == "":
            continue
        elif "map" in line:
            parts = line.split(" ")[0].split("-to-")
            source, destination = parts
        else:
            numbers = re.findall(r"\d+", line)
            numbers = [int(number) for number in numbers]
            dest_start, src_start, range_num = numbers
            if source not in table:
                table[source] = {}
                table[source][destination] = []
            table[source][destination].append([dest_start, src_start, range_num])

    ret = sys.maxsize
    for i in range(0, len(seeds), 2):
        pair = seeds[i : i + 2]
        value = [[pair[0], pair[1] + pair[0] - 1]]
        start = "seed"
        next = list(table[start].keys())[0]
        while True:
            ranges = table[start][next]
            not_overlapped = value
            overlappeds = []
            for dest_start, src_start, range_num in ranges:
                new_not_overlapped = []
                for i in range(len(not_overlapped)):
                    overlapped = segment(
                        not_overlapped[i], [src_start, src_start + range_num]
                    )
                    if len(overlapped) > 0:
                        remaining = remaining_range(not_overlapped[i], overlapped)
                        new_not_overlapped.extend(remaining)
                        overlapped[0] = dest_start + overlapped[0] - src_start
                        overlapped[1] = dest_start + overlapped[1] - src_start
                        overlappeds.append(overlapped)
                    else:
                        new_not_overlapped.append(not_overlapped[i])
                not_overlapped = new_not_overlapped
            overlappeds.extend(not_overlapped)
            value = overlappeds
            if next == "location":
                break
            start = next
            next = list(table[start].keys())[0]
        value.sort()
        ret = min(ret, value[0][0])

    return ret


print("part one:", partone())
print("part two:", parttwo())
