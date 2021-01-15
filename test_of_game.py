import os
import random
import sys

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


FPS = 50


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
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
                perehod('z')
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                perehod('s')
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)


def perehod(key):
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
        game_window()
        return
    if time >= 30 and key == 's':
        results()
        return


def game_window():
    g = 1
    stars = []
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock = pygame.time.Clock()
        if g <= 200:
            for i in range(25):
                star_x = random.random() * width
                star_y = random.random() * height
                screen.fill(pygame.Color('white'),
                            (star_x,
                             star_y, 1, 1))
                stars.append([star_x, star_y])
        else:
            for i in range(5000):
                screen.fill(pygame.Color('white'),
                            (stars[i][0],
                             stars[i][1], 1, 1))
        pygame.display.flip()
        clock.tick(FPS)
        if g > 250:
            fout = open("stars.txt", "wt", encoding="utf8")
            fout.write(str(stars))
            fout.close()
            Choose(stars)
        g += 1


def results():
    g = 1
    stars = []
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock = pygame.time.Clock()
        if g <= 40:
            for i in range(25):
                star_x = random.random() * width
                star_y = random.random() * height
                screen.fill(pygame.Color('white'),
                            (star_x,
                             star_y, 1, 1))
                stars.append([star_x, star_y])
        else:
            for i in range(1000):
                screen.fill(pygame.Color('white'),
                            (stars[i][0],
                             stars[i][1], 1, 1))
        pygame.display.flip()
        clock.tick(FPS)
        g += 1


class Choose:

    def __init__(self, stars):
        self.stars = stars
        self.sprites()

    def terminate(self):
        pygame.quit()
        sys.exit()

    def start_screen(self):
        intro_text = ["[A]      [F]", "",
                      "[S]      [G]", "",
                      "[D]      [H]", ""]
        rights = ["Выберите космический корабль,", "которым вы будете управлять",
                  "Images made by Kenney.nl"]

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
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.terminate()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                    running = False
                    self.terminate()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    image = "playerShip1_red.png"
                    fout = open("plane.txt", "wt", encoding="utf8")
                    fout.write(image)
                    fout.close()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    image = "playerShip2_blue.png"
                    fout = open("plane.txt", "wt", encoding="utf8")
                    fout.write(image)
                    fout.close()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    image = "playerShip3_green.png"
                    fout = open("plane.txt", "wt", encoding="utf8")
                    fout.write(image)
                    fout.close()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                    image = "playerShip1_green.png"
                    fout = open("plane.txt", "wt", encoding="utf8")
                    fout.write(image)
                    fout.close()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                    image = "playerShip2_orange.png"
                    fout = open("plane.txt", "wt", encoding="utf8")
                    fout.write(image)
                    fout.close()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                    image = "playerShip3_red.png"
                    fout = open("plane.txt", "wt", encoding="utf8")
                    fout.write(image)
                    fout.close()

            pygame.display.flip()
            clock.tick(FPS)

    def load_image(self, name, colorkey=None):
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

    def sprites(self):
        all_sprites = pygame.sprite.Group()
        red_plane_A = pygame.sprite.Sprite()
        red_plane_A.image = self.load_image("playerShip1_red.png")
        red_plane_A.rect = red_plane_A.image.get_rect()
        all_sprites.add(red_plane_A)
        red_plane_A.rect.x = 120
        red_plane_A.rect.y = 50
        blue_plane_S = pygame.sprite.Sprite()
        blue_plane_S.image = self.load_image("playerShip2_blue.png")
        blue_plane_S.rect = blue_plane_S.image.get_rect()
        all_sprites.add(blue_plane_S)
        blue_plane_S.rect.x = 120
        blue_plane_S.rect.y = 210
        green_plane_D = pygame.sprite.Sprite()
        green_plane_D.image = self.load_image("playerShip3_green.png")
        green_plane_D.rect = green_plane_D.image.get_rect()
        all_sprites.add(green_plane_D)
        green_plane_D.rect.x = 120
        green_plane_D.rect.y = 370
        green_plane_second_version_F = pygame.sprite.Sprite()
        green_plane_second_version_F.image = self.load_image("playerShip1_green.png")
        green_plane_second_version_F.rect = green_plane_second_version_F.image.get_rect()
        all_sprites.add(green_plane_second_version_F)
        green_plane_second_version_F.rect.x = 480
        green_plane_second_version_F.rect.y = 50
        blue_plane_second_version_G = pygame.sprite.Sprite()
        blue_plane_second_version_G.image = self.load_image("playerShip2_orange.png")
        blue_plane_second_version_G.rect = blue_plane_second_version_G.image.get_rect()
        all_sprites.add(blue_plane_second_version_G)
        blue_plane_second_version_G.rect.x = 480
        blue_plane_second_version_G.rect.y = 210
        red_plane_second_version_H = pygame.sprite.Sprite()
        red_plane_second_version_H.image = self.load_image("playerShip3_red.png")
        red_plane_second_version_H.rect = red_plane_second_version_H.image.get_rect()
        all_sprites.add(red_plane_second_version_H)
        red_plane_second_version_H.rect.x = 480
        red_plane_second_version_H.rect.y = 370
        self.choose_player(all_sprites)

    def choose_player(self, all_sprites):
        running = True
        while running:
            for i in range(5000):
                screen.fill(pygame.Color('white'),
                            (self.stars[i][0],
                             self.stars[i][1], 1, 1))
            all_sprites.draw(screen)
            self.start_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                all_sprites.draw(screen)
                all_sprites.update(event)
                pygame.display.flip()
        pygame.quit()


start_screen()
terminate()
