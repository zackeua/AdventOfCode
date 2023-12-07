import sys

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
PAIR = 1
HIGH_CARD = 0


class Hand:
    def __init__(self, cards, bid) -> None:
        self.cards: str = cards
        self.bid = int(bid)

    def __repr__(self) -> str:
        return f'({self.cards}, {self.bid})'

    def five_of_a_kind(self) -> bool:
        if self.cards.count(self.cards[0]) == 5:
            return True
        if self.n_of_a_kind(4, 'J') and self.cards.count('J') == 1:
            return True
        if self.n_of_a_kind(3, 'J') and self.cards.count('J') == 2:
            return True
        if self.n_of_a_kind(2, 'J') and self.cards.count('J') == 3:
            return True
        if self.n_of_a_kind(1, 'J') and self.cards.count('J') == 4:
            return True

        return False

    def four_of_a_kind(self) -> bool:
        if self.cards.count(self.cards[0]) == 4 or self.cards.count(self.cards[1]) == 4:
            return True
        if self.n_of_a_kind(3, 'J') and self.cards.count('J') == 1:
            return True
        if self.n_of_a_kind(2, 'J') and self.cards.count('J') == 2:
            return True
        if self.n_of_a_kind(1, 'J') and self.cards.count('J') == 3:
            return True
        return False

    def full_house(self) -> bool:
        pair = False
        three = False

        for i in range(5):
            if self.cards[i] != 'J' and self.cards.count(self.cards[i]) == 3:
                three = True
            elif self.cards[i] != 'J' and self.cards.count(self.cards[i]) == 2:
                pair = True

        return three and pair

    def n_of_a_kind(self, n, other='') -> bool:
        for i in range(5):
            if self.cards[i] != other and self.cards.count(self.cards[i]) == n:
                return True

        return False

    def two_pair(self) -> bool:
        first_pair = None
        second_pair = None

        for i in range(5):
            if self.cards.count(self.cards[i]) == 2:
                if first_pair is None:
                    first_pair = self.cards[i]
                elif second_pair is None and first_pair != self.cards[i]:
                    second_pair = self.cards[i]

        return first_pair is not None and second_pair is not None

    def high_card(self) -> bool:
        for i in range(5):
            if self.cards.count(self.cards[i]) == 1:
                continue
            else:
                return False
        return True

    def get_val(self):

        if self.five_of_a_kind():
            return (FIVE_OF_A_KIND, hand_to_num(self.cards))

        elif self.four_of_a_kind():
            return (FOUR_OF_A_KIND, hand_to_num(self.cards))

        elif self.full_house():
            return (FULL_HOUSE, hand_to_num(self.cards))

        elif self.n_of_a_kind(3):
            return (THREE_OF_A_KIND, hand_to_num(self.cards))

        elif self.two_pair():
            if self.cards.count('J') == 1:
                return (FULL_HOUSE, hand_to_num(self.cards))
            elif self.cards.count('J') == 2:
                return (FOUR_OF_A_KIND, hand_to_num(self.cards))
            return (TWO_PAIR, hand_to_num(self.cards))

        elif self.n_of_a_kind(2):
            if self.cards.count('J') == 1:
                return (THREE_OF_A_KIND, hand_to_num(self.cards))
            elif self.cards.count('J') == 2:
                if self.n_of_a_kind(1):
                    return (THREE_OF_A_KIND, hand_to_num(self.cards))

            return (PAIR, hand_to_num(self.cards))

        elif self.high_card():
            if self.cards.count('J') == 1:
                return (PAIR, hand_to_num(self.cards))
            elif self.cards.count('J') == 2:
                return (THREE_OF_A_KIND, hand_to_num(self.cards))
            return (HIGH_CARD, hand_to_num(self.cards))

        print(self.__repr__())
        assert False  # sgould not be here
        return (0, 0)


def hand_to_num(hand):
    total = 0
    for val in hand:
        total *= 14
        if val == 'A':
            total += 13
        elif val == 'K':
            total += 12
        elif val == 'Q':
            total += 11
        elif val == 'J':
            total += 0
        elif val == 'T':
            total += 10
        else:
            total += int(val)
    return total


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [Hand(*line.strip().split()) for line in data]

        hands = data
        # print(hands)
        hands.sort(key=lambda x: x.get_val())

        total = 0

        for rank, hand in enumerate(hands, start=1):
            if rank == FULL_HOUSE:
                assert hand.cards.count('J') != 2
            if rank == HIGH_CARD:
                assert hand.cards.count('J') != 1
            if rank == TWO_PAIR:
                assert hand.cards.count('J') != 1
            total += rank * hand.bid
        print(total)
        assert total > 254833898
        assert total < 254902501
        assert total < 255250490


if __name__ == '__main__':
    main()
