import sys
from collections import defaultdict


class Instruction:
    def __init__(self, steps: int, turn: str) -> None:
        self.steps = steps
        self.direction = turn

class Character:
    def __init__(self, data) -> None:
        self.prev = None
        self.current = self.get_first_position(data[0])
        self.board = set_board(data[:-2])
        self.direction  = 0 # 
        self.size = (len(data[:-2]), max([len(row) for row in data[:-2]]))

    def turn(self, direction: str):
        if direction.lower() == 'r':
            self.direction += 1 
        if direction.lower() == 'l':
            self.direction -= 1 

        self.direction = self.direction % 4
    
    def get_first_position(self, row):
        for i, c in enumerate(row):
            if c == '.':
                return (0, i)
    
    def get_update(self):
        if self.direction == 0:
            return (0, 1)
        elif self.direction == 1:
            return (1, 0)
        elif self.direction == 2:
            return (0, -1)
        else:
            return (-1, 0)
    
    def get_password(self):
        #print(self.current[0])
        #print(self.current[1])
        #print(self.direction)

        return 1000 * (self.current[0] + 1) + 4 * (self.current[1] + 1) + self.direction

def compose_update(current_position, update, size, board):
    #print(current_position, update)
    while board[current_position] == None:
        current_position = (0 if current_position[0] >= size[0] else size[0] if current_position[0] < 0 else (current_position[0] + update[0]), 0 if current_position[1] >= size[1] else size[1] if current_position[1] < 0 else (current_position[1] + update[1]))
    return (0 if current_position[0] >= size[0] else size[0] if current_position[0] < 0 else (current_position[0] + update[0]), 0 if current_position[1] >= size[1] else size[1] if current_position[1] < 0 else (current_position[1] + update[1]))

def set_board(proposed_board: list[list[str]]) -> defaultdict:
    board = defaultdict(lambda: None)
    for row_index, row in enumerate(proposed_board):
        for column_index, element in enumerate(row):
            if element == '.' or element == '#':
                board[(row_index, column_index)] = element
    return board


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
        print(character.current)
        for instruction in instructions(data[-1]):
            steps = 0
            update = character.get_update()

            next_position = compose_update(character.current, update, character.size, character.board)
            
            while steps < instruction.steps and character.board[next_position] != '#':
                character.prev = next_position

                next_position = compose_update(next_position, update, character.size, character.board)
                steps += 1

            next_position = (next_position[0] - update[0], next_position[1] - update[1])

            character.current = next_position
            character.turn(instruction.direction)
            print(character.current)
        print(character.get_password())

if __name__ == '__main__':
    main()