import sys

class Dice:

    def __init__(self, number_color, color = None) -> None:
        if color is None:
            number, color = number_color.split(' ')
            self.number = int(number)
            self.color = color
        else:
            self.number = number_color
            self.color = color

    def __repr__(self) -> str:
        return f'{self.number}, {self.color}'


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [elem.split(': ')[1].strip() for elem in data]
        data = [[[Dice(dice) for dice in game_round.split(', ')] for game_round in game.split('; ')] for game in data]

        total = 0
        for game in data:
            max_possible_blue = Dice('0 blue')
            max_possible_red = Dice('0 red')
            max_possible_green = Dice('0 green')
            max_possible_other = Dice('0 other')

            for game_round in game:
                for dice in game_round:
                    if dice.color == 'blue':
                        max_possible_blue.number = max([max_possible_blue.number, dice.number])
                    elif dice.color == 'red':
                        max_possible_red.number = max([max_possible_red.number, dice.number])
                    elif dice.color == 'green':
                        max_possible_green.number = max([max_possible_green.number, dice.number])
                    else:
                        max_possible_other.number = max([max_possible_other.number, dice.number])
            power = max_possible_blue.number * max_possible_red.number * max_possible_green.number

            total += power
        print(total)

if __name__ == '__main__':
    main()