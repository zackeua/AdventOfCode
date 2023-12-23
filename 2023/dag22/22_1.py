import sys


class Corner:

    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.z == other.z)

    def __str__(self):

        return f'Corner({self.x}, {self.y}, {self.z})'

    def __repr__(self):

        return self.__str__()


class Block:

    def __init__(self, index, corner1, corner2):
        x_min = min(corner1.x, corner2.x)
        y_min = min(corner1.y, corner2.y)
        z_min = min(corner1.z, corner2.z)
        x_max = max(corner1.x, corner2.x)
        y_max = max(corner1.y, corner2.y)
        z_max = max(corner1.z, corner2.z)
        self.index = index
        self.min_corner = Corner(x_min, y_min, z_min)
        self.max_corner = Corner(x_max, y_max, z_max)
        self.supported_by = []
        self.supporting = []

    def __lt__(self, other):
        return (self.min_corner.z, self.max_corner.z) < (other.min_corner.z, other.max_corner.z)

    def __eq__(self, other):
        return self.min_corner == other.min_corner and self.max_corner == other.max_corner

    def __str__(self):
        return f'Block({self.min_corner}, {self.max_corner})'

    def __repr__(self):
        return self.__str__()

    def base_coordinates(self):
        base = []

        for x in range(self.min_corner.x, self.max_corner.x + 1):
            for y in range(self.min_corner.y, self.max_corner.y + 1):
                base.append((x, y, self.min_corner.z))
        return base

    def supporting_coordinates(self):
        top = []

        for x in range(self.min_corner.x, self.max_corner.x + 1):
            for y in range(self.min_corner.y, self.max_corner.y + 1):
                top.append((x, y, self.max_corner.z + 1))
        return top

    def supports(self, other):
        for coord in self.supporting_coordinates():
            if coord in other.base_coordinates():
                return True
        return False


def determine_supports(blocks):
    for i in range(len(blocks)):
        for j in range(len(blocks)):
            # print(chr(ord('A') + i), chr(ord('A') + j), blocks[i].supports(blocks[j]))
            if blocks[i].supports(blocks[j]):
                blocks[j].supported_by.append(blocks[i].index)
                blocks[i].supporting.append(blocks[j].index)


def determine_safe_to_remove(blocks):
    total = 0
    for block in blocks:
        count = 0
        supports_none = True
        for other in blocks:
            if block.supports(other):
                supports_none = False
                if len(other.supported_by) > 1:
                    count += 1
        # print(chr(ord('A') + block.index),
        #       list(map(lambda x: chr(ord('A') + x), block.supported_by)),
        #       list(map(lambda x: chr(ord('A') + x), block.supporting)),
        #       count or (1 if supports_none else 0))
        if count >= 1 or supports_none:
            total += 1
    return total


def fall_down(blocks):
    for i, block in enumerate(blocks):
        print(i+1, '/', len(blocks))
        while True:
            final = False
            if block.min_corner.z == 1:
                final = True

            if not final:
                for other in range(max(0, i-100), i):
                    if blocks[other].supports(block):
                        final = True
                        break
            if final:
                print(block)
                break
            block.min_corner.z -= 1
            block.max_corner.z -= 1


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip().split('~') for line in data]
        data = [[Corner(*elem.split(',')) for elem in line] for line in data]
        blocks = [Block(i, *line) for i, line in enumerate(data)]

        blocks = sorted(blocks)

        print('Sorted blocks')
        for block in blocks:
            print(block)

        fall_down(blocks)

        blocks = sorted(blocks)

        determine_supports(blocks)
        total = determine_safe_to_remove(blocks)
        print(total)

        assert total > 507
        assert total < 670


if __name__ == '__main__':
    main()
