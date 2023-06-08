import random


# Create a class to represent a playing card
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


# Create a class to represent a deck of cards
class Deck:
    def __init__(self):
        ranks = [str(num) for num in range(2, 11)] + list("JQKA")
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    
# Create a class to represent a player
class Player:
    def __init__(self, name):
        self.name = name
        self.stack = []

    def add_cards(self, cards):
        self.stack.extend(cards)

    def is_out_of_cards(self):
        return len(self.stack) == 0


# Create the War game
class WarGame:
    @staticmethod
    def compare_cards(card1, card2):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        return card1 if ranks.index(card1.rank) > ranks.index(card2.rank) else card2

    @staticmethod
    def play_war_game():
        # Set up the game
        deck = Deck()
        deck.shuffle()
        player1 = Player("Player 1")
        player2 = Player("Player 2")

        # Divide the deck evenly among the players
        while len(deck.cards) > 0:
            player1.add_cards([deck.deal_card()])
            player2.add_cards([deck.deal_card()])

        # Start the game
        round_num = 1
        while not player1.is_out_of_cards() and not player2.is_out_of_cards():
            print(f"Round {round_num}:")

            card1 = player1.stack.pop()
            card2 = player2.stack.pop()
            print(f"{player1.name} plays: {card1}")
            print(f"{player2.name} plays: {card2}")

            # Determine the winner of the battle
            if card1.rank == card2.rank:
                print("War!")
                war_cards = [card1, card2]
                while True:
                    if len(player1.stack) == 1 or len(player2.stack) == 1:
                        if len(player1.stack) == 1 and len(player2.stack) > 1:
                            face_up_card1 = player1.stack.pop()
                            war_cards.append(face_up_card1)
                            print(f"{player1.name} plays: {face_up_card1}")

                            face_up_card2 = player2.stack.pop()
                            war_cards.append(face_up_card2)
                            print(f"{player2.name} plays: {face_up_card2}")

                        elif len(player2.stack) == 1 and len(player1.stack) >= 1:
                            face_up_card2 = player2.stack.pop()
                            war_cards.append(face_up_card2)
                            print(f"{player2.name} plays: {face_up_card2}")

                            face_up_card1 = player1.stack.pop()
                            war_cards.append(face_up_card1)
                            print(f"{player1.name} plays: {face_up_card1}")

                        winner = WarGame.compare_cards(face_up_card1, face_up_card2)
                        print(f"{winner} wins the war!")
                        if winner == face_up_card1:
                            player1.add_cards(war_cards)
                        else:
                            player2.add_cards(war_cards)
                        break

                    else:
                        if len(player1.stack) >= 2 and len(player2.stack) >= 2:
                            face_down_card1 = player1.stack.pop()
                            face_down_card2 = player2.stack.pop()
                            war_cards.extend([face_down_card1, face_down_card2])

                            face_up_card1 = player1.stack.pop() if len(player1.stack) > 0 else None
                            face_up_card2 = player2.stack.pop() if len(player2.stack) > 0 else None

                            if face_up_card1:
                                war_cards.append(face_up_card1)
                                print(f"{player1.name} plays: {face_up_card1}")
                            if face_up_card2:
                                war_cards.append(face_up_card2)
                                print(f"{player2.name} plays: {face_up_card2}")

                            if face_up_card1 and face_up_card2 and face_up_card1.rank != face_up_card2.rank:
                                winner = WarGame.compare_cards(face_up_card1, face_up_card2)
                                print(f"{winner} wins the war!")
                                if winner == face_up_card1:
                                    player1.add_cards(war_cards)
                                else:
                                    player2.add_cards(war_cards)
                                break

                            if len(player1.stack) >= 1:
                                player1.add_cards(war_cards)
                            elif len(player2.stack) >= 1:
                                player2.add_cards(war_cards)
                            break

                        else:
                            if len(player1.stack) >= 1:
                                player1.add_cards(war_cards)
                            elif len(player2.stack) >= 1:
                                player2.add_cards(war_cards)
                            break


            else:
                winner = WarGame.compare_cards(card1, card2)
                print(f"{winner} wins the battle!")
                if winner == card1:
                    player1.add_cards([card1, card2])
                else:
                    player2.add_cards([card1, card2])

            round_num += 1
            print(f"{player1.name} has {len(player1.stack)} cards.")
            print(f"{player2.name} has {len(player2.stack)} cards.")
            print("-----------------------")

        # End the game
        if player1.is_out_of_cards():
            print(f"{player2.name} wins the game!")
        else:
            print(f"{player1.name} wins the game!")


# Create an instance of the WarGame class and play the game
game = WarGame()
game.play_war_game()