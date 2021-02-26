import random

import pygame
from pygame.math import Vector2


class Projectile(pygame.sprite.Sprite):

    def __init__(self, x, y, vel, centerx, top, bullet_images, shoot_sound):
        super().__init__()
        self.image = random.choice(bullet_images)
        self.rect = self.image.get_rect(topleft=(centerx, top))
        self.vel = Vector2(vel)
        shoot_sound.play()

    def update(self):
        self.rect.move_ip(self.vel)