import sys


class Graph:

    def __init__(self):
        self._ingoing_edges = {}
        self._outgoing_edges = {}
        self._nodes = []

    def add_edge(self, f, to):
        if f not in self._nodes:
            self._nodes.append(f)

        if f not in self._outgoing_edges:
            self._outgoing_edges[f] = []
        self._outgoing_edges[f].append(to)

        if to not in self._nodes:
            self._nodes.append(to)

        if to not in self._ingoing_edges:
            self._ingoing_edges[to] = []
        self._ingoing_edges[to].append(f)

    def get_nodes(self):
        return self._nodes

    def get_parents(self, node):
        return self._ingoing_edges.get(node, [])

    def get_children(self, node):
        return self._outgoing_edges.get(node, [])


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
    graph = Graph()
    for i in range(len(blocks)):
        for j in range(len(blocks)):
            # print(chr(ord('A') + i), chr(ord('A') + j), blocks[i].supports(blocks[j]))
            if blocks[i].supports(blocks[j]):
                graph.add_edge(i, j)
    return graph


def determine_safe_to_remove(blocks):
    total = 0
    for block in blocks:
        safe_to_remove = True
        for other in block.supporting:
            if len(blocks[other].supported_by) == 1:
                safe_to_remove = False
                break
        if safe_to_remove:
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
                for other in range(i):
                    if blocks[other].max_corner.z < block.min_corner.z and blocks[other].supports(block):
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

        fall_down(blocks)

        blocks = sorted(blocks)

        graph = determine_supports(blocks)

        total = 0
        for n in graph.get_nodes():
            supporting = graph.get_children(n)
            all_safe = True
            for c in graph.get_children(n):
                if len(graph.get_parents(c)) == 1:
                    all_safe = False
            total += all_safe

        print(total)

        assert total > 507
        assert total != 531
        assert total < 670


if __name__ == '__main__':
    main()
