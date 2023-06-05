# War Card Game

Creating a simple command-line implementation of the War card game using Python.

## Game requirements

1. Set up the game:
Shuffle a standard deck of 52 playing cards.
Divide the deck evenly among the players. Each player receives 26 cards.

2. Start the game:
Both players simultaneously reveal the top card of their deck (their "battle" card).

3. Determine the winner of the battle:
The player with the higher card value (Aces high, suits ignored) takes both cards and moves them to their stack.
If the cards have the same value, proceed to a war.

4. Conduct a war:
Each player places the next card from their pile face down, and then another card face-up.
Compare the face-up cards:
- If one player's face-up card has a higher value, that player takes all the cards on the table (including the face-down cards) and adds them to their stack.
- If the face-up cards have the same value, repeat the war by placing another set of face-down/up cards.
- Continue this process until one player's face-up card is higher.

5. End the game:
The game continues until one player has collected all 52 cards in their stack.
The player with all the cards is declared the winner.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/sbudvytis/PeerProjectWarGame.git
```

2. Navigate to the directory:
```bash
cd PeerProjectWarGame
```

3. Make sure you have Python 3.x installed.

## Usage

1. Run the program
```bash
python war_game.py
```
## Additional Notes

The game supports one player.
Aces are considered high, and suits are ignored during comparison.
In case of a war, each player places one face-down card followed by one face-up card.
If a player runs out of cards during a war, they lose the game.
The game continues until one player has all 52 cards in their stack.
