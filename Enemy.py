from Projectile import *
import random
from os import path

import pygame
from pygame.math import Vector2


class Enemy(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, x_, y_, projectiles, enemy_images, delay,
                 point, all_sprites, width, height, horizontal_borders, vertical_borders, bullet_images, shoot_sound):
        super().__init__(all_sprites)
        self.radius = radius
        self.bullet_images = bullet_images
        self.shoot_sound = shoot_sound
        self.width = width
        self.height = height
        self.vertical_borders = vertical_borders
        self.horizontal_borders = horizontal_borders
        BLACK = (0, 0, 0)
        img_dir = path.join(path.dirname(__file__), 'data')
        enemy_images = []
        enemy_list = ['enemyBlack1.png', 'enemyBlue2.png', 'enemyGreen3.png',
                      'enemyRed4.png']
        for img in enemy_list:
            enemy_images.append(pygame.image.load(path.join(img_dir, img)).convert())
        self.image_orig = random.choice(enemy_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        # self.rect = self.image.get_rect()
        #  self.radius = int(self.rect.width * .85 / 2)
        #  self.rect.x = random.randrange(width - self.rect.width)
        # self.rect.y = random.randrange(-150, -100)
        #    self.speedy = random.randrange(1, 8)
        #  self.speedx = random.randrange(-3, 3)
        #    self.rot = 0
        #   self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()
        self.rect = pygame.Rect(random.choice(point), random.choice(point), 2 * radius, 2 * radius)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.width - self.rect.width)
        self.rect.y = random.randrange(100, 240)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)
        self.previous_time = pygame.time.get_ticks()
        self.shoot_delay = random.choice(delay)
        self.speed = 1
        self.projectiles = projectiles

    def update(self):
        if self.rect.top > self.height + 10 or self.rect.left < -25 or self.rect.right > self.width + 20:
            self.rect.x = random.randrange(self.width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, self.horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, self.vertical_borders):
            self.vx = -self.vx
        now = pygame.time.get_ticks()
        if now - self.previous_time > self.shoot_delay:
            self.previous_time = now
            vel = Vector2(self.speed, 31)
            self.projectiles.add(Projectile(self.rect.x, self.rect.y, vel, self.rect.centerx, self.rect.top,
                                            self.bullet_images, self.shoot_sound))
