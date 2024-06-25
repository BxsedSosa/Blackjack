import sys, os
from random import shuffle


def clear_console() -> None:
    os.system("cls || clear")


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
        self.cards = []
        self.score = 0
        self.under_21 = True

    def get_score(self, card):
        if card[1] == "Ace":
            if self.score + 11 >= 22:
                self.score += 1
            else:
                self.score += 11
        elif card[1] in ["King", "Queen", "Jack"]:
            self.score += 10
        else:
            self.score += int(card[1])

    def check_valid_hand(self):
        if self.score > 21:
            return False

        return True


class Dealer:

    def __init__(self, deck, hand, player_hand):
        self.deck = deck.deck
        self.hand = hand
        self.player_hand = player_hand

    def start_game(self):
        for _ in range(2):
            self.draw_card(self.player_hand)
            self.draw_card(self.hand)

    def draw_card(self, hand):
        card = self.deck.pop()
        hand.cards.append(card)
        hand.get_score(card)


def main():
    deck = Deck()

    while True:
        clear_console()
        player = Hand()
        dealer = Dealer(deck, Hand(), player)
        dealer.start_game()

        while player.under_21:
            print(f"Score: {player.score}, Cards: {player.cards}")
            print(f"Score: {dealer.hand.score}, Cards: {dealer.hand.cards[0]}")
            user_input = input(f"Enter: \n")

            if user_input == "h":
                dealer.draw_card(player.cards)

            if user_input == "s":
                break

            clear_console()

            player.under_21 = player.check_valid_hand()

        user_input = input(f"Continue?:\n")

        if user_input == "f":
            sys.exit()


main()
