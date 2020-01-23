import pygame
from characters import *
from map import *
from items import *

SPRITE_WIDTH = 20
SPRITE_HEIGHT = 20

pygame.init()
pygame.display.init()

# Sets up the display
size = width, height = 300, 300
screen = pygame.display.set_mode((width, height))
background = pygame.Surface(screen.get_size())
background = background.convert()

# Loads images and corrects scaling issues
sprites_sheet = pygame.image.load("Resources/floor-tiles-20x20.png").convert()
wall_sprite = sprites_sheet.subsurface((320, 0, 20, 20))
goal_sprite = sprites_sheet.subsurface((160, 20, 20, 20))
hero_sprite = pygame.image.load("Resources/MacGyver.png").convert()
hero_sprite = pygame.transform.scale(hero_sprite, (SPRITE_WIDTH, SPRITE_HEIGHT))
item1_sprite = pygame.image.load("Resources/ether.png").convert()
item1_sprite = pygame.transform.scale(item1_sprite, (SPRITE_WIDTH, SPRITE_HEIGHT))
item2_sprite = pygame.image.load("Resources/seringue.png").convert()
item2_sprite = pygame.transform.scale(item2_sprite, (SPRITE_WIDTH, SPRITE_HEIGHT))
item3_sprite = pygame.image.load("Resources/tube_plastique.png").convert()
item3_sprite = pygame.transform.scale(item3_sprite, (SPRITE_WIDTH, SPRITE_HEIGHT))
enemy_sprite = pygame.image.load("Resources/Gardien.png").convert()
enemy_sprite = pygame.transform.scale(enemy_sprite, (SPRITE_WIDTH, SPRITE_HEIGHT))

# All classes instances that are required for this project
map = Map("config.txt")
player = Player(map)
goal = Goal(map)
enemy = Enemies(map)
# List comprehension that creates all 3 items in the game
items = [Item(map) for x in range(3)]


def display_sprites():
    """ This function applies the sprites on screen at their required positions
    x and y are inversed here to cope with the pygame coordinates system
    """
    # x and y are replaced by the index of the self position as defined in classes __init__
    background.blit(item1_sprite, (items[0].position[1] * SPRITE_WIDTH, items[0].position[0] * SPRITE_HEIGHT))
    background.blit(item2_sprite, (items[1].position[1] * SPRITE_WIDTH, items[1].position[0] * SPRITE_HEIGHT))
    background.blit(item3_sprite, (items[2].position[1] * SPRITE_WIDTH, items[2].position[0] * SPRITE_HEIGHT))
    background.blit(hero_sprite, (player.position[1] * SPRITE_WIDTH, player.position[0] * SPRITE_HEIGHT))
    background.blit(goal_sprite, (goal.position[1] * SPRITE_WIDTH, goal.position[0] * SPRITE_HEIGHT))
    background.blit(enemy_sprite, (enemy.position[1] * SPRITE_WIDTH, enemy.position[0] * SPRITE_HEIGHT))
    screen.blit(background, (0, 0))


def end_screen(screen, message):
    """ The "end_screen" function draws three items on the screen
    The first one, a red rectangle, gets outlined by the second one, a white line
    A text is then printed on top, via the "message" argument
    """
    # The substracted values are here calculated in regards to the two possible messages in the game
    pygame.font.init()
    font = pygame.font.Font(None, 18)
    # First item, rectangle. The color is obtained by its (r, g, b) value
    pygame.draw.rect(screen, (255, 0, 0),
                     ((screen.get_width() / 2) - 75,
                      screen.get_height() / 2 - 20,
                      150, 40), 0)
    # Second item, white outline
    pygame.draw.rect(screen, (255, 255, 255),
                     ((screen.get_width() / 2) - 75,
                      screen.get_height() / 2 - 20,
                      150, 40), 1)
    # Third item, text
    screen.blit(font.render(message, 1, (255, 255, 255)),
                (screen.get_width() / 2 - 28,
                 screen.get_height() / 2 - 40 / 2 + 14))
