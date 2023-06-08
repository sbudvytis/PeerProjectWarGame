import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        ranks = ["14", "13", "12", "11", "10", "9", "8", "7", "6", "6", "5", "4", "3", "2"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(rank,suit) for suit in suits for rank in ranks]
        
    def deal_cards(self):
        random.shuffle(self.cards)
        return (self.cards[:26], self.cards[26:])

class Player:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2


a = Player("sarunas","player2")
deck = Deck()
a.player1, a.player2 = deck.deal_cards()
print(f"\n{input('Player name: ')}'s deck:\n")
for card in a.player2:
    print(card)
print("\nComputer's deck:\n")
for card in a.player1:
    print(card)
print("\n")
print("\n")
print(a.player2.pop())
print(a.player1.pop())

