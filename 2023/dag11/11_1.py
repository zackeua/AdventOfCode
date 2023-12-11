import sys


def expand_rows(grid):
    data = []

    for line in grid:
        data.append(line)
        if '#' not in line:
            data.append(line)
    return data

def flip_axes(grid):
    data = []

    for x in zip(*grid):
        data.append(''.join(x))
    return data

def expand_cols(grid):
    data = flip_axes(grid)
    data = expand_rows(data)
    return flip_axes(data)


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]

        
        data = expand_rows(data)
        data = expand_cols(data)

        #for line in data:
        #    print(line)
        #print()

        galaxies = []
        for i, line in enumerate(data):
            for j, elem in enumerate(line):
                if elem == '#':
                    galaxies.append((i, j))
        
        total = 0
        for i in range(len(galaxies)):
            for j in range(i+1, len(galaxies)):
                x_diff = abs(galaxies[i][0] - galaxies[j][0])
                y_diff = abs(galaxies[i][1] - galaxies[j][1])

                diff = x_diff + y_diff
                #print(f'{i+1}, {j+1}: {diff}')
                total += diff
                
        print(total)




if __name__ == '__main__':
    main()