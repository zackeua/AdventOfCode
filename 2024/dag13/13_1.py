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
    for i in range(0, 101):
        current_cost = 0
        current_position = Coordinate(0, 0)

        current_position.update(game[0].scale(i))
        current_cost += i * a_cost

        j = 0
        while j < 100 and current_position.x < game[2].x:
            current_position.update(game[1])
            current_cost += b_cost
            j += 1
        # print(current_position, current_cost, game[2])
        if current_position == game[2]:
            # print(current_cost, i, j)
            if best_cost is None or current_cost < best_cost:
                best_cost = current_cost

    # input()
    if best_cost is None:
        return 0
    return best_cost


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
        prize_location = Coordinate(
            int(prize_group[0][0]), int(prize_group[0][1]))
        games.append((a_button, b_button, prize_location))
        i += 4

    total = 0

    for game in games:
        total += solve_game(game)
    print(total)


if __name__ == '__main__':
    main()
