import sys
import functools

# global_game_id = 1

game_memory = ()


def make_tuple(arg):
    return tuple([tuple(row) for row in arg])


def play_round(player_1_deck, player_2_deck):
    # print(player_1_deck, player_2_deck)
    global game_memory
    if (player_1_deck, player_2_deck) in game_memory:
        return player_1_deck, (), 3

    card1, player_1_deck = player_1_deck[0], player_1_deck[1:]
    card2, player_2_deck = player_2_deck[0], player_2_deck[1:]

    winner = -1
    if card1 <= len(player_1_deck) and card2 <= len(player_2_deck):
        # global_game_id += 1
        tmp_player_1_deck, tmp_player_2_deck, winner = play_game(
            player_1_deck[:card1], player_2_deck[:card2], True)
        # input()
        if winner == 3:
            return tmp_player_1_deck, None, 3
        if winner == 1:
            player_1_deck += (card1, card2)
        else:
            player_2_deck += (card2, card1)
    elif card1 > card2:
        player_1_deck += (card1, card2)
        winner = 1
    else:
        player_2_deck += (card2, card1)
        winner = 2
    return player_1_deck, player_2_deck, winner


def play_game(player_1_deck: tuple[int], player_2_deck: tuple[int], run_greedy_checks: bool = False):
    if run_greedy_checks:
        all_cards = player_1_deck
        all_cards += player_2_deck

        if max(all_cards) in player_1_deck:
            return None, None, 1
        else:
            return None, None, 2

    # round_index = 0
    # this_game_id = global_game_id + 0
    winner = -1
    while len(player_1_deck) != 0 and len(player_2_deck) != 0:
        # round_index += 1
        player_1_deck, player_2_deck, winner = play_round(
            player_1_deck, player_2_deck)

    game_winner = (1 if len(player_1_deck) > len(
        player_2_deck) or winner == 3 else 2)
    return player_1_deck, player_2_deck, game_winner


def calculate_score(cards):
    return sum(w * i for w, i in enumerate(cards[::-1], 1))


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.read()
        data = data.split('\n\n')
        data = [list(map(int, row.split('\n')[1:])) for row in data]
        player_1_cards = tuple(data[0])
        player_2_cards = tuple(data[1])
        player_1_cards, player_2_cards, winner = play_game(
            player_1_cards, player_2_cards)
        if winner == 1:
            total = calculate_score(player_1_cards)
        else:
            total = calculate_score(player_2_cards)
        print(player_1_cards)
        print(player_2_cards)
        print(total)
        assert total > 31702
        assert total < 33799
        assert total < 38268


if __name__ == '__main__':
    main()
