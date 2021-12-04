

class Tile:
    """docstring for Pice."""

    def __init__(self, number, grid):
        self._number = number
        self._grid = grid

    def __str__(self):
        s = ''
        s += f'Tile {self._number}\n'
        for row in self._grid:
            for c in row:
                s += c
            s += '\n'
        return s
    
    def hashes(self):
        pam = {'#':0, '.':1}
        h1 = sum([10**i * pam[num] for i, num in enumerate(self._grid[0])])
        + sum([10**i * pam[num] for i, num in enumerate(self._grid[0][::-1])])

        h2 = sum([10**i * pam[num] for i, num in enumerate(self._grid[-1])])
        + sum([10**i * pam[num] for i, num in enumerate(self._grid[-1][::-1])])

        h3 = sum([10**i * pam[num[0]] for i, num in enumerate(self._grid)])
        + sum([10**i * pam[num[0]] for i, num in enumerate(self._grid[::-1])])

        h4 = sum([10**i * pam[num[-1]] for i, num in enumerate(self._grid)])
        + sum([10**i * pam[num[-1]] for i, num in enumerate(self._grid[::-1])])
        return [h1, h2, h3, h4]
        
with open('small20.txt','r') as f:
    data = f.readlines()

#print(data)

parse = False
tiles = []
for i in range(len(data)):
    if '\n' == data[i]:
        parse = False
        #print(num)
        #print(grid)
        tiles.append(Tile(num, grid))
        print(tiles[-1])
        print(tiles[-1].hashes())
    
    if parse:
        l = []
        for c in data[i][:-1]:
            l.append(c)
        grid.append(l)

    if 'Tile' in data[i]:
        parse = True
        num = int(data[i][5:-2])
        grid = []

hash_list = []
for tile in tiles:
    hash_list.extend(tile.hashes())

prod = []
for tile in tiles:    
    hash_match = [hash_list.count(h) for h in tile.hashes()]
    print(f'Tile {tile._number} matches : {hash_match} tiles')