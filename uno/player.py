import random
from itertools import groupby
from typing import List, Optional

from .card import Card, CardColor


class Player:
    def __init__(self, id):
        self.__id = id
        self.__hand: List[Card] = []

    def __repr__(self):
        return f"Player({self.__id})"

    def draw(self, deck: List[Card]):
        self.__hand.append(deck.pop(0))

    def hand_is_empty(self) -> bool:
        return not self.__hand

    def play_random_valid_card(self, card_on_stack: Card) -> Optional[Card]:
        valid_cards = self.__get_playable_cards(card_on_stack)

        if valid_cards:
            card = random.choice(valid_cards)
            self.__hand.remove(card)
            return card

        return None

    def play_best_valid_card(self, card_on_stack: Card) -> Optional[Card]:
        valid_cards = self.__get_playable_cards(card_on_stack)

        if not valid_cards:
            return None

        # See commit message for explanation.
        cards_by_color = sorted(valid_cards, key=lambda c: (c.color, c.face))
        cards_by_color = groupby(cards_by_color, key=lambda c: (c.color, c.face))
        cards_by_color = [
            (face, list(cards)) for ((color, face), cards) in cards_by_color
            if color == card_on_stack.color]

        cards_by_face = sorted(valid_cards, key=lambda c: (c.face, c.color))
        cards_by_face = groupby(cards_by_face, key=lambda c: (c.face, c.color))
        cards_by_face = [
            (color, list(cards)) for ((face, color), cards) in cards_by_face
            if face == card_on_stack.face]

        if len(cards_by_color) >= len(cards_by_face):
            # cards_by_color: [(Face, [Card])]
            cards = cards_by_color

        else:
            # cards_by_face: List[Tuple[Color, List[Card]]]
            cards = cards_by_face

        card = max(cards, key=lambda t: len(t[1]))[1][-1]
        self.__hand.remove(card)
        return card

    def __get_playable_cards(self, card_on_stack: Card) -> List[Card]:
        return [c for c in self.__hand if c.can_be_placed_onto(card_on_stack)]

    @property
    def hand(self):
        return self.__hand


def test():
    p = Player(1)
    p.hand.extend([
        Card(4, CardColor.RED),
        Card(4, CardColor.GREEN),
        Card(4, CardColor.BLUE),
        Card(4, CardColor.YELLOW),
        Card(5, CardColor.YELLOW)])
    c = p.play_random_valid_card(Card(4, CardColor.RED))
    print(f"\033[36;1m{c}\033[0m")
    p.hand.append(c)
    c = p.play_best_valid_card(Card(4, CardColor.RED))
    print(f"\033[35;1m{c}\033[0m")
    p.hand.append(c)
    c = p.play_best_valid_card(Card(7, CardColor.YELLOW))
    print(f"\033[35;1m{c}\033[0m")
    p.hand.append(c)
    p.hand.append(Card(5, CardColor.YELLOW))
    c = p.play_best_valid_card(Card(7, CardColor.YELLOW))
    print(f"\033[35;1m{c}\033[0m")
    p.hand.append(c)


#test()
