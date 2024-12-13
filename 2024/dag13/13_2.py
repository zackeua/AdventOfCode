import sys
import re


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, o):
        self.x += o.x
        self.y += o.y
        return Coordinate(self.x, self.y)

    def scale(self, n):
        return Coordinate(self.x * n, self.y * n)

    def __eq__(self, o):
        return (self.x, self.y) == (o.x, o.y)

    def __repr__(self):
        return f'({self.x}, {self.y})'


def solve_game(game: tuple[Coordinate]):

    best_cost = None
    a_cost = 3
    b_cost = 1

    det = game[0].x * game[1].y - game[0].y * game[1].x
    assert det != 0, f'{game[0]}, {game[1]}, {game[2]}'

    a_button_load = (game[1].y * game[2].x - game[1].x * game[2].y)
    b_button_load = (-game[0].y * game[2].x + game[0].x * game[2].y)

    a_button_presses = a_button_load // det
    b_button_presses = b_button_load // det

    if game[0].x * a_button_presses + game[1].x * b_button_presses == game[2].x:
        if game[0].y * a_button_presses + game[1].y * b_button_presses == game[2].y:
            return a_button_presses * a_cost + b_button_presses
    return 0


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()

    button_expression = re.compile(r'Button .: ..(\d+), ..(\d+)')
    prize_expression = re.compile(r'Prize: .=(\d+), .=(\d+)')
    games = []
    i = 0
    while i < len(data):
        button_a_group = button_expression.findall(data[i])
        button_b_group = button_expression.findall(data[i + 1])
        prize_group = prize_expression.findall(data[i + 2])
        a_button = Coordinate(
            int(button_a_group[0][0]), int(button_a_group[0][1]))
        b_button = Coordinate(
            int(button_b_group[0][0]), int(button_b_group[0][1]))
        extra = 10000000000000
        prize_location = Coordinate(
            int(prize_group[0][0]) + extra, int(prize_group[0][1]) + extra)
        games.append((a_button, b_button, prize_location))
        i += 4

    total = 0

    for game in games:
        total += solve_game(game)
    print(total)


if __name__ == '__main__':
    main()
