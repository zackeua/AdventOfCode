import sys
from typing import List

def merge_lists(l1: List[int], l2: List[int]):
    new_list = [0]*max([len(l1), len(l2)])
    for i, _ in enumerate(new_list):
        if i < len(l1): new_list[i] += l1[i]
        if i < len(l2): new_list[i] += l2[i]
    return new_list


def get_count(l: list, index: int, total: int, depth: int):
    if total > 150:
        return [0]
    if total == 150:
        result = [0] * (depth + 1)
        result[depth] = 1
        return result
    if index == len(l):
        return [0]

    temp = [0]
    temp = merge_lists(temp, get_count(l, index+1, total + l[index], depth + 1))
    temp = merge_lists(temp, get_count(l, index+1, total, depth))
    return temp

with open(sys.argv[1], 'r') as f:
    data = list(map(int, f.readlines()))

print(data)
result = get_count(data, 0, 0, 0)
for i in result:
    if i != 0:
        print(i)
        break