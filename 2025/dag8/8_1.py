import sys


class Circuit:
    def __init__(self, index: int):
        self.index = index

    def __repr__(self):
        return f"{self.index}"


class JunctionBox:
    def __init__(self, coordinates: tuple, circuit: Circuit | None = None):
        self.coordinates = coordinates
        self.circuit = circuit

    def __repr__(self):
        return f"({self.coordinates}, {self.circuit})"


def distance(box1: JunctionBox, box2: JunctionBox) -> int:
    x1, y1, z1 = box1.coordinates
    x2, y2, z2 = box2.coordinates

    if box1.circuit is not None and box2.circuit is not None:
        if box1.circuit.index == box2.circuit.index:
            return sys.float_info.max

    return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2


def get_lowest_circuit(box1: JunctionBox, box2: JunctionBox) -> Circuit | None:
    if box1.circuit is None and box2.circuit is None:
        return None
    elif box1.circuit is None and box2.circuit is not None:
        return box2.circuit.index
    elif box1.circuit is not None and box2.circuit is None:
        return box1.circuit.index
    else:
        return min(box1.circuit.index, box2.circuit.index)


def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        data = [JunctionBox(tuple(map(int, line.strip().split(",")))) for line in data]
        # print(data)

    next_circuit_index = 0
    circuit_dict = {}

    for _ in range(1000):
        min_distance = sys.float_info.max
        min_indexes = [0, 0]
        for i, box1 in enumerate(data):
            for j, box2 in enumerate(data):
                if i == j:
                    continue
                tmp_distance = distance(box1, box2)
                if tmp_distance < min_distance:
                    min_distance = tmp_distance
                    min_indexes = [i, j]
        # print(data[min_indexes[0]])
        # print(data[min_indexes[1]])
        min_circuit = get_lowest_circuit(data[min_indexes[0]], data[min_indexes[1]])
        # print(min_circuit)
        # input()
        if min_circuit is None:
            c = Circuit(next_circuit_index)
            circuit_dict[next_circuit_index] = c
            next_circuit_index += 1
            data[min_indexes[0]].circuit = c
            data[min_indexes[1]].circuit = c
        else:
            data[min_indexes[0]].circuit = circuit_dict[min_circuit]
            data[min_indexes[1]].circuit = circuit_dict[min_circuit]
        # print("\n" * 10)
        # for elem in data:
        # print(elem)
        # input()
    # print("\n" * 10)
    for elem in data:
        print(elem)

    circuit_counts = {}
    for elem in data:
        if elem.circuit is not None:
            if elem.circuit.index not in circuit_counts:
                circuit_counts[elem.circuit.index] = 0
            circuit_counts[elem.circuit.index] += 1

    circuit_counts = sorted(circuit_counts.values())

    print(circuit_counts)

    total = circuit_counts[-1] * circuit_counts[-2] * circuit_counts[-3]
    print(total)


if __name__ == "__main__":
    main()
