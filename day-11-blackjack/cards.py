from random import choice

FACES = list([str(i) for i in range(2, 11)]) + list('JQKA')

SUITS = {
    'C': '\N{BLACK CLUB SUIT}',
    'D': '\N{BLACK DIAMOND SUIT}',
    'H': '\N{BLACK HEART SUIT}',
    'S': '\N{BLACK SPADE SUIT}',
}


class Card:

    def __init__(self, shown=True):
        self.face = choice(FACES)
        self.suit = choice(list(SUITS.keys()))
        self.shown = shown  # True or False

    def draw(self):
        """ Returns a list of strings for drawing this card from top to bottom. """
        face = self.face if self.shown else ' '
        suit = SUITS[self.suit] if self.shown else ' '
        pad = ('' if face == '10' else ' ')
        return [
            '┌───────┐',
            '│ ff    │'.replace('ff', face + pad),
            '│       │',
            '│   s   │'.replace('s', suit),
            '│       │',
            '│    ff │'.replace('ff', pad + face),
            '└───────┘',
        ]

    def value(self):
        """ Returns the integer value of this card. """
        if self.face == 'A':
            return 11
        if self.face in ['J', 'Q', 'K']:
            return 10
        return int(self.face)
