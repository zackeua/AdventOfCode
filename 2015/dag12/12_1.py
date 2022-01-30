import sys
import json

def sum_list(l: list) -> int:
    result = 0
    for i in l:
        if type(i) == int:
            result += i
        elif type(i) == list:
            result += sum_list(i)
        elif type(i) == dict:
            result += sum_dict(i)
    return result

def sum_dict(d: dict) -> int:
    result = 0
    for i in d:
        if type(d[i]) == int:
            result += d[i]
        elif type(d[i]) == list:
            result += sum_list(d[i])
        elif type(d[i]) == dict:
            result += sum_dict(d[i])
    return result


with open(sys.argv[1], 'r') as f:
    data = json.load(f)

print(sum_list(data))
    