import pygame

pygame.init()

size = width, height = 800, 800
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)


class Map:
    wall_selection_images = pygame.image.load("floor-tiles-20x20.png").convert_alpha()
    wall_image = wall_selection_images.subsurface((300, 20, 40, 40))
    X = wall_image
    self.rect(self.rect.x, self.rect.y)
    self.image
    ### subsurface((x_left_corner, y_left_corner, width, height))

    ### Don't forget to implement a refresh everytime an event occurs, maps stays in BG
    ### Can't walk on walls, can't go out of the grid

    def __init__(self):
        self.width = 15
        self.height = 15
        self.maze = [XXXXXXXXXXXXXXX,
                     X....XXXXXXXXXX,
                     XXX......XXXXXX,
                     XXXXX...XXXXXXX,
                     XXXXX....XXXXXX,
                     XXXXXXXXXXXXXXX,
                     XXXXXXXXXXXXXXX,
                     XXXXXXXXXXXXXXX,
                     XXXXXXXXXXXXXXX,
                     XXXXXXXXXXXXXXX,
                     XXXXXXXXXXXXXXX,
                     XXXXXXXXXXXXXXX,
                     XXXXXXXXXXXXXXX,
                     XXXXXXXXXXXXXXX,
                     XXXXXXXXXXXXXXX, ]


class Positions:
    def __init__(self, x, y):
        self.pos = (x, y)
    pass

    def __hash__(self):
        return hash(self.position)
    pass


maze = Map

walls = set()
path = set()

for x in maze.width:
    for y in maze.height:
        # create tuple list for each X x, y
        if X:
            self.walls.add(pos(x, y))
            blit(wall_image)

        # create tuple list for each empty x, y
        if empty:
            self.path.ad(pos(x, y))


