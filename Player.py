from Bullet import *
import pygame



class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, player_img, POWERUP_TIME, all_sprites, bullets, shoot_sound, bullet_img):
        pygame.sprite.Sprite.__init__(self)
        self.POWERUP_TIME = POWERUP_TIME
        BLACK = (0, 0, 0)
        self.bullet_img = bullet_img
        self.shoot_sound = shoot_sound
        self.bullets = bullets
        self.all_sprites = all_sprites
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = self.width / 2
        self.rect.bottom = self.height - 10
        self.speedx = 0
        self.shield = 100
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_time = pygame.time.get_ticks()

    def update(self):
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > self.POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = self.width / 2
            self.rect.bottom = self.height - 10

        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_SPACE]:
            self.shoot()
        self.rect.x += self.speedx
        if self.rect.right > self.width:
            self.rect.right = self.width
        if self.rect.left < 0:
            self.rect.left = 0

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top, self.bullet_img)
                self.all_sprites.add(bullet)
                self.bullets.add(bullet)
                self.shoot_sound.play()
            if self.power >= 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery, self.bullet_img)
                bullet2 = Bullet(self.rect.right, self.rect.centery, self.bullet_img)
                self.all_sprites.add(bullet1)
                self.all_sprites.add(bullet2)
                self.bullets.add(bullet1)
                self.bullets.add(bullet2)
                self.shoot_sound.play()

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (self.width / 2, self.height + 200)
