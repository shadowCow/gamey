from enum import Enum
from typing import List

class CardValue(Enum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14


class Suit(Enum):
    Clubs = 1
    Diamonds = 2
    Hearts = 3
    Spades = 4


class Card:
    def __init__(
        self,
        value: CardValue,
        suit: Suit,
    ):
        self.value = value
        self.suit = suit


def create_deck() -> List[Card]:
    deck = []

    for suit in Suit:
        for value in CardValue:
            deck.append(Card(value, suit))

    return deck

