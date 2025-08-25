import sys


def compare(num1, num2):
    if num1 > num2:
        return True, [num1, num2]
    else:
        return False, [num2, num1]


def play(decks):
    player1 = decks[0]
    player2 = decks[1]

    round_index = 0
    while len(player1) != 0 and len(player2) != 0:
        round_index += 1
        print(f'-- Round {round_index} --')
        card1 = player1[0]
        card2 = player2[0]
        print(f"Player 1's deck: {player1}")
        print(f"Player 2's deck: {player2}")
        print(f"Player 1 plays: {card1}")
        print(f"Player 2 plays: {card2}")
        player1 = player1[1:]
        player2 = player2[1:]

        check, cards = compare(card1, card2)
        if check:
            player1.extend(cards)
        else:
            player2.extend(cards)
        print(f'Player {1 if check else 2} wins the round!')

    print(f'== Post-game results ==')
    print(f"Player 1's deck: {player1}")
    print(f"Player 2's deck: {player2}")

    if len(player1) != 0:
        winner = player1
    else:
        winner = player2
    score = sum([w*i for w, i in zip(range(1, len(winner)+1), winner[::-1])])
    print(score)


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.read()
        data = data.split('\n\n')
        data = [list(map(int, row.split('\n')[1:])) for row in data]
        print(data)
        play(data)


if __name__ == '__main__':
    main()
