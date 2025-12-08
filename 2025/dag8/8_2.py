import sys
import itertools


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

    sorted_junction_boxes = [(a, b) for a, b in itertools.combinations(data, 2)]
    sorted_junction_boxes = sorted(
        sorted_junction_boxes, key=lambda a: distance(a[0], a[1])
    )

    # for elem in sorted_junction_boxes:
    # print(elem, distance(elem[0], elem[1]))

    total = 0
    for box1, box2 in sorted_junction_boxes:
        min_circuit = get_lowest_circuit(box1, box2)
        if min_circuit is None:
            c = Circuit(next_circuit_index)
            circuit_dict[next_circuit_index] = c
            next_circuit_index += 1
            box1.circuit = c
            box2.circuit = c

        else:
            for b in [box1, box2]:
                if b.circuit is not None and b.circuit.index != min_circuit:
                    box_circuit_index = b.circuit.index
                    for box in data:
                        if (
                            box.circuit is not None
                            and box.circuit.index == box_circuit_index
                        ):
                            box.circuit = circuit_dict[min_circuit]
            box1.circuit = circuit_dict[min_circuit]
            box2.circuit = circuit_dict[min_circuit]

        should_break = True
        prev_index = -1
        for b in data:
            if b.circuit is None:
                should_break = False
                break
            if prev_index == -1:
                prev_index = b.circuit.index
            if b.circuit is not None and b.circuit.index != prev_index:
                should_break = False
                break
        if should_break:
            total = box1.coordinates[0] * box2.coordinates[0]
            break

    print(total)


if __name__ == "__main__":
    main()
