SPRITE_HEIGHT = 30
SPRITE_WIDTH = 30


class Map:

    def __init__(self, configfile):
        self.configfile = configfile

        self.paths = set()
        self.paths_sprite = set()

        self.start = set()
        self.start_sprite = set()

        self.goal = set()
        self.goal_sprite = set()

        self.walls = set()
        self.walls_sprite = set()

        self.load_from_file()

    def load_from_file(self):
        with open(self.configfile) as file:
            for x, line in enumerate(file):
                for y, col in enumerate(line):
                    if col == ".":
                        self.paths.add((x, y))
                        self.paths_sprite.add((x * SPRITE_HEIGHT, y * SPRITE_WIDTH))
                    elif col == "S":
                        self.start.add((x, y))
                        self.start_sprite.add((x * SPRITE_HEIGHT, y * SPRITE_WIDTH))
                        self.paths.add((x, y))
                    elif col == "G":
                        self.goal.add((x, y))
                        self.paths.add((x, y))
                    else:
                        self.walls.add((x, y))
                        pass

    # @property
    # def adapt_to_sprite(self):
    #     sprites_coords = []
    #     for item in list(self.paths):
    #         sprites_coords.append(x * 30)
    #         print(sprites_coords)


    # y = tuple([z * 10 for z in img.size])
    # tuple(10*x for x in img.size)


map = Map("config.txt")
print(map.paths)
print(list(map.paths))
print(map.adapt_to_sprite)

