class Characters:
    def __init__(self, sprite, x, y):
        self.sprite = sprite
        self.pos = (x, y)
        sprite_width = 20
        sprite_height = 20
        pygame.transform.scale(macgyver_image, (sprite_width, sprite_height))

    pass

    self.pos = (x, y)

    def move_right(self):
        self.pos = self.pos(x + 1, y)

    def move_left(self):
        self.pos = self.pos(x - 1, y)

    def move_up(self):
        self.pos = self.pos(x, y - 1)

    def move_down(self):
        self.pos = self.pos(x, y + 1)
