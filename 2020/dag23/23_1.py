import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_cups(cups, current_cup):
    if cups.value == current_cup:
        print(f"({cups.value}) ", end="")
    else:
        print(f"{cups.value} ", end="")
    first_cup_value = cups.value
    cups = cups.next
    while cups.value != first_cup_value:
        if cups.value == current_cup:
            print(f"({cups.value}) ", end="")
        else:
            print(f"{cups.value} ", end="")
        cups = cups.next
    print()


def main():
    with open(sys.argv[1], "r") as f:
        data = f.readline()
        data = data.strip("\n")
        data = [int(c) for c in data]
        print(data)
    node_pointer = {}
    for val in data:
        node = Node(val)
        node_pointer[val] = node
    for val_1, val_2 in zip(data, data[1:] + [data[0]]):
        node_pointer[val_1].next = node_pointer[val_2]

    i = 1
    current_cup = data[0]
    max_iter = 100
    while i <= max_iter:
        # print(f"-- move {i} --")

        # print("cups: ", end="")
        # print_cups(node_pointer[current_cup], current_cup)

        tmp_pointer = node_pointer[current_cup].next
        node_pointer[current_cup].next = node_pointer[current_cup].next.next.next.next
        destination = current_cup - 1
        removed_nodes = [
            tmp_pointer.value,
            tmp_pointer.next.value,
            tmp_pointer.next.next.value,
        ]

        # print(f"pick up: {', '.join(str(c) for c in removed_nodes)}")

        while destination in removed_nodes or destination <= 0:
            destination -= 1
            if destination <= 0:
                destination = len(data)

        # print(f"destination: {destination}")
        # print()

        tmp_pointer.next.next.next = node_pointer[destination].next
        node_pointer[destination].next = tmp_pointer

        current_cup = node_pointer[current_cup].next.value

        i += 1

    current_cup = node_pointer[1].next
    result = ""
    while current_cup.value != 1:
        result += str(current_cup.value)

        current_cup = current_cup.next
    print(result)


if __name__ == "__main__":
    main()
