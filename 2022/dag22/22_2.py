import sys
from collections import defaultdict
from typing import Any


class Transition:
    def __init__(self, current_position, next_position, update_direction) -> None:
        self.current_position = current_position
        self.next_position = next_position
        self.update_direction = update_direction

    def __call__(self, current_position, update_direction) -> tuple[int, int]:
        if current_position == self.current_position and self.update_direction == update_direction:
            return self.next_position
        else:
            return current_position

class Instruction:
    def __init__(self, steps: int, turn: str) -> None:
        self.steps = steps
        self.direction = turn

class State:
    def __init__(self, position, direction) -> None:
        self.position = position
        self.direction = direction

    def __add__(self, update: tuple[int, int]):
        return State((self.position[0] + update[0], self.position[1] + update[1]), self.direction)

    def __eq__(self, __value: object) -> bool:
        return self.position == __value.position and self.direction == self.direction 

    def __hash__(self) -> int:
        return self.position[0] + self.position[1]*1000 + self.direction*1_000_000

class Character:
    def __init__(self, data) -> None:
        self.state = self.get_first_position(data[0])
        self.board, self.edge_transition = set_board(data[:-2])
        self.visited = {}

    def turn(self, direction: str):
        if direction.lower() == 'r':
            self.state.direction += 1 
        if direction.lower() == 'l':
            self.state.direction -= 1 

        self.state.direction = self.state.direction % 4
    
    def get_first_position(self, row):
        for i, c in enumerate(row):
            if c == '.':
                return State((0, i), 0)
        return State((0, 0), 0) # just to make IntelliSense play well
    
    def get_update(self):
        if self.state.direction == 0:
            return (0, 1)
        elif self.state.direction == 1:
            return (1, 0)
        elif self.state.direction == 2:
            return (0, -1)
        else:
            return (-1, 0)
    
    def get_password(self):
        #print(self.state.position[0])
        #print(self.state.position[1])
        #print(self.state.direction)

        return 1000 * (self.state.position[0] + 1) + 4 * (self.state.position[1] + 1) + self.state.direction

    def show_board(self):
        for i in range(200):
            for j in range(150):
                if (i, j) in self.visited:
                    if self.visited[(i, j)] == 0:
                        print('>', end='')
                    elif self.visited[(i, j)] == 1:
                        print('v', end='')
                    elif self.visited[(i, j)] == 2:
                        print('<', end='')
                    else:
                        print('^', end='')
                elif (i, j) in self.board:
                    print(self.board[(i, j)], end='')
                else:
                    print(' ', end='')
            print()
        

def move(current_state: State, update: tuple[int, int], board: defaultdict, edge_transition: defaultdict):

    next_state = current_state + update

    if edge_transition[next_state]:
        next_state = edge_transition[next_state]
    
    if board[next_state.position] != '.':
        return current_state

    return next_state
        
def set_board(proposed_board: list[list[str]]) -> defaultdict:

    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

    board = defaultdict(lambda: None)
    edge_transition = defaultdict(lambda: None)
    
    
    for row_index, row in enumerate(proposed_board):
        for column_index, element in enumerate(row):
            if element == '.' or element == '#':
                board[(row_index, column_index)] = element

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
    # for i in range(4):
    #     edge_transition[State((i, 8-1), 2)] = State((4+i, 4), 1)
    #     edge_transition[State((4+i, 4-1), 3)] = State((i, 8), 0)

    #     edge_transition[State((0-1, i+8), 3)] = State((4-i, 4), 1)
    #     edge_transition[State((4-i, 4-1), 3)] = State((0, i+8), 1)

    #     edge_transition[State((7+1, i+4), 1)] = State((12-i, 8), 0)
    #     edge_transition[State((12-i, 8-1), 2)] = State((7, i+4), 3)

    #     edge_transition[State((7+1, i), 1)] = State((11, 11-i), 3)
    #     edge_transition[State((11+1, 11-i), 1)] = State((7, i), 3)

    #     edge_transition[State((4+i, 11+1), 0)] = State((8, 15-i), 1)
    #     edge_transition[State((8-1, 15-i), 3)] = State((4+i, 11), 2)

    #     edge_transition[State((8+i, 15+1), 0)] = State((11, 4-i), 2)
    #     edge_transition[State((11+1, 4-i), 0)] = State((8+i, 15), 2)

    #     edge_transition[State((4+i, 0-1), 2)] = State((11, 15-i), 3)
    #     edge_transition[State((11+1, 15-i), 1)] = State((4+i, 0), 0)


    for i in range(50):
        edge_transition[State((100-1, i), UP)] = State((50+i, 50), RIGHT)
        edge_transition[State((50+i, 50-1), LEFT)] = State((100, i), DOWN)

        edge_transition[State((100+i, 0-1), LEFT)] = State((49-i, 50), RIGHT)
        edge_transition[State((49-i, 50-1), LEFT)] = State((100+i, 0), RIGHT)

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

    return board, edge_transition


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
        print(character.state.position)
        character.visited[character.state.position] = character.state.direction

        for instruction in instructions(data[-1]):
            steps = 0

            while steps < instruction.steps:
                update = character.get_update()
                
                character.state = move(character.state, update, character.board, character.edge_transition)
                character.visited[character.state.position] = character.state.direction
                steps += 1
                print(character.state.position)

            print(f'Update: {update}')
            character.show_board()
            character.turn(instruction.direction)
            print(character.state.position)
        answer = character.get_password()
        assert answer < 21270
        assert answer < 94299
        print(answer)

if __name__ == '__main__':
    main()