import sys
from collections import defaultdict


class Hexagon:

    def __init__(self, q=0, r=0, s=0):
        self.q = q
        self.r = r
        self.s = s
        assert self.q + self.r + self.s == 0, f"({q=}, {r=}, {s=})"

    def __repr__(self):
        return str(self._tuple())

    def __hash__(self):
        return self.q * self.r * self.s

    def _tuple(self):
        return (self.q, self.r, self.s)

    def __eq__(self, other):
        return self._tuple() == other._tuple()

    def __lt__(self, other):
        return self._tuple() < other._tuple()

    def __add__(self, other):
        return Hexagon(self.q + other.q, self.r + other.r, self.s + other.s)

    def get_neighbors(self):
        directions = [Hexagon(1, 0, -1), Hexagon(-1, 0, 1),
                      Hexagon(1, -1, 0), Hexagon(-1, 1, 0),
                      Hexagon(0, -1, 1), Hexagon(0, 1, -1)]
        return [self + d for d in directions]


def get_hexagon(line: str) -> Hexagon:

    hexagon = Hexagon()

    d = ""
    for c in line:

        d += c

        match d:
            case "e":
                hexagon += Hexagon(1, 0, -1)
                d = ""
            case "w":
                hexagon += Hexagon(-1, 0, 1)
                d = ""
            case "ne":
                hexagon += Hexagon(1, -1, 0)
                d = ""
            case "sw":
                hexagon += Hexagon(-1, 1, 0)
                d = ""
            case "nw":
                hexagon += Hexagon(0, -1, 1)
                d = ""
            case "se":
                hexagon += Hexagon(0, 1, -1)
                d = ""

    return hexagon


def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        data = [line.strip() for line in data]

    grid = defaultdict(lambda: 0)

    for line in data:
        hexagon = get_hexagon(line)
        grid[hexagon] = not grid[hexagon]

    total = sum(grid.values())
    print(f"Day {0}: {total}")

    for i in range(1, 100+1):
        tiles_to_flip_to_white = []
        tiles_to_flip_to_black = []
        tiles_to_consider = [key for key in grid.keys()]
        for tile in [key for key in grid.keys()]:
            for n in tile.get_neighbors():
                if n not in tiles_to_consider:
                    tiles_to_consider.append(n)

        for tile in tiles_to_consider:
            tile_is_black = grid[tile] == 1
            black_neighbors = sum(grid[t] for t in tile.get_neighbors())
            if tile_is_black and (black_neighbors == 0 or black_neighbors > 2):
                if tile not in tiles_to_flip_to_white:
                    tiles_to_flip_to_white.append(tile)
            if not tile_is_black and black_neighbors == 2:
                if tile not in tiles_to_flip_to_black:
                    tiles_to_flip_to_black.append(tile)

        for tile in tiles_to_flip_to_black:
            grid[tile] = 1
        for tile in tiles_to_flip_to_white:
            grid[tile] = 0
        total = sum(grid.values())
        print(f"Day {i}: {total}")

    print(total)


if __name__ == "__main__":
    main()
