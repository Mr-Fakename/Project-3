from movements import Position
from map import *


class Player:

    def __init__(self, map):
        # super().__init__(x, y)
        self.map = map
        self.position = self.map.start

    def move(self, direction):
        """ docstring """
        # getattr can access a property using a string
        new_position = getattr(self.position, direction)()
        if new_position in self.map:
            self.position = new_position


map = Map("config.txt")
player = Player(map)

print(map.start)
print(player.position)
player.position.move_up()
