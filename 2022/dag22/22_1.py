import sys

class Character:
    def __init__(self, data) -> None:
        self.prev = None
        self.current = self.get_first_position(data[0])
        self.board = data[:-2]
        self.instructions = self.set_instructions(data[-1])
        self.direction  = 0 # 

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
            
    def set_instructions(self, row: str):
        instructions = []
        steps = ''
        operations = row + 'M'
        for c in operations:
            if not c.isnumeric():
                instructions.append((int(steps), c))
                steps = ''
            else:
                steps += c
        
        return instructions

    def get_instruction(self):
        for instruction in self.instructions:
            yield instruction
    
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
        return 1000 * (self.current[0] + 1) + 4 * (self.current[1] + 1) + self.direction


def main():
    
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        character = Character(data)

        for instruction in character.get_instruction():
            steps = 0
            current_position = character.current
            update = character.get_update()
            next_position = current_position
            next_position = (next_position[0] + update[0], next_position[1] + update[1])
            
            while steps < instruction[0] and character.board[next_position[0]][next_position[1]] == '.':
                character.prev = character.current
                next_position = (next_position[0] + update[0], next_position[1] + update[1])
            
                steps += 1
            next_position = (next_position[0] - update[0], next_position[1] - update[1])
            
            character.current = next_position
            character.turn(instruction[1])
            print(character.current)
        print(character.get_password())
if __name__ == '__main__':
    main()