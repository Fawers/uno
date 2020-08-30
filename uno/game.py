import random
from typing import List, Literal

from .card import Card, CardColor
from .player import Player


class Game:
    def __init__(self, num_players: int, interactive: bool,
                 cpu_play_mode: Literal['random', 'best'],
                 random: random.Random):
        self.__interactive = interactive
        self.__random = random

        self.__deck: List[Card] = []
        self.__stack: List[Card] = []

        self.__players: List[Player] = []
        self.__curplayer = 0
        self.__direction = 1
        self.__cpm = cpu_play_mode

        self.__create_deck()
        self.__create_players(num_players)

        for _ in range(7):
            for p in self.__players:
                p.draw(self.__deck)

        self.__stack.append(self.__deck.pop(0))

    def __create_players(self, num_players: int):
        self.__players.extend(Player(i) for i in range(1, num_players+1))

    def __create_deck(self):
        colors_in_order = [CardColor.RED, CardColor.GREEN, CardColor.BLUE, CardColor.YELLOW]

        for color in colors_in_order:
            self.__deck.append(Card(0, color))

        for face in range(1, 10):
            for color in colors_in_order:
                self.__deck.extend([Card(face, color), Card(face, color)])

        self.__random.shuffle(self.__deck)
