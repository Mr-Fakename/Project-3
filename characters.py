class Player:

    def __init__(self):
        self.position = self.map.start

    def valid_move(self, direction):
        new_position = getattr(self.position, direction)()
        if new_position in map:
            self.position = new_position
