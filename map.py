from movements import *


class Map:

    def __init__(self, configfile):
        self.configfile = configfile

        self.paths = set()
        self.start = set()
        self.goal = set()

        # self.walls = set()

        self.load_from_file()

    def __contains__(self, position):
        return position in self.paths

    # @property
    # def start(self):
    #     return list(self.start)[0]

    def load_from_file(self):
        with open(self.configfile) as file:
            for x, line in enumerate(file):
                for y, col in enumerate(line):
                    if col == ".":
                        self.paths.add(Position(x, y))
                    elif col == "S":
                        self.start.add(Position(x, y))
                        self.paths.add(Position(x, y))
                    elif col == "G":
                        self.goal.add(Position(x, y))
                        self.paths.add(Position(x, y))
                    # else:
                    #     self.walls.add((x, y))
                    #     pass

    # @start.setter
    # def start(self, value):
    #     self._start = value

# map = Map("config.txt")
# p = Position(0, 6)

# print(p.move_up().move_up())
# print(p in map)
