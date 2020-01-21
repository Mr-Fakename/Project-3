class Position:

    def __init__(self, x, y):
        self.position = (x, y)

    def __repr__(self):
        return str(self.position)

    def __hash__(self):
        return hash(self.position)

    def __eq__(self, pos):
        return self.position == pos.position

    def move_up(self):
        x, y = self.position
        return x - 1, y

    def move_right(self):
        x, y = self.position
        return x, y + 1

    def move_left(self):
        x, y = self.position
        return x, y - 1

    def move_down(self):
        x, y = self.position
        return x + 1, y

    def valid_move(self, direction):
        new_position = getattr(self, direction)()
        if new_position not in self.map.walls:
            self.position = new_position
