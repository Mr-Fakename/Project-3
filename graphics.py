import sys
import pygame
# from setup import *
from map import *
from movements import *
from characters import *

SPRITE_WIDTH = 20
SPRITE_HEIGHT = 20

pygame.init()
pygame.display.init()

size = width, height = 300, 300
# speed = [2, 2]
# black = 0, 0, 0

screen = pygame.display.set_mode((width, height))

# background = pygame.Surface(screen.get_size())
# background = background.convert()
# background.fill((150, 150, 250))
# screen.blit(background, (0, 0))
# pygame.display.flip()

wall_sprites = pygame.image.load("floor-tiles-20x20.png").convert()
wall_sprite = wall_sprites.subsurface((320, 0, 20, 20))
goal_sprite = wall_sprites.subsurface((160, 20, 20, 20))
start_sprite = pygame.image.load("MacGyver.png").convert()
start_sprite = pygame.transform.scale(start_sprite, (SPRITE_WIDTH, SPRITE_HEIGHT))

map = Map("config.txt")
player = Player(map)

# print(player.position)
# player.valid_move("move_right")
# print(player.position)

for item in map.walls:
    # print(item)
    # print(type(item))
    screen.blit(wall_sprite, (item[1] * SPRITE_WIDTH, item[0] * SPRITE_HEIGHT))
    pygame.display.flip()

player_sprite = start_sprite
screen.blit(player_sprite, (player.position[1] * SPRITE_WIDTH, player.position[0] * SPRITE_HEIGHT))
pygame.display.flip()
player.valid_move("move_down")
screen.blit(player_sprite, (player.position[1] * SPRITE_WIDTH, player.position[0] * SPRITE_HEIGHT))
# pygame.display.flip()
pygame.display.update()

player.valid_move("move_down")
screen.blit(player_sprite, (player.position[1] * SPRITE_WIDTH, player.position[0] * SPRITE_HEIGHT))
pygame.display.flip()
# print(player.position)
# print(player.y, player.x)
# player.valid_move("move_down")
# print(player.position)
# print(player.y, player.x)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT or event.key == ord('a'):
        #         print('left')
        #     if event.key == pygame.K_RIGHT or event.key == ord('d'):
        #         print('right')
        #     if event.key == pygame.K_UP or event.key == ord('w'):
        #         print('jump')
        # pygame.display.flip()
