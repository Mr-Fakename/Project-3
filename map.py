class Map:

    def __init__(self, configfile):
        self.configfile = configfile

        self.paths = set()
        self.start = set()
        self.goal = set()

        self.walls = set()

        self.load_from_file()

    def load_from_file(self):
        with open(self.configfile) as file:
            for x, line in enumerate(file):
                for y, col in enumerate(line):
                    if col == ".":
                        self.paths.add((x, y))
                    elif col == "S":
                        self.start.add((x, y))
                    elif col == "G":
                        self.goal.add((x, y))
                    else:
                        self.walls.add((x, y))
