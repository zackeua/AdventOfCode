import sys

class Hand:
    def __init__(self, cards, bid) -> None:
        self.cards:str = cards
        self.bid = int(bid) 
        #print(self.get_val())

    def __repr__(self) -> str:
        return f'({self.cards}, {self.bid})'

    def five_of_a_kind(self) -> bool:
        return self.cards.count(self.cards[0]) == 5
    def four_of_a_kind(self) -> bool:
        return self.cards.count(self.cards[0]) == 4 or self.cards.count(self.cards[1]) == 4

    def full_house(self) -> bool:
        pair = False
        three = False

        for i in range(5):
            if self.cards.count(self.cards[i]) == 3:
                three = True
            elif self.cards.count(self.cards[i]) == 2:
                pair = True

        return three and pair

    def n_of_a_kind(self, n) -> bool:
        n_kind = False
        for i in range(5):
            if self.cards.count(self.cards[i]) == n:
                n_kind = True
        return n_kind

    def two_pair(self) -> bool:
        first_pair = None
        second_pair = None

        for i in range(5):
            if self.cards.count(self.cards[i]) == 2:
                if first_pair == None:
                    first_pair = self.cards[i]
                elif second_pair == None and  first_pair != self.cards[i]:
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
            return (6, hand_to_num(self.cards))
        elif self.four_of_a_kind():
            return (5, hand_to_num(self.cards))
        elif self.full_house():
            return (4, hand_to_num(self.cards))
        elif self.n_of_a_kind(3):
            return (3, hand_to_num(self.cards))
        elif self.two_pair():
            return (2, hand_to_num(self.cards))
        elif self.n_of_a_kind(2):
            return (1, hand_to_num(self.cards))
        elif self.high_card():
            return (0, hand_to_num(self.cards))
        
        print(self.__repr__())
        assert False # sgould not be here
        return (0, 0)

def hand_to_num(hand):
    total = 0
    for val in hand:
        total *= 15
        if val == 'A':
            total += 14
        elif val == 'K':
            total += 13
        elif val == 'Q':
            total += 12
        elif val == 'J':
            total += 11
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
        #print(hands)
        hands.sort(key=lambda x: x.get_val())

        total = 0

        for rank, hand in enumerate(hands, start=1):
            total += rank * hand.bid
        print(total)


if __name__ == '__main__':
    main()