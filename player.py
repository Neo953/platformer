import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, pos, images):
        super().__init__()
        self.images = images
        self.image = images['p1_jump']
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.xy_speed = pygame.math.Vector2(0,0)
        self.facing = "R"
        2
    def update(self):
        self.image = self.images('p1_jump')
        if self.facing == "L":
            self.image = pygame.transform.flip(self.image, True, False)

    def left(self):
        self.facing = 'L'

    def right(self):
        self.facing = 'R'