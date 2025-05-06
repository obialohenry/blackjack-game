# Blackjack Game

A command-line implementation of the classic casino card game Blackjack (also known as 21).

## Description

This Python-based Blackjack game simulates the experience of playing against a dealer. The game follows standard Blackjack rules where the goal is to have a hand value closer to 21 than the dealer without exceeding it.

### Features:

- Full implementation of basic Blackjack rules
- Dealer AI that hits until reaching a hand value of 17 or higher
- Proper handling of Ace cards (can be worth 1 or 11)
- User-friendly command-line interface with emoji feedback
- Option to hit (take another card) or stand (keep current hand)
- Continuous gameplay with the option to play multiple rounds

### Game Rules:

- Cards are valued at their number (2-10), face cards (Jack, Queen, King) are worth 10, and Aces can be worth 1 or 11
- The player and dealer each start with two cards
- The player can see one of the dealer's cards
- The player can choose to "hit" (take another card) or "stand" (keep current hand)
- If the player's hand exceeds 21, they lose immediately (bust)
- After the player stands, the dealer reveals their cards and hits until reaching at least 17
- The winner is whoever has the highest hand value without exceeding 21

## How to Play

1. Run the script in your terminal
2. When prompted, type 'y' to start a game of Blackjack
3. View your cards and decide whether to hit ('y') or stand ('n')
4. After each game, choose whether to play again

## Requirements

- Python 3.x
- The 'art' package for displaying the Blackjack logo

## Installation

```bash
# Clone this repository
git clone [https://github.com/obialohenry/blackjack-game.git](https://github.com/obialohenry/blackjack-game.git)

# Navigate to the project directory
cd blackjack-game

# Install required packages
pip install art
```

## Usage

```bash
python main.py
```

## Future Improvements

- Implement betting system
- Add split and double down options
- Create a graphical user interface
- Add multiplayer support
