class Position:
    def __init__(self, x, y):
        self.position = (x, y)

    def __repr__(self):
        return str(self.position)

    def __hash__(self):
        return hash(self.position)

    def __eq__(self, pos):
        return self.position == pos.position

    @staticmethod
    def move_up(self):
        x, y = self.position
        return self.__class__(x - 1, y)

    def move_right(self):
        x, y = self.position
        return self.__class__(x, y + 1)

    def move_left(self):
        x, y = self.position
        return self.__class__(x, y - 1)

    def move_down(self):
        x, y = self.position
        return self.__class__(x + 1, y)
