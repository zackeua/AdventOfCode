import sys
import ast
from math import floor, ceil

def magnitude(number):
    result = [0, 0]
    if type(number[0]) == int:
        result[0] = number[0]
    else:
        result[0] = magnitude(number[0])
    
    if type(number[1]) == int:
        result[1] = number[1]
    else:
        result[1] = magnitude(number[1])

    return 3 * result[0] + 2 * result[1]

def reduce_number(number):
    op = True
    while(op):
        number, op, _, _ = explode_number(number)
        if not op:
            number, op = split_number(number)
    return number

def explode_add_l(number, val):
    if type(number) == int:
        return number + val, 0
    else:
        temp_num, val = explode_add_l(number[1], val)
        if val == 0:
            number = [number[0], temp_num]
        else:
            temp_num, val = explode_add_l(number[0], val)
            if val == 0:
                number = [temp_num, number[1]]
        return number, val

def explode_add_r(number, val):
    if type(number) == int:
        return number + val, 0
    else:
        temp_num, val = explode_add_r(number[0], val)
        if val == 0:
            number = [temp_num, number[1]]
        else:
            temp_num, val = explode_add_r(number[1], val)
            if val == 0:
                number = [number[0], temp_num]
        return number, val

def explode_number(number, depth = 0):
    if type(number) == list:
        if depth == 4:
            return 0, True, number[0], number[1]
        else:
            temp_num, explode, add_l, add_r = explode_number(number[0], depth+1)
            if explode:
                number[1], add_r = explode_add_r(number[1], add_r)
                number = [temp_num, number[1]]
            else:
                temp_num, explode, add_l, add_r = explode_number(number[1], depth+1)
                if explode:
                    number[0], add_l = explode_add_l(number[0], add_l)
                    number = [number[0], temp_num]
            return number, explode, add_l, add_r
    else:
        return number, False, 0, 0

def split_number(number):
    #print(number)
    if type(number) == int:
        if number > 9:
            number = [floor(number/2), ceil(number/2)]
            return number, True
        else:
            return number, False
    else:
        temp_num, split = split_number(number[0])
        if split:
            number = [temp_num, number[1]]
        else:
            temp_num, split = split_number(number[1])
            if split:
                number = [number[0], temp_num]
    return number, split

def add(a, b):
    if a == None: return b
    result = [a, b]
    result = reduce_number(result)
    return result


with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [ast.literal_eval(elem) for elem in data]
res = None
for row in data:
    res = add(res, row)
    #print(explode_number(row))
    #print(magnitude(row))
print(magnitude(res))