import random
from movements import Position


class Item(Position):

    def __init__(self, map):
        self.map = map
        self.random_pos = random.choice(list(self.map.paths))
        # This "random" module implementation is set to randomly spawn items when loaded
        super().__init__(self.random_pos[0], self.random_pos[1])


class Goal(Position):

    def __init__(self, map):
        self.map = map
        self.goal = list(self.map.goal)[0]
        super().__init__(self.goal[0], self.goal[1])
