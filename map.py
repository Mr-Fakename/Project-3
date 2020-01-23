class Map:

    def __init__(self, configfile):
        """ This class changes the characters in .txt file to coordinates tuple
            The "configfile" argument represents the level, hence Map() can be used to switch levels ingame
        """
        self.configfile = configfile

        self.paths = set()
        self.start = set()
        self.goal = set()
        self.enemies = set()
        self.walls = set()

        self.load_from_file()

    def load_from_file(self):
        """ Gets x and y coordinates from a .txt file and adds them as tuples in a dedicated set() per item type"""
        with open(self.configfile) as file:
            for x, line in enumerate(file):
                for y, col in enumerate(line):
                    if col == ".":
                        self.paths.add((x, y))
                    elif col == "S":
                        self.start.add((x, y))
                    elif col == "G":
                        self.goal.add((x, y))
                    elif col == "E":
                        self.enemies.add((x, y))
                    else:
                        self.walls.add((x, y))
