from movements import Position
from map import *


class Player(Position):
    def __init__(self, map):
        self.map = map
        self.start = list(self.map.start)[0]
        super().__init__(self.start[0], self.start[1])
