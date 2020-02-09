# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 17:50:44 2020

@author: micha
"""

import enum
from collections import namedtuple

__all__ = [
        'Player',
        'Point'
]
        

# Using an enum to represent players
class Player(enum.Enum):
    black = 1
    white = 2
    
    @property
    def other(self):
        return Player.black if self == Player.white else Player.white


# using tuples to represent points of a Go board
class Point(namedtuple('Point', 'row col')):
    def neighbors(self):
        return [
            Point(self.row - 1, self.col),
            Point(self.row + 1, self.col),
            Point(self.row, self.col - 1),
            Point(self.row, self.col + 1)
        ]
    
    
    def __deepcopy__(self, memodict={}):
        # These are very immutable.
        return self