from enum import Enum
from math import sqrt
import sys


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


def rotate_90_counterclockwise(grid: list[list[str]]):
    data = [line.copy() for line in grid]
    for i, line in enumerate(grid):
        for j, elem in enumerate(line):
            data[j][len(line)-i-1] = elem
    return data


def flip(grid):
    return [line[::-1] for line in grid]


class Tile:
    def __init__(self, number, grid):
        self._number = number
        self._grid = grid
        assert len(self._grid) == 10, "Not 10 rows in this tile"
        assert len(self._grid[0]) == 10, "Not 10 columns in this tile"
        self._neighbors = []

    def add_neighbor(self, tile):
        if tile._number == self._number:
            return
        self._neighbors.append(tile._number)
        self._neighbors = list(set(self._neighbors))
        assert 0 <= len(
            self._neighbors) <= 4, "Maximum 4 neighbours for each tile"

    def rotate(self):
        self._grid = rotate_90_counterclockwise(self._grid)

    def flip(self):

        self._grid = flip(self._grid)

    def matches_direction(tile1, tile2, direction: Direction):
        tile1_hashes = tile1.hashes()
        match direction:
            case Direction.UP:
                tile1_hashes = [tile1_hashes[0], tile1_hashes[1]]
            case Direction.RIGHT:
                tile1_hashes = [tile1_hashes[2], tile1_hashes[3]]
            case Direction.DOWN:
                tile1_hashes = [tile1_hashes[4], tile1_hashes[5]]
            case Direction.LEFT:
                tile1_hashes = [tile1_hashes[6], tile1_hashes[7]]
        for tile_hash in tile1_hashes:
            if tile_hash not in tile2.hashes():
                return False
        return True

    def sides_equal(tile1, tile2, direction: Direction):
        tile1_hashes = tile1.hashes()
        tile2_hashes = tile2.hashes()
        match direction:
            case Direction.UP:
                return tile1_hashes[0] == tile2_hashes[5] and tile1_hashes[1] == tile2_hashes[4]
            case Direction.RIGHT:
                return tile1_hashes[2] == tile2_hashes[7] and tile1_hashes[3] == tile2_hashes[6]
            case Direction.DOWN:
                print(tile1_hashes, tile2_hashes)
                return tile1_hashes[5] == tile2_hashes[0] and tile1_hashes[4] == tile2_hashes[1]
            case Direction.LEFT:
                return tile1_hashes[7] == tile2_hashes[2] and tile1_hashes[6] == tile2_hashes[3]
        assert False, "Should not reach this"
        return False

    def __str__(self):
        s = ''
        s += f'Tile {self._number}\n'
        for row in self._grid:
            for c in row:
                s += c
            s += '\n'
        return s

    def hashes(self):
        char_mapping = {'#': 0, '.': 1}

        # top row of piece
        h11 = sum([10**i * char_mapping[num]
                  for i, num in enumerate(self._grid[0])])

        h12 = sum([10**i * char_mapping[num]
                  for i, num in enumerate(self._grid[0][::-1])])

        # right column of piece
        h21 = sum([10**i * char_mapping[num[-1]]
                  for i, num in enumerate(self._grid)])
        h22 = sum([10**i * char_mapping[num[-1]]
                  for i, num in enumerate(self._grid[::-1])])

        # bottom row of piece
        h31 = sum([10**i * char_mapping[num]
                  for i, num in enumerate(self._grid[-1])])
        h32 = sum([10**i * char_mapping[num]
                  for i, num in enumerate(self._grid[-1][::-1])])

        # left column of piece
        h41 = sum([10**i * char_mapping[num[0]]
                  for i, num in enumerate(self._grid)])
        h42 = sum([10**i * char_mapping[num[0]]
                  for i, num in enumerate(self._grid[::-1])])

        # this order to keep internal order during rotation
        return list(map(lambda x: int(str(x), 2),
                        [h11, h12, h21, h22, h32, h31, h42, h41]))

    def __repr__(self) -> str:
        res = ""
        for line in self._grid:
            res += "".join(line) + "\n"
        return res


def parse_tiles(data):
    parse = False
    tiles = []
    for i in range(len(data)):
        if '\n' == data[i]:
            parse = False
            tiles.append(Tile(num, grid))

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
    return tiles


def find_neighbors(tiles: list[Tile]):

    for t1 in tiles:
        for t2 in tiles:
            t1_haches = t1.hashes()
            t2_haches = t2.hashes()
            matches = 0
            for t1_hash in t1_haches:
                matches += t1_hash in t2_haches
            if matches:
                t1.add_neighbor(t2)
                t2.add_neighbor(t1)


def get_tile(tiles, number):
    for tile in tiles:
        if tile._number == number:
            return tile


def place_tiles(img, tiles):

    corners = [tile for tile in tiles if len(tile._neighbors) == 2]
    edges = [tile for tile in tiles if len(tile._neighbors) == 3]
    internal = [tile for tile in tiles if len(tile._neighbors) == 4]

    assert len(corners) + len(edges) + len(internal) == len(tiles)

    img[0][0] = corners[0]

    frontier = [(0, 1), (1, 0)]
    added_tiles = [img[0][0]._number]

    while frontier:
        # print(frontier)
        (i, j), frontier = frontier[0], frontier[1:]

        placed_neighbors = 0
        placed_neighbors_left = 0 <= j - \
            1 < len(img) and img[i][j-1] is not None
        placed_neighbors_right = 0 <= j + \
            1 < len(img) and img[i][j+1] is not None
        placed_neighbors_above = 0 <= i - \
            1 < len(img) and img[i-1][j] is not None
        placed_neighbors_below = 0 <= i + \
            1 < len(img) and img[i+1][j] is not None
        placed_neighbors = placed_neighbors_above + placed_neighbors_below + \
            placed_neighbors_left + placed_neighbors_right

        # print(placed_neighbors)

        if placed_neighbors == 1:
            if placed_neighbors_left:
                tile_id = [e for e in img[i]
                           [j-1]._neighbors if e not in added_tiles][0]
                img[i][j] = get_tile(tiles, tile_id)
                added_tiles.append(img[i][j]._number)
            if placed_neighbors_above:
                tile_id = [e for e in img[i-1]
                           [j]._neighbors if e not in added_tiles][0]
                img[i][j] = get_tile(tiles, tile_id)
                added_tiles.append(img[i][j]._number)
        if placed_neighbors == 2:
            left_tile_neighbors = img[i][j-1]._neighbors
            above_tile_neighbors = img[i-1][j]._neighbors
            overlap = [
                e for e in left_tile_neighbors if e in above_tile_neighbors and e not in added_tiles]
            # print(overlap)
            img[i][j] = get_tile(tiles, overlap[0])
            added_tiles.append(img[i][j]._number)

        # show_number_image(img)

        if i < len(img) - 1:
            if (i+1, j) not in frontier:
                frontier.append((i+1, j))
        if j < len(img) - 1:
            if (i, j+1) not in frontier:
                frontier.append((i, j+1))

        frontier = frontier


def rotate_and_flip_tiles(img):

    if not Tile.matches_direction(img[0][0], img[0][1], Direction.RIGHT):
        img[0][0].rotate()
    if not Tile.matches_direction(img[0][0], img[0][1], Direction.RIGHT):
        img[0][0].rotate()
    if not Tile.matches_direction(img[0][0], img[0][1], Direction.RIGHT):
        img[0][0].rotate()
    if not Tile.matches_direction(img[0][0], img[0][1], Direction.RIGHT):
        img[0][0].rotate()

    if not Tile.matches_direction(img[0][0], img[1][0], Direction.DOWN):
        img[0][0].flip()

    if not Tile.matches_direction(img[0][0], img[0][1], Direction.RIGHT):
        img[0][0].rotate()
    if not Tile.matches_direction(img[0][0], img[0][1], Direction.RIGHT):
        img[0][0].rotate()
    if not Tile.matches_direction(img[0][0], img[0][1], Direction.RIGHT):
        img[0][0].rotate()
    if not Tile.matches_direction(img[0][0], img[0][1], Direction.RIGHT):
        img[0][0].rotate()

    assert Tile.matches_direction(img[0][0], img[0][1], Direction.RIGHT)
    assert Tile.matches_direction(img[0][0], img[1][0], Direction.DOWN)

    for i, row in enumerate(img):
        for j, elem in enumerate(row):
            if i == 0 and j == 0:
                continue
            if j != 0:
                if not Tile.sides_equal(img[i][j-1], img[i][j], Direction.RIGHT):
                    img[i][j].rotate()
                if not Tile.sides_equal(img[i][j-1], img[i][j], Direction.RIGHT):
                    img[i][j].rotate()
                if not Tile.sides_equal(img[i][j-1], img[i][j], Direction.RIGHT):
                    img[i][j].rotate()
                if not Tile.sides_equal(img[i][j-1], img[i][j], Direction.RIGHT):
                    img[i][j].rotate()
                if not Tile.sides_equal(img[i][j-1], img[i][j], Direction.RIGHT):
                    img[i][j].flip()
                if not Tile.sides_equal(img[i][j-1], img[i][j], Direction.RIGHT):
                    img[i][j].rotate()
                if not Tile.sides_equal(img[i][j-1], img[i][j], Direction.RIGHT):
                    img[i][j].rotate()
                if not Tile.sides_equal(img[i][j-1], img[i][j], Direction.RIGHT):
                    img[i][j].rotate()
                if not Tile.sides_equal(img[i][j-1], img[i][j], Direction.RIGHT):
                    img[i][j].rotate()
            if i != 0:
                if not Tile.sides_equal(img[i-1][j], img[i][j], Direction.DOWN):
                    img[i][j].rotate()
                if not Tile.sides_equal(img[i-1][j], img[i][j], Direction.DOWN):
                    img[i][j].rotate()
                if not Tile.sides_equal(img[i-1][j], img[i][j], Direction.DOWN):
                    img[i][j].rotate()
                if not Tile.sides_equal(img[i-1][j], img[i][j], Direction.DOWN):
                    img[i][j].rotate()
                if not Tile.sides_equal(img[i-1][j], img[i][j], Direction.DOWN):
                    img[i][j].flip()
                if not Tile.sides_equal(img[i-1][j], img[i][j], Direction.DOWN):
                    img[i][j].rotate()
                if not Tile.sides_equal(img[i-1][j], img[i][j], Direction.DOWN):
                    img[i][j].rotate()
                if not Tile.sides_equal(img[i-1][j], img[i][j], Direction.DOWN):
                    img[i][j].rotate()
                if not Tile.sides_equal(img[i-1][j], img[i][j], Direction.DOWN):
                    img[i][j].rotate()

            if j != 0:
                assert Tile.sides_equal(
                    img[i][j-1], img[i][j], Direction.RIGHT)
            if i != 0:
                assert Tile.sides_equal(img[i-1][j], img[i][j], Direction.DOWN)


def show_number_image(img):
    for row in img:
        print([tile._number if tile is not None else None for tile in row])


def show_raw_image(img):
    for img_i in range(len(img)):
        for elem_i in range(len(img[0][0]._grid)):
            for img_j in range(len(img)):
                total = ""
                for elem_j in range(len(img[0][0]._grid)):
                    total += img[img_i][img_j]._grid[elem_i][elem_j]
                print(total, end="")
            print()


def create_full_image(img):
    full_image = []
    for img_i in range(len(img)):
        for elem_i in range(len(img[0][0]._grid)):
            if elem_i == 0 or elem_i == len(img[0][0]._grid) - 1:
                continue
            line = []
            for img_j in range(len(img)):
                for elem_j in range(len(img[0][0]._grid)):
                    if elem_j == 0 or elem_j == len(img[0][0]._grid) - 1:
                        continue
                    line.append(img[img_i][img_j]._grid[elem_i][elem_j])
            if line:
                full_image.append(line)
    return full_image


def show_full_image(img):
    for line in img:
        print("".join(line))


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()

    tiles = parse_tiles(data)
    find_neighbors(tiles)

    for tile in tiles:
        match len(tile._neighbors):
            case 2:
                print(tile)
            case 3:
                pass
            case 4:
                pass
            case _:
                assert False, f"Should not have {_} neighbors"

    img = [[None]*int(sqrt(len(tiles))) for _ in range(int(sqrt(len(tiles))))]

    place_tiles(img, tiles)

    # print(img[0][0].hashes())
    # print(img[1][0].hashes())
    # print(img[0][1].hashes())

    show_number_image(img)

    print()
    show_raw_image(img)

    # print("Top      , right    , bottom  , left")
    # print(img[0][0].hashes())
    # print(img[0][1].hashes())
    # print(img[1][0].hashes())
    #
    # img[0][0].rotate()
    # img[0][1].rotate()
    # # img[0][1].flip()
    # # img[0][1].rotate()
    # # img[0][1].rotate()
    #
    # print("Top      , right    , bottom  , left")
    # print(img[0][0].hashes())
    # print(img[0][1].hashes())
    # print(img[1][0].hashes())
    #
    # print()
    # show_raw_image(img)

    rotate_and_flip_tiles(img)

    print()
    show_raw_image(img)

    full_image = create_full_image(img)

    print()
    show_full_image(full_image)


if __name__ == "__main__":
    main()
