__author__ = 'Jake Mackay'
# A program for simulating blackjack
# The idea is to have two loops, one loop for the dealer and player hands(COMPLETED,
# and a second loop to keep the game going until 21 is reached, or overshot(UNDER CONSTRUCTION).

import random

# Sets names and values for cards and the deck
SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
         "Jack", "Queen", "King"]
VALUES = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
         'Jack': 10, 'Queen': 10, 'King': 10}
PLAYERS = ["Dealer", "Player"]
CARDS = 52
CARDS_PER_HAND = 13

def game():
    # Create a deck as a list of integers from 0 to 51
    deck = list(range(CARDS))

    # Shuffle the deck
    random.shuffle(deck)

    # Sets counter to 0 and begins game
    score = 0
    while score <= 21:

        # Loops for dealer and player
        for i in range(2):
            # Pulls card from deck
            card = deck.pop(0)
            card_value = VALUES[RANKS[card % CARDS_PER_HAND]]

            # Prints card received and card value for later calculations
            print(PLAYERS[i], "got the", RANKS[card % CARDS_PER_HAND], "of", SUITS[card // CARDS_PER_HAND], "\n", "Card value:", card_value)
            score = score + card_value
        # Tests score
        print(score)

game()
