from typing import List

from .card import Card


class Player:
    def __init__(self, id):
        self.__id = id
        self.__hand: List[Card] = []

    def __repr__(self):
        return f"Player({self.__id})"

    def draw(self, deck: List[Card]) -> None:
        self.__hand.append(deck.pop(0))
