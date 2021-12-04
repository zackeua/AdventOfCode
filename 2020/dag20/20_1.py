

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
        h11 = sum([10**i * pam[num] for i, num in enumerate(self._grid[0])])

        h12 = sum([10**i * pam[num] for i, num in enumerate(self._grid[0][::-1])])

        h21 = sum([10**i * pam[num] for i, num in enumerate(self._grid[-1])])
        h22 = sum([10**i * pam[num] for i, num in enumerate(self._grid[-1][::-1])])

        h31 = sum([10**i * pam[num[0]] for i, num in enumerate(self._grid)])
        h32 =  sum([10**i * pam[num[0]] for i, num in enumerate(self._grid[::-1])])

        h41 = sum([10**i * pam[num[-1]] for i, num in enumerate(self._grid)])
        h42 = sum([10**i * pam[num[-1]] for i, num in enumerate(self._grid[::-1])])
        return [h11, h12, h22, h21, h31, h32, h41, h42]
        
with open('input.txt','r') as f:
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
tiles.append(Tile(num, grid))
print(tiles[-1])
print(tiles[-1].hashes())


hash_list = []
for tile in tiles:
    hash_list.extend(tile.hashes())

prod = []
res = 1
for tile in tiles:
    hash_match = [hash_list.count(h)-1 for h in tile.hashes()]
    print(f'Tile {tile._number} matches : {hash_match} tiles')
    if hash_match.count(0) == 4:
        res *= tile._number

print(res)