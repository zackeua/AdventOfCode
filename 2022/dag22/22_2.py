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

def move(current_state: State, update: tuple[int, int], board: defaultdict, edge_transition: defaultdict):

    next_state = current_state + update

    if edge_transition[next_state]:
        next_state = edge_transition[next_state]
    
    if board[next_state.position] != '.':
        return current_state

    return next_state
        
def set_board(proposed_board: list[list[str]]) -> defaultdict:
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
        edge_transition[State((100-1, i), 3)] = State((50+i, 50), 0)
        edge_transition[State((50+i, 50-1), 2)] = State((100, i), 1)

        edge_transition[State((100+i, 0-1), 2)] = State((49-i, 50), 0)
        edge_transition[State((49-i, 50-1), 2)] = State((100+i, 0), 0)

        edge_transition[State((49+1, 100+i), 1)] = State((50+i, 99), 2)
        edge_transition[State((50+i, 100), 0)] = State((49, 100+i), 3)

        edge_transition[State((150, 50+i), 1)] = State((150+i, 49), 2)
        edge_transition[State((150+i, 50), 0)] = State((149, 50+i), 3)

        edge_transition[State((100+i, 100), 0)] = State((49-i, 149), 2)
        edge_transition[State((49-i, 150), 0)] = State((100+i, 99), 2)

        edge_transition[State((0-1, 50+i), 3)] = State((150+i, 0), 0)
        edge_transition[State((150+i, 0-1), 2)] = State((0, 50+i), 1)

        edge_transition[State((0-1, 100+i), 3)] = State((200-1, i), 3)
        edge_transition[State((200, i), 1)] = State((0, 100+i), 1)



















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
        for instruction in instructions(data[-1]):
            steps = 0

            while steps < instruction.steps:
                update = character.get_update()
                
                character.state = move(character.state, update, character.board, character.edge_transition)
                steps += 1
                print(character.state.position)


            character.turn(instruction.direction)
            print(f'Update: {update}')      
            print(character.state.position)
        answer = character.get_password()
        assert answer < 21270
        print(answer)

if __name__ == '__main__':
    main()