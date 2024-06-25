import sys
from random import shuffle


class Deck:
    suits = ["Spade", "Club", "Clover", "Diamond"]
    values = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]

    def __init__(self):
        self.deck = []
        self.create_deck()

    def create_deck(self):
        self.deck = [[suit, value] for suit in self.suits for value in self.values] * 3
        shuffle(self.deck)


class Hand:

    def __init__(self):
        self.hand = []
        self.score = 0

    def get_score(self, card):
        if card[1] == "Ace":
            if self.score + 11 > 21:
                self.score += 1
            else:
                self.score += 11
        elif card[1] in ["King", "Queen", "Jack"]:
            self.score += 10
        else:
            self.score += int(card[1])

    def draw_card(self, deck):
        card = deck.deck.pop()
        self.hand.append(card)
        self.get_score(card)


class Player:

    def __init__(self, hand):
        self.hand = hand


class Dealer:

    def __init__(self, hand):
        self.hand = hand


def main():
    deck = Deck()
    hand = Hand()
    player = Player()
    dealer = Dealer()

    while True:
        print(hand.hand)
        print(hand.score)

        user_input = input(f"Enter: \n")

        if user_input == "f":
            sys.exit()

        if user_input == "d":
            hand.draw_card(deck)


main()
