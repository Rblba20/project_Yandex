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
name = pygame.sprite.Sprite()
name.image = load_image("name_game.png")
name.rect = name.image.get_rect()
all_sprites.add(name)
name.rect.x = 20
name.rect.y = 0
start_image = load_image("start.png")
start = pygame.sprite.Sprite(all_sprites)
start.image = start_image
start.rect = start.image.get_rect()
start.rect.x = -87
start.rect.y = 125
results_image = load_image("results.png")
results = pygame.sprite.Sprite(all_sprites)
results.image = results_image
results.rect = results.image.get_rect()
results.rect.x = 50
results.rect.y = 200
exit_image = load_image("exit.png")
exit = pygame.sprite.Sprite(all_sprites)
exit.image = exit_image
exit.rect = exit.image.get_rect()
exit.rect.x = 50
exit.rect.y = 260
copyrights_image = load_image("copyrights.png")
copyrights = pygame.sprite.Sprite(all_sprites)
copyrights.image = copyrights_image
copyrights.rect = copyrights.image.get_rect()
copyrights.rect.x = 30
copyrights.rect.y = 500

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
