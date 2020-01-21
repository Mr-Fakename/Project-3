import random
from map import *
from movements import Position


def win_condition():
    if Item.ITEM_INDEX == 3:
        print("You have gathered the items, let's escape!")
        return True
    else:
        print("You die")
        return False


class Item(Position):
    ITEM_INDEX = 0

    def __init__(self, map):
        self.map = map
        self.random_pos = random.choice(list(self.map.paths))
        super().__init__(self.random_pos[1], self.random_pos[0])

    def destroy_item(self, player):
        if self.position == player.position:
            del self
            Item.ITEM_INDEX += 1


map = Map("config.txt")

items = list()
for i in range(3):
    items.append(Item(map))
print(items)

win_condition()
Item.ITEM_INDEX = 3
win_condition()