from enum import IntFlag


class CardColor(IntFlag):
    RED = 1
    GREEN = 2
    BLUE = 4
    YELLOW = 8
    ANY = 15


class Card:
    def __init__(self, face: int, color: CardColor):
        self.__face = face
        self.__color = color

    @property
    def face(self):
        return self.__face

    @property
    def color(self):
        return self.__color
