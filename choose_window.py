import os
import random

import pygame

pygame.init()
pygame.display.set_caption('Star Fighter')
size = width, height = 650, 675
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


all_sprites = pygame.sprite.Group()
black_plane = pygame.sprite.Sprite()
black_plane.image = load_image("player_cadet_n1_black.png")
black_plane.rect = black_plane.image.get_rect()
all_sprites.add(black_plane)
black_plane.rect.x = 20
black_plane.rect.y = 140
letter_A_image = load_image("A.png")
letter_A = pygame.sprite.Sprite(all_sprites)
letter_A.image = letter_A_image
letter_A.rect = letter_A.image.get_rect()
letter_A.rect.x = 60
letter_A.rect.y = 40
pink_plane_image = load_image("player_cadet_n1_pink.png")
pink_plane = pygame.sprite.Sprite(all_sprites)
pink_plane.image = pink_plane_image
pink_plane.rect = pink_plane.image.get_rect()
pink_plane.rect.x = 20
pink_plane.rect.y = 290
letter_D_image = load_image("B.png")
letter_D = pygame.sprite.Sprite(all_sprites)
letter_D.image = letter_D_image
letter_D.rect = letter_D.image.get_rect()
letter_D.rect.x = 50
letter_D.rect.y = 260
blue_plane_image = load_image("player_cadet_n1_blue.png")
blue_plane = pygame.sprite.Sprite(all_sprites)
blue_plane.image = blue_plane_image
blue_plane.rect = blue_plane.image.get_rect()
blue_plane.rect.x = 220
blue_plane.rect.y = 220
letter_C_image = load_image("C.png")
letter_C = pygame.sprite.Sprite(all_sprites)
letter_C.image = letter_C_image
letter_C.rect = letter_C.image.get_rect()
letter_C.rect.x = 250
letter_C.rect.y = 180
green_plane_image = load_image("player_cadet_n1_green.png")
green_plane = pygame.sprite.Sprite(all_sprites)
green_plane.image = green_plane_image
green_plane.rect = green_plane.image.get_rect()
green_plane.rect.x = 450
green_plane.rect.y = 150
letter_D_image = load_image("D.png")
letter_D = pygame.sprite.Sprite(all_sprites)
letter_D.image = letter_D_image
letter_D.rect = letter_D.image.get_rect()
letter_D.rect.x = 500
letter_D.rect.y = 70
red_plane_image = load_image("player_cadet_n1_red.png")
red_plane = pygame.sprite.Sprite(all_sprites)
red_plane.image = red_plane_image
red_plane.rect = red_plane.image.get_rect()
red_plane.rect.x = 450
red_plane.rect.y = 300
letter_E_image = load_image("E.png")
letter_E = pygame.sprite.Sprite(all_sprites)
letter_E.image = letter_E_image
letter_E.rect = letter_E.image.get_rect()
letter_E.rect.x = 450
letter_E.rect.y = 280





running = True
i = 0
stars = []
while running:
    screen.fill(pygame.Color('black'))
    if i == 0:
        for i in range(5000):
            a = random.random() * width
            b = random.random() * height
            screen.fill(pygame.Color('white'),
                        (a,
                         b, 1, 1))
            stars.append([a, b])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            all_sprites.draw(screen)
            pygame.display.flip()
    else:
        for i in range(5000):
            screen.fill(pygame.Color('white'),
                        (stars[i][0],
                         stars[i][1], 1, 1))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                pass
            all_sprites.draw(screen)
            all_sprites.update(event)
            pygame.display.flip()
    i += 1
pygame.quit()