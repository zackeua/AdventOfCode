import sys


def expand_rows(grid, galaxies, factor):
    new_galaxies = {key: val for key, val in galaxies.items()}

    for i, line in enumerate(grid):
        if '#' not in line:
            for key in galaxies.keys():
                if galaxies[key][0] >= i:
                    new_galaxies[key] = (new_galaxies[key][0]+(factor-1), new_galaxies[key][1])
    return new_galaxies

def flip_axes(grid, galaxies):
    data = []
    
    new_galaxies = {key: (val[1], val[0]) for key, val in galaxies.items()}


    for x in zip(*grid):
        data.append(''.join(x))
    
    return data, new_galaxies

def expand_cols(grid, galaxies, factor):
    data, new_galaxies = flip_axes(grid, galaxies)
    new_galaxies = expand_rows(data, new_galaxies, factor)
    data, new_galaxies = flip_axes(data, new_galaxies)
    return new_galaxies

def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]

        galaxies = {}

        num_galaxies = 0
        for i, line in enumerate(data):
            for j, elem in enumerate(line):
                if elem == '#':
                    galaxies[num_galaxies] = (i, j)
                    num_galaxies += 1

        expansion_factor = 1000000
        new_galaxies = expand_rows(data, galaxies, expansion_factor)
        new_galaxies = expand_cols(data, new_galaxies, expansion_factor)


        total = 0
        for i in range(num_galaxies):
            for j in range(i+1, num_galaxies):
                x_diff = abs(new_galaxies[i][0] - new_galaxies[j][0])
                y_diff = abs(new_galaxies[i][1] - new_galaxies[j][1])

                diff = x_diff + y_diff
                #print(f'{i+1}, {j+1}: {diff}')
                total += diff
                
        print(total)




if __name__ == '__main__':
    main()