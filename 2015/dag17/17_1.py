import sys

def get_count(l: list, index: int, total: int):
    if total > 150:
        return 0
    if total == 150:
        return 1
    if index == len(l):
        return 0

    temp = 0
    temp += get_count(l, index+1, total + l[index])
    temp += get_count(l, index+1, total)
    return temp



with open(sys.argv[1], 'r') as f:
    data = list(map(int, f.readlines()))

print(data)
print(get_count(data, 0, 0))
