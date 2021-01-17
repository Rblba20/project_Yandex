import os
import random
import sys

import pygame

pygame.init()
pygame.display.set_caption('Star Fighter')
size = width, height = 650, 675
screen = pygame.display.set_mode(size)
stars = []
for i in range(5000):
    star_x = random.random() * width
    star_y = random.random() * height
    screen.fill(pygame.Color('white'),
                (star_x,
                 star_y, 1, 1))
    stars.append([star_x, star_y])


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


FPS = 50


def terminate():
    pygame.quit()
    sys.exit()


def start_screen(stars):
    intro_text = ["  Star Fighter", "",
                  "[Z]Играть",
                  "[S]Результаты",
                  "[X]Выход", ""]
    rights = ["© Made by Rblba20 and lapin01", "",
              "All rights reserved"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font('data/text.ttf', 70)
    font_ = pygame.font.Font('data/text.ttf', 35)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    for line in rights:
        string_rendered = font_.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                perehod('z', stars)
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                perehod('s', stars)
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)


def perehod(key, stars):
    time = 0
    running = True
    while running and time < 30:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock = pygame.time.Clock()
        for i in range(10000):
            screen.fill(pygame.Color('black'),
                        (random.random() * width,
                         random.random() * height, 1, 1))
        pygame.display.flip()
        clock.tick(FPS)
        time += 0.1
    if time >= 30 and key == 'z':
        game_window(stars)
        return
    if time >= 30 and key == 's':
        results(stars)
        return


def game_window(stars):
    g = 1
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock = pygame.time.Clock()
        if g <= 200:
            for i in range(25):
                screen.fill(pygame.Color('white'),
                            (stars[25 * (g - 1) + i][0],
                             stars[25 * (g - 1) + i][1], 1, 1))
        else:
            for i in range(5000):
                screen.fill(pygame.Color('white'),
                            (stars[i][0],
                             stars[i][1], 1, 1))
        pygame.display.flip()
        clock.tick(FPS)
        if g > 200:
            return
        g += 1


def results(stars):
    g = 1
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock = pygame.time.Clock()
        if g <= 40:
            for i in range(25):
                screen.fill(pygame.Color('white'),
                            (stars[25 * (g - 1) + i][0],
                             stars[25 * (g - 1) + i][1], 1, 1))
        else:
            for i in range(5000):
                screen.fill(pygame.Color('white'),
                            (stars[i][0],
                             stars[i][1], 1, 1))
        pygame.display.flip()
        clock.tick(FPS)
        if g > 200:
            return
        g += 1


start_screen(stars)
terminate()