import sys
from collections import defaultdict
from typing import Any


class Instruction:
    def __init__(self, steps: int, turn: str) -> None:
        self.steps = steps
        self.direction = turn


class State:
    def __init__(self, position, direction, f=lambda: None) -> None:
        self.position = position
        self.direction = direction
        self.f = f

    def __add__(self, update: tuple[int, int]):
        return State((self.position[0] + update[0], self.position[1] + update[1]), self.direction, self.f)

    def __copy__(self):
        return State((self.position[0], self.position[1]), (self.direction[0], self.direction[1]), self.f)

    def __eq__(self, __value: object) -> bool:
        return self.position == __value.position and self.direction == __value.direction

    def __hash__(self) -> int:
        return 1_000 * (self.position[0] + 1) + 4 * (self.position[1] + 1) + self.rotation_direction()

    def __str__(self) -> str:
        return f'{self.position[0]}, {self.position[1]}, {self.direction}'

    def __repr__(self) -> str:
        return self.__str__()

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.f()

    def rotation_direction(self):
        if self.direction == (0, 1):
            return 0
        elif self.direction == (1, 0):
            return 1
        elif self.direction == (0, -1):
            return 2
        elif self.direction == (-1, 0):
            return 3
        else:
            print(self.direction)
            raise Exception('Invalid direction')


class Character:
    def __init__(self, data) -> None:
        self.state = self.get_first_position(data[0])
        self.board, self.edge_transition, self.max_size = set_board(data[:-2])
        self.visited = {}

    def turn(self, direction: str):
        if direction.lower() == 'r':
            self.state.direction = (self.state.direction[1], -self.state.direction[0])
        if direction.lower() == 'l':
            self.state.direction = (-self.state.direction[1], self.state.direction[0])

    def get_first_position(self, row):
        for i, c in enumerate(row):
            if c == '.':
                return State((0, i), (0, 1))

        raise Exception('No starting position found')

    def get_password(self):
        # print(self.state.position[0])
        # print(self.state.position[1])
        # print(self.state.direction)
        return self.state.__hash__()

    def show_board(self):
        for i in range(self.max_size[0] + 1):  # range(200):
            for j in range(self.max_size[1] + 1):  # range(150):
                if (i, j) in self.visited:
                    if self.visited[(i, j)] == (0, 1):
                        print('>', end='')
                    elif self.visited[(i, j)] == (1, 0):
                        print('v', end='')
                    elif self.visited[(i, j)] == (0, -1):
                        print('<', end='')
                    else:
                        print('^', end='')
                elif (i, j) in self.board:
                    print(self.board[(i, j)], end='')
                else:
                    print(' ', end='')
            print()

        print(self.state, self.max_size)


def set_board(proposed_board: list[list[str]]) -> tuple[defaultdict, defaultdict, tuple[int, int]]:

    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)
    UP = (-1, 0)

    board = defaultdict(lambda: None)
    edge_transition = defaultdict(lambda: None)

    max_size = (0, 0)

    for row_index, row in enumerate(proposed_board):
        for column_index, element in enumerate(row):
            if element == '.' or element == '#':
                board[(row_index, column_index)] = element
                if row_index > max_size[0]:
                    max_size = (row_index, max_size[1])
                if column_index > max_size[1]:
                    max_size = (max_size[0], column_index)

    # hardcode edge transitions
    # test for part 1 test input
    # for i in range(4):
    #     edge_transition[State((0-1, i+8), 3)] = State((11, i+8), 3)
    #     edge_transition[State((11+1, i+8), 1)] = State((0, i+8), 1)

    #     edge_transition[State((4-1, i), 3)] = State((7, i), 3)
    #     edge_transition[State((7+1, i), 1)] = State((4, i), 1)

    #     edge_transition[State((4-1, i+4), 3)] = State((7, i+4), 3)
    #     edge_transition[State((7+1, i+4), 1)] = State((4, i+4), 1)

    #     edge_transition[State((8-1, i+12), 3)] = State((11, i+12), 3)
    #     edge_transition[State((11+1, i+12), 1)] = State((8, i+12), 1)

    #     edge_transition[State((i, 8-1), 2)] = State((i, 11), 2)
    #     edge_transition[State((i, 11+1), 0)] = State((i, 8), 0)

    #     edge_transition[State((i+4, 0-1), 2)] = State((i+4, 11), 2)
    #     edge_transition[State((i+4, 11+1), 0)] = State((i+4, 0), 0)

    #     edge_transition[State((i+9, 8-1), 2)] = State((i+9, 15), 2)
    #     edge_transition[State((i+9, 15+1), 0)] = State((i+9, 8), 0)

    # test for part 2 test input
    if len(proposed_board) < 50:
        for i in range(4):
            edge_transition[State((i, 8-1), LEFT)] = State((4, 4+i), DOWN)
            edge_transition[State((4-1, 4+i), UP)] = State((i, 8), RIGHT)

            edge_transition[State((0-1, i+8), UP)] = State((4-i, 4), DOWN)
            edge_transition[State((4-i, 4-1), UP)] = State((0, i+8), DOWN)

            edge_transition[State((7+1, i+4), DOWN)] = State((12-i, 8), RIGHT)
            edge_transition[State((12-i, 8-1), LEFT)] = State((7, i+4), UP)

            edge_transition[State((7+1, i), DOWN)] = State((11, 11-i), UP)
            edge_transition[State((11+1, 11-i), DOWN)] = State((7, i), UP)

            edge_transition[State((4+i, 11+1), RIGHT)] = State((8, 15-i), DOWN)
            edge_transition[State((8-1, 15-i), UP)] = State((4+i, 11), LEFT)

            edge_transition[State((8+i, 15+1), RIGHT)] = State((11, 4-i), LEFT)
            edge_transition[State((11+1, 4-i), RIGHT)] = State((8+i, 15), LEFT)

            edge_transition[State((4+i, 0-1), LEFT)] = State((11, 15-i), UP)
            edge_transition[State((11+1, 15-i), DOWN)] = State((4+i, 0), RIGHT)
    else:

        for i in range(50):
            edge_transition[State((100-1, i), UP)] = State((50+i, 50), RIGHT, lambda: print('-1'))
            edge_transition[State((50+i, 50-1), LEFT)] = State((100, i), DOWN, lambda: print('2'))

            edge_transition[State((100+i, 0-1), LEFT)] = State((49-i, 50), RIGHT, lambda: print('3'))
            edge_transition[State((49-i, 50-1), LEFT)] = State((100+i, 0), RIGHT, lambda: print('4'))

            edge_transition[State((49+1, 100+i), DOWN)] = State((50+i, 99), LEFT)
            edge_transition[State((50+i, 99+1), RIGHT)] = State((49, 100+i), UP)

            edge_transition[State((149+1, 50+i), DOWN)] = State((150+i, 49), LEFT)
            edge_transition[State((150+i, 49+1), RIGHT)] = State((149, 50+i), UP)

            edge_transition[State((100+i, 99+1), RIGHT)] = State((49-i, 149), LEFT)
            edge_transition[State((49-i, 149+1), RIGHT)] = State((100+i, 99), LEFT)

            edge_transition[State((0-1, 50+i), UP)] = State((150+i, 0), RIGHT)
            edge_transition[State((150+i, 0-1), LEFT)] = State((0, 50+i), DOWN)

            edge_transition[State((0-1, 100+i), UP)] = State((199, i), UP)
            edge_transition[State((199+1, i), DOWN)] = State((0, 100+i), DOWN)

    return board, edge_transition, max_size


def instructions(row: str) -> list[Instruction]:
    steps = ''
    operations = row + 'M'
    for c in operations:
        if not c.isnumeric():
            yield Instruction(int(steps), c)
            steps = ''
        else:
            steps += c


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        character = Character(data)
        character.visited[character.state.position] = character.state.direction

        for index, instruction in enumerate(instructions(data[-1])):
            steps = 0

            for _ in range(instruction.steps):

                update = character.state.direction

                next_state = character.state + update

                if next_state in character.edge_transition:
                    assert next_state + update not in character.board
                    next_state = character.edge_transition[next_state].__copy__()

                if character.board[next_state.position] == '#':
                    next_state = character.state
                    break

                if next_state.direction != character.state.direction:
                    character.visited[character.state.position] = character.state.direction
                else:
                    character.visited[character.state.position] = next_state.direction
                character.state = next_state

                character.visited[character.state.position] = character.state.direction

            character.turn(instruction.direction)

        answer = character.get_password()
        # character.show_board()
        print(answer)


if __name__ == '__main__':
    main()
