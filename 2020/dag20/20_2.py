from math import sqrt
import sys


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
        pam = {'#': 0, '.': 1}

        # top row of piece
        h11 = sum([10**i * pam[num] for i, num in enumerate(self._grid[0])])

        h12 = sum([10**i * pam[num]
                  for i, num in enumerate(self._grid[0][::-1])])

        # bottom row of piece
        h21 = sum([10**i * pam[num] for i, num in enumerate(self._grid[-1])])
        h22 = sum([10**i * pam[num]
                  for i, num in enumerate(self._grid[-1][::-1])])

        # left column of piece
        h31 = sum([10**i * pam[num[0]] for i, num in enumerate(self._grid)])
        h32 = sum([10**i * pam[num[0]]
                  for i, num in enumerate(self._grid[::-1])])

        # right column of piece
        h41 = sum([10**i * pam[num[-1]] for i, num in enumerate(self._grid)])
        h42 = sum([10**i * pam[num[-1]]
                  for i, num in enumerate(self._grid[::-1])])

        return list(map(lambda x: int(str(x), 2),
                        [h11, h12, h22, h21, h31, h32, h41, h42]))

    def __repr__(self) -> str:
        res = ""
        for line in self._grid:
            res += "".join(line) + "\n"
        return res


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()

    # print(data)

    parse = False
    tiles = []
    for i in range(len(data)):
        if '\n' == data[i]:
            parse = False
            # print(num)
            # print(grid)
            tiles.append(Tile(num, grid))
            # print(tiles[-1])
            # print(tiles[-1].hashes())

        if parse:
            line = []
            for c in data[i][:-1]:
                line.append(c)
            grid.append(line)

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

    corners = []
    edges = []
    centers = []
    for tile in tiles:
        hash_match = [hash_list.count(h)-1 for h in tile.hashes()]
        print(f'Tile {tile._number} matches : {hash_match} tiles')
        if hash_match.count(0) == 4:
            corners.append(tile)
            # img[0][0] = tile._number
        elif hash_match.count(0) == 2:
            edges.append(tile)
        elif hash_match.count(0) == 0:
            centers.append(tile)
        else:
            assert False, "Should not happen"

    print("Corners")
    for c in corners:
        hash_match = [hash_list.count(h)-1 for h in c.hashes()]
        print(c._number, hash_match)
        print(c)
    # print("Edges")
    # for e in edges:
    #     hash_match = [hash_list.count(h)-1 for h in tile.hashes()]
    #     print(c._number, hash_match)
    #     print(e)
    # print("Centers")
    # for c in centers:
        # print(c)

    img[0][0] = corners[0]._number

    assert img[0][0] in [e._number for e in corners]
    for row in img:
        print(row)
    print()

    i = 0
    while i != int(sqrt(len(tiles)))-2:
        for tile in edges:
            if 1 not in [tile._number in row for row in img]:
                matches = 0
                for tile_hash in tile_map[img[0][i]]:
                    matches += tile_hash in tile.hashes()
                if matches == 2:
                    i += 1
                    img[0][i] = tile._number
                if i == int(sqrt(len(tiles)))-1:
                    break
    for tile in corners:
        if 1 not in [tile._number in row for row in img]:
            matches = 0
            for tile_hash in tile_map[img[0][i]]:
                matches += tile_hash in tile.hashes()
            if matches == 2:
                i += 1
                img[0][i] = tile._number
            if i == int(sqrt(len(tiles)))-1:
                break

    print()
    for row in img:
        print(row)

    assert img[0][-1] in [e._number for e in corners]
    j = 0
    while j != int(sqrt(len(tiles)))-2:
        for tile in edges:
            if 1 not in [tile._number in row for row in img]:
                matches = 0
                for tile_hash in tile_map[img[j][0]]:
                    matches += tile_hash in tile.hashes()
                if matches == 2:
                    j += 1
                    img[j][0] = tile._number
                if j == int(sqrt(len(tiles)))-1:
                    break
    for tile in corners:
        if 1 not in [tile._number in row for row in img]:
            matches = 0
            for tile_hash in tile_map[img[j][0]]:
                matches += tile_hash in tile.hashes()
            if matches == 2:
                j += 1
                img[j][0] = tile._number
            if j == int(sqrt(len(tiles)))-1:
                break

    print()
    for row in img:
        print(row)
    assert img[-1][0] in [e._number for e in corners]

    i = 0
    while i != int(sqrt(len(tiles)))-2:
        for tile in edges:
            if 1 not in [tile._number in row for row in img]:
                matches = 0
                for tile_hash in tile_map[img[-1][i]]:
                    matches += tile_hash in tile.hashes()
                if matches == 2:
                    i += 1
                    img[-1][i] = tile._number
                if i == int(sqrt(len(tiles)))-1:
                    break
    for tile in corners:
        if 1 not in [tile._number in row for row in img]:
            matches = 0
            for tile_hash in tile_map[img[-1][i]]:
                matches += tile_hash in tile.hashes()
            if matches == 2:
                i += 1
                img[-1][i] = tile._number
            if i == int(sqrt(len(tiles)))-1:
                break

    assert img[-1][-1] in [e._number for e in corners]

    print()
    for row in img:
        print(row)

    j = 0
    while j != int(sqrt(len(tiles)))-2:
        for tile in tiles:
            if 1 not in [tile._number in row for row in img]:
                matches = 0
                for tile_hash in tile_map[img[j][-1]]:
                    matches += tile_hash in tile.hashes()
                if matches == 2:
                    j += 1
                    img[j][-1] = tile._number
                if j == int(sqrt(len(tiles)))-2:
                    break

    print()
    for row in img:
        print(row)

    i = 1
    j = 1
    while j != int(sqrt(len(tiles)))-1:
        if not any([None in row for row in img]):
            break
        c = True
        for tile in centers:
            if 1 not in [tile._number in row for row in img] and c:
                matches = 0
                # print(j, i - 1)
                for tile_hash in tile_map[img[j][i-1]]:
                    matches += tile_hash in tile.hashes()
                for tile_hash in tile_map[img[j-1][i]]:
                    matches += tile_hash in tile.hashes()
                if img[j][i+1] is not None:
                    for tile_hash in tile_map[img[j][i-1]]:
                        matches += tile_hash in tile.hashes()
                if img[j+1][i] is not None:
                    for tile_hash in tile_map[img[j+1][i]]:
                        matches += tile_hash in tile.hashes()
                if matches == 6 or matches == 8:
                    img[j][i] = tile._number
                    i += 1
                if matches == 4 and img[j][i+1] is None and img[j+1][i] is None:
                    img[j][i] = tile._number
                    i += 1

                if i == int(sqrt(len(tiles)))-2:
                    j += 1
                    i = 1
                    c = False

        print()
        for row in img:
            print(row)

    used_tiles = []
    for row in img:
        used_tiles.extend(e for e in row if e is not None)

    # for tile in used_tiles:
        # print(tile)

    unused_tiles = []
    for tile in tiles:
        if tile._number not in used_tiles:
            unused_tiles.append(tile._number)
    print(unused_tiles)

    input()
    i = -2
    j = 1
    while j != int(sqrt(len(tiles)))-1:
        if not any([None in row for row in img]):
            break
        c = True
        for tile in unused_tiles:
            if 1 not in [tile in row for row in img] and c:
                matches = 0
                # print(j, i - 1)
                for tile_hash in tile_map[img[j][i-1]]:
                    matches += tile_hash in tile_map[tile]
                for tile_hash in tile_map[img[j-1][i]]:
                    matches += tile_hash in tile_map[tile]
                for tile_hash in tile_map[img[j][i-1]]:
                    matches += tile_hash in tile_map[tile]
                if img[j+1][i] is not None:
                    for tile_hash in tile_map[img[j+1][i]]:
                        matches += tile_hash in tile_map[tile]
                if matches > 0:
                    img[j][i] = tile
                    j += 1
                    print()
                    for row in img:
                        print(row)

    print()
    for row in img:
        print(row)

    # picture = [None for _ in range()]


if __name__ == "__main__":
    main()
