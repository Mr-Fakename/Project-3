from movements import Position


class Player(Position):

    def __init__(self, map):
        self.map = map
        self.start = list(self.map.start)[0]
        # Converts the data structure to be used as unpacked coordinates
        super().__init__(self.start[0], self.start[1])


class Enemies(Position):

    def __init__(self, map):
        self.map = map
        self.start = list(self.map.enemies)[0]
        super().__init__(self.start[0], self.start[1])
