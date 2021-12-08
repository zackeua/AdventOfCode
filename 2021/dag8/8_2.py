import sys

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [row[:-1] for row in data]
    data = [row.split(' | ') for row in data]
    nums = [elem[0].split(' ') for elem in data]
    output = [elem[1].split(' ') for elem in data]

total = 0

for i, row in enumerate(nums):
    # 1 = index of str of len 2
    # 4 = index of str of len 4
    # 7 = index of str of len 3
    # 8 = index of str of len 7

    # 3 = index of str of len 5 where both letters of 1 are included
    # 5 = index of str of len 5 where all letters are in 3 or 4
    # 2 = index of str of len 5 that is not 3 or 5
    # 9 = index of str of len 6 with 1 non matching letter to 3
    # 6 = index of str of len 6 where 1 has one non matching letter
    # 0 = index of str of len 6 if not 6 or 9

    index_of = [None] * 10
    for index, elem in enumerate(row):
        if len(elem) == 2: index_of[1] = index
        if len(elem) == 4: index_of[4] = index
        if len(elem) == 3: index_of[7] = index
        if len(elem) == 7: index_of[8] = index
    
    for index, elem in enumerate(row):
        if len(elem) == 5 and sum([1 for letter in elem if letter in row[index_of[1]]]) == 2: index_of[3] = index
    
    for index, elem in enumerate(row):
        if len(elem) == 5 and index != index_of[3]:
            if sum([1 for letter in elem if (letter in row[index_of[3]] or letter in row[index_of[4]])]) == 5:
                index_of[5] = index
    for index, elem in enumerate(row):
        if len(elem) == 5 and index not in [index_of[3], index_of[5]]: index_of[2] = index

    for index, elem in enumerate(row):
        if len(elem) == 6 and sum([1 for letter in elem if letter not in row[index_of[3]]]) == 1: index_of[9] = index

    for index, elem in enumerate(row):
        if len(elem) == 6 and sum([1 for letter in row[index_of[1]] if letter not in elem]) == 1: index_of[6] = index

    for index, elem in enumerate(row):
        if len(elem) == 6 and index not in [index_of[6], index_of[9]]: index_of[0] = index
    
    mapping = {}
    for index, val in enumerate(index_of):
        row[val] = [char for char in row[val]]
        row[val].sort()
        row[val] = ''.join(row[val])
        mapping[row[val]] = str(index)

    res = ''
    for elem in output[i]:
        elem = [char for char in elem]
        elem.sort()
        elem = ''.join(elem)
        res += mapping[elem]
    total += int(res)

print(total)
