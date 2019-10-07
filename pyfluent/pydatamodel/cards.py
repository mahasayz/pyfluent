import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """
    Class to show the usage of namedtuple and special methods: __getitem__ and __len__
    >> deck = FrenchDeck()
    >> len(deck)
    52
    >> deck[0]
    Card(rank='2', suit='spades')
    >> from random import choice
    >> choice(deck)
    Card(rank='3', suit='hearts')
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
