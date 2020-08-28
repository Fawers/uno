import random
from typing import List, Optional

from .card import Card


class Player:
    def __init__(self, id):
        self.__id = id
        self.__hand: List[Card] = []

    def __repr__(self):
        return f"Player({self.__id})"

    def draw(self, deck: List[Card]):
        self.__hand.append(deck.pop(0))

    def choose_random_valid_card(self, card_on_stack: Card) -> Optional[Card]:
        valid_cards = [c for c in self.__hand if c.can_be_placed_onto(card_on_stack)]

        if valid_cards:
            card = random.choice(valid_cards)
            self.__hand.remove(card)
            return card

        return None
