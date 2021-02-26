import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        BLACK = (0, 0, 0)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()