import sys
from collections import defaultdict


class Bounds:
    def __init__(self, minimum, maximum) -> None:
        self.minimum = minimum
        self.maximum = maximum

    def __repr__(self) -> str:
        return f'({self.minimum}, {self.maximum})'


class Instruction:
    def __init__(self, steps: int, turn: str) -> None:
        self.steps = steps
        self.direction = turn

class Character:
    def __init__(self, data) -> None:
        self.prev = None
        self.current = self.get_first_position(data[0])
        self.board, self.column_bounds, self.row_bounds = set_board(data[:-2])

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

def move(current_position, update, board, row_bounds, column_bounds):

    match update:
        case (0, 1):
            next_position = (current_position[0], current_position[1] + 1)
            if next_position[1] > row_bounds[next_position[0]].maximum:
                next_position = (next_position[0], row_bounds[next_position[0]].minimum) 
            if board[next_position] != '.':
                return current_position
            return next_position
        case (0, -1):
            next_position = (current_position[0], current_position[1] - 1)
            if next_position[1] < row_bounds[next_position[0]].minimum:
                next_position = (next_position[0], row_bounds[next_position[0]].maximum)
            if board[next_position] != '.':
                return current_position
            return next_position
        case (1, 0):
            next_position = (current_position[0] + 1, current_position[1])
            if next_position[0] > column_bounds[next_position[1]].maximum:
                next_position = (column_bounds[next_position[1]].minimum, next_position[1])
            if board[next_position] != '.':
                return current_position
            return next_position
        case (-1, 0):
            next_position = (current_position[0] - 1, current_position[1])
            if next_position[0] < column_bounds[next_position[1]].minimum:
                next_position = (column_bounds[next_position[1]].maximum, next_position[1])
            if board[next_position] != '.':
                return current_position
            return next_position
        
def set_board(proposed_board: list[list[str]]) -> defaultdict:
    board = defaultdict(lambda: None)
    column_bounds = []
    row_bounds = []
    for _ in range(max([len(row) for row in proposed_board])):
        column_bounds.append(Bounds(-1, -1))
    
    for row_index, row in enumerate(proposed_board):
        row_bounds.append(Bounds(-1, -1))
        for column_index, element in enumerate(row):
            if element == '.' or element == '#':
                board[(row_index, column_index)] = element
                if row_bounds[-1].minimum == -1:
                    row_bounds[-1].minimum = column_index

                if column_bounds[column_index].minimum == -1:
                    column_bounds[column_index].minimum = row_index


            elif element == ' ' or element == '\n':
                if row_bounds[-1].minimum != -1 and row_bounds[-1].maximum == -1:
                    row_bounds[-1].maximum = column_index - 1


                if column_bounds[column_index].minimum != -1 and column_bounds[column_index].maximum == -1:
                    column_bounds[column_index].maximum = row_index - 1


            if column_bounds[column_index].maximum == -1:
                column_bounds[column_index].maximum = len(row) - 1
                if column_bounds[column_index].minimum == -1:
                    for i in range(column_index, -1, -1):
                        if board[(i, column_index)] != None:
                            column_bounds[column_index].minimum = i
            

 
    for column_index, _ in enumerate(column_bounds):
        lower_bound = True
        upper_bound = True
        for row_index, _ in enumerate(row_bounds):
            if lower_bound and board[(row_index, column_index)] not in  (' ', None):
                column_bounds[column_index].minimum = row_index
                lower_bound = False
            elif not lower_bound and upper_bound and board[(row_index, column_index)] in (' ', None):
                upper_bound = False
            elif lower_bound and board[(row_index, column_index)] in (' ', None):
                column_bounds[column_index].minimum = row_index
            elif upper_bound and board[(row_index, column_index)] not in (' ', None):
                column_bounds[column_index].maximum = row_index

    return board, column_bounds[:-1], row_bounds


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
        for instruction in instructions(data[-1]):
            steps = 0
            update = character.get_update()

            while steps < instruction.steps:

                character.current = move(character.current, update, character.board, character.row_bounds, character.column_bounds)
                steps += 1


            character.turn(instruction.direction)      
        answer = character.get_password()
        
        print(answer)

if __name__ == '__main__':
    main()