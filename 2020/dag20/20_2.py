from math import sqrt

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
        return list(map(lambda x: int(str(x),2), [h11, h12, h22, h21, h31, h32, h41, h42]))
        
with open('test.txt','r') as f:
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
        #print(tiles[-1])
        #print(tiles[-1].hashes())
    
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



hash_list = []
tile_map = {}
for tile in tiles:
    hash_list.extend(tile.hashes())
    tile_map[tile._number] = tile.hashes()


for tile in tiles:
    print(f'Tile {tile._number} matches : {tile.hashes()} tiles')

img = [[None]*int(sqrt(len(tiles))) for _ in range(int(sqrt(len(tiles))))]

for tile in tiles:
    hash_match = [hash_list.count(h)-1 for h in tile.hashes()]
    print(f'Tile {tile._number} matches : {hash_match} tiles')
    if hash_match.count(0) == 4:
        img[0][0] = tile._number
'''
for row in img:
    print(row)
print()
'''

i = 0
while i != int(sqrt(len(tiles)))-1:
    for tile in tiles:
        if 1 not in [tile._number in row for row in img]:
            matches = 0
            for tile_hash in tile_map[img[0][i]]:
                matches += tile_hash in tile.hashes()
            if matches == 2:
                i += 1
                img[0][i] = tile._number
            if i == int(sqrt(len(tiles)))-1:
                break
'''
for row in img:
    print(row)
'''

j = 0
while j != int(sqrt(len(tiles)))-1:
    for tile in tiles:
        if 1 not in [tile._number in row for row in img]:
            matches = 0
            for tile_hash in tile_map[img[j][0]]:
                matches += tile_hash in tile.hashes()
            if matches == 2:
                j += 1
                img[j][0] = tile._number
            if j == int(sqrt(len(tiles)))-1:
                break
'''
for row in img:
    print(row)
'''

i = 0
j = 0

while j != int(sqrt(len(tiles)))-1:
    c = True
    for tile in tiles:
        if 1 not in [tile._number in row for row in img] and c:
            matches = 0
            for tile_hash in tile_map[img[j][i+1]]:
                matches += tile_hash in tile.hashes()
            for tile_hash in tile_map[img[j+1][i]]:
                matches += tile_hash in tile.hashes()

            if matches == 4:
                i += 1
                img[j+1][i] = tile._number
            if i == int(sqrt(len(tiles)))-1:
                j += 1
                i = 0
                c = False
        '''
        for row in img:
            print(row)
        '''

for row in img:
    print(row)

picture = [None for _ in range()]