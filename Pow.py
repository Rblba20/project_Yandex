import random

import pygame


class Pow(pygame.sprite.Sprite):
    def __init__(self, center, height, powerup_images):
        pygame.sprite.Sprite.__init__(self)
        BLACK = (0, 0, 0)
        self.height = height
        self.type = random.choice(['shield', 'gun'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > self.height:
            self.kill()