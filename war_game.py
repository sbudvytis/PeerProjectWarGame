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

    def players(self):
        deck = Deck()
        player1, player2 = deck.deal_cards()

a = Player("sarunas", "mahedi")
print(a.players)