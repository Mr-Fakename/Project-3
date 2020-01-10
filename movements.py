class Position:

    def __init__(self, x, y):
        self.position = (x, y)

    def __eq__(self, pos):
        return self.position == pos.position

    def move_up(self):
        x, y = self.position
        return Position(x - 1, y)

    def move_right(self):
        x, y = self.position
        return Position(x, y + 1)

    def move_left(self):
        x, y = self.position
        return Position(x, y - 1)

    def move_down(self):
        x, y = self.position
        return Position(x + 1, y)


    # def move_right(self):
    #     self.pos = self.pos(x + 1, y)
    #
    # def move_left(self):
    #     self.pos = self.pos(x - 1, y)
    #
    # def move_up(self):
    #     self.pos = self.pos(x, y - 1)
    #
    # def move_down(self):
    #     self.pos = self.pos(x, y + 1)