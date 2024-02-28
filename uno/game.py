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

    def run(self):
        cpu_play_method = (Player.play_random_valid_card
                           if self.__cpm == 'random'
                           else Player.play_best_valid_card)

        top_card = self.__stack[-1]
        print(f"The game starts with a {top_card}.")

        while len(self.__players) > 1:
            self.__check_deck()
            player = self.__players[self.__curplayer]

            card = cpu_play_method(player, top_card)

            if card is not None:
                self.__stack.append(card)
                top_card = card
                print(f"{player} played a {card}.")

            else:
                player.draw(self.__deck)
                print(f"{player} drew a card.")
                card = cpu_play_method(player, top_card)

                if card is not None:
                    self.__stack.append(card)
                    top_card = card
                    print(f"{player} played a {card}.")

                else:
                    print(f"{player} passed their turn.")

            if player.hand_is_empty():
                print(f"{player} played all their cards.")
                self.__players.remove(player)

                if self.__direction == 1:
                    self.__curplayer %= len(self.__players)
                    continue

            self.__curplayer = (self.__curplayer + self.__direction) % len(self.__players)

        print(f"{self.__players.pop()} lost the game.")

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

    def __check_deck(self):
        if len(self.__deck) <= 4:
            print("Re-shuffling deck")
            top_card = self.__stack.pop()

            self.__random.shuffle(self.__stack)
            self.__deck.extend(self.__stack)
            self.__stack.clear()
            self.__stack.append(top_card)


random.seed(1)
g = Game(3, False, 'random', random._inst)
