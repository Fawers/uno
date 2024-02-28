from enum import IntFlag


class CardColor(IntFlag):
    RED = 1
    GREEN = 2
    BLUE = 4
    YELLOW = 8
    ANY = RED | GREEN | BLUE | YELLOW


class CardEffect(IntFlag):
    SKIP = 0x10
    TAKE_2 = 0x20
    TAKE_4 = 0x40
    TAKE_2_OR_4 = TAKE_2 | TAKE_4
    INVERT_DIRECTION = 0x80
    CHANGE_COLOR = 0x100


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

    def can_be_placed_onto(self, card: 'Card') -> bool:
        return self.color in card.color or self.face == card.face

    def __repr__(self):
        return f"Card({self.face}, {self.color.name})"


class SpecialCard(Card):
    @property
    def face(self):
        return self.__face.name  # comes from CardEffect
