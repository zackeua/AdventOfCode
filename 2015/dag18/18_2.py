import sys

def disp(inp):
    for row in inp:
        for elem in row:
            print('#' if elem else '.', end='')
        print()
    print()

def calc_next(inp, out):
    SIZE = 99

    inp[0][0] = True
    inp[0][SIZE] = True
    inp[SIZE][0] = True
    inp[SIZE][SIZE] = True

    for i in range(1, SIZE):
        for j in range(1, SIZE):
            count = 0
            count += inp[i-1][j-1]
            count += inp[i-1][j]
            count += inp[i-1][j+1]
            count += inp[i][j-1]
            count += inp[i][j+1]
            count += inp[i+1][j-1]
            count += inp[i+1][j]
            count += inp[i+1][j+1]
            if inp[i][j]:
                out[i][j] = count in [2, 3]
            else:
                out[i][j] = count == 3
    for i in range(1, SIZE):
        count1 = 0
        count1 += inp[0][i-1]
        count1 += inp[0][i+1]
        count1 += inp[1][i-1]
        count1 += inp[1][i]
        count1 += inp[1][i+1]

        if inp[0][i]:
            out[0][i] = count1 in [2, 3]
        else:
            out[0][i] = count1 == 3
        
        count2 = 0
        count2 += inp[SIZE-1][i-1]
        count2 += inp[SIZE-1][i]
        count2 += inp[SIZE-1][i+1]
        count2 += inp[SIZE][i-1]
        count2 += inp[SIZE][i+1]
        
        if inp[SIZE][i]:
            out[SIZE][i] = count2 in [2, 3]
        else:
            out[SIZE][i] = count2 == 3

        count3 = 0
        count3 += inp[i-1][0]
        count3 += inp[i+1][0]
        count3 += inp[i-1][1]
        count3 += inp[i][1]
        count3 += inp[i+1][1]

        if inp[i][0]:
            out[i][0] = count3 in [2, 3]
        else:
            out[i][0] = count3 == 3


        count4 = 0
        count4 += inp[i-1][SIZE-1]
        count4 += inp[i][SIZE-1]
        count4 += inp[i+1][SIZE-1]
        count4 += inp[i-1][SIZE]
        count4 += inp[i+1][SIZE]

        if inp[i][SIZE]:
            out[i][SIZE] = count4 in [2, 3]
        else:
            out[i][SIZE] = count4 == 3

    out[0][0] = True
    out[0][SIZE] = True
    out[SIZE][0] = True
    out[SIZE][SIZE] = True

def step(data0, data1):
    i = 0
    steps = 100
    #disp(data0)
    while i < steps:
        calc_next(data0, data1)
        i += 1
        #disp(data1)
        if i < steps:
            calc_next(data1, data0)
            i += 1
            #disp(data0)
        else:
            return data1
        
    return data0

with open(sys.argv[1], 'r') as f:
    data0 = f.readlines()
    data0 = [row.replace('\n', '') for row in data0]
    data0 = [[elem=='#' for elem in row] for row in data0]

data1 = [[0 for _ in row] for row in data0]

result = step(data0, data1)
#disp(result)
print(sum([sum(line) for line in result]))