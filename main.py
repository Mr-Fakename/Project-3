import sys
from graphics import *


def main():

    item_index = 0

    while True:

        # Calls on the function in "graphics.py" to get visuals on screen
        display_sprites()
        for wall in map.walls:
            screen.blit(wall_sprite, (wall[1] * SPRITE_WIDTH, wall[0] * SPRITE_HEIGHT))

        # This block outputs the item counter on the top right
        font = pygame.font.Font(None, 20)
        item_count = font.render("items : " + str(item_index), 1, (255, 255, 255))
        screen.blit(item_count, (220, 20))

        for event in pygame.event.get():
            # Stops the game by clicking the cross
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Binds a key press with movement methods, calling on the collision detection function
            if event.type == pygame.KEYDOWN:
                # Refreshes the sprites and avoids them being definitely printed
                background.fill((0, 0, 0))
                if event.key == pygame.K_LEFT or event.key == ord("q"):
                    player.valid_move("move_left")
                if event.key == pygame.K_RIGHT or event.key == ord("d"):
                    player.valid_move("move_right")
                if event.key == pygame.K_UP or event.key == ord("z"):
                    player.valid_move("move_up")
                if event.key == pygame.K_DOWN or event.key == ord("s"):
                    player.valid_move("move_down")

            # Handles item pick up by making them go offscreen and adding 1 to the item count
            if player.position == items[0].position:
                items[0].position = 100, 100
                item_index += 1
            if player.position == items[1].position:
                items[1].position = 100, 100
                item_index += 1
            if player.position == items[2].position:
                items[2].position = 100, 100
                item_index += 1

        # Updates the items on screen
        pygame.display.flip()

        # When the player gets to the enemy, triggers the end of the game
        if player.position == enemy.position:
            # If the player gathered the items, they can proceed and escape
            if item_index == 3:
                end_screen(screen, "You win!")
            # If they didn't get the items, they die
            else:
                end_screen(screen, "You die")
            pygame.display.flip()
            pygame.time.wait(60000)
            break


if __name__ == "__main__":
    main()
