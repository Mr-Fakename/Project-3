import sys
import pygame
from map import *

SPRITE_HEIGHT = 30
SPRITE_WIDTH = 30

# IMAGESDICT = {'uncovered goal': pygame.image.load('RedSelector.png'),
#               'ugly tree': pygame.image.load('Tree_Ugly.png')}



# sprite_width = 20
# sprite_height = 20
# pygame.transform.scale(macgyver_image, (sprite_width, sprite_height))

pygame.init()
pygame.display.init()

size = width, height = 300, 300
speed = [2, 2]
black = 0, 0, 0

# screen = pygame.display.set_mode((400, 400), pygame.FULLSCREEN)
screen = pygame.display.set_mode((width, height))

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((150, 150, 250))
screen.blit(background, (0, 0))
pygame.display.flip()

wall = pygame.image.load("mur.png").convert()

while True:

    map = Map("config.txt")

    for position in map.paths_sprite:
        # print(position)
        screen.blit(wall, position)
        pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
